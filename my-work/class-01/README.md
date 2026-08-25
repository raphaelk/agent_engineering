# Class 1 Assignment

## Student Information
- Name: Raphael Kochuvaried
- GitHub username: raphaelk
- Date completed: 08/03/2026

## Workspace Setup
- [x] Forked the repo
- [x] Cloned my fork
- [x] Opened in AntiGravity
- [x] Created my-work/class-01
- [x] Committed and pushed

## What I learned

### 1. Git, GitHub, and Development Workflows
- **Reproducible State Control**: Learned the critical importance of creating a distinct work directory (`my-work/class-01`) separate from upstream templates, allowing for independent development. 
- **Upstream Synchronization**: Mastered setting up upstream tracking to sync baseline templates while maintaining custom assignment solutions in a fork.
- **Checkpoint Commit Pattern**: Practiced making granular, atomic commits mapping to specific steps in the development process to maintain a clean history and ease debugging.

### 2. AntiGravity IDE and Agentic Engineering Tools
- **Contextual Alignment**: Understood how tools such as `run_command`, `replace_file_content`, and `view_file` interact with the codebase. Learn how agents utilize metadata and rules inside `.agents/rules/` and `.agents/workflows/` to orient themselves.
- **Agent Alignment**: Discovered that clear, unambiguous project files (`SPEC.md` and `acceptance-criteria.md`) serve as a "contract" that keeps AI development agents properly aligned, preventing them from hallucinating capabilities or drifting from business requirements.

### 3. Repository Harnessing and Continuous Verification
- **Deterministic Quality Gates**: Realized that establishing a robust quality gate (`scripts/check.sh`) early is crucial. The harness combines code formatting (`ruff format`), static lint checks (`ruff check`), strict type enforcement (`mypy`), and contract tests (`pytest`) into a single command that runs deterministically.
- **Environment Invariant Verification**: Wrote and refined verification scripts (`scripts/verify_environment.py`) that validate python versions, package structures, and verify that no real API keys, environment configuration files (`.env`), or secret credentials have been accidentally committed.

### 4. Architectural Safety Boundaries
- **Bounded Autonomy (ADR 0001)**: Learned to restrict agent capabilities to the "Prepare" phase (preparing draft outreach and qualification results) rather than the "Execute" phase.
- **No-Outbound-Send Constraint (ADR 0002)**: Understood why the system must lack outbound capabilities (e.g. SMTP/HTTP send methods, CRM write APIs) by design, rather than relying on runtime model instructions. This provides a structural guarantee of safety.

## Completion Checklist
- [x] `./scripts/check.sh` passes cleanly from a fresh clone.
- [x] `pip install -e ".[dev]"` succeeds with no manual workaround.
- [x] `docs/widgetware-business-brief.md` states the product, ICP, and exclusions in a form someone unfamiliar with WidgetWare could repeat back correctly.
- [x] `SPEC.md` states required behavior, prohibited behavior, and completion criteria as falsifiable statements, not marketing language.
- [x] Every criterion in `docs/acceptance-criteria.md` Section A names a specific, checkable signal, and is actually checked by `./scripts/check.sh`.
- [x] All three `tests/scenarios/*.md` files have a matching pair in `tests/fixtures/accounts/` and `tests/fixtures/expected/`.
- [x] `docs/architecture.md` and the three architecture decision records are present and consistent with `SPEC.md`.
- [x] `.agents/rules/` and `.agents/workflows/` exist and describe real, followable practices.
- [x] No credential, API key, or real project identifier is committed anywhere.
- [x] No Gemini call, no ADK agent, and no send-capable code exists anywhere in this checkpoint.

## Status
- [x] Class 1 — Foundations and repository harness (Book 1, Chapters 1–2)
- [ ] Class 2 — Gemini context and instruction architecture
- [ ] Classes 3–10 — see `../../00_Course_Framework.md`

## Challenges

### Challenge 1: Package Importability and Virtual Environment Isolation
- **Problem**: When first running `./scripts/check.sh`, the check script crashed during `verify_environment.py` with `ModuleNotFoundError: No module named 'widgetware_sdr'`.
- **Root Cause**: The script was executed outside of an isolated virtual environment, or before the package itself was installed. In modern Python packaging, files inside `src/` are not on the system's `sys.path` by default. Without a proper package installation, the environment verification script cannot locate or import `widgetware_sdr`.
- **Resolution**: Resolved by creating a clean virtual environment via `python3 -m venv .venv`, activating it via `source .venv/bin/activate`, and executing `pip install -e ".[dev]"`. The `-e` flag performs an editable installation, creating a symlink in the `.venv`'s `site-packages` directory pointing to the local workspace. This ensures `widgetware_sdr` is importable system-wide inside the virtual environment without manual path modifications.

### Challenge 2: Translating Qualitative Business Rules into Falsifiable Technical Contracts
- **Problem**: Translating high-level, human-oriented business constraints (e.g. "do not send outbound messages") into strict, automated, and falsifiable technical specifications.
- **Root Cause**: Traditional specification documents are usually written in prose and are not easily mapable to automated tests, leading to drift or unaligned agents.
- **Resolution**: Designed specific contract tests in `tests/unit/test_repository_contract.py` that check for forbidden packages (`google.generativeai`, `google.adk`, `vertexai`), scan source files for send-shaped function patterns (`send_email`, `send_message`), and search the codebase for accidental API key or credential patterns using regular expressions. This successfully bridged the gap between human specification and automated machine verification.

