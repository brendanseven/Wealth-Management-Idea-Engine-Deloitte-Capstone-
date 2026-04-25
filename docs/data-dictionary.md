# Data Dictionary

## competitor_tracker_merged.csv

The primary market intelligence dataset. Each row represents a product launch by a major wealth management firm.

| Field | Type | Description |
|-------|------|-------------|
| firm | string | Name of the wealth management firm (e.g., "JPMorgan", "Goldman Sachs") |
| product_name | string | Name of the launched product or service |
| launch_date | date | Date of launch or public announcement (YYYY-MM-DD) |
| asset_class | string | Broad asset class category (e.g., "Fixed Income", "Private Equity", "Multi-Asset") |
| product_structure | string | Legal/delivery structure (e.g., "ETF", "Interval Fund", "BDC", "SMA", "Advisory Service") |
| target_client | string | Intended client segment (e.g., "Retail", "HNW", "Institutional") |
| min_investment | string | Minimum investment amount, where available |
| fees | string | Fee structure or expense ratio, where available |
| description | string | Brief description of the product and its value proposition |
| source_link | string | URL to the source of the information |
| source_person | string | Team member who collected this entry ("Person 1" or "Person 2") |

## idea_engine_scenarios.json

Pre-generated scenario outputs. Each scenario contains:

| Field | Type | Description |
|-------|------|-------------|
| scenario_id | string | Unique identifier (e.g., "S1", "S2") |
| scenario_title | string | Descriptive title of the market scenario |
| scenario_description | string | Full narrative description of the market context |
| market_signals | array[string] | Key market signals driving this scenario |
| ideas | array[object] | Generated product ideas (see below) |

Each idea object contains:

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique idea identifier (e.g., "S1-001") |
| name | string | Product or service name |
| category | string | Asset class or service type |
| description | string | 2-3 sentence description of the concept |
| market_signal_link | string | Explanation of which market signals make this idea timely |
| target_client_segment | string | Who this product is designed for |
| dvf_scores.desirability.score | integer (0-100) | Client demand score |
| dvf_scores.desirability.justification | string | Reasoning behind the score |
| dvf_scores.viability.score | integer (0-100) | Business economics score |
| dvf_scores.viability.justification | string | Reasoning behind the score |
| dvf_scores.feasibility.score | integer (0-100) | Implementation readiness score |
| dvf_scores.feasibility.justification | string | Reasoning behind the score |
| key_risks | array[string] | 1-2 primary risks or challenges |
| suggested_next_steps | array[string] | Recommended actions to pursue the idea |

## hierarchy_and_feedback.json

Contains two top-level objects:

**hierarchies**: Array of hierarchy objects, one per scenario. Each contains:

| Field | Type | Description |
|-------|------|-------------|
| scenario_id | string | Matches the scenario_id in scenarios JSON |
| themes | array[object] | Strategic themes grouping the ideas |
| themes[].theme | string | Theme name (e.g., "Income & Yield Products") |
| themes[].description | string | One-sentence description of the strategic direction |
| themes[].idea_ids | array[string] | IDs of ideas belonging to this theme |
| themes[].sub_categories | array[object] | Sub-groupings within the theme |

**feedback**: Object keyed by idea_id. Each contains:

| Field | Type | Description |
|-------|------|-------------|
| variations | array[object] | Alternative versions of the idea with DVF impact notes |
| segment_adaptations | array[object] | How the idea changes for different client segments |
| implementation_deep_dive | object | Critical path, key decisions, and cost estimates |

## market_context.txt

Plain text file containing the assembled market context that gets injected into the LLM prompt. Includes summarized competitor launch data, key competitive trends observed across all 10 firms, and macroeconomic/fund flow context. Approximately 14,000 characters.

## data_config.json

Metadata about the data sources:

| Field | Type | Description |
|-------|------|-------------|
| macro_summary | string | Full macroeconomic summary text |
| trend_synthesis | string | Key competitive trends observed |
| competitor_data_path | string | Path to the competitor CSV |
| data_date_range | string | Coverage period |
| total_launches_tracked | integer | Number of launches in the dataset |
| firms_covered | integer | Number of firms tracked |
