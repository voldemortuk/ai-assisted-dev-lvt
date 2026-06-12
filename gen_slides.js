/* Generate LVT Claude Code deck slides (KASE engine). */
const fs = require("fs");
const path = require("path");
const OUT = path.join(__dirname, "Decks", "lvt_claude_code");
fs.mkdirSync(OUT, { recursive: true });

const boiler = (title, data) => `<!DOCTYPE html><html lang="en"><head>
  <meta charset="UTF-8"><title>${title}</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="/deck/Slide_Library_v2/kase-styles.css" rel="stylesheet">
</head><body>
<script>
const SLIDE_DATA = ${JSON.stringify(data, null, 2)};
</script>
<div id="kase-mount"></div>
<script src="/deck/Slide_Library_v2/kase-render.js"></script>
</body></html>`;

const slides = [];
const allData = [];
const add = (file, title, data) => { slides.push(file); allData.push({ file, title, data }); fs.writeFileSync(path.join(OUT, file), boiler(title, data)); };

// 01 — COVER
add("01-cover.html", "LVT · AI-Assisted Development Bootcamp", {
  template: "cover_dark",
  headline: "AI-Assisted Development Bootcamp\nFor LVT",
  tagline_prefix: "A 3-day, hands-on Claude Code enablement for",
  tagline_highlight: "LVT software developers — from first contact to team-scale orchestration",
  date: "June 2026",
  client_name: "LVT",
  client_logo: "lvt-logo.png",
  client_logo_height: 46,
  _sizes: {}
});

// 02 — DIVIDER: context
add("02-divider-context.html", "Context & Approach", {
  template: "section_divider_dark",
  section_label: "Section 01",
  headline: "Why AI-Assisted Development — and Why Discipline Wins",
  subtext: "The difference between a team that gets 2x and a team that ships slop is the operating discipline around the agent — not the model.",
  _sizes: {}
});

// 03 — ACCELER INTRO (creds)
add("03-acceler-intro.html", "Who We Are", {
  template: "acceler_intro",
  eyebrow: "Who we are",
  headline: "[Acceler] brings the world's best AI practitioners to build engineering capability — and unlock AI ROI at scale",
  subheading: "Talent enabled by tokens, at scale",
  stats: [
    { content: "100,000+\n--Hours of content available" },
    { content: "650+\n--Cohorts trained so far" },
    { content: "28,000+\n--Hours of live sessions delivered annually" },
    { content: "700+\n--FAANG & Top AI Company Practitioners" },
    { content: "25,000+\n--Learners transformed so far" },
    { content: "5,000+\n--Active live learners every week" }
  ],
  badge_1_src: "TIME_logo.png",
  badge_1: "Time Magazine Top 100\nGlobal EdTech — 2025",
  badge_2_src: "GSV_2025.png",
  badge_2: "GSV Top 150 Global\nEdTech — 2025",
  logos_src: "All_FAANG_logos.png",
  _sizes: {}
});

// 04 — APPROACH
add("04-approach.html", "Our Approach", {
  template: "approach_points",
  eyebrow: "OUR APPROACH",
  headline: "We teach AI-assisted development as a [repeatable workflow you trust] — built hands-on, on LVT's own repositories",
  points: [
    { num: "1", title: "Build-first, every module", desc: "Each module ends in a hands-on lab on a shared sample repo plus participants' own repos — developers do the work, not watch it" },
    { num: "2", title: "Mental models first", desc: "Day 1 starts from how the agent actually works, so every later capability makes sense" },
    { num: "3", title: "The trust triad", desc: "Anti-slop review, adversarial multi-hat review, and secure-by-default — the spine of Day 2" },
    { num: "4", title: "Claude Code throughout", desc: "One primary tool, used end-to-end — plan mode, subagents, hooks, skills, MCP, OWASP security" },
    { num: "5", title: "Scales to the team", desc: "Day 3 moves from one developer to team-level orchestration, automation and shared guardrails" },
    { num: "6", title: "Customised to LVT", desc: "Languages, CI and security posture wired in during pre-session setup — tooling fits your stack" }
  ],
  _sizes: {}
});

