#!/usr/bin/env python3
"""code_graph.py — a tiny AST-parsed context graph for the Day 4 tokenomics demo.

Indexes the repo into a graph of functions, imports, and call edges using Python's
stdlib `ast`, then answers "what depends on this function?" by returning just the
relevant subgraph instead of making the agent re-read whole files.

This is the dependency-free, Python-only version of the idea. The multi-language
production form uses a parser such as Tree-sitter; the principle is identical:
retrieve the minimum relevant structure, not the whole file.

Usage:
    python tools/code_graph.py build                 # index the repo, print the graph
    python tools/code_graph.py whodepends get_note   # who calls get_note (transitively)?
    python tools/code_graph.py cost get_note         # subgraph tokens vs whole-file tokens
"""

import ast
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PKG = REPO / "notes_api"


def _index():
    """Return (defs, calls): function defs by name, and caller->callees edges."""
    defs = {}          # func name -> (file, lineno, source_len_chars)
    calls = {}         # caller func name -> set(callee names)
    for path in sorted(PKG.glob("*.py")):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                src = ast.get_source_segment(path.read_text(), node) or ""
                defs[node.name] = (path.name, node.lineno, len(src))
                callees = set()
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Call):
                        f = sub.func
                        name = getattr(f, "attr", None) or getattr(f, "id", None)
                        if name:
                            callees.add(name)
                calls[node.name] = callees
    return defs, calls


def build():
    defs, calls = _index()
    print(f"# code graph — {len(defs)} functions across {len(list(PKG.glob('*.py')))} files\n")
    for name, (file, line, _) in sorted(defs.items()):
        edges = sorted(c for c in calls.get(name, ()) if c in defs)
        arrow = " -> " + ", ".join(edges) if edges else ""
        print(f"  {name}  ({file}:{line}){arrow}")


def whodepends(target):
    defs, calls = _index()
    if target not in defs:
        print(f"'{target}' is not a known function. Try: {', '.join(sorted(defs))}")
        return
    callers = {c for c, callees in calls.items() if target in callees and c in defs}
    print(f"# direct callers of {target}: {', '.join(sorted(callers)) or '(none)'}")
    # one transitive hop
    trans = {c for c, callees in calls.items() if callers & callees and c in defs}
    if trans - callers:
        print(f"# one hop out:        {', '.join(sorted(trans - callers))}")


def cost(target):
    defs, calls = _index()
    if target not in defs:
        print(f"'{target}' not found.")
        return
    # subgraph: the function + its direct callers' signatures
    callers = {c for c, callees in calls.items() if target in callees}
    subgraph_chars = defs[target][2] + sum(80 for _ in callers)  # ~sig-sized stubs
    whole_files = sum(len((PKG / f).read_text()) for f in {defs[target][0]}
                      | {defs[c][0] for c in callers if c in defs})
    # rough 4 chars/token heuristic
    print(f"# answering 'what depends on {target}?'")
    print(f"  subgraph retrieval : ~{subgraph_chars // 4:>5} tokens")
    print(f"  whole-file reads   : ~{whole_files // 4:>5} tokens")
    if whole_files:
        saved = 100 * (1 - subgraph_chars / whole_files)
        print(f"  reduction          : ~{saved:.0f}%   (pilot, then measure quality too)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    arg = sys.argv[2] if len(sys.argv) > 2 else None
    if cmd == "build":
        build()
    elif cmd == "whodepends" and arg:
        whodepends(arg)
    elif cmd == "cost" and arg:
        cost(arg)
    else:
        print(__doc__)
