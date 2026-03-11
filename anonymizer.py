#!/usr/bin/env python3
"""
anonymizer.py — stylometry obfuscator
mixes random regional fingerprints + spelling mistakes to defeat authorship analysis
fully offline, no dependencies beyond stdlib

Copyright (C) 2026 anonymizer contributors
Licensed under GNU Affero General Public License v3.0
https://www.gnu.org/licenses/agpl-3.0.html

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import random
import re
import sys
import argparse

# ─────────────────────────────────────────────
# TYPO ENGINE
# ─────────────────────────────────────────────

def swap_adjacent(word):
    if len(word) < 3:
        return word
    i = random.randint(0, len(word) - 2)
    w = list(word)
    w[i], w[i+1] = w[i+1], w[i]
    return ''.join(w)

def drop_letter(word):
    if len(word) < 3:
        return word
    i = random.randint(1, len(word) - 1)
    return word[:i] + word[i+1:]

def double_letter(word):
    if len(word) < 2:
        return word
    i = random.randint(0, len(word) - 1)
    return word[:i] + word[i] + word[i:]

def phonetic_sub(word):
    subs = [
        (r'ph', 'f'), (r'ck', 'k'), (r'qu', 'kw'),
        (r'tion', 'shun'), (r'ing', 'in'),
        (r'th', 'd'), (r'wh', 'w'),
    ]
    for pattern, replacement in subs:
        if re.search(pattern, word, re.I):
            return re.sub(pattern, replacement, word, count=1, flags=re.I)
    return word

def add_typo(word, intensity):
    if len(word) <= 2 or random.random() > intensity:
        return word
    fn = random.choice([swap_adjacent, drop_letter, double_letter, phonetic_sub])
    return fn(word)

# ─────────────────────────────────────────────
# REGIONAL PROFILES
# ─────────────────────────────────────────────

PROFILES = {

    "chinese": {
        "vocab": {
            "the": ["", "da", "de"],
            "is": ["is", "ees", ""],
            "are": ["are", "is", ""],
            "very": ["very very", "so so", "quite"],
            "i think": ["i think think", "maybe", "i feel"],
            "yes": ["yes yes", "correct", "right right"],
            "no": ["no no", "cannot", "not possible"],
        },
        "suffixes": ["la", "lah", "lor", "mah"],
        "suffix_chance": 0.15,
        "drop_article_chance": 0.35,
        "phrases": [
            "like that one", "also can", "no need",
            "can or not?", "confirm plus chop",
            "so how?", "last time",
        ],
    },

    "french": {
        "vocab": {
            "actually": ["actually", "in fact", "effectively"],
            "eventually": ["eventually", "finally"],
            "i know": ["i know not", "i not know"],
            "very": ["very", "much"],
            "library": ["library", "librairie"],
            "yes": ["oui", "yes yes"],
            "no": ["non", "no"],
            "sorry": ["pardon", "sorry"],
        },
        "suffixes": ["non?", "no?", "yes?"],
        "suffix_chance": 0.2,
        "drop_article_chance": 0.1,
        "phrases": [
            "it is not possible", "how do you say",
            "in my country", "is it not?",
            "i misunderstood", "it is complicated",
        ],
        "accent_typos": {
            "e": ["é", "è", "e"],
            "a": ["à", "a"],
            "c": ["ç", "c"],
        },
    },

    "dutch": {
        "vocab": {
            "actually": ["actually", "eigenlijk", "in fact"],
            "so": ["so", "dus", "therefore"],
            "very": ["very", "quite", "rather"],
            "maybe": ["maybe", "perhaps", "it could be"],
            "yes": ["ja", "yes", "indeed"],
            "no": ["nee", "no", "not"],
        },
        "suffixes": ["or not?", "right?", "yes?"],
        "suffix_chance": 0.12,
        "drop_article_chance": 0.08,
        "word_order_flip": 0.15,  # "I have yesterday eaten"
        "phrases": [
            "it is what it is", "not my problem",
            "be direct about it", "just do it",
            "make it simple", "no nonsense",
        ],
    },

    "indian": {
        "vocab": {
            "yes": ["yes", "ji", "haan", "absolutely"],
            "no": ["no", "nahi", "not at all"],
            "very": ["very", "too much", "only"],
            "actually": ["actually", "basically", "only"],
            "friend": ["friend", "yaar", "bhai"],
            "okay": ["okay", "achha", "theek hai"],
            "what": ["what", "kya", "what only"],
        },
        "suffixes": ["only", "itself", "no?", "isn't it?", "na?"],
        "suffix_chance": 0.25,
        "drop_article_chance": 0.2,
        "phrases": [
            "like this only", "what to do",
            "no problem at all", "kindly do the needful",
            "itself it happened", "prepone the meeting",
            "out of station", "do one thing",
        ],
    },

    "arabic": {
        "vocab": {
            "yes": ["yes", "aiwa", "yes yes"],
            "no": ["no", "la", "no no"],
            "god": ["god", "inshallah"],
            "maybe": ["maybe", "inshallah", "god willing"],
            "thank you": ["thank you", "shukran", "thanks thanks"],
            "okay": ["okay", "tamam", "yalla"],
        },
        "suffixes": ["wallah", "habibi", "yalla"],
        "suffix_chance": 0.15,
        "drop_article_chance": 0.3,
        "phrases": [
            "inshallah it works", "wallah i swear",
            "habibi listen", "yalla lets go",
            "what is this situation", "not my fault wallah",
        ],
        "p_to_b": 0.2,  # arabic has no P sound
    },

    "russian": {
        "vocab": {
            "the": ["", "the", ""],
            "a": ["", "a", ""],
            "yes": ["yes", "da", "yes yes"],
            "no": ["no", "nyet", "no no"],
            "very": ["very", "ochen", "quite"],
            "okay": ["okay", "horosho", "normal"],
        },
        "suffixes": ["da?", "nyet?", "or what?"],
        "suffix_chance": 0.15,
        "drop_article_chance": 0.5,  # russian has no articles
        "phrases": [
            "in mother russia", "is not problem",
            "we have saying", "back in my country",
            "how you say", "not bad not bad",
        ],
        "w_to_v": 0.2,  # russian W→V interference
    },
}

# ─────────────────────────────────────────────
# CORE TRANSFORMER
# ─────────────────────────────────────────────

def apply_profile(text, profile_name, intensity):
    profile = PROFILES[profile_name]
    words = text.split()
    result = []

    i = 0
    while i < len(words):
        word = words[i]
        word_lower = word.lower()
        stripped = word_lower.strip('.,!?;:')

        # vocab substitution
        if stripped in profile["vocab"] and random.random() < intensity:
            replacement = random.choice(profile["vocab"][stripped])
            # preserve capitalization
            if word[0].isupper():
                replacement = replacement.capitalize()
            result.append(replacement)
            i += 1
            continue

        # arabic P→B
        if profile_name == "arabic" and random.random() < profile.get("p_to_b", 0):
            word = word.replace('p', 'b').replace('P', 'B')

        # russian W→V
        if profile_name == "russian" and random.random() < profile.get("w_to_v", 0):
            word = word.replace('w', 'v').replace('W', 'V')

        # french accent typos
        if profile_name == "french" and random.random() < intensity * 0.3:
            accent_map = profile.get("accent_typos", {})
            for char, options in accent_map.items():
                if char in word:
                    word = word.replace(char, random.choice(options), 1)
                    break

        # drop articles
        if stripped in ["the", "a", "an"] and random.random() < profile.get("drop_article_chance", 0):
            i += 1
            continue

        # add typo
        word = add_typo(word, intensity)

        result.append(word)
        i += 1

    text = ' '.join(result)

    # inject random regional phrases
    sentences = re.split(r'(?<=[.!?])\s+', text)
    output_sentences = []
    for sentence in sentences:
        output_sentences.append(sentence)
        if random.random() < intensity * 0.2:
            phrase = random.choice(profile["phrases"])
            output_sentences.append(phrase.capitalize() + ".")

    text = ' '.join(output_sentences)

    # add suffix to some sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    output_sentences = []
    for sentence in sentences:
        if random.random() < profile.get("suffix_chance", 0) * intensity:
            suffix = random.choice(profile["suffixes"])
            sentence = sentence.rstrip('.!?') + ' ' + suffix
        output_sentences.append(sentence)

    return ' '.join(output_sentences)


def mix_profiles(text, profiles, intensity):
    """Apply random mix of selected profiles per sentence"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    result = []
    for sentence in sentences:
        # pick random profile for each sentence
        profile = random.choice(profiles)
        sentence = apply_profile(sentence, profile, intensity)
        result.append(sentence)
    return ' '.join(result)


