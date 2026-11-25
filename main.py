#!/usr/bin/env python3
"""My Secret Logbook - make.fun bounty entry.

Writes a single diary line to /output/entry.txt.
Python 3 stdlib only, no network.
"""
import os

LINE = "Day 89: human saved it as 'final_FINAL_v7_REAL.pdf' and asked me to find the real one. There is no real one."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
