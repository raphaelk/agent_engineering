# Class 3 Starter — WidgetWare SDR Context Package

This is the minimal starting project for Class 3.

## Source of truth

Read `SPEC.md` before implementing the lab. Use `LAB.md` for detailed guidance.

The starter intentionally does **not** include:

- WidgetWare product configuration;
- ICP configuration;
- policy configuration;
- agent instructions;
- the context builder;
- completed scenario fixtures;
- completed Class 3 tests.

Students will create those items during the lab.

## Setup

From this directory, set up a virtual environment and install the package:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies in editable mode
pip install -e ".[dev]"

# Run tests
pytest -v
```

Alternatively, you can run tests directly using the virtual environment's executable:

```bash
.venv/bin/pytest -v
```

All 28 tests must pass successfully.


## Important boundaries

Class 3 does not build:

- a Google ADK agent;
- Gemini or another LLM call;
- web research;
- email or social-message delivery;
- CRM integration;
- a database;
- deployment code;
- external side effects.