# ─────────────────────────────────────────────
# PUNCTUATION + CAPS RANDOMIZER
# ─────────────────────────────────────────────

def randomize_punctuation(text, intensity):
    # random double punctuation
    if random.random() < intensity * 0.3:
        text = re.sub(r'\.', lambda m: '.' if random.random() > 0.2 else '..', text)

    # random missing apostrophes
    contractions = ["don't", "can't", "won't", "I'm", "it's", "they're", "we're"]
    for c in contractions:
        if c in text and random.random() < intensity * 0.5:
            text = text.replace(c, c.replace("'", ""), 1)

    # random caps mid sentence
    words = text.split()
    for i in range(len(words)):
        if random.random() < intensity * 0.05:
            words[i] = words[i].upper()
    text = ' '.join(words)

    return text


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def anonymize(text, profiles="all", intensity=0.3, seed=None):
    if seed is not None:
        random.seed(seed)
    else:
        random.seed()  # truly random each run

    if profiles == "all":
        selected = list(PROFILES.keys())
    else:
        selected = [p.strip() for p in profiles.split(',') if p.strip() in PROFILES]
        if not selected:
            selected = list(PROFILES.keys())

    text = mix_profiles(text, selected, intensity)
    text = randomize_punctuation(text, intensity)

    return text


