# AGENT GUIDE: Papier-mache Academic Pipeline

This guide is for AI agents interacting with the Papier-mache repository. It outlines the architecture, tool protocols, and strategies for token-efficient academic research and writing.

## 🏗️ Repository Architecture

Papier-mache is a modular system composed of **Skills**, **Agents**, and **Deterministic Tools**.

1.  **Skills (`skills/`)**: High-level workflows (e.g., `deep-research`, `academic-paper`).
2.  **Agents (`skills/*/agents/`)**: Specialized LLM personas that handle specific cognitive tasks within a skill.
3.  **Tools (`tools/`)**: Python scripts for heavy-lifting (downloading papers, parsing data, local search).
4.  **Schemas (`pipeline.md`)**: Data contracts that govern handoffs between agents and skills.

## ⚙️ Environment Setup

To ensure deterministic execution, always use the project's virtual environment. If `.venv` is missing, create it using Python 3.11:

```bash
python3.11 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
```

## 🛠️ Tool Usage Protocol

Agents should prioritize using scripts in `tools/` for data retrieval. Always invoke tools using the project virtual environment:

| Tool | Purpose | Usage Command |
| :--- | :--- | :--- |
| `download_arxiv.py` | Search & download from arXiv | `./.venv/bin/python3 tools/download_arxiv.py --query "..."` |
| `download_pubmed.py` | Search & download from PubMed | `./.venv/bin/python3 tools/download_pubmed.py --query "..."` |
| `download_openalex.py` | Search & download from OpenAlex| `./.venv/bin/python3 tools/download_openalex.py --query "..."` |

**Agent Rule**: When performing literature searches (`bibliography_agent`), always check if these tools can be used before attempting multi-turn web searches.

## 🔁 Handoff & Pipeline Logic

The `pipeline.md` file defines the **Ground Truth** for data exchange. 

- **Always Validate**: Before accepting a handoff from another agent, validate the input against the required fields in `pipeline.md`.
- **Schema Violations**: If a handoff is incomplete, trigger the `HANDOFF_INCOMPLETE` failure path and request re-generation with specific missing fields.
- **Material Passport**: Every artifact MUST contain a `Material Passport` (Schema 9) to track provenance and verification status.

## 💎 Token Efficiency Patterns

To optimize for performance and cost:

1.  **Delegate Summary**: Use smaller models (e.g., Gemini Flash) for `report_compiler` and `formatting` tasks.
2.  **Concentrate Logic**: Use larger models (e.g., Gemini Pro) for `synthesis_agent`, `devils_advocate`, and `editor_in_chief`.
3.  **Tool-First Retrieval**: Let Python tools download and index papers; agents should only read the extracted metadata or targeted sections.

## ⚠️ Critical Checkpoints

- **Devil's Advocate**: Mandatory checkpoints at Phase 1, 3, and 5.
- **Integrity Verification**: Stage 2.5 and 4.5 are **NON-SKIPPABLE**. They must pass 100% verification before proceeding to Review or Finalization.

---
*Version: 1.0*
*Last Updated: 2026-03-13*
