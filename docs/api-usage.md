# API and Usage Notes

## LLM Integration

The Idea Engine uses Anthropic's Claude (Haiku 4.5) via AWS Bedrock for two AI calls:

### Call 1: Idea Generation

**Endpoint**: AWS Bedrock `InvokeModel`
**Model ID**: `us.anthropic.claude-haiku-4-5-20251001-v1:0`
**Max tokens**: 6,000

The system prompt includes:
1. A role definition (senior wealth management strategist)
2. The full market context (competitor data, macro indicators, fund flows) injected from `market_context.txt`
3. Instructions to ground ideas in the provided data and not fabricate market intelligence
4. Output format specification (JSON array with defined schema)

The user provides a free-text market scenario describing the competitive situation they want to explore.

**Prompt engineering decisions**:
- Requesting 5 ideas (rather than 6-8) to stay within token limits and avoid truncated JSON responses
- Requiring justifications to be 1-2 sentences to manage output length
- Explicit instruction to reference actual data points from the context
- JSON-only output instruction to enable programmatic parsing

### Call 2: Hierarchy Generation

**Endpoint**: AWS Bedrock `InvokeModel`
**Model ID**: `us.anthropic.claude-haiku-4-5-20251001-v1:0`
**Max tokens**: 2,000

Takes the generated ideas (names, categories, and brief descriptions) and organizes them into 3-5 strategic themes with sub-categories. This is a smaller, faster call since it only receives idea summaries, not the full market context.

### Error Handling

The app includes a JSON truncation safety net. If the LLM response is cut off mid-JSON (common with larger outputs), the parser attempts to salvage all complete idea objects by finding the last valid `},` boundary and closing the array.

## AWS Configuration

### Required IAM Permissions

The EC2 instance role needs:
- `AmazonBedrockFullAccess`
- `AWSMarketplaceManageSubscriptions`
- `AWSMarketplaceRead-only`

### Bedrock Region

The app is configured for `us-east-2` (Ohio). To change the region, modify the `region_name` parameter in the `get_bedrock_client()` function in `app.py`.

### Timeout Configuration

The Bedrock client is configured with:
- `read_timeout`: 120 seconds (default 60 is too short for larger generations)
- `connect_timeout`: 10 seconds
- `retries`: 1 attempt (to fail fast rather than wait through multiple timeouts)

## Running the App

### Pre-built Scenarios (no AWS required)

Select "Pre-built Scenarios" in the sidebar. Two scenarios are available:
1. **The Alternatives Democratization Play**: 7 ideas across 4 themes
2. **The Aging Affluent & Retirement Income Crisis**: 6 ideas across 4 themes

### Live Generation (requires AWS Bedrock)

Select "Live Generation" in the sidebar. Type a market scenario and click "Generate Ideas." The app makes two sequential API calls (idea generation + hierarchy organization), typically completing in 30-60 seconds.

### View Modes

- **Ranked List**: Traditional flat ranking with DVF score bars, composite scores, and expandable analysis cards. Supports category filtering and minimum score threshold.
- **Thematic Hierarchy**: Ideas organized into strategic themes with aggregate DVF scores per theme. Expandable sub-categories with nested idea cards.

### DVF Weight Adjustment

The sidebar sliders control the relative weight of each DVF dimension. Weights are automatically normalized to sum to 100%. Changing weights immediately reorders the rankings in both view modes.
