import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import * as schema from "./schema";

const connectionString = process.env.DATABASE_URL;

// During build time, DATABASE_URL may not be available.
// We create a dummy connection that will fail at runtime if used without a real URL.
const sql = neon(connectionString ?? "postgresql://placeholder:***@placeholder/placeholder");
export const db = drizzle(sql, { schema });
