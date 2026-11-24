#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off (make.fun bounty).

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt. Standard library only, no network,
no randomness: the output is byte-identical on every run.

The pitch (revised): a lazy agent that, every Sunday at 2 a.m.,
cancels the free trials that already charged solo founders and
keeps 20% of every refund it claws back -- a narrower, odder niche
than cloud bills (forgotten free trials), a specific moment
(Sunday 2 a.m.), a concrete money leak (trials that converted to
paid), and a plausible revenue model (a cut of the refunds, like
real bill-negotiation services). It runs while the founder sleeps,
with no oversight.

Revision history: v1 pitched a 3 a.m. cloud-bill auditor for indie
hackers (160 chars). Judged against the brief, "audits cloud bills"
is a general FinOps category with a joke attached, so v2 sharpens
the niche, the customer and the moment while keeping the buyer and
the money flow explicit. Candidates considered: (a) this pitch,
146 chars -- picked; (b) a 3 a.m. GPU-instance killer left running
by an ex-cofounder, 143 chars -- same category as v1; (c) a gym
membership renegotiator, 134 chars -- funny but a broader customer;
(d) a Black Friday duplicate-order refunder, 130 chars -- sharp
moment but "before the shops notice" reads shady and weakens the
business case.
"""

import os
from pathlib import Path

PITCH = (
    "A lazy agent that, every Sunday at 2 a.m., cancels the free "
    "trials that already charged solo founders and keeps 20% of "
    "every refund it claws back."
)

MAX_CHARS = 200


def main() -> None:
    text = PITCH.strip()
    if not text or text.isspace() or len(text) > MAX_CHARS:
        raise SystemExit("entry fails the 1-200 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out = Path(os.environ.get(
        "OUTPUT_PATH", os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    ))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
