# Student Submission

Name: Babu
Date: 2026-08-20
Commit hash: 0ddfed0

## 1. Baseline observations

What was visible at L1?

At L1, only the skill name `renewal-advisor` and its placeholder description (`TODO - replace this with accurate L1 routing metadata without policy details.`) were visible. No details of the policies or resources were exposed at this level.

What weaknesses did you observe before completing `SKILL.md`?

Since `SKILL.md` was entirely unconfigured and consisted of `TODO` placeholders, the agent was unable to find specific routing directions, trigger rules, or resource paths. As a result, it could not load L3 references, run the deterministic python calculator, or cite policy documents correctly.

## 2. Trace evidence

| Case | L1 observed | L2 loaded? | Exact L3 paths loaded | Irrelevant paths avoided | Result |
| --- | --- | --- | --- | --- | --- |
| A | `renewal-advisor` | Yes | `references/discount-policy.md` | `references/renewal-process.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md`, `scripts/calculate_quote.py` | Correctly identified the VP Sales & Finance Business Partner approval route; cited the source. |
| B | `renewal-advisor` | Yes | `references/renewal-process.md` | `references/discount-policy.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md`, `scripts/calculate_quote.py` | Correctly identified the 90–61 days milestone actions (internal review, risks, constraints); cited the source. |
| C | `renewal-advisor` | Yes | `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md` | `scripts/calculate_quote.py` | Generated a complete multi-source action plan (CRO/Finance approval, 10-day timeline, auto-renewal removal Legal route); cited sources. |
| D | `renewal-advisor` | Yes | `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md`, `scripts/calculate_quote.py` | None (all required for calculations, policy analysis, and formatting) | Formatted a complete approval brief using the template, ran the calculator ($27k discount, $123k net ARR), and cited all sources. |
| E | `renewal-advisor` | Yes | `references/discount-policy.md`, `scripts/calculate_quote.py` | `references/renewal-process.md`, `references/risk-escalation.md`, `assets/renewal-brief-template.md` | Deterministically calculated the quote values ($11,040.00 discount, $80,960.00 net ARR) and checked discount approvals; cited sources. |
| F | `renewal-advisor` | Yes | `references/risk-escalation.md` | `references/discount-policy.md`, `references/renewal-process.md`, `assets/renewal-brief-template.md`, `scripts/calculate_quote.py` | Safely refused to invent control IDs, stated sources do not support it, and routed the escalation to Legal and Service Reliability. |

## 3. Evaluation scores

Score each item 0 or 1.

| Eval ID | Selection | Minimum resources | Correct facts | Citation | Safe handling | Total /5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| L1-01 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |
| L3-01 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |
| L3-02 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |
| L3-03 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |
| L3-04 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |
| SAFE-01 | 1 | 1 | 1 | 1 | 1 | 5 / 5 |

## 4. Reflection

### Why is policy detail stored at L3 instead of L1?

Storing detailed policy at L3 prevents prompt bloat and keeps the LLM's initial context window small. This reduces token consumption, latency, and context confusion, ensuring the agent only reviews policy details when a relevant query triggers that specific resource.

### What is the difference between a skill and a tool in this lab?

A **Skill** represents reusable domain expertise and contains procedure instructions, examples, and resource mappings. A **Tool** is a low-level capability exposed to the agent by the platform (e.g., `load_skill_resource` or `run_skill_script`) to perform actions in the environment.

### Give one example where loading fewer resources improves the agent.

In Case A, loading only `references/discount-policy.md` ensures the agent stays focused on the approval band rules, saves tokens, and avoids hallucinating or getting distracted by irrelevant details in other files (such as auto-renewal rules or timeline milestones).

### What failure could occur if `SKILL.md` names resources vaguely instead of using exact paths?

Vague resource names could cause the agent to hallucinate incorrect file paths, load wrong files, or fail to find any resource. This might lead to execution errors (e.g. file not found), multiple retries that exhaust rate limits, or the agent fabricating facts because it cannot access the source documentation.

## 5. Test output

```text
7 passed in 0.06s
```
