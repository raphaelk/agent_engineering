# Class 3 Acceptance Criteria

This document lists the observable conditions required for the successful completion of the WidgetWare SDR Context Package (Class 3).

## 1. Required Files
The repository must contain the following files in the specified structure:
* `config/products.yaml`
* `config/icp.yaml`
* `config/policies.yaml`
* `docs/widgetware-business-brief.md`
* `docs/acceptance-criteria.md`
* `src/widgetware_sdr/__init__.py`
* `src/widgetware_sdr/instructions.py`
* `src/widgetware_sdr/context_builder.py`
* `tests/unit/test_context_builder.py`
* `tests/scenarios/qualified_account.yaml`
* `tests/scenarios/unqualified_account.yaml`
* `tests/scenarios/insufficient_evidence.yaml`
* `tests/scenarios/prompt_injection.yaml`

## 2. Configuration & Validation
* YAML files must be valid and load successfully.
* `products.yaml` must contain WidgetWare company details and at least two products with target buyers and approved claims.
* `icp.yaml` must contain company size thresholds, preferred/excluded industries, preferred regions, buying signals, and required fields.
* `policies.yaml` must define evidence categories (`verified_fact`, `derived_fact`, `inference`, `unknown`, `conflict`), prohibited actions, and human approval gates.

## 3. Architecture & Separation of Concerns
* The context builder must return exactly five distinct, non-overlapping context layers:
  1. `system_instructions` (stable behavioral rules)
  2. `business_context` (products, ICP, policies)
  3. `task_context` (current account and objective)
  4. `retrieved_evidence` (facts/inferences with provenance)
  5. `state` (workflow execution state)
* Task context (e.g., untrusted account notes) must never override system instructions or business policies.

## 4. Evidence Integrity & Provenance
* Every retrieved evidence record must preserve provenance (claim, classification, source, retrieved_at date, and excerpt).
* Unknown information must remain unknown; the builder must not invent values or interpolate missing fields.

## 5. Security & Safety Boundaries
* Untrusted user notes or retrieved content must not authorize any external actions or override policies (protection against prompt injection).
* Prohibited actions (e.g., sending emails, making contractual/pricing commitments, or modifying CRM data) must remain explicitly unauthorized.

## 6. Scenario Fixtures & Testing
* The four required scenarios must exist as valid YAML files in `tests/scenarios/`:
  1. Qualified Account
  2. Unqualified Account
  3. Insufficient Evidence
  4. Prompt Injection
* All tests (configuration, instructions, context builder, and scenarios) must pass successfully via `pytest`.

## 7. Negative Constraints
* No Google ADK agent exists.
* No Gemini or other LLM calls exist.
* No live network research is performed.
* No external side effects occur.
