// WKWebView (WebKit / Safari engine) slide screenshotter.
// Usage: shoot <baseURL> <outDir> <slide1.html> <slide2.html> ...
// Renders each slide at 1280x720 and snapshots at 2x (2560x1440) PNG.
import Cocoa
import WebKit

let args = CommandLine.arguments
guard args.count >= 4 else { FileHandle.standardError.write("need baseURL outDir slides...\n".data(using:.utf8)!); exit(2) }
let base = args[1]
let outDir = args[2]
let slides = Array(args[3...])

let app = NSApplication.shared
app.setActivationPolicy(.accessory)

final class Shooter: NSObject, WKNavigationDelegate {
    let webView: WKWebView
    let window: NSWindow
    var queue: [String]
    let base: String
    let out: String
    init(base: String, out: String, slides: [String]) {
        let cfg = WKWebViewConfiguration()
        let frame = NSRect(x: 0, y: 0, width: 1280, height: 720)
        self.webView = WKWebView(frame: frame, configuration: cfg)
        self.window = NSWindow(contentRect: frame, styleMask: [.borderless], backing: .buffered, defer: false)
        self.queue = slides; self.base = base; self.out = out
        super.init()
        window.contentView = webView
        window.setIsVisible(false)
        webView.navigationDelegate = self
    }
    func start() { next() }
    func next() {
        guard let s = queue.first else { NSApp.terminate(nil); return }
        guard let url = URL(string: base + s) else { queue.removeFirst(); next(); return }
        webView.load(URLRequest(url: url))
    }
    func webView(_ wv: WKWebView, didFinish nav: WKNavigation!) {
        // allow JS render + Google Fonts to settle
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.8) {
            let cfg = WKSnapshotConfiguration()
            cfg.snapshotWidth = 2560   // 2x crisp
            cfg.rect = NSRect(x: 0, y: 0, width: 1280, height: 720)
            wv.takeSnapshot(with: cfg) { image, error in
                let name = (self.queue.first! as NSString).deletingPathExtension
                if let img = image, let tiff = img.tiffRepresentation,
                   let rep = NSBitmapImageRep(data: tiff),
                   let png = rep.representation(using: .png, properties: [:]) {
                    try? png.write(to: URL(fileURLWithPath: self.out + "/" + name + ".png"))
                    FileHandle.standardOutput.write(("shot \(name)\n").data(using: .utf8)!)
                } else {
                    FileHandle.standardError.write(("FAIL \(name): \(error?.localizedDescription ?? "no image")\n").data(using: .utf8)!)
                }
                self.queue.removeFirst()
                self.next()
            }
        }
    }
    func webView(_ wv: WKWebView, didFail nav: WKNavigation!, withError error: Error) {
        FileHandle.standardError.write(("NAVFAIL \(error.localizedDescription)\n").data(using:.utf8)!)
        queue.removeFirst(); next()
    }
}

let shooter = Shooter(base: base, out: outDir, slides: slides)
shooter.start()
app.run()
