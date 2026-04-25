"use client";

import { useState, useRef, useEffect, type FormEvent } from "react";
import { toast } from "sonner";
import { ArrowRight, Loader2 } from "lucide-react";

export function EmailCapture() {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
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

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!email.trim()) return;

    setLoading(true);
    try {
      const res = await fetch("/api/subscribe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim() }),
      });

      const data = await res.json();

      if (!res.ok) {
        toast.error(data.error || "Something went wrong.");
        return;
      }

      toast.success(data.message);
      setSubmitted(true);
      setEmail("");
    } catch {
      toast.error("Network error. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section
      id="subscribe"
      ref={ref}
      className="relative bg-zinc-950 px-6 py-24 sm:py-32"
    >
      <div
        className={`mx-auto max-w-xl text-center transition-all duration-700 ${
          visible ? "translate-y-0 opacity-100" : "translate-y-6 opacity-0"
        }`}
      >
        <h2 className="text-2xl font-bold tracking-tight text-zinc-200 sm:text-3xl">
          Get early access
        </h2>
        <p className="mx-auto mt-3 max-w-md text-[14px] leading-relaxed text-zinc-500">
          We&apos;re building the first batch of AI workflow kits. Join the
          waitlist and be the first to know when they&apos;re ready.
        </p>

        {!submitted ? (
          <form
            onSubmit={handleSubmit}
            className="mt-8 flex flex-col gap-3 sm:flex-row sm:justify-center"
          >
            <input
              type="email"
              required
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              disabled={loading}
              className="h-11 flex-1 rounded-lg border border-white/[0.08] bg-white/[0.03] px-4 text-[14px] text-zinc-200 placeholder:text-zinc-600 outline-none transition-colors focus:border-white/[0.15] disabled:opacity-50 sm:max-w-xs"
            />
            <button
              type="submit"
              disabled={loading}
              className="inline-flex h-11 items-center justify-center gap-2 rounded-lg bg-zinc-100 px-6 text-[13px] font-semibold text-zinc-950 transition-all hover:bg-zinc-200 disabled:opacity-50"
            >
              {loading ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <>
                  Join waitlist
                  <ArrowRight className="h-3.5 w-3.5" />
                </>
              )}
            </button>
          </form>
        ) : (
          <div className="mt-8 rounded-xl border border-emerald-500/20 bg-emerald-500/5 px-6 py-4 text-[14px] text-emerald-400">
            You&apos;re on the list. We&apos;ll be in touch.
          </div>
        )}

        <p className="mt-4 text-[11px] text-zinc-700">
          No spam, ever. Just launch updates.
        </p>
      </div>
    </section>
  );
}
