# -*- coding: utf-8 -*-
r"""Garhwali CLI tool with UTF-8 support on all platforms."""

import sys
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import garhwali

def main():
    parser = argparse.ArgumentParser(
        prog="garhwali",
        description="Garhwali (गढ़वाली) Language Library & Multi-Dialect Tool"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # translate
    t_parser = subparsers.add_parser("translate", help="Translate English/Hindi/Hinglish to Garhwali")
    t_parser.add_argument("text", type=str, help="Text to translate")
    t_parser.add_argument("--dialect", "-d", type=str, default="srinagariya",
                          choices=["srinagariya", "rathwali", "tehri", "salani", "badhani"],
                          help="Garhwali dialect variant")

    # lookup
    l_parser = subparsers.add_parser("lookup", help="Look up a Garhwali word")
    l_parser.add_argument("word", type=str, help="Word to look up")

    # num
    n_parser = subparsers.add_parser("num", help="Convert numbers to Garhwali words")
    n_parser.add_argument("value", type=int, help="Integer value")

    # culture
    c_parser = subparsers.add_parser("culture", help="Explore Garhwali culture, proverbs, and calendar")

    args = parser.parse_args()

    if args.command == "translate":
        res = garhwali.translate(args.text, dialect=args.dialect)
        print(f"\nGarhwali [{res.dialect}]: {res.text}")
        print(f"Confidence: {res.confidence * 100:.1f}% | Target: {res.target_lang}")
    elif args.command == "lookup":
        d = garhwali.lookup(args.word)
        if d:
            print(f"\nWord: {d.get('garhwali')}")
            print(f"Hindi: {d.get('hindi')}")
            print(f"English: {d.get('english')}")
            print(f"POS: {d.get('pos')}")
            if "dialect_variants" in d:
                print(f"Dialects: {d['dialect_variants']}")
        else:
            print(f"Word '{args.word}' not found in dictionary.")
    elif args.command == "num":
        w = garhwali.num_to_words(args.value)
        d = garhwali.to_devanagari_numerals(args.value)
        print(f"\nNumber: {args.value} ({d})")
        print(f"Garhwali words: {w}")
    elif args.command == "culture":
        s = garhwali.get_current_season()
        print(f"\nCurrent Himalayan Ritu: {s.get('name_garhwali')} ({s.get('name_hindi')}) - {s.get('english_season')}")
        print("\nRandom Garhwali Proverb (पखाणा):")
        p = garhwali.proverbs.random()
        print(f"  \"{p.get('pakhana')}\"")
        print(f"  Meaning: {p.get('meaning')}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
