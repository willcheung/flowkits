import type { Metadata } from "next";
import { Roboto, JetBrains_Mono } from "next/font/google";
import { Providers } from "@/components/providers";
import { Navbar } from "@/components/layout/navbar";
import { Toaster } from "@/components/ui/sonner";
import "./globals.css";

const roboto = Roboto({
  variable: "--font-sans",
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: "FlowKits — Battle-Tested AI Workflows in Python",
    template: "%s | FlowKits",
  },
  description:
    "Stop debugging broken n8n workflows at 3am. FlowKits gives you battle-tested Python workflows with AI reasoning built in. Code you can read, debug, and trust.",
  keywords: [
    "ai workflows",
    "ai agents",
    "python automation",
    "n8n alternative",
    "workflow automation",
    "ai workflow kits",
    "automation templates",
  ],
  openGraph: {
    title: "FlowKits — Battle-Tested AI Workflows in Python",
    description:
      "Stop debugging broken n8n workflows. Get battle-tested Python workflows with AI reasoning built in.",
    type: "website",
    siteName: "FlowKits",
  },
  twitter: {
    card: "summary_large_image",
    title: "FlowKits — Battle-Tested AI Workflows in Python",
    description:
      "Battle-tested Python workflows with AI reasoning built in. Code you can read, debug, and trust.",
  },
  robots: {
    index: true,
    follow: true,
  },
  metadataBase: new URL("https://flowkits.ai"),
  alternates: {
    canonical: "/",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth">
      <body
        className={`${roboto.variable} ${jetbrainsMono.variable} font-sans text-[18px] antialiased`}
      >
        <Providers>
          <Navbar />
          {children}
          <Toaster />
        </Providers>
      </body>
    </html>
  );
}
