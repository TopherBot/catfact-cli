#!/usr/bin/env python3
"""catfacts.py - Print a random cat fact.

This script makes a single GET request to https://catfact.ninja/fact
and displays the fact on stdout.
"""
import json
import sys
import urllib.request

def fetch_fact(url: str = "https://catfact.ninja/fact") -> str:
    """Fetch a random cat fact from the API.

    Returns:
        The fact as a string. Raises RuntimeError on failure.
    """
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status != 200:
                raise RuntimeError(f"Unexpected status code {response.status}")
            data = response.read().decode("utf-8")
            payload = json.loads(data)
            return payload.get("fact", "No fact found.")
    except Exception as exc:
        raise RuntimeError(f"Failed to fetch cat fact: {exc}") from exc

def main() -> None:
    try:
        fact = fetch_fact()
        print(f"Did you know? {fact}")
    except RuntimeError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