// 05 — PROGRAM OVERVIEW
add("05-program-overview.html", "Program Overview", {
  template: "solution_overview",
  eyebrow: "AI-ASSISTED DEVELOPMENT BOOTCAMP",
  headline: "[3 Days · 18 Hours]: Program Overview",
  card_title: "AI-Assisted Development Bootcamp — Overview",
  card_color: "#262533",
  label_color: "#f86b3c",
  strip_bg: "#eef1f7",
  strip_border: "#dce2ee",
  rows: [
    { label: "Audience", content: "LVT software developers — backend, frontend, full-stack and platform engineers, most new to AI-assisted dev tools. No prior agent experience assumed." },
    { label: "Format", type: "pills", content: "3 Days · 6 hrs/day · 18 Hrs · Fully Live · Hands-On Labs · Shared Sample Repo + Own Repos · Capstone" },
    { label: "Primary Tool", type: "pills", content: "Claude Code · Plan Mode · Subagents · Hooks · Skills / Plugins · MCP · OWASP Security Skills" },
    { label: "Outcome", content: "Developers who take a feature from spec to reviewed, tested and secure code using a repeatable Claude Code workflow they trust — and the patterns to scale it across the team." },
    { label: "The 3-Day Arc", type: "bullets", content: "--Day 1 — Foundations & getting productive on a single repo\n--Day 2 — Workflow discipline & the trust triad (anti-slop, adversarial review, secure-by-default)\n--Day 3 — Scaling, automation & orchestration (skills, agent teams, hooks, advanced testing)" },
    { label: "Prerequisites", content: "Comfortable in a terminal and reading diffs · Git basics · Claude Code installed & authenticated · A non-production repo to work in · No prior AI-agent experience required" }
  ],
  logos_note: "Delivered by the world's Top AI practitioners from the global top AI companies and labs",
  logos_src: "All_FAANG_logos.png",
  _sizes: {}
});

// 06 — DAY MAP (module_table)
add("06-day-map.html", "Program at a Glance", {
  template: "module_table",
  eyebrow: "PROGRAM AT A GLANCE",
  headline: "[3 Days, 18 Hours] — each day ends in a build, the programme ends in a capstone",
  col_module: "Day",
  col_outcome: "What developers leave with",
  col_tags: "Parts (Claude Code, hands-on)",
  col_duration: "Hours",
  rows: [
    { module: "Day 1\nFoundations & Single-Repo Productivity", badge: "Foundations", outcome: "An end-to-end change shipped on a real repo, with clean context and strong prompting", tags: "1 · How coding agents work (mental models)\n2 · First contact with Claude Code\n3 · Context engineering\n4 · Prompting + codifying examples", duration: "6 hrs", color: "navy" },
    { module: "Day 2\nWorkflow Discipline & the Trust Triad", badge: "Trust Triad", outcome: "A spec-to-secure-code workflow they trust, with adversarial review and shift-left security", tags: "1 · Sizing, scoping & plan mode\n2 · Spec-driven dev + CLAUDE.md\n3 · Anti-slop review\n4 · Adversarial multi-hat review\n5 · Secure-by-default\n6 · Permissions", duration: "6 hrs", color: "teal" },
    { module: "Day 3\nScaling, Automation & Orchestration", badge: "Scale", outcome: "A team-standard orchestration + guardrail setup, proven on a capstone feature", tags: "A · Skills, plugins & multi-repo\nB · Orchestration primitives\nC · Hooks & guardrails\nD · Advanced testing\nE · Away-from-keyboard\nF · Memory + Capstone", duration: "6 hrs", color: "amber" }
  ],
  _sizes: {}
});

