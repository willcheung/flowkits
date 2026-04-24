"use client";

import { useEffect, useRef, useState } from "react";
import { Shield, Code2, Brain, Bug } from "lucide-react";

const features = [
  {
    icon: Code2,
    title: "Real code, not JSON",
    description:
      "Every workflow is clean, typed Python. Read it, modify it, version control it. No more clicking through a visual editor to find the bug.",
  },
  {
    icon: Brain,
    title: "AI reasoning built in",
    description:
      "Each kit includes structured prompts, decision traces, and fallback logic. Your workflows actually think before they act.",
  },
  {
    icon: Shield,
    title: "Error handling that works",
    description:
      "Exponential backoff, circuit breakers, dead letter queues. The stuff n8n should have but doesn't. Because production doesn't forgive.",
  },
  {
    icon: Bug,
    title: "Debuggable by default",
    description:
      "Structured logging, health checks, and monitoring hooks. When something breaks at 3am, you'll know what happened and why.",
  },
];

function FeatureCard({
  feature,
  index,
}: {
  feature: (typeof features)[number];
  index: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.disconnect();
        }
      },
      { threshold: 0.2 }
    );

    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`rounded-xl border border-white/[0.06] bg-white/[0.02] p-6 transition-all duration-700 ${
        visible
          ? "translate-y-0 opacity-100"
          : "translate-y-6 opacity-0"
      }`}
      style={{ transitionDelay: `${index * 100}ms` }}
    >
      <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-lg border border-white/[0.08] bg-white/[0.03]">
        <feature.icon className="h-5 w-5 text-zinc-400" />
      </div>
      <h3 className="mb-2 text-[15px] font-semibold text-zinc-200">
        {feature.title}
      </h3>
      <p className="text-[13px] leading-relaxed text-zinc-500">
        {feature.description}
      </p>
    </div>
  );
}

export function WhyFlowKits() {
  return (
    <section id="why" className="relative px-6 py-24 sm:py-32">
      <div className="mx-auto max-w-6xl">
        {/* Section header */}
        <div className="mb-16 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-zinc-200 sm:text-3xl">
            Why FlowKits?
          </h2>
          <p className="mx-auto mt-3 max-w-lg text-[14px] leading-relaxed text-zinc-500">
            n8n workflows are great for prototyping. Terrible for production.
            Here&apos;s what&apos;s different.
          </p>
        </div>

        {/* Feature grid */}
        <div className="grid gap-4 sm:grid-cols-2 lg:gap-6">
          {features.map((feature, i) => (
            <FeatureCard key={feature.title} feature={feature} index={i} />
          ))}
        </div>

        {/* Comparison strip */}
        <div className="mt-16 rounded-xl border border-white/[0.06] bg-white/[0.02] p-6 sm:p-8">
          <div className="grid gap-6 sm:grid-cols-2">
            <div>
              <h3 className="mb-3 text-[13px] font-semibold uppercase tracking-wider text-zinc-600">
                n8n workflows
              </h3>
              <ul className="space-y-2.5 text-[13px] text-zinc-500">
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-red-400/70">✕</span>
                  Break silently at 3am
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-red-400/70">✕</span>
                  No AI reasoning or fallback logic
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-red-400/70">✕</span>
                  JSON you can&apos;t version control
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-red-400/70">✕</span>
                  Debugging is clicking through nodes
                </li>
              </ul>
            </div>
            <div>
              <h3 className="mb-3 text-[13px] font-semibold uppercase tracking-wider text-zinc-600">
                FlowKits
              </h3>
              <ul className="space-y-2.5 text-[13px] text-zinc-400">
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-emerald-400">✓</span>
                  Structured error handling with retries
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-emerald-400">✓</span>
                  AI decision traces and fallback chains
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-emerald-400">✓</span>
                  Clean Python in git, reviewable in PRs
                </li>
                <li className="flex items-start gap-2">
                  <span className="mt-0.5 text-emerald-400">✓</span>
                  Logs, health checks, and monitoring hooks
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
