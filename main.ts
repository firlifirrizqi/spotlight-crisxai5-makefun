// Entry for the make.fun bounty "Spotlight @crisxai5: AI & Crypto Expert
// on X" (Node 22, standard library only). The entry is the X post itself:
// POST.json names the post, and this program copies POST.json from the
// repository root to /output/POST.json, where the gate reads it. That is
// all the program has to do. Nothing written here about the post is scored.
//
// POST.json ships with a placeholder address, so the gate refuses it as it
// stands. The placeholder is replaced with the real post address only
// after Firli posts the spotlight image on X from @firrizqi45914 — this
// program refuses to hand a placeholder to the gate.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

// Read POST.json and insist it names a real X post before copying it:
// a leftover placeholder (or an id of all zeros) must never reach the gate.
const postPath = join(BOT_DIR, 'POST.json');
const post = JSON.parse(readFileSync(postPath, 'utf8'));
if (
  typeof post.url !== 'string' ||
  !/^https:\/\/(x\.com|twitter\.com)\/\S+\/status\/\d+$/.test(post.url) ||
  /\/status\/0+$/.test(post.url) ||
  post.url.includes('<handle>') ||
  post.url.includes('<id>')
) {
  console.error(`POST.json at ${postPath} does not name a real X post URL.`);
  process.exit(1);
}
copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
