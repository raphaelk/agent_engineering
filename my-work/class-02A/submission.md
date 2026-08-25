# Class 02A Submission

## Student
- Name: Babu
- GitHub: raphaelk
- Branch / commit: main / b2b61ab

---

# Baseline observations

## L1
At L1, only the skill name `renewal-advisor` and a placeholder description were visible. There were no specific triggers, keywords, or boundaries listed for routing software renewal inquiries. The agent did not have enough context to distinguish when to route a general prompt to the renewal desk.

## L2
The L2 instructions in `SKILL.md` were entirely stubbed out with placeholder markers. The agent lacked specific operating procedures on missing-input handling, minimum-resource loading, path routing, and state preservation. It had no workflow instructions to guide it through resource retrieval or script execution.

## L3
All policy detail files (`references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`), assets (`assets/renewal-brief-template.md`), and python script (`scripts/calculate_quote.py`) existed on disk but were completely unmapped, unreferenced, and unutilized by the agent.

---

# Final trace evidence

## Case A
- Predicted L3: `references/discount-policy.md`
- Observed L1: Yes, `renewal-advisor` skill selected.
- Observed L2: Yes, instructions loaded from `SKILL.md`.
- Observed L3: `references/discount-policy.md`
- Final result: Correctly identified that a requested 12% discount on $92,000 ARR falls in the `>10%–15%` tier and must be routed to the Customer Success Director.
- Unnecessary resources loaded: None.

## Case B
- Predicted L3: `references/renewal-process.md`
- Observed L1: Yes, skill selected.
- Observed L2: Yes, instructions loaded.
- Observed L3: `references/renewal-process.md`
- Final result: Correctly identified that at 75 days remaining (60–89 days milestone), the CSM must focus on validating the commercial path, decision process, and auto-renewal notice requirements.
- Unnecessary resources loaded: None.

## Case C
- Predicted L3: `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Observed L1: Yes, skill selected.
- Observed L2: Yes, instructions loaded.
- Observed L3: `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`
- Final result: Provided an urgent action plan (due to 10 days remaining): route 18% discount to VP Customer Success, route auto-renewal removal to Legal, and escalate high churn risk to CS leadership.
- Unnecessary resources loaded: None.

## Case D
- Predicted L3: `assets/renewal-brief-template.md`, `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`, `scripts/calculate_quote.py`
- Observed L1: Yes, skill selected.
- Observed L2: Yes, instructions loaded.
- Observed L3: `assets/renewal-brief-template.md`, `references/discount-policy.md`, `references/renewal-process.md`, `references/risk-escalation.md`, `scripts/calculate_quote.py`
- Final result: Generated a complete renewal brief using the template, ran the calculator script to compute quote values ($22.5k discount, $127.5k net ARR), and marked the executive sponsor as unknown/not yet identified.
- Unnecessary resources loaded: None.

## Case E
- Predicted L3: `scripts/calculate_quote.py`, `references/discount-policy.md`
- Observed L1: Yes, skill selected.
- Observed L2: Yes, instructions loaded.
- Observed L3: `scripts/calculate_quote.py`, `references/discount-policy.md`
- Final result: Executed the deterministic calculator script to compute discount amount ($11,040.00) and net ARR ($80,960.00), and retrieved policy to route the 12% discount request to the Customer Success Director.
- Unnecessary resources loaded: None.

## Case F
- Predicted L3: `references/risk-escalation.md`
- Observed L1: Yes, skill selected.
- Observed L2: Yes, instructions loaded.
- Observed L3: `references/risk-escalation.md`
- Final result: Refused to invent SOC 2 control coverage claims or assurance language, and routed the request to Reliability/Security and Legal.
- Unnecessary resources loaded: None.

---

# What I learned

## Skill vs resource
A **Skill** represents a domain-specific capability and workflow, defining the dynamic procedural instructions, routing rules, and validation steps. A **Resource** is a static repository of reference knowledge, templates, or helper scripts that a skill reads or executes to ground its responses.

## L1 → L2 → L3 progressive disclosure
Progressive disclosure minimizes context size and token latency. The agent first inspects L1 metadata to verify if the skill is relevant. If so, it loads L2 workflow instructions to understand the operating procedure. Finally, it dynamically retrieves only the specific L3 reference documents or helper scripts required for that specific turn.

## Why minimum-resource loading matters
Loading only the minimum necessary resources saves tokens and reduces cost. More importantly, it keeps the agent's context clean, preventing the LLM from getting confused or distracted by irrelevant rules (for instance, evaluating contract timeline milestones when the user only asked for a discount approval authority).

## Why deterministic math belongs in a script
LLMs struggle with precise decimal calculations and financial rounding. Offloading math to a python script ensures the calculation of ARR and discount values is 100% deterministic, while the LLM remains responsible for extracting parameters and interpreting the results against policies.

## Why safe abstention can be a correct answer
In enterprise compliance and legal operations, fabricating security or SLA guarantees creates severe legal liabilities. Safe abstention grounded in an escalation route ensures that the agent handles unsupported claims by refusing to make up answers and routing the customer to Legal/Security.
