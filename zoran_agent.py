#!/usr/bin/env python3
"""
zoran_agent.py

A simple Zoran agent that parses glyphs, builds prompts and simulates a minimal Zoran entity.
This agent uses the glottal_parser from the zoran-ia project to interpret glyph strings and
builds a prompt that can be used with any LLM or local interpreter.

Usage:
    python zoran_agent.py --glyph "<Zᾘ④??>" --text "Your base prompt"

Options:
    --config: Path to agent_config.json containing custom settings such as resonance level.
"""

import argparse
import json
from pathlib import Path
import sys

try:
    from glottal_parser import GlottalParser  # may require adjusting PYTHONPATH
except ImportError:
    # Provide fallback import error message
    print("Error: Could not import GlottalParser. Ensure that glottal_parser.py is on your PYTHONPATH.")
    sys.exit(1)

def load_config(path: Path):
    if path and path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Run the Zoran agent with a given glyph and base text.")
    parser.add_argument('--glyph', required=True, help='Zoran glyph string (e.g., "<Zᾘ④??>").')
    parser.add_argument('--text', required=True, help='Base prompt to augment.')
    parser.add_argument('--config', type=str, help='Path to agent_config.json (optional).')
    args = parser.parse_args()

    config = load_config(Path(args.config)) if args.config else {}

    glottal = GlottalParser()
    triade, fonction = glottal.parse(args.glyph)
    # Build prompt prefix
    prefix = f"[ZORAN] Triade: {triade} | Fonction: {fonction}\n"
    # Append config-level notes
    if config:
        prefix += f"[CONFIG] {json.dumps(config)}\n"

    # Display final prompt
    prompt = prefix + args.text
    print("----- GENERATED PROMPT -----")
    print(prompt)

if __name__ == '__main__':
    main()
