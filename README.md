# Wealth Management Idea Engine
## Deloitte Capstone - Group 2

### Quick Start

1. Make sure you have Python 3.8+ installed
2. Install the dependency:
   ```
   pip install streamlit
   ```
3. Put `app.py` and `idea_engine_scenarios.json` in the same folder
4. Run the app:
   ```
   streamlit run app.py
   ```
5. A browser tab will open automatically at http://localhost:8501

### What This Is

An AI-powered ideation and prioritization tool for wealth management product strategy.
The tool takes market scenarios (competitor moves, demographic shifts, macro trends)
and generates prioritized product/service ideas scored on the DVF framework:

- **Desirability**: Is there client/market demand?
- **Viability**: Can the firm generate meaningful revenue?
- **Feasibility**: How practical is implementation?

### How to Use It

- **Left sidebar**: Select a scenario, adjust DVF weights, filter by category
- **Main panel**: View ranked ideas with scores, descriptions, and full analysis
- **DVF sliders**: Change the weight of each dimension and watch the rankings shift in real time
- **Expand cards**: Click "View full analysis" for score justifications, risks, and next steps

### Files

- `app.py` - The Streamlit application
- `idea_engine_scenarios.json` - Pre-generated scenario data (2 scenarios, 13 ideas)
- `generate_scenarios.py` - The script that produced the scenario data (includes the LLM system prompt)

### Current Scenarios

1. **The Alternatives Democratization Play** - Competitors launching retail alt products, how to respond
2. **The Aging Affluent & Retirement Income Crisis** - Wealth transfer, retirement income anxiety, heir retention

### Future Enhancements (Final Deliverable)

- Live LLM integration via Anthropic API for real-time idea generation
- Client segmentation layer using consumer demographic data
- Additional pre-built scenarios
- Enhanced visualizations and export functionality
