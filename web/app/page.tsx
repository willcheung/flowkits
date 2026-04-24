import { Hero } from "@/components/landing/hero";
import { WorkflowShowcase } from "@/components/landing/workflow-showcase";
import { WhyFlowKits } from "@/components/landing/why-flowkits";
import { OpenSourceModel } from "@/components/landing/open-source-model";
import { EmailCapture } from "@/components/landing/email-capture";
import { Footer } from "@/components/landing/footer";

export default function Home() {
  return (
    <div className="min-h-screen bg-zinc-950">
      <Hero />
      <WorkflowShowcase />
      <WhyFlowKits />
      <OpenSourceModel />
      <EmailCapture />
      <Footer />
    </div>
  );
}
