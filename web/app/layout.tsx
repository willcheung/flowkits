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
    "Production-ready AI workflows in Python, operated by your AI agent. Built from n8n's most popular templates with AI reasoning, error handling, and retry logic.",
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
      "AI workflows in Python, operated by your AI agent. Built from n8n's top templates with reasoning, error handling, and auto-healing.",
    type: "website",
    siteName: "FlowKits",
  },
  twitter: {
    card: "summary_large_image",
    title: "FlowKits — Battle-Tested AI Workflows in Python",
    description:
      "AI workflows in Python, operated by your AI agent. Built from n8n's top templates with reasoning, error handling, and auto-healing.",
  },
  robots: {
    index: true,
    follow: true,
  },
  icons: {
    icon: [
      { url: "/favicon-32.png", sizes: "32x32", type: "image/png" },
      { url: "/favicon-16.png", sizes: "16x16", type: "image/png" },
    ],
    apple: "/apple-touch-icon.png",
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