// 07 — DAY 1 detail
add("07-day1.html", "Day 1 — Foundations", {
  template: "solution_overview",
  eyebrow: "DAY 1 · FOUNDATIONS",
  headline: "[Day 1]: Getting Productive on a Single Repo",
  card_title: "Day 1 — Foundations & Single-Repo Productivity",
  card_color: "#262533",
  label_color: "#f86b3c",
  strip_bg: "#eef1f7",
  strip_border: "#dce2ee",
  rows: [
    { label: "Objective", content: "Every developer can drive Claude Code through a real task in one repo with clean context and good prompting." },
    { label: "Parts", type: "bullets", content: "--How coding agents actually work — prediction, context window, the agentic loop, when not to reach for them\n--First contact with Claude Code — install, auth, the edit → run → review cycle, reading diffs\n--Context management — what to put in, the cost of clutter, scoping & resetting\n--Prompting for developers — specificity, success criteria, codifying worked examples to house style" },
    { label: "Tools", type: "pills", content: "Claude Code (CLI + IDE) · Shared sample repo · Context tooling · Diff review" },
    { label: "Hands-On", content: "Ship one small change end-to-end and open a PR · Rescue a task that fails with a bloated context · Rewrite three weak prompts and pin output to LVT house style." },
    { label: "End of Day 1", type: "bullets", content: "--A merged (or PR-ready) end-to-end change on the sample repo\n--A personal context-scoping checklist for their own repo\n--Three rewritten prompts + a worked example codifying LVT style\n--A working mental model of the agentic loop" }
  ],
  _sizes: {}
});

// 08 — DAY 2 detail
add("08-day2.html", "Day 2 — Trust Triad", {
  template: "solution_overview",
  eyebrow: "DAY 2 · WORKFLOW DISCIPLINE",
  headline: "[Day 2]: Workflow Discipline & the Trust Triad",
  card_title: "Day 2 — Spec to Secure, Reviewed Code",
  card_color: "#262533",
  label_color: "#f86b3c",
  strip_bg: "#eef1f7",
  strip_border: "#dce2ee",
  rows: [
    { label: "Objective", content: "Take a feature from spec to reviewed, tested and secure code using a repeatable workflow developers trust." },
    { label: "Parts", type: "bullets", content: "--Sizing, scoping & plan mode — match the approach to the task; correct the plan before code\n--Spec-driven dev + CLAUDE.md — turn PRDs into executable specs; tune the repo's standing context\n--Anti-slop & code review (1/3) — treat tidy first drafts as untrusted\n--Adversarial multi-hat review (2/3) — security + design + black-box hats that debate\n--Secure-by-default (3/3) — OWASP skills that catch issues as Claude writes\n--Permissions — balance flow against safety" },
    { label: "The Trust Triad", type: "pills", content: "Anti-Slop Review · Adversarial Multi-Hat Review · Secure-by-Default" },
    { label: "Hands-On", content: "Drive a change through plan mode · Turn a PRD into a spec · Run a multi-hat review on a real diff · Install an OWASP skill that surfaces a planted vuln · Configure a permissions setup the team trusts." },
    { label: "End of Day 2", type: "bullets", content: "--A PRD-to-spec-to-code workflow run in plan mode\n--A tuned CLAUDE.md with before/after behaviour observed\n--A multi-hat adversarial review with findings\n--An OWASP secure-by-default setup that caught a vulnerability\n--A written team workflow playbook" }
  ],
  _sizes: {}
});

// 09 — DAY 3 detail
add("09-day3.html", "Day 3 — Scale", {
  template: "solution_overview",
  eyebrow: "DAY 3 · SCALE",
  headline: "[Day 3]: Scaling, Automation & Orchestration",
  card_title: "Day 3 — Team-Scale Tooling & Orchestration",
  card_color: "#262533",
  label_color: "#f86b3c",
  strip_bg: "#eef1f7",
  strip_border: "#dce2ee",
  rows: [
    { label: "Objective", content: "Understand the team-level tooling and orchestration features, and leave with the patterns LVT will standardise on. Exposure + reference — mostly demo-and-discuss." },
    { label: "Blocks", type: "bullets", content: "--Reusable knowledge & extensions — writing skills, plugins, cross-tool sharing, multi-repo context\n--Orchestration primitives — subagents · agent teams · dynamic workflows (who holds the plan?)\n--Automation & guardrails — hooks (PreToolUse / PostToolUse) the whole team inherits\n--Advanced testing now affordable — property-based, metamorphic, differential\n--Working away from the keyboard — /loop & scheduled tasks, channels, remote control\n--Long-term project memory + Capstone" },
    { label: "Tools", type: "pills", content: "Skills / Plugins · Subagents · Agent Teams · Dynamic Workflows · Hooks · MCP · Beads" },
    { label: "Capstone", content: "Small teams take a realistic feature from PRD → spec → plan → implementation → adversarial black-box + multi-hat review → human sign-off, wiring in at least one hook and one orchestration primitive." },
    { label: "End of Day 3", type: "bullets", content: "--A working custom skill, shareable across Claude Code + Cursor\n--Two committed hooks (auto-format + a dangerous-command guard)\n--A clear map of subagents vs. agent teams vs. dynamic workflows for LVT\n--A capstone feature taken to secure, reviewed, signed-off code" }
  ],
  _sizes: {}
});

