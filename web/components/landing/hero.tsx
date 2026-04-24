"use client";

import { useEffect, useState } from "react";
import { ArrowDown } from "lucide-react";

export function Hero() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 100);
    return () => clearTimeout(timer);
  }, []);

  return (
    <section
      id="hero"
      className="relative flex min-h-screen flex-col items-center justify-center overflow-hidden px-6 pt-14"
    >
      {/* Subtle grid */}
      <div className="pointer-events-none absolute inset-0">
        <div
          className="absolute inset-0 opacity-[0.025]"
          style={{
            backgroundImage:
              "linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)",
            backgroundSize: "64px 64px",
          }}
        />
      </div>

      <div className="relative z-10 mx-auto max-w-3xl text-center">
        {/* Badge */}
        <div
          className={`mb-8 inline-flex items-center gap-2 rounded-full border border-white/[0.08] bg-white/[0.03] px-4 py-1.5 text-[12px] text-zinc-400 transition-all duration-700 ${
            visible
              ? "translate-y-0 opacity-100"
              : "translate-y-4 opacity-0"
          }`}
        >
          <span className="h-1.5 w-1.5 rounded-full bg-red-400" />
          Your automation broke again.
        </div>

        {/* Headline */}
        <h1
          className={`mx-auto max-w-3xl text-4xl font-bold leading-[1.1] tracking-tight text-zinc-100 transition-all duration-700 delay-100 sm:text-5xl md:text-6xl ${
            visible
              ? "translate-y-0 opacity-100"
              : "translate-y-4 opacity-0"
          }`}
        >
          n8n workflows are where automation goes to die.
        </h1>

        {/* Subheadline */}
        <p
          className={`mx-auto mt-6 max-w-xl text-[15px] leading-relaxed text-zinc-500 transition-all duration-700 delay-200 sm:text-base ${
            visible
              ? "translate-y-0 opacity-100"
              : "translate-y-4 opacity-0"
          }`}
        >
          They break at 3am. No AI reasoning. No error handling. No way to
          debug. FlowKits gives you battle-tested Python workflows with AI built
          in. Code you can read, debug, and trust.
        </p>

        {/* CTA */}
        <div
          className={`mt-10 flex flex-col items-center gap-3 sm:flex-row sm:justify-center transition-all duration-700 delay-300 ${
            visible
              ? "translate-y-0 opacity-100"
              : "translate-y-4 opacity-0"
          }`}
        >
          <a
            href="#subscribe"
            className="group inline-flex h-11 items-center gap-2 rounded-lg bg-zinc-100 px-6 text-[13px] font-semibold text-zinc-950 shadow-lg shadow-zinc-100/5 transition-all hover:bg-zinc-200 hover:shadow-zinc-100/10"
          >
            Get early access
          </a>
          <a
            href="#why"
            className="inline-flex h-11 items-center gap-2 rounded-lg border border-white/[0.08] bg-white/[0.02] px-6 text-[13px] font-medium text-zinc-300 transition-all hover:border-white/[0.15] hover:bg-white/[0.05]"
          >
            Why FlowKits?
          </a>
        </div>
      </div>

      {/* Scroll indicator */}
      <div
        className={`absolute bottom-8 left-1/2 -translate-x-1/2 transition-all duration-1000 delay-700 ${
          visible ? "opacity-50" : "opacity-0"
        }`}
      >
        <a href="#why" className="block text-zinc-600 hover:text-zinc-400 transition-colors">
          <ArrowDown className="h-5 w-5 animate-bounce" />
        </a>
      </div>

      {/* Bottom fade */}
      <div className="pointer-events-none absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-zinc-950 to-transparent" />
    </section>
  );
}
