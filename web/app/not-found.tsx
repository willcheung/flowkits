import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-zinc-950 px-6">
      <div className="relative z-10 text-center">
        <p className="mb-2 font-mono text-[12px] font-medium uppercase tracking-widest text-zinc-500">
          404
        </p>
        <h1 className="mb-4 text-4xl font-bold tracking-tight text-zinc-100 sm:text-5xl">
          Page not found
        </h1>
        <p className="mx-auto mb-8 max-w-md text-[15px] leading-relaxed text-zinc-500">
          The page you&apos;re looking for doesn&apos;t exist or has been moved.
        </p>
        <Link
          href="/"
          className="inline-flex h-11 items-center gap-2 rounded-lg bg-zinc-100 px-6 text-[13px] font-semibold text-zinc-950 transition-all hover:bg-zinc-200"
        >
          Back to Home
        </Link>
      </div>
    </div>
  );
}
