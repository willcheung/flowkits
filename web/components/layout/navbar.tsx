"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useSession } from "next-auth/react";
import { useState } from "react";
import { Menu, X } from "lucide-react";
import { SignInButton } from "@/components/auth/sign-in-button";
import { UserMenu } from "@/components/auth/user-menu";

export function Navbar() {
  const { data: session } = useSession();
  const pathname = usePathname();
  const isLanding = pathname === "/";
  const [mobileOpen, setMobileOpen] = useState(false);

  const landingLinks = [
    { href: isLanding ? "#why" : "/#why", label: "Why FlowKits" },
    { href: isLanding ? "#subscribe" : "/#subscribe", label: "Get Early Access" },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 border-b border-white/[0.06] bg-zinc-950/80 backdrop-blur-xl">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-6">
        <Link
          href="/"
          className="flex items-center gap-2 text-[15px] font-bold tracking-tight text-zinc-100"
        >
          <span className="flex h-7 w-7 items-center justify-center rounded-md bg-zinc-800 border border-white/[0.08] text-[11px] font-black text-zinc-300">
            FK
          </span>
          <span>
            Flow<span className="font-mono text-zinc-400">Kits</span>
          </span>
        </Link>

        {/* Desktop nav links */}
        <div className="hidden items-center gap-1 md:flex">
          {landingLinks.map((link) =>
            link.href.startsWith("#") ? (
              <a
                key={link.href}
                href={link.href}
                className="rounded-md px-3 py-1.5 text-[13px] text-zinc-400 transition-colors hover:text-zinc-100"
              >
                {link.label}
              </a>
            ) : (
              <Link
                key={link.href}
                href={link.href}
                className="rounded-md px-3 py-1.5 text-[13px] text-zinc-400 transition-colors hover:text-zinc-100"
              >
                {link.label}
              </Link>
            )
          )}
        </div>

        <div className="flex items-center gap-3">
          {session?.user ? <UserMenu /> : <SignInButton />}

          {/* Mobile hamburger */}
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className="inline-flex items-center justify-center rounded-md p-1.5 text-zinc-400 transition-colors hover:text-zinc-100 md:hidden"
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* Mobile menu dropdown */}
      {mobileOpen && (
        <div className="border-t border-white/[0.06] bg-zinc-950/95 backdrop-blur-xl md:hidden">
          <div className="flex flex-col px-6 py-3">
            {landingLinks.map((link) =>
              link.href.startsWith("#") ? (
                <a
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileOpen(false)}
                  className="rounded-md py-2 text-[14px] text-zinc-400 transition-colors hover:text-zinc-100"
                >
                  {link.label}
                </a>
              ) : (
                <Link
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileOpen(false)}
                  className="rounded-md py-2 text-[14px] text-zinc-400 transition-colors hover:text-zinc-100"
                >
                  {link.label}
                </Link>
              )
            )}
          </div>
        </div>
      )}
    </nav>
  );
}
