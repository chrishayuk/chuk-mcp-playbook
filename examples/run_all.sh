#!/bin/bash
# Run all example scripts

echo "🧪 Running All Chuk MCP Playbook Examples"
echo "=========================================="
echo ""

EXAMPLES_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$EXAMPLES_DIR"

# Ensure virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment not activated"
    echo "   Run: source ../.venv/bin/activate"
    exit 1
fi

# Run each example
for example in 01_*.py 02_*.py 03_*.py 04_*.py 05_*.py; do
    if [ -f "$example" ]; then
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "▶ Running: $example"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""

        python "$example"

        if [ $? -ne 0 ]; then
            echo ""
            echo "❌ Example $example failed!"
            exit 1
        fi

        echo ""
        echo "✅ Example $example completed"
        echo ""
    fi
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ All examples completed successfully!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