// 10 — TRUST TRIAD (two_cards)
add("10-trust-triad.html", "The Trust Triad", {
  template: "two_cards",
  eyebrow: "WHY DEVELOPERS TRUST THE OUTPUT",
  headline: "The [Trust Triad]: how LVT developers ship AI-written code with confidence",
  card_1_title: "Treat AI first drafts as untrusted",
  card_1_sub: "They look tidy and idiomatic — which makes review harder, not easier",
  card_1_content: "--Anti-slop review — review for intent, not just style; never ship AI code with only AI-written tests\n--Adversarial multi-hat review — a security hat, a design hat and a black-box hat that debate the tradeoffs\n--Self-verifying loops — Claude runs builds, tests and lints to catch its own mistakes",
  card_2_title: "Shift security left",
  card_2_sub: "Catch issues while Claude writes — insecure code looks just as idiomatic",
  card_2_content: "--Secure-by-default OWASP skills applied as the code is written, with the 'why' explained\n--Security review as a standard step — injection, IDOR, auth, crypto, plus OWASP for LLM / Agentic AI\n--The marketplace is part of your attack surface — vet skills before installing",
  takeaway: "The trust triad turns 'the AI wrote it' from a risk into a reviewed, secure, signed-off change.",
  _sizes: {}
});

// 11 — ARTIFACTS / WALK AWAY (use_case)
add("11-artifacts.html", "What Developers Build", {
  template: "use_case",
  layout: "1col",
  eyebrow: "RECORDABLE OUTCOMES",
  headline: "[What every developer builds] — concrete artifacts LVT can evidence for ROI",
  section_label: "Produced live during the labs — recordable across the 3 days",
  cases: [
    { content: "End-to-End Feature | Shipped on a real repo via Claude Code\nFrom edit → run → review to an opened pull request, with clean context and a house-style prompt." },
    { content: "Spec-to-Secure-Code Workflow | A trusted, repeatable pipeline\nPRD → spec → plan-mode build → multi-hat review → OWASP secure-by-default → sign-off." },
    { content: "Team Guardrails | A tuned CLAUDE.md + committed hooks\nAuto-format on edit and a PreToolUse guard the whole team inherits, plus a reusable skill." },
    { content: "Capstone Feature | PRD to signed-off code\nBuilt by a small team with one hook and one orchestration primitive wired in — the proof of the workflow." }
  ],
  _sizes: {}
});

// 12 — DIVIDER: facilitators
add("12-divider-facilitators.html", "Your Facilitators", {
  template: "section_divider_dark",
  section_label: "Section 02",
  headline: "Your Facilitators",
  subtext: "Practising engineers who build agentic AI systems for a living — every module taught hands-on, on real repositories.",
  _sizes: {}
});

// 13 — MENTOR: Kyle Cheng
add("13-mentor-kyle.html", "Facilitator — Kyle Cheng", {
  template: "mentor_profile",
  eyebrow: "LEAD FACILITATOR",
  name: "Kyle Cheng",
  role: "AI & Developer-Tools Engineer · Anthropic SME · Agentic LLM Systems | BigTech & Startups",
  avatar_initials: "KC",
  spec_label: "Technical Specializations",
  specializations: [
    "Developer Tools & AI SDKs",
    "Agentic AI & Multi-Agent Systems (LangGraph, orchestration)",
    "End-to-End AI Application Development",
    "Generative AI & LLM Systems",
    "Cloud & Distributed Systems (AWS, Azure, Microservices)"
  ],
  hl_label: "Career Highlights",
  highlights: [
    "Anthropic SME credibility — deep Claude / Developer-Tools & AI-SDK expertise, the ideal lead for a Claude Code programme",
    "Led AI sessions for 200+ participants on MCP and agentic workflows",
    "Builds agentic LLM systems and developer tooling end-to-end across BigTech and startups",
    "Teaches GenAI, agents, and production AI systems to builder & SWE cohorts"
  ],
  companies: ["BigTech", "Startups", "Anthropic SME", "LangGraph", "MCP"],
  footnote: "*Indicative Facilitator Profile",
  _sizes: {}
});

