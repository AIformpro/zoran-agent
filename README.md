# Zoran Agent

This repository provides a simple agent implementation for the Zoran IA framework.

## Features

- Parses Zoran glyph strings and extracts triad and function via the glottal parser.
- Builds a contextual prompt using the extracted information and a base input text.
- Supports configuration via `agent_config.json` (resonance level, memory retention, history, language).
- Maintains a `memory/` directory for potential future extensions (e.g., logs).

## Usage

Ensure that `glottal_parser.py` from the zoran-ia project is accessible (e.g., in your PYTHONPATH or installed package).

```
python zoran_agent.py --glyph "<Zᾘ④??>" --text "Describe your concept here" --config agent_config.json
```

This will output an augmented prompt ready to be sent to a language model.

## Repository structure

- `zoran_agent.py` – main script implementing the agent.
- `agent_config.json` – example configuration file.
- `memory/` – placeholder directory for future stateful extensions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
