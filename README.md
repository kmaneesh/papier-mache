# Academic Research Skills for Agents

Papier-mache is a comprehensive suite of Skills and Tools for academic research, paper writing, peer review, and orchestration. It is designed to work with Codex and other editors that are not code-centric, making it accessible for users who prefer a more document-focused workflow. 

---

## Features

- **Deep Research** — 13-agent research team with Socratic guided mode + systematic review / PRISMA
- **Academic Paper** — 12-agent paper writing with LaTeX output hardening, visualization, revision coaching, and citation conversion
- **Academic Paper Reviewer** — Multi-perspective peer review with 0-100 quality rubrics (EIC + 3 dynamic reviewers + Devil's Advocate)
- **Academic Pipeline** — Full 10-stage pipeline orchestrator with adaptive checkpoints, claim verification, and material passport

### Full Pipeline

```
Research → Write → Integrity Check → Review (5-person) → Socratic Coaching
  → Revise → Re-Review → Re-Revise → Final Integrity Check → Finalize
  → Process Summary (with Collaboration Quality Evaluation)
```

**Key Features:**
1. Adaptive checkpoints (FULL / SLIM / MANDATORY) after every stage
2. Pre-review integrity verification — 100% reference, data, and claim validation (Phase A-E)
3. Two-stage review with Devil's Advocate + 0-100 quality rubrics
4. Socratic revision coaching between review and revision stages
5. Final integrity verification before publication
6. Output: MD + DOCX + LaTeX (APA 7.0 `apa7` class / IEEE / Chicago) → PDF via tectonic
7. Post-pipeline process summary with 6-dimension collaboration quality scoring (1–100)
8. Material passport for mid-entry provenance tracking
9. Cross-skill mode advisor (14 scenarios + user archetypes)

---

## Showcase: Real Pipeline Output

See the complete artifacts from a real 10-stage pipeline run — including **peer review reports, integrity verification reports, and the final paper**:

**[Browse all pipeline artifacts →](examples/showcase/)**

| Artifact | Description |
|----------|-------------|
| [Final Paper (EN)](examples/showcase/full_paper_apa7.pdf) | APA 7.0 formatted, LaTeX-compiled |
| [Integrity Report — Pre-Review](examples/showcase/integrity_report_stage2.5.pdf) | Stage 2.5: caught 15 fabricated refs + 3 statistical errors |
| [Integrity Report — Final](examples/showcase/integrity_report_stage4.5.pdf) | Stage 4.5: zero regressions confirmed |
| [Peer Review Round 1](examples/showcase/stage3_review_report.pdf) | EIC + 3 Reviewers + Devil's Advocate |
| [Re-Review](examples/showcase/stage3prime_rereview_report.pdf) | Verification after revisions |
| [Peer Review Round 2](examples/showcase/stage3_review_report_r2.pdf) | Follow-up review |
| [Response to Reviewers](examples/showcase/response_to_reviewers_r2.pdf) | Point-by-point author response |
| [Post-Publication Audit Report](examples/showcase/post_publication_audit_2026-03-09.md) | Independent full-reference audit: found 21/68 issues missed by 3 rounds of integrity checks |

---

## Performance Notes


> The full academic pipeline (10 stages) consumes a **large amount of tokens** — a single end-to-end run can exceed 200K input + 100K output tokens depending on paper length and revision rounds. Budget accordingly.
>
> Individual skills (e.g., `deep-research` alone, or `academic-paper-reviewer` alone) consume significantly less.



## Usage Overview

- **Skills**: Each skill (deep-research, academic-paper, academic-paper-reviewer, academic-pipeline) can be used independently or in combination. You can trigger research, writing, review, or full pipeline orchestration as needed.
- **Custom Tools**: Custom tools are available to download papers and manage research materials. These tools are accessible from the editor interface and do not require code interaction.
- **Delegation of Large Tasks**: Token-intensive or complex operations (such as full paper generation or large-scale literature review) are delegated to deterministic Python tools. This ensures reliability and reproducibility, and avoids overloading the editor or skill agents.

## Getting Started

1. Open papier-mache in Codex or your preferred editor.
2. Select the skill or tool you want to use (research, write, review, pipeline).
3. For downloading papers or handling large tasks, use the custom tools provided. These will run deterministic Python scripts in the background and return results to your editor.
4. Review outputs, make edits, and iterate as needed.

## Workflow Example

1. Start with deep-research to investigate your topic.
2. Use academic-paper to draft and structure your manuscript.
3. Apply academic-paper-reviewer for peer review and feedback.
4. Use academic-pipeline to orchestrate the full process if desired.
5. For large or complex tasks, delegate to Python tools via the editor interface.

## Key Philosophy

- **Orchestra Conductor Architecture**: Papier-mache is not just a collection of prompts; it is a 10-stage orchestration of specialized agents (13 for research, 12 for writing). The AI acts as the **Conductor**, firing each agent sequentially.
- **Tool-First Search (Deterministic)**: To save tokens and ensure academic reproducibility, all literature searches are handled by Python scripts (`tools/`) rather than stochastic web searches.
- **Works with Document-Focused Editors**: Designed for Codex, Claude Projects, and other non-code-centric environments.


## Installation and Use

Papier-mache can be used in a variety of editors and platforms. You do not need to set up any API keys or perform coding tasks. Simply download or copy the skills and reference files into your preferred workspace or project folder.

### Methods

- **Local Folder**: Download or clone the repository and place it in your project or research folder. The skills and templates will be available for use in your editor.
- **Desktop Workspace**: Open the folder in your desktop editor (such as Codex, Claude Cowork, or any document-focused tool). The skills will be auto-detected and ready for use.
- **Web Platform**: Upload the SKILL.md files and reference materials to your web-based research platform (such as claude.ai Projects). Follow the platform's instructions for adding files.

No coding or API setup is required. All features are accessible through the editor interface.

---

## Usage


### Quick Start

```
# Start a full research pipeline
You: "I want to write a research paper on AI's impact on higher education QA"


# Start with Socratic guidance
You: "Guide my research on AI in educational evaluation"


# Write a paper with guided planning
You: "Guide me through writing a paper on demographic decline"


# Review an existing paper
You: "Review this paper" (then provide the paper)


# Check pipeline status
You: "status"

```

### Individual Skills

#### Deep Research (7 modes)
```
"Research the impact of AI on higher education"       → full mode

"Give me a quick brief on X"                          → quick mode

"Do a systematic review on X with PRISMA"             → systematic-review mode (new)

"Guide my research on X"                              → socratic mode (guided)

"Fact-check these claims"                             → fact-check mode

"Do a literature review on X"                         → lit-review mode

"Review this paper's research quality"                → review mode

```

#### Academic Paper (9 modes)
```
"Write a paper on X"                                  → full mode

"Guide me through writing a paper"                    → plan mode (guided)

"I have a draft, here are reviewer comments"          → revision mode

"Parse these reviewer comments into a roadmap"        → revision-coach mode (new)
"Convert to LaTeX" / "Convert citations to IEEE"      → format-convert mode
"Check citations"                                     → citation-check mode
"Write a bilingual abstract"                          → bilingual-abstract mode
"Polish my writing style"                             → writing-polish mode
"Write the full paper autonomously"                   → full-auto mode
```

#### Academic Paper Reviewer (5 modes)
```
"Review this paper"                                   → full mode (EIC + R1/R2/R3 + Devil's Advocate)
"Quick assessment of this paper"                      → quick mode
"Guide me to improve this paper"                      → guided mode
"Check the methodology"                               → methodology-focus mode
"Verify the revisions"                                → re-review mode
```

#### Academic Pipeline (Orchestrator)
```
"I want to write a complete research paper"           → full pipeline from Stage 1
"I already have a paper, review it"                   → mid-entry at Stage 2.5 (integrity first)
"I received reviewer comments"                        → mid-entry at Stage 4
```
> Pipeline ends with **Stage 6: Process Summary** — auto-generates a paper creation process record with 6-dimension Collaboration Quality Evaluation (1–100 scoring).


### Supported Citation Formats

- APA 7.0 (default, including Chinese citation rules)
- Chicago (Notes & Author-Date)
- MLA
- IEEE
- Vancouver

### Supported Paper Structures

- IMRaD (empirical research)
- Thematic Literature Review
- Theoretical Analysis
- Case Study
- Policy Brief
- Conference Paper

---

## Skill Details

### Deep Research (v2.3)

13-agent pipeline for rigorous academic research:

| Agent | Role |
|-------|------|
| Research Question Agent | FINER-scored RQ formulation |
| Research Architect | Methodology design |
| Bibliography Agent | Systematic literature search |
| Source Verification Agent | Evidence grading, predatory journal detection |
| Synthesis Agent | Cross-source integration |
| Report Compiler | APA 7.0 report drafting |
| Editor-in-Chief | Q1 journal editorial review |
| Devil's Advocate | Assumption challenging (3 checkpoints) |
| Ethics Review Agent | AI disclosure, attribution integrity |
| Socratic Mentor | Guided research dialogue with convergence criteria |
| Risk of Bias Agent | RoB 2 + ROBINS-I assessment, traffic-light output |
| Meta-Analysis Agent | Effect sizes, heterogeneity, forest plot data, GRADE |
| Monitoring Agent | Post-pipeline literature monitoring alerts |

**Modes:** full, quick, paper-review, lit-review, fact-check, socratic, **systematic-review** (new)

### Academic Paper (v2.4)

12-agent pipeline for academic paper writing:

| Agent | Role |
|-------|------|
| Intake Agent | Configuration interview + handoff detection |
| Literature Strategist | Search strategy + annotated bibliography |
| Structure Architect | Paper outline + word allocation |
| Argument Builder | Thesis + claim-evidence chains |
| Draft Writer | Section-by-section writing |
| Citation Compliance | Multi-format citation audit + APA↔Chicago↔MLA↔IEEE↔Vancouver conversion |
| Abstract Bilingual | EN + Chinese abstracts |
| Peer Reviewer | 5-dimension review (max 2 rounds) |
| Formatter | LaTeX/DOCX/PDF output — mandatory `apa7` class, XeCJK bilingual, `ragged2e` justification fix, tectonic compilation |
| Socratic Mentor | Chapter-by-chapter guided planning with convergence criteria |
| Visualization Agent | 9 chart types, matplotlib/ggplot2, APA 7.0 standards |
| Revision Coach Agent | Parses unstructured reviewer comments → Revision Roadmap |

**Modes:** full, plan, revision, citation-check, format-convert, bilingual-abstract, writing-polish, full-auto, **revision-coach** (new)

### Academic Paper Reviewer (v1.4)

7-agent multi-perspective review with **0-100 quality rubrics**:

| Agent | Role |
|-------|------|
| Field Analyst | Identifies domain, configures reviewer personas |
| Editor-in-Chief | Journal fit, novelty, significance |
| Methodology Reviewer | Research design, statistics, reproducibility |
| Domain Reviewer | Literature coverage, theoretical framework |
| Perspective Reviewer | Cross-disciplinary, practical impact |
| Devil's Advocate Reviewer | Core thesis challenge, logical fallacy detection, strongest counter-argument |
| Editorial Synthesizer | Consensus analysis, revision roadmap, **rubric-based scoring** |

**Modes:** full, re-review (verification), quick, methodology-focus, guided

**Decision mapping:** ≥80 Accept, 65-79 Minor Revision, 50-64 Major Revision, <50 Reject

### Academic Pipeline (v2.6)

10-stage orchestrator with integrity verification, two-stage review, Socratic coaching, and collaboration evaluation:

| Stage | Skill | Purpose |
|-------|-------|---------|
| 1. RESEARCH | deep-research | Clarify RQ, find literature |
| 2. WRITE | academic-paper | Draft the paper |
| **2.5. INTEGRITY** | **integrity_verification_agent** | **100% reference & data verification (v2.0: anti-hallucination mandate)** |
| 3. REVIEW | academic-paper-reviewer | 5-person review (EIC + R1/R2/R3 + Devil's Advocate) |
| → | *Socratic Revision Coaching* | *Guide user through review feedback* |
| 4. REVISE | academic-paper | Address review comments |
| 3'. RE-REVIEW | academic-paper-reviewer | Verification review of revisions |
| → | *Socratic Residual Coaching* | *Guide user through remaining issues (if Major)* |
| 4'. RE-REVISE | academic-paper | Final revision (if needed) |
| **4.5. FINAL INTEGRITY** | **integrity_verification_agent** | **100% final verification (zero issues required)** |
| 5. FINALIZE | academic-paper | Ask format style → MD + DOCX + LaTeX → tectonic → PDF |
| **6. PROCESS SUMMARY** | **pipeline** | **Paper creation process record + Collaboration Quality Evaluation (1–100)** |

**Pipeline guarantees:**
- Every stage requires user confirmation checkpoint
- Integrity verification (Stage 2.5 + 4.5) cannot be skipped
- Reproducible — standardized process with full audit trail
- Post-pipeline collaboration evaluation with honest, evidence-based scoring

---

## License

This work is licensed under [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).


---

## Credit

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

