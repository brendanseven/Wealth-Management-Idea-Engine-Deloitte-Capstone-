# Wealth Management Idea Engine

Deloitte Capstone Project
Carnegie Mellon University, Tepper School of Business
MS in Business Analytics, Class of 2026

## Project Purpose

Wealth management firms lack a structured, repeatable way to identify and prioritize new product opportunities. Product development decisions are fragmented, driven by qualitative judgment, and slow to respond to market shifts.

The Wealth Management Idea Engine is an AI-powered decision-support tool that addresses this gap. It ingests real market signals (competitor product launches, macroeconomic indicators, fund flow data), generates concrete product and service ideas using a large language model (Claude via AWS Bedrock), organizes them into navigable thematic hierarchies, and scores each idea on a Desirability-Viability-Feasibility (DVF) framework.

The hierarchical organization and interactive feedback loop features are informed by research on AI-assisted creative ideation from CMU's Human-Computer Interaction Institute (Yang et al., 2025).

## How to Run

### Prerequisites

- Python 3.8+
- AWS account with Bedrock access (for live idea generation)
- AWS credentials configured (for Bedrock API calls)

### Local Setup

```bash
git clone https://github.com/brendanseven/Wealth-Management-Idea-Engine-Deloitte-Capstone-.git
cd Wealth-Management-Idea-Engine-Deloitte-Capstone-
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app will open at http://localhost:8501.

### AWS Deployment

A CloudFormation template (`cloudformation.yaml`) is included for infrastructure-as-code deployment. It provisions an EC2 instance with the necessary IAM roles for Bedrock access, security group rules, and an Elastic IP. See `docs/aws-deployment.md` for detailed instructions.

### Running Without AWS/Bedrock

The app works without Bedrock access using the pre-built scenarios. Select "Pre-built Scenarios" in the sidebar to explore two fully populated demo scenarios with 13 product ideas, thematic hierarchies, and feedback loop content. Live idea generation requires Bedrock access.

## Repository Structure

```
.
├── app.py                          # Main Streamlit application (entry point)
├── context_assembler.py            # Formats market data into LLM prompt context
├── generate_scenarios.py           # Script that generated pre-built scenario data
├── requirements.txt                # Python dependencies
├── cloudformation.yaml             # AWS CloudFormation IaC template
│
├── data/
│   ├── competitor_tracker_merged.csv   # 49 competitor product launches (10 firms, Sep 2024-Mar 2026)
│   ├── market_context.txt              # Assembled market context for LLM prompt
│   ├── data_config.json                # Data source metadata
│   └── data-access.md                  # Data sourcing notes and access information
│
├── results/
│   ├── idea_engine_scenarios.json      # Pre-built scenario outputs (2 scenarios, 13 ideas)
│   └── hierarchy_and_feedback.json     # Hierarchical organization + feedback loop data
│
├── docs/
│   ├── data-dictionary.md              # Field definitions for all data files
│   ├── api-usage.md                    # LLM prompt engineering and API integration notes
│   └── aws-deployment.md              # AWS deployment instructions
│
└── README.md
```

### Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main application. Streamlit UI with pre-built scenarios, live AI generation via Bedrock, thematic hierarchy view, DVF scoring with adjustable weights, and interactive feedback loop. |
| `context_assembler.py` | Reads competitor tracker and macro data, formats them into structured context that gets injected into the LLM prompt. Ensures AI-generated ideas are grounded in real market intelligence. |
| `generate_scenarios.py` | The script used to generate the pre-built demo scenarios. Contains the full LLM system prompt and two complete scenario outputs. |
| `competitor_tracker_merged.csv` | Real competitor data: 49 product launches across JP Morgan, Morgan Stanley, Merrill Lynch, Schwab, Fidelity, UBS, Wells Fargo, Goldman Sachs, Raymond James, and Edward Jones. |
| `idea_engine_scenarios.json` | Pre-generated output from the Idea Engine: two market scenarios with 13 total product ideas, each with DVF scores, justifications, risks, and next steps. |
| `hierarchy_and_feedback.json` | Thematic hierarchy organization for both scenarios, plus deep-dive feedback data (product variations, segment adaptations, implementation plans) for select ideas. |
| `cloudformation.yaml` | AWS CloudFormation template generated via IaC Generator. Captures the full infrastructure setup for reproducible deployment. |

## Features

**AI-Powered Ideation**: Claude (via AWS Bedrock) synthesizes real competitor data, macroeconomic indicators, and fund flow trends into concrete product and service concepts for wealth management firms.

**Hierarchical Organization**: Informed by Yang et al. (2025), generated ideas are automatically organized into strategic themes and sub-categories using a second AI call. Users explore at different levels of abstraction rather than scrolling a flat list.

**DVF Scoring Framework**: Every idea is scored 0-100 on Desirability (client demand), Viability (business economics), and Feasibility (implementation readiness). Each score includes a written justification. Dimension weights are adjustable via sliders.

**Interactive Feedback Loop**: Promising ideas can be explored further through product variations, segment adaptations (how the idea changes for different client types), and implementation deep dives (critical path, key decisions, cost estimates).

**Real Data Grounding**: The LLM prompt includes 49 real competitor product launches and current macroeconomic context, reducing hallucination risk and producing ideas that reference actual market moves.

## Tech Stack

- **Frontend**: Streamlit (Python)
- **AI/LLM**: Anthropic Claude (Haiku 4.5) via AWS Bedrock
- **Infrastructure**: AWS EC2, IAM, CloudFormation
- **Data Sources**: PitchBook, SEC EDGAR, FRED, ICI, Morningstar, industry publications

## References

Yang, Y., Mohanty, V., Martelaro, N., Kittur, A., Chen, Y.-Y., & Hong, M. K. (2025). From Overload to Insight: Scaffolding Creative Ideation through Structuring Inspiration. arXiv:2504.15482. Carnegie Mellon University.

## Contact

**Brendan Bourges-Sevenier**
MS in Business Analytics, Class of 2026
Carnegie Mellon University, Tepper School of Business
bbourges@andrew.cmu.edu
