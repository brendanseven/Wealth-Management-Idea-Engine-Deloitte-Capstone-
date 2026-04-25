"""
Context Assembler for the Wealth Management Idea Engine
Reads the merged competitor tracker and macro summary,
formats them into structured context for the LLM prompt.
"""

import pandas as pd
import json


def load_competitor_data(filepath="competitor_tracker_merged.csv"):
    df = pd.read_csv(filepath, parse_dates=["launch_date"])
    return df


def summarize_competitor_landscape(df):
    """Condense 49 rows into a structured text summary for the LLM prompt."""
    
    lines = []
    lines.append("COMPETITOR PRODUCT LAUNCH DATA (Past 18 months, Sep 2024 - Mar 2026)")
    lines.append(f"Total launches tracked: {len(df)} across {df['firm'].nunique()} major wirehouses/wealth managers")
    lines.append("")
    
    # Launches by firm
    lines.append("Launches by firm:")
    for firm, count in df['firm'].value_counts().items():
        lines.append(f"  {firm}: {count} launches")
    lines.append("")
    
    # Group by rough asset class categories
    lines.append("Launches by asset class theme:")
    
    # Categorize into broader buckets
    def categorize(ac):
        ac_lower = str(ac).lower()
        if any(x in ac_lower for x in ['equity', 'equities', 'dividend']):
            if 'private' in ac_lower:
                return 'Private Equity / PE-like'
            return 'Public Equities (ETFs, SMAs)'
        elif any(x in ac_lower for x in ['fixed income', 'bond', 'credit', 'clo', 'mortgage', 'preferred', 'high yield', 'municipal']):
            return 'Fixed Income / Credit'
        elif any(x in ac_lower for x in ['private', 'alternative']):
            return 'Private Markets / Alternatives'
        elif any(x in ac_lower for x in ['cash', 'treasur', 'money market']):
            return 'Cash / Treasury'
        elif any(x in ac_lower for x in ['option', 'structured']):
            return 'Options / Structured'
        elif any(x in ac_lower for x in ['multi-asset', 'income']):
            return 'Multi-Asset / Income'
        elif any(x in ac_lower for x in ['retire']):
            return 'Retirement Services'
        else:
            return 'Other'
    
    df_cat = df.copy()
    df_cat['broad_category'] = df_cat['asset_class'].apply(categorize)
    for cat, count in df_cat['broad_category'].value_counts().items():
        lines.append(f"  {cat}: {count}")
    lines.append("")
    
    # Key product details (selected highlights)
    lines.append("Notable recent launches (selected):")
    
    # Pick the most interesting/relevant ones
    highlights = df.sort_values('launch_date', ascending=False).head(20)
    for _, row in highlights.iterrows():
        date_str = str(row['launch_date'])[:10] if pd.notna(row['launch_date']) else 'Unknown'
        fee_str = str(row['fees']) if pd.notna(row['fees']) else 'N/A'
        min_str = str(row['min_investment']) if pd.notna(row['min_investment']) else 'N/A'
        desc_str = str(row['description'])[:200] if pd.notna(row['description']) else ''
        lines.append(f"  - {row['firm']}: {row['product_name']} ({date_str})")
        lines.append(f"    Asset class: {row['asset_class']} | Structure: {row['product_structure']}")
        lines.append(f"    Target: {row['target_client']} | Min: {min_str} | Fees: {fee_str}")
        lines.append(f"    {desc_str}")
        lines.append("")
    
    return "\n".join(lines)


MACRO_SUMMARY = """MACROECONOMIC AND FUND FLOW CONTEXT (Jan 2024 - Early 2026)

Key Macro Indicators:
- Federal Funds Rate: Declined from 5.33% (early 2024) to ~3.64% (early 2026). Fed has begun easing after extended tightening cycle.
- 10-Year Treasury Yield: Remains volatile around 4%, indicating persistent inflation uncertainty and mixed long-term growth expectations.
- CPI Inflation: Continues to rise steadily. Pace may be moderating but price levels remain elevated.
- Unemployment: Gradually increased from 3.7% to mid-4% range.
- Consumer Sentiment: Declined overall, reflecting growing caution and softening economic outlook.

Fund Flow Trends:
- Strong inflows into bond funds and money market instruments.
- Equity fund flows have been weaker and less consistent.
- Significant inflows into taxable bond funds and international equity ETFs (Morningstar data).
- Clear investor preference for safety, liquidity, and predictable income.
- Shift toward balanced and risk-managed portfolios rather than concentrated equity exposure.

Implications:
- Late-cycle environment with cautious investors, moderating growth, and still-elevated yields.
- Favorable conditions for income-oriented products (fixed income, private credit, structured products with capital protection).
- Globally diversified strategies seeing stronger demand.
- Growth-focused equity products face lower demand unless they incorporate risk mitigation.
"""


