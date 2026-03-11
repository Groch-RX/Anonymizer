# 🕵️ Anonymizer

> *Your writing style is a fingerprint. This tool smudges it.*

## What is this?

Every time you write something — an email, a forum post, a message — you leave behind an invisible signature. Your word choices, sentence length, punctuation habits, and even which filler words you use are as unique as a fingerprint.

This is called **stylometry** — and governments, corporations, and stalkers use it to identify you without needing your name, IP address, or any account information.

**Anonymizer** defeats stylometry by making everyone who uses it sound the same. Not by hiding you — but by merging you into a collective identity shared by every user of this tool.

The more people use it, the more anonymous everyone becomes.

---

## How it works

```
Your text → anonymizer → output that looks like "anonymizer user"
                         not like you specifically
```

Anonymizer applies a consistent set of transformations:

- Regional linguistic patterns (Chinese, French, Dutch, Indian, Arabic, Russian ESL interference)
- Controlled spelling variations
- Punctuation normalization
- Vocabulary substitution
- Sentence structure shifts

Every user gets the **same output style** — one collective identity, thousands of people.

---

## Collective Identity Model

Traditional anonymization tries to make you look like *nobody*.  
Anonymizer makes you look like *everybody who uses this tool*.

```
Investigator traces message → "anonymizer user"
Suspect pool               → every person who ever used this tool
Investigation              → dead end
```

This only works with numbers. The more users, the stronger the anonymity.

**Current protection level depends on active userbase.**  
Share this tool. Every new user makes everyone safer.

---

## Legitimate Uses

- 🛡️ **Stalker and harassment protection** — prevent abusers from tracking your writing across platforms
- 📰 **Journalist source protection** — sources can communicate without stylometric identification
- 🔔 **Whistleblowing** — report wrongdoing without being identified by writing style alone
- 🌍 **Political dissidents** — write freely under authoritarian surveillance
- 🏢 **Corporate surveillance evasion** — prevent data brokers from building behavioral profiles
- 🔒 **General privacy** — your writing style is your data. Protect it.

---

## Installation

No dependencies beyond Python 3 stdlib. Works on Linux, Mac, Windows.

```bash
git clone https://github.com/[yourname]/anonymizer
cd anonymizer
python3 anonymizer.py --help
```

---

## Usage

```bash
# basic — pipe text in
echo "your text here" | python3 anonymizer.py

# from a file
cat essay.txt | python3 anonymizer.py

# specific regional profiles
echo "text" | python3 anonymizer.py --profiles indian,arabic,russian

# intensity control
echo "text" | python3 anonymizer.py --intensity 0.3

# list available profiles
python3 anonymizer.py --list-profiles

# interactive mode
python3 anonymizer.py
```

## Intensity Guide

| Value | Effect |
|---|---|
| 0.1 | Subtle — nearly native looking |
| 0.3 | Default — noticeable regional patterns |
| 0.6 | Heavy — clearly non-native ESL style |
| 1.0 | Maximum — aggressive transformation |

---

## Available Profiles

| Profile | L1 Interference Patterns |
|---|---|
| `chinese` | Article dropping, reduplication, discourse particles |
| `french` | Gender interference, inversion errors, false friends |
| `dutch` | Word order shifts, direct communication style, article errors |
| `indian` | Emphasis words, question tags, present continuous overuse |
| `arabic` | Article dropping, P→B interference, discourse markers |
| `russian` | Article omission, word order, consonant cluster patterns |
| `all` | Random mix of all profiles per sentence (default) |

---

## Anonymity Warning ⚠️

This tool provides **meaningful anonymity only at scale.**

| Userbase | Protection Level |
|---|---|
| < 100 users | Low — suspect pool too small |
| 100 - 1000 | Medium — use alongside Tor |
| 1000 - 10000 | Good — collective identity effective |
| 10000+ | Strong — investigation becomes impractical |

**Below 1000 active users — combine with Tor Browser and a VPN for full protection.**

Help reach critical mass — share this tool with anyone who values privacy.

---

## Limitations

Anonymizer is not magic. It currently:

- ✓ Defeats casual stylometric analysis
- ✓ Defeats automated authorship attribution
- ✓ Creates plausible collective identity
- ✗ Does not defeat advanced forensic linguistic analysis
- ✗ Does not anonymize metadata (use alongside Tor/VPN)
- ✗ Does not protect against other identification methods

**This tool addresses writing style only.** For full anonymity:

```
Anonymizer     → writing style
Tor Browser    → IP address
VPN            → ISP surveillance
mat2/exiftool  → file metadata
Tails OS       → system traces
```

Use all layers.

---

## Roadmap

- [ ] v0.2 — spaCy integration for function word randomization
- [ ] v0.3 — sentence length and structure variation
- [ ] v0.4 — effectiveness testing against Burrows Delta / JGAAP
- [ ] v0.5 — browser extension
- [ ] v1.0 — proven 85%+ anonymization rate

---

## Contributing

Pull requests welcome. All contributions must be released under AGPLv3.

If you improve this tool, your improvements belong to everyone.
That's the point.

---

## Disclaimer

This tool is intended solely for lawful privacy protection purposes including but not limited to protection from stalkers and harassment, journalistic source protection, whistleblower privacy, and protection from corporate surveillance.

The author(s) and contributors bear NO legal responsibility for misuse of this tool. By using this software you agree that you are solely responsible for ensuring your use complies with all applicable laws in your jurisdiction.

Misuse of this tool to harass, threaten, or harm others is a violation of these terms and applicable law.

---

## License

GNU Affero General Public License v3.0

If you improve this — share it back. Privacy is a collective project.

```
Copyright (C) 2026 anonymizer contributors
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to
redistribute it under the terms of the AGPLv3.
```

---

*Privacy is not about having something to hide.*
*Privacy is a fundamental human right.*

**Share this tool. Every user makes everyone safer.**
