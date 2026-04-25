"use client";

import { useEffect, useRef, useState } from "react";
import { Eye, Activity, Bell } from "lucide-react";

const tiers = [
  {
    icon: Eye,
    label: "Free",
    title: "The code",
    description:
      "Every workflow is open-source. Read every line, modify anything. Each kit includes AGENTS.md so your AI agent knows how to run and extend it.",
  },
  {
    icon: Activity,
    label: "Paid",
    title: "The monitoring",
    description:
      "Execution dashboard, success rates, duration tracking. Your AI agent reports what it did — you see the results without building observability.",
  },
  {
    icon: Bell,
    label: "Paid",
    title: "The auto-healing",
    description:
      "When a workflow fails, your AI agent diagnoses the issue, applies a fix, and retries. You get a notification, not a 3am wake-up call.",
  },
];

export function OpenSourceModel() {
  const ref = useRef<HTMLElement>(null);
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
    <section ref={ref} id="model" className="relative bg-zinc-50 px-6 py-24 sm:py-32">
      <div
        className={`mx-auto max-w-6xl transition-all duration-700 ${
          visible ? "translate-y-0 opacity-100" : "translate-y-6 opacity-0"
        }`}
      >
        {/* Section header */}
        <div className="mb-16 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-zinc-900 sm:text-3xl">
            Code is free. Monitoring is the product.
          </h2>
          <p className="mx-auto mt-3 max-w-lg text-[14px] leading-relaxed text-zinc-500">
            The code is open-source. Your AI agent runs it. We sell the
            monitoring and auto-healing that makes it reliable.
          </p>
        </div>

        {/* Tiers */}
        <div className="grid gap-4 sm:grid-cols-3 lg:gap-6">
          {tiers.map((tier, i) => (
            <div
              key={tier.title}
              className="rounded-xl border border-zinc-200 bg-white p-6 shadow-sm transition-all duration-500"
              style={{ transitionDelay: `${i * 100}ms` }}
            >
              <div className="mb-4 flex items-center justify-between">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-zinc-200 bg-zinc-50">
                  <tier.icon className="h-5 w-5 text-zinc-500" />
                </div>
                <span
                  className={`rounded-full border px-2.5 py-0.5 text-[11px] font-medium ${
                    tier.label === "Free"
                      ? "border-emerald-200 bg-emerald-50 text-emerald-600"
                      : "border-zinc-200 bg-zinc-100 text-zinc-600"
                  }`}
                >
                  {tier.label}
                </span>
              </div>
              <h3 className="mb-2 text-[15px] font-semibold text-zinc-900">
                {tier.title}
              </h3>
              <p className="text-[13px] leading-relaxed text-zinc-500">
                {tier.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
