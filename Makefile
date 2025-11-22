.PHONY: clean clean-pyc clean-build clean-test clean-all test run build publish publish-test help install dev-install version docker-build docker-run

# Default target
help:
	@echo "Available targets:"
	@echo "  clean          - Remove Python bytecode and basic artifacts"
	@echo "  clean-all      - Deep clean everything (pyc, build, test, cache)"
	@echo "  clean-pyc      - Remove Python bytecode files"
	@echo "  clean-build    - Remove build artifacts"
	@echo "  clean-test     - Remove test artifacts"
	@echo "  install        - Install package in current environment"
	@echo "  dev-install    - Install package in development mode"
	@echo "  test           - Run tests"
	@echo "  test-cov       - Run tests with coverage report"
	@echo "  lint           - Run code linters"
	@echo "  format         - Auto-format code"
	@echo "  check          - Run all checks (lint, test)"
	@echo "  run            - Run the MCP server (stdio mode)"
	@echo "  run-http       - Run the MCP server (HTTP mode)"
	@echo "  build          - Build the project"
	@echo "  docker-build   - Build Docker image"
	@echo "  docker-run     - Run Docker container"

# Basic clean - Python bytecode and common artifacts
clean: clean-pyc clean-build
	@echo "Basic clean complete."

# Remove Python bytecode files and __pycache__ directories
clean-pyc:
	@echo "Cleaning Python bytecode files..."
	@find . -type f -name '*.pyc' -delete 2>/dev/null || true
	@find . -type f -name '*.pyo' -delete 2>/dev/null || true
	@find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true

# Remove build artifacts
clean-build:
	@echo "Cleaning build artifacts..."
	@rm -rf build/ dist/ *.egg-info 2>/dev/null || true
	@rm -rf .eggs/ 2>/dev/null || true
	@find . -name '*.egg' -exec rm -f {} + 2>/dev/null || true

# Remove test artifacts
clean-test:
	@echo "Cleaning test artifacts..."
	@rm -rf .pytest_cache/ 2>/dev/null || true
	@rm -rf .coverage 2>/dev/null || true
	@rm -rf htmlcov/ 2>/dev/null || true
	@rm -rf .tox/ 2>/dev/null || true
	@rm -rf .cache/ 2>/dev/null || true
	@find . -name '.coverage.*' -delete 2>/dev/null || true

# Deep clean - everything
clean-all: clean-pyc clean-build clean-test
	@echo "Deep cleaning..."
	@rm -rf .mypy_cache/ 2>/dev/null || true
	@rm -rf .ruff_cache/ 2>/dev/null || true
	@rm -rf .uv/ 2>/dev/null || true
	@find . -name '.DS_Store' -delete 2>/dev/null || true
	@find . -name '*.log' -delete 2>/dev/null || true
	@find . -name '*.tmp' -delete 2>/dev/null || true
	@find . -name '*~' -delete 2>/dev/null || true
	@echo "Deep clean complete."

# Install package
install:
	@echo "Installing package..."
	uv pip install .

# Install package in development mode
dev-install:
	@echo "Installing package in development mode..."
	uv venv
	uv pip install -e .

# Run tests
test:
	@echo "Running tests..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run pytest -v; \
	else \
		python -m pytest -v; \
	fi

# Run tests with coverage
test-cov coverage:
	@echo "Running tests with coverage..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run pytest --cov=src/chuk_mcp_playbook --cov-report=html --cov-report=term; \
	else \
		pytest --cov=src/chuk_mcp_playbook --cov-report=html --cov-report=term; \
	fi
	@echo "HTML coverage report saved to: htmlcov/index.html"

# Lint code
lint:
	@echo "Running linters..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run ruff check src/ tests/; \
	else \
		ruff check src/ tests/; \
	fi

# Format code
format:
	@echo "Formatting code..."
	@if command -v uv >/dev/null 2>&1; then \
		uv run ruff format src/ tests/; \
	else \
		ruff format src/ tests/; \
	fi

# Run all checks
check: lint test
	@echo "All checks passed!"

# Run the MCP server (stdio mode - default for Claude Desktop)
run:
	@echo "Running Chuk MCP Playbook Server (stdio mode)..."
	@if command -v uv >/dev/null 2>&1; then \
		PYTHONPATH=src uv run chuk-mcp-playbook; \
	else \
		PYTHONPATH=src python -m chuk_mcp_playbook.server; \
	fi

# Run the MCP server in HTTP mode
run-http:
	@echo "Running Chuk MCP Playbook Server (HTTP mode)..."
	@if command -v uv >/dev/null 2>&1; then \
		PYTHONPATH=src uv run chuk-mcp-playbook http; \
	else \
		PYTHONPATH=src python -m chuk_mcp_playbook.server http; \
	fi

# Build the project
build: clean-build
	@echo "Building project..."
	@if command -v uv >/dev/null 2>&1; then \
		uv build; \
	else \
		python -m build; \
	fi
	@echo "Build complete. Distributions are in the 'dist' folder."

# Docker targets
docker-build:
	@echo "Building Docker image..."
	docker build -t chuk-mcp-playbook:latest .
	@echo "Docker image built: chuk-mcp-playbook:latest"

docker-run:
	@echo "Running Docker container..."
	docker run --rm -p 8000:8000 chuk-mcp-playbook:latest
