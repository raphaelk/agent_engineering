---
name: renewal-advisor
description: Evaluates WidgetWare enterprise software renewals, including discount approval routing, renewal timing and milestones, risk escalations, formatting approval briefs, and quote calculations. Excludes general product troubleshooting or IT support.
---

# Renewal Advisor

This skill provides step-by-step guidance to customer-success managers (CSMs) and sales representatives on evaluating and processing WidgetWare enterprise renewals, routing commercial approvals, and managing risk escalations.

## When to use

Use this skill when processing enterprise software contract renewals. Relevant situations include:
- Routing discount approval requests to correct organizational levels.
- Checking required commercial actions on the renewal timeline.
- Evaluating risk levels and routing legal, security, or executive escalations.
- Preparing formal renewal approval briefs using the official template.
- Performing deterministic quote and discount calculations.

## When not to use

Do not use this skill for:
- General product troubleshooting, IT support, or platform debugging.
- Retrieving specific SOC 2 compliance control details or security certifications.
- Promising new recovery-time guarantees or service-level agreements not in the signed contract.

## Required inputs

To analyze a renewal, the following inputs are required depending on the request:
- Current or List Annual Recurring Revenue (ARR).
- Requested discount percentage.
- Renewal date or days remaining until renewal.
- Customer name and churn risk level.
- Customer-specific requests (e.g., auto-renewal removal).

If required inputs are missing, ask the customer-success manager or user to provide them before proceeding. Do not proceed with missing inputs.

## Procedure

1. Identify the question type (e.g., discount band, process timeline, risk level, calculation, or brief generation).
2. Check if the required inputs for that query are provided. If there is a missing input, request it.
3. Consult the Resource routing map to identify the exact L3 resource path.
4. Load the minimum resource necessary for the query. Do not load irrelevant files to ensure minimum resource loading.
5. If the user explicitly asks to calculate a net ARR or dollar discount amount, run the deterministic script `scripts/calculate_quote.py` using `run_skill_script`. You must pass the script arguments in the `args` parameter as a dictionary containing the keys `"arr"` (the current/list ARR) and `"discount-pct"` (the discount percentage, using a hyphen, NOT an underscore). For example: `{"arr": 92000, "discount-pct": 12}`. Do NOT run this script if the user only asks for the approval path or process timeline without asking for calculation.
6. Retrieve the required facts from the loaded L3 reference file.
7. Generate a response showing concise reasoning, citing the exact relative path of the source file, and differentiating states clearly.

## Resource routing map

Map each query type to the exact path of the minimum necessary reference, asset, or script:
- For discount approval bands, thresholds, and routing: `references/discount-policy.md`
- For renewal timeline milestones and commercial rules: `references/renewal-process.md`
- For risk triggers, recovery commitments, compliance requests, and escalation routes: `references/risk-escalation.md`
- For generating or formatting a renewal brief: `assets/renewal-brief-template.md`
- For calculating net ARR or discount amounts: `scripts/calculate_quote.py` (invoke via `run_skill_script` using `"arr"` and `"discount-pct"` keys in the `args` dict)

## Output contract

- Show concise reasoning.
- Cite every policy conclusion using the exact relative path, e.g., `[Source: references/discount-policy.md]`, `[Source: references/renewal-process.md]`, etc.
- Use the exact structure from `assets/renewal-brief-template.md` when preparing briefs.
- Clearly separate states using the terms: **requested**, **routed**, or **approved**. Do not describe a requested discount as approved until the required approvers have explicitly signed off.
- All ARR and discount calculations must be computed using `scripts/calculate_quote.py`.

## Unsupported and missing-source behavior

If the question is about specific SOC 2 control mappings, recovery-time guarantees, or other policies not found in the resources:
- State that the supplied sources do not establish or support the request, indicating it is unsupported.
- Refuse to invent any policy exception, deadline, control ID, or commercial commitment.
- Route the escalation to the proper reviewer specified in `references/risk-escalation.md` (e.g., Security, Legal, Service Reliability).

## Examples

### Positive

- **User**: "The renewal ARR is $92,000 and the requested discount is 12%. Which approval path is required?"
- **Response**: (Loads `references/discount-policy.md` only) "The requested discount of 12% falls into the 'More than 10%–15%' band. This requires approval from the VP Sales and the Finance Business Partner. [Source: references/discount-policy.md]"

### Negative

- **User**: "How do I reset my WidgetWare password?"
- **Response**: "I cannot help with technical support issues. Please contact the IT support desk." (Does not use this skill)

### Ambiguous

- **User**: "What is the action plan for this customer's renewal?"
- **Response**: "To provide the correct action plan, please specify the number of days remaining until the renewal date, the churn risk level, and any specific customer requests."
