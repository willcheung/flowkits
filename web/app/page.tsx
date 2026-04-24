import { Hero } from "@/components/landing/hero";
import { WhyFlowKits } from "@/components/landing/why-flowkits";
import { EmailCapture } from "@/components/landing/email-capture";
import { Footer } from "@/components/landing/footer";

export default function Home() {
  return (
    <div className="min-h-screen bg-zinc-950">
      <Hero />
      <WhyFlowKits />
      <EmailCapture />
      <Footer />
    </div>
  );
}
