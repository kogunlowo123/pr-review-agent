#!/bin/bash
set -euo pipefail
echo "Setting up Pull Request Review Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
