"use client";

import { signIn } from "next-auth/react";
import { usePathname } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Github } from "lucide-react";

export function SignInButton() {
  const pathname = usePathname();

  return (
    <Button
      onClick={() => signIn("github", { callbackUrl: pathname || "/" })}
      variant="outline"
      className="gap-2"
    >
      <Github className="h-4 w-4" />
      <span className="hidden sm:inline">Sign in with GitHub</span>
      <span className="sm:hidden">Sign in</span>
    </Button>
  );
}
