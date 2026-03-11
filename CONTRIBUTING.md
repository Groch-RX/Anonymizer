# Contributing to Anonymizer

First — thank you. Every contribution makes everyone more anonymous.

## Ground Rules

- All contributions must be released under AGPLv3
- No telemetry, no analytics, no calling home — ever
- No dependencies that aren't absolutely necessary
- Code must run fully offline after install

## How to Contribute

### Report a bug
Open an issue. Describe what happened vs what you expected.

### Suggest a profile
Know a language's ESL interference patterns well?
Open an issue with examples of real patterns — not stereotypes.
We want statistically accurate patterns, not caricatures.

### Improve effectiveness
The goal is defeating real stylometry tools:
- Burrows Delta
- JGAAP  
- Writeprints
- AuthorMiner

If you can test against these and improve the evasion rate — open a PR.

### Add a language profile
1. Research real L1 interference patterns for that language
2. Source from actual ESL corpora if possible (Lang-8, Tatoeba)
3. Add to PROFILES dict in anonymizer.py
4. Test that it doesn't make output obviously artificial

## What we don't want

- Backdoors
- Any form of tracking or logging
- Dependencies on cloud services
- Anything that phones home
- Marketing to criminals

## Philosophy

This tool works through collective identity.
Every improvement benefits every user equally.
That's why AGPLv3 — improvements belong to everyone.