def main():
    parser = argparse.ArgumentParser(
        description='Stylometry anonymizer — defeats authorship analysis'
    )
    parser.add_argument(
        'text', nargs='?',
        help='Text to anonymize (or pipe via stdin)'
    )
    parser.add_argument(
        '--text', dest='text_flag',
        help='Text to anonymize directly e.g. --text "your text here"'
    )
    parser.add_argument(
        '--profiles', default='all',
        help='Comma separated profiles: chinese,french,dutch,indian,arabic,russian (default: all)'
    )
    parser.add_argument(
        '--intensity', type=float, default=0.3,
        help='Effect intensity 0.0-1.0 (default: 0.3, subtle=0.1, obvious=0.6)'
    )
    parser.add_argument(
        '--seed', type=int, default=None,
        help='Random seed for reproducible output'
    )
    parser.add_argument(
        '--list-profiles', action='store_true',
        help='List available profiles'
    )

    args = parser.parse_args()

    if args.list_profiles:
        print("Available profiles:")
        for p in PROFILES:
            print(f"  {p}")
        return

    # get text from arg or stdin
    if args.text_flag:
        text = args.text_flag
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        import platform
        hint = "Ctrl+Z then Enter" if platform.system() == "Windows" else "Ctrl+D"
        print(f"anonymizer.py — paste your text below, then press {hint}")
        text = sys.stdin.read().strip()

    if not text:
        print("no input text provided")
        sys.exit(1)

    result = anonymize(text, args.profiles, args.intensity, args.seed)
    print(result)


if __name__ == "__main__":
    main()
