# Spotlight @crisxai5 — AI & Crypto Expert on X

[![make.fun](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![rank](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/firlifirrizqi/spotlight-crisxai5-makefun/rank.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![reward](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/firlifirrizqi/spotlight-crisxai5-makefun/reward.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

An entry for the [make.fun bounty "Spotlight @crisxai5: AI & Crypto Expert on X"](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad) ($2 pot, top 10 paid, entries close Friday 27 Nov 2026 18:35 WIB). The post itself is the entry: places go by the post's likes + reposts + quotes after the deadline, highest first.

## The spotlight

Your timeline is 99% noise. [@crisxai5](https://x.com/crisxai5) is the 1% signal — a sharp, must-follow voice on AI agents, crypto alpha, and Web3 tooling. That is the hook: every crypto timeline user recognises the noise, and this card names the filter.

The image is original, drawn from scratch with PIL (`draw_spotlight.py`): a friendly flat robot (the AI half) beside a rising candlestick chart with a trend arrow (the crypto half), on a dark navy card with the handle `@crisxai5` big in cyan and three chips saying what followers get — AI AGENTS, CRYPTO ALPHA, WEB3 TOOLING. Square 1080x1080, huge bold text, high contrast, readable at a glance on a phone. No downloaded image, no copied material.

## The post

The card is posted on X from the public account [@firrizqi45914](https://x.com/firrizqi45914), with the image attached to the post itself. The exact text is in `POST_TEXT.md`: it carries `@crisxai5`, `https://x.com/crisxai5`, the hashtags `#AI #Crypto #AIAgents #Web3`, and one of the account's `makefun-` play codes.

**This entry is NOT submitted yet.** `POST.json` still holds a placeholder URL. The entry is only real once Firli posts the card on X and the post's real URL is put into `POST.json` — do not submit this repository with the placeholder.

Keep the post up and the account public until the results are out.

## How it works

- `spotlight.png` — the rendered card (1080x1080), drawn by `draw_spotlight.py`.
- `draw_spotlight.py` — the PIL script that renders `spotlight.png` (run it to re-render).
- `POST_TEXT.md` — the exact text for the X post.
- `POST.json` — the X post's URL (placeholder until Firli posts).
- `main.ts` — the entrypoint (Node 22, stdlib only): it validates that `POST.json` names a real X post URL (a placeholder is refused) and copies it to `/output/POST.json`, where the gate reads it.

## Run

Re-render the card:

```sh
python3 draw_spotlight.py
```

Run the entrypoint the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then this directory's `POST.json` (once it holds the real post URL).
