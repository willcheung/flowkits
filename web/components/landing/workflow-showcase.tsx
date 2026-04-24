"use client";

import { useEffect, useRef, useState } from "react";
import { Mail, Calendar, Send, ArrowRight } from "lucide-react";

const workflows = [
  {
    icon: Mail,
    name: "Gmail AI Labeler",
    category: "Personal Productivity",
    price: "Free",
    priceColor: "text-emerald-400 bg-emerald-400/10 border-emerald-400/20",
    description:
      "AI reads your inbox and labels emails automatically. Learns your categories, creates new ones when needed. Runs every 5 minutes.",
    tech: "Gmail API + GPT-4o-mini",
    n8nBasis: "Based on n8n template #2740",
  },
  {
    icon: Calendar,
    name: "Pre-Meeting Briefing",
    category: "Sales",
    price: "$15",
    priceColor: "text-zinc-300 bg-white/[0.05] border-white/[0.08]",
    description:
      "Scans your calendar, fetches company news, and emails you talking points before every meeting. Never walk in cold again.",
    tech: "Google Calendar + NewsAPI + GPT-4o-mini",
    n8nBasis: "Based on n8n template #2110",
  },
  {
    icon: Send,
    name: "Sheets Email Campaign",
    category: "Marketing",
    price: "$19",
    priceColor: "text-zinc-300 bg-white/[0.05] border-white/[0.08]",
    description:
      "AI-personalized outbound email from a Google Sheet. Auto follow-up for non-responders. Rate limiting and weekend skip built in.",
    tech: "Google Sheets + GPT-4o-mini + SMTP",
    n8nBasis: "Based on n8n template #2088",
  },
];

function WorkflowCard({
  workflow,
  index,
}: {
  workflow: (typeof workflows)[number];
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
      className={`group rounded-xl border border-white/[0.06] bg-white/[0.02] p-6 transition-all duration-700 hover:border-white/[0.12] ${
        visible ? "translate-y-0 opacity-100" : "translate-y-6 opacity-0"
      }`}
      style={{ transitionDelay: `${index * 120}ms` }}
    >
      {/* Header */}
      <div className="mb-4 flex items-start justify-between">
        <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-white/[0.08] bg-white/[0.03]">
          <workflow.icon className="h-5 w-5 text-zinc-400" />
        </div>
        <span
          className={`rounded-full border px-2.5 py-0.5 text-[11px] font-medium ${workflow.priceColor}`}
        >
          {workflow.price}
        </span>
      </div>

      {/* Content */}
      <h3 className="mb-1 text-[15px] font-semibold text-zinc-200">
        {workflow.name}
      </h3>
      <p className="mb-3 text-[11px] font-medium uppercase tracking-wider text-zinc-600">
        {workflow.category}
      </p>
      <p className="mb-4 text-[13px] leading-relaxed text-zinc-500">
        {workflow.description}
      </p>

      {/* Workflow visualization placeholder */}
      <div className="mb-4 flex h-32 items-center justify-center rounded-lg border border-dashed border-white/[0.06] bg-white/[0.01]">
        <p className="text-[11px] text-zinc-700">Workflow visualization</p>
      </div>

      {/* Footer */}
      <div className="flex items-center justify-between">
        <p className="text-[11px] text-zinc-600">{workflow.tech}</p>
        <p className="text-[10px] text-zinc-700">{workflow.n8nBasis}</p>
      </div>
    </div>
  );
}

export function WorkflowShowcase() {
  return (
    <section id="workflows" className="relative px-6 py-24 sm:py-32">
      <div className="mx-auto max-w-6xl">
        {/* Section header */}
        <div className="mb-16 text-center">
          <h2 className="text-2xl font-bold tracking-tight text-zinc-200 sm:text-3xl">
            Workflows that actually run
          </h2>
          <p className="mx-auto mt-3 max-w-lg text-[14px] leading-relaxed text-zinc-500">
            Each kit is a complete Python project with error handling, retry
            logic, and AI reasoning. Download, configure, run.
          </p>
        </div>

        {/* Workflow grid */}
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 lg:gap-6">
          {workflows.map((workflow, i) => (
            <WorkflowCard key={workflow.name} workflow={workflow} index={i} />
          ))}
        </div>

        {/* More coming */}
        <div className="mt-8 text-center">
          <p className="inline-flex items-center gap-1.5 text-[13px] text-zinc-600">
            7 more workflows in development
            <ArrowRight className="h-3.5 w-3.5" />
          </p>
        </div>
      </div>
    </section>
  );
}