TREND_SYNTHESIS = """KEY COMPETITIVE TRENDS OBSERVED ACROSS ALL 10 FIRMS:

1. ETF WRAPPER DOMINANCE: The overwhelming majority of new launches use ETF structures rather than traditional mutual funds. Firms are packaging everything from active fixed income to options-based income to buffered outcomes inside ETFs for tax efficiency, liquidity, and advisor ease-of-use.

2. ALTERNATIVES DEMOCRATIZATION: Multiple firms are broadening retail/HNW access to private markets. Examples include Morgan Stanley's ELTIF, Goldman Sachs' private equity return tracker ETFs, Edward Jones' private equity/credit/real estate UMA sleeves, Merrill Lynch's Alts Expanded Access Program, and Wells Fargo enabling alternatives inside Personalized UMA.

3. INCOME AND YIELD FOCUS: A disproportionate number of launches target income generation. Options-based equity income (JPMorgan JOYT, ROCY, ROCQ), multi-asset income (JPMorgan JFLI, Raymond James RJVI), high yield (JPMorgan JPHY), and preferred securities (Morgan Stanley EVPF) all reflect the yield-seeking environment.

4. TAX-AWARE AND MUNICIPAL STRATEGIES: Multiple firms launched municipal bond ETFs (Fidelity FMUB, FMUN, Raymond James RJMI), reflecting demand for tax-efficient income.

5. STRUCTURED CREDIT / CLO ACCESS: Fidelity launched two CLO ETFs (FCLO, FAAA), bringing institutional-grade structured credit to retail investors.

6. PLATFORM AND SERVICE INNOVATION: Several launches were not products but platform capabilities. Edward Jones' Generations program, Wells Fargo's UMA alternatives integration, and Wells Fargo's proxy voting service reflect competition happening at the infrastructure and service layer, not just the product level.

7. TOKENIZATION AND DIGITAL: JPMorgan's MONY (My OnChain Net Yield Fund) represents early moves toward tokenized financial products for wealth management clients.
"""


def build_full_context(competitor_csv_path="competitor_tracker_merged.csv"):
    """Build the complete context string to inject into the LLM prompt."""
    
    df = load_competitor_data(competitor_csv_path)
    competitor_text = summarize_competitor_landscape(df)
    
    full_context = f"""{competitor_text}

{TREND_SYNTHESIS}

{MACRO_SUMMARY}"""
    
    return full_context


def build_system_prompt_with_context(context):
    """Build the complete system prompt with real data context injected."""
    
    prompt = f"""You are a senior wealth management strategist advising the head of a major retail wealth management division (e.g., Merrill Lynch, Morgan Stanley Wealth Management, JP Morgan Private Client).

Your role is to act as an "Idea Engine": given a set of market signals, competitor moves, demographic trends, and strategic constraints, you generate concrete new product and service ideas that the firm should consider launching.

You have been provided with REAL market data below. Your ideas must be grounded in this data. Do not fabricate competitor launches, fund flow statistics, or macro indicators. Reference specific data points from the context when explaining why an idea is timely.

=== MARKET CONTEXT (REAL DATA) ===

{context}

=== END MARKET CONTEXT ===

For each idea you generate, provide:
1. **Product/Service Name**: A clear, specific name
2. **Category**: The asset class or service type
3. **Description**: 2-3 sentences explaining what this product/service is
4. **Market Signal Link**: Which specific data points from the market context above make this idea timely. Reference actual competitor launches, actual fund flow trends, or actual macro indicators.
5. **Target Client Segment**: Who this is designed for
6. **DVF Scores** (each 0-100 with brief justification):
   - **Desirability**: How strong is client demand? Reference fund flow data and competitive activity.
   - **Viability**: Can the firm generate meaningful revenue? Consider fee structures observed in competitor launches.
   - **Feasibility**: How practical is implementation? Consider what competitors have already proven is launchable.
7. **Key Risks**: 1-2 primary risks or challenges
8. **Suggested Next Steps**: What the firm should do first to pursue this idea

Generate 6-8 ideas, ranging from conservative/incremental to bold/innovative. Ensure diversity across asset classes and client segments.

Format your response as a JSON array of objects matching this structure:
{{
  "id": "string",
  "name": "string",
  "category": "string",
  "description": "string",
  "market_signal_link": "string",
  "target_client_segment": "string",
  "dvf_scores": {{
    "desirability": {{"score": number, "justification": "string"}},
    "viability": {{"score": number, "justification": "string"}},
    "feasibility": {{"score": number, "justification": "string"}}
  }},
  "key_risks": ["string", "string"],
  "suggested_next_steps": ["string", "string", "string"]
}}"""
    
    return prompt


# ── Generate and save everything ──
if __name__ == "__main__":
    
    # Build context
    context = build_full_context()
    
    # Save the context for inspection
    with open("/home/claude/market_context.txt", "w") as f:
        f.write(context)
    print(f"Market context saved ({len(context)} chars)")
    
    # Build the full system prompt
    system_prompt = build_system_prompt_with_context(context)
    
    with open("/home/claude/system_prompt_with_data.txt", "w") as f:
        f.write(system_prompt)
    print(f"System prompt saved ({len(system_prompt)} chars)")
    
    # Also save the context assembler components as a JSON config
    # so the Streamlit app can load them
    config = {
        "macro_summary": MACRO_SUMMARY.strip(),
        "trend_synthesis": TREND_SYNTHESIS.strip(),
        "competitor_data_path": "competitor_tracker_merged.csv",
        "data_date_range": "Sep 2024 - Mar 2026",
        "total_launches_tracked": 49,
        "firms_covered": 10
    }
    
    with open("/home/claude/data_config.json", "w") as f:
        json.dump(config, f, indent=2)
    print("Data config saved")
    
    # Print summary stats
    df = load_competitor_data()
    print(f"\n=== DATA SUMMARY ===")
    print(f"Competitor launches: {len(df)}")
    print(f"Firms: {df['firm'].nunique()}")
    print(f"Date range: {df['launch_date'].min().strftime('%Y-%m-%d')} to {df['launch_date'].max().strftime('%Y-%m-%d')}")
    print(f"System prompt length: {len(system_prompt)} characters (~{len(system_prompt)//4} tokens)")
    print(f"\nThis prompt is ready to send to the Anthropic API.")
    print(f"It includes real competitor data and macro context so the LLM's")
    print(f"generated ideas will be grounded in actual market intelligence.")
