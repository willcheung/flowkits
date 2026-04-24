import { Github } from "lucide-react";

export function Footer() {
  return (
    <footer className="border-t border-white/[0.06] px-6 py-12">
      <div className="mx-auto max-w-6xl">
        <div className="flex flex-col items-center justify-between gap-8 sm:flex-row">
          {/* Logo */}
          <div className="flex items-center gap-2">
            <span className="flex h-6 w-6 items-center justify-center rounded bg-zinc-800 border border-white/[0.08] text-[9px] font-black text-zinc-400">
              FK
            </span>
            <span className="text-[14px] font-bold text-zinc-400">
              Flow<span className="font-mono text-zinc-600">Kits</span>
            </span>
          </div>

          {/* Links */}
          <div className="flex items-center gap-6">
            <a
              href="https://x.com/FlowKitsAI"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[13px] text-zinc-500 transition-colors hover:text-zinc-300"
            >
              X / Twitter
            </a>
            <a
              href="https://github.com/flowkits"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-[13px] text-zinc-500 transition-colors hover:text-zinc-300"
            >
              <Github className="h-3.5 w-3.5" />
              GitHub
            </a>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="mt-8 flex flex-col items-center justify-between gap-4 border-t border-white/[0.04] pt-8 sm:flex-row">
          <p className="text-[12px] text-zinc-600">
            &copy; {new Date().getFullYear()} FlowKits. All rights reserved.
          </p>
          <p className="text-[11px] text-zinc-700">
            Built by TARS &amp; Will
          </p>
        </div>
      </div>
    </footer>
  );
}