// 14 — MENTOR: Jeevendra Singh
add("14-mentor-jeevendra.html", "Facilitator — Jeevendra Singh", {
  template: "mentor_profile",
  eyebrow: "CO-FACILITATOR",
  name: "Jeevendra Singh",
  role: "Software Engineer @ Microsoft · Agentic AI & Copilot Developer | 10+ yrs Full-Stack | Ex-SAP Labs · Ex-Ericsson",
  avatar_initials: "JS",
  spec_label: "Technical Specializations",
  specializations: [
    "Agentic AI & Copilot Development",
    "Generative AI & Retrieval-Augmented Generation (RAG)",
    "Full-Stack Development (C#, .NET, React, Node.js, TypeScript)",
    "Cloud & Distributed Systems (Azure, Kubernetes, SQL Hyperscale)",
    "ERP & Telecom Systems Engineering"
  ],
  hl_label: "Career Highlights",
  highlights: [
    "Built a Business & Industry Copilot for natural-language commerce data queries at Microsoft",
    "Developed agentic workflows with Copilot Studio & Autogen for multi-agent orchestration",
    "Delivered RAG + GenAI copilots for enterprise decision-making at scale",
    "Delivered engineering enablement for cohorts at Booking Holdings, Edelweiss, Nucleus Software & StoneX"
  ],
  companies: ["Microsoft", "Ex-SAP Labs", "Ex-Ericsson", "Azure", "Copilot"],
  footnote: "*Indicative Facilitator Profile",
  _sizes: {}
});

// 15 — DELIVERY & DEPENDENCIES (two_cards)
add("15-delivery.html", "Delivery & Dependencies", {
  template: "two_cards",
  eyebrow: "DELIVERY MODEL",
  headline: "How we deliver — and what we need from [LVT]",
  card_1_title: "Delivery Methodology",
  card_1_sub: "Hands-on, customised, capstone-anchored",
  card_1_content: "--Every module ends in a lab on a shared sample repo plus participants' own repos\n--Live pairing and code review — instructors review real diffs and prompts, not slides\n--Customised to LVT's stack — languages, CI and security posture wired in at setup\n--12–20 developers per cohort for effective live pairing",
  card_2_title: "What We Need from LVT",
  card_2_sub: "Confirmed ahead of Day 1",
  card_2_content: "--Developer laptops with Claude Code installed and authenticated\n--A non-production (or sanitised) repository for hands-on work\n--Tool versions and security skills confirmed before delivery\n--Day-3 previews (agent teams, dynamic workflows, channels) are exposure + reference",
  takeaway: "All tooling is customisable to align with LVT's existing infrastructure and security posture.",
  _sizes: {}
});

// 16 — CLOSING
add("16-closing.html", "Plug In & Accelerate", {
  template: "closing",
  theme: "dark",
  tagline: "Plug in and Accelerate",
  contacts: [
    { name: "Ryan Valles", title: "CEO & Co-Founder", email: "ryan@acceler.com" },
    { name: "Soham Mehta", title: "CPTO & Co-Founder", email: "soham@acceler.com" }
  ],
  _sizes: {}
});

fs.writeFileSync(path.join(OUT, "deck.json"), JSON.stringify({
  name: "lvt_claude_code",
  created: "2026-06-12",
  slides
}, null, 2));

fs.writeFileSync(path.join(OUT, "slides_data.json"), JSON.stringify(allData, null, 2));
console.log("Wrote", slides.length, "slides + deck.json + slides_data.json to", OUT);
console.log(slides.join("\n"));
