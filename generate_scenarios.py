# Wealth Management Idea Engine - System Prompt & Scenario Generation
# This script defines the ideation prompt and pre-generates demo scenario outputs.

import json

# ============================================================
# SYSTEM PROMPT - This is the prompt that would be sent to the
# LLM API in the live version. For now we use it to guide
# manual generation of realistic outputs.
# ============================================================

SYSTEM_PROMPT = """You are a senior wealth management strategist advising the head of a major retail wealth management division (e.g., Merrill Lynch, Morgan Stanley Wealth Management, JP Morgan Private Client).

Your role is to act as an "Idea Engine": given a set of market signals, competitor moves, demographic trends, and strategic constraints, you generate concrete new product and service ideas that the firm should consider launching.

For each idea you generate, provide:
1. **Product/Service Name**: A clear, specific name
2. **Category**: The asset class or service type (e.g., Private Credit, Thematic ETF, Advisory Service, Structured Product)
3. **Description**: 2-3 sentences explaining what this product/service is
4. **Market Signal Link**: Which specific input signals make this idea timely and relevant
5. **Target Client Segment**: Who this is designed for (e.g., mass affluent millennials, HNWI retirees, etc.)
6. **DVF Scores** (each 0-100 with brief justification):
   - **Desirability**: How strong is client demand? Is there demonstrated market appetite?
   - **Viability**: Can the firm generate meaningful revenue? What are the economics?
   - **Feasibility**: How practical is implementation? Consider regulatory, operational, and technology requirements.
7. **Key Risks**: 1-2 primary risks or challenges
8. **Suggested Next Steps**: What the firm should do first to pursue this idea

Generate 6-8 ideas per scenario, ranging from conservative/incremental to bold/innovative. Ensure diversity across asset classes and client segments.

Format your response as a JSON array of objects."""


# ============================================================
# SCENARIO 1: "The Alternatives Democratization Play"
# ============================================================
# Context: You're the head of wealth management at a major
# wireframe firm. Private markets AUM has grown 20%+ YoY,
# JP Morgan and Schwab have launched retail alt products,
# affluent clients are asking about private equity and credit,
# and new SEC rules are lowering accredited investor barriers.

scenario_1 = {
    "scenario_id": "S1",
    "scenario_title": "The Alternatives Democratization Play",
    "scenario_description": (
        "You are the head of wealth management at a top-5 US wirehouse. "
        "Private markets AUM across the industry has grown over 20% year-over-year. "
        "JP Morgan recently launched a retail-accessible private equity interval fund with a $25K minimum. "
        "Charles Schwab introduced a private credit BDC targeting mass affluent investors. "
        "Your affluent client base (ages 35-60, $500K-$5M investable assets) is increasingly asking advisors about private market access. "
        "The SEC has proposed broadening the accredited investor definition. "
        "Meanwhile, your firm's product shelf is still dominated by traditional mutual funds and ETFs, "
        "and you're losing wallet share to competitors with alternative offerings."
    ),
    "market_signals": [
        "Private markets AUM growing 20%+ YoY across industry",
        "JP Morgan launched retail PE interval fund ($25K min)",
        "Schwab launched private credit BDC for mass affluent",
        "SEC proposing broader accredited investor definition",
        "Advisor surveys show 65% of affluent clients asking about alts",
        "Firm's product shelf is 90% traditional funds/ETFs"
    ],
    "ideas": [
        {
            "id": "S1-001",
            "name": "RetailAccess Private Credit Interval Fund",
            "category": "Private Credit",
            "description": (
                "A semi-liquid interval fund investing in senior secured direct loans to US middle-market companies, "
                "offered with a $10K minimum to compete directly with Schwab's BDC offering. Quarterly liquidity windows "
                "with a target net yield of 8-10%. Designed as an income-generating allocation within a diversified portfolio."
            ),
            "market_signal_link": (
                "Directly responds to Schwab's BDC launch and the 20%+ growth in private credit AUM. "
                "Lower minimum than JP Morgan's offering creates competitive differentiation. "
                "Addresses the 65% of clients asking advisors about alternative income sources."
            ),
            "target_client_segment": "Mass affluent investors (ages 40-65, $250K-$1M investable assets) seeking yield enhancement",
            "dvf_scores": {
                "desirability": {
                    "score": 88,
                    "justification": (
                        "Private credit is the fastest-growing alternative asset class. Client demand is already validated "
                        "by advisor survey data and competitor product launches. Income-focused positioning resonates strongly "
                        "with the current rate environment."
                    )
                },
                "viability": {
                    "score": 76,
                    "justification": (
                        "1.25% management fee on target AUM of $500M+ generates substantial revenue. However, the low minimum "
                        "investment means higher servicing costs per dollar, and the fund needs to reach $150M+ to be economically "
                        "viable. Expected 18-month ramp to breakeven."
                    )
                },
                "feasibility": {
                    "score": 70,
                    "justification": (
                        "Interval fund structure is well-understood by regulators. Requires SEC registration and ongoing "
                        "compliance infrastructure. Need to either build or partner for direct lending origination capability. "
                        "Existing advisor network can distribute, but requires training on alternatives selling."
                    )
                }
            },
            "key_risks": [
                "Credit cycle downturn could impair loan portfolio and damage reputation with retail investors new to private credit",
                "Regulatory scrutiny of retail access to illiquid investments may increase compliance burden"
            ],
            "suggested_next_steps": [
                "Conduct competitive fee analysis against Schwab BDC and JP Morgan interval fund",
                "Identify 2-3 potential sub-advisory partners with direct lending track records",
                "Survey top 50 advisors on client appetite and minimum investment sensitivity"
            ]
        },
        {
            "id": "S1-002",
            "name": "Private Equity Co-Investment Access Program",
            "category": "Private Equity",
            "description": (
                "A curated program offering HNWI clients ($1M+ minimum) access to PE co-investment opportunities "
                "alongside top-tier GPs. Structured as a series of deal-by-deal SPVs with 5-7 year horizons. "
                "Positions the firm as providing institutional-quality PE access to individual investors."
            ),
            "market_signal_link": (
                "JP Morgan's retail PE fund validates demand, but this targets the higher end with a more exclusive, "
                "institutional-quality offering. Differentiates from competitors' fund-of-funds approach by offering "
                "direct deal exposure. Aligns with the trend of GPs seeking co-investment capital from wealth channels."
            ),
            "target_client_segment": "HNWI clients (ages 45-65, $2M+ investable assets) seeking institutional-quality PE exposure",
            "dvf_scores": {
                "desirability": {
                    "score": 72,
                    "justification": (
                        "Strong demand from HNWI segment, but smaller addressable market than mass affluent products. "
                        "Co-investment narrative is compelling to sophisticated investors. However, the 5-7 year lock-up "
                        "limits appeal to a subset of even the HNWI population."
                    )
                },
                "viability": {
                    "score": 82,
                    "justification": (
                        "Premium economics: 1.5% management fee + 10-15% carried interest. High minimum investment means "
                        "lower servicing costs per dollar. Strong potential for follow-on participation. "
                        "Fewer clients needed to reach viable fund size."
                    )
                },
                "feasibility": {
                    "score": 52,
                    "justification": (
                        "Requires establishing GP relationships and sourcing pipeline, which takes significant time and expertise. "
                        "Complex legal structuring for each SPV. Accredited/qualified purchaser requirements limit distribution. "
                        "Need specialized team with PE background that the firm may not currently have."
                    )
                }
            },
            "key_risks": [
                "GP relationship-dependent: losing access to top-tier co-investments would undermine the value proposition",
                "Deal-by-deal structure creates lumpy revenue and uneven client experience"
            ],
            "suggested_next_steps": [
                "Map existing GP relationships across the firm and identify co-investment capacity",
                "Hire or designate a PE specialist to lead deal sourcing and due diligence",
                "Pilot with 10-15 top HNWI clients to validate demand and refine the offering"
            ]
        },
        {
            "id": "S1-003",
            "name": "Alternatives Allocation Model Portfolios",
            "category": "Advisory Service",
            "description": (
                "A set of pre-built model portfolios (Conservative, Moderate, Growth) that integrate alternative "
                "investments at 10-30% allocation alongside traditional holdings. Available through the firm's existing "
                "managed account platform. Removes the burden from advisors of figuring out how to blend alts into client portfolios."
            ),
            "market_signal_link": (
                "Addresses the gap between client interest in alternatives (65% asking) and advisor confidence in recommending them. "
                "Competitors are launching individual alt products, but nobody is solving the portfolio construction problem. "
                "This makes the firm's entire product shelf more competitive by packaging alts as part of a complete solution."
            ),
            "target_client_segment": "Broad affluent client base ($250K-$5M) via financial advisors who lack alternatives expertise",
            "dvf_scores": {
                "desirability": {
                    "score": 82,
                    "justification": (
                        "Solves a real pain point for both clients and advisors. Clients get diversified alt exposure without "
                        "complexity, advisors get a turnkey solution. Broad addressable market. However, demand depends on "
                        "advisor adoption, which requires training and incentive alignment."
                    )
                },
                "viability": {
                    "score": 85,
                    "justification": (
                        "Overlay fee of 0.25-0.50% on top of underlying product fees creates a scalable revenue stream. "
                        "Leverages existing managed account infrastructure. Drives AUM into the firm's proprietary or preferred "
                        "alt products, generating additional fee revenue downstream."
                    )
                },
                "feasibility": {
                    "score": 88,
                    "justification": (
                        "Can be built largely on existing platform and infrastructure. Uses products already on the shelf "
                        "(or soon to be). Minimal regulatory incremental burden since model portfolios are a well-established "
                        "format. Primary investment is in portfolio construction expertise and advisor training."
                    )
                }
            },
            "key_risks": [
                "If underlying alt products underperform, the firm bears reputational risk for the recommended allocation",
                "Advisor adoption may be slow if incentive structures favor traditional products"
            ],
            "suggested_next_steps": [
                "Assemble a 3-person team (CIO office + alts specialist + platform lead) to design the model portfolios",
                "Identify which existing alt products to include in initial models",
                "Run a pilot with 25 advisors in one region to test adoption and gather feedback"
            ]
        },
        {
            "id": "S1-004",
            "name": "Tokenized Real Estate Income Fund",
            "category": "Real Assets",
            "description": (
                "A blockchain-enabled real estate fund that tokenizes shares of a diversified commercial real estate portfolio, "
                "allowing $5K minimum investments with enhanced liquidity through a secondary trading platform. "
                "Targets monthly income distributions from rental cash flows."
            ),
            "market_signal_link": (
                "Affluent clients are increasingly interested in real estate as an inflation hedge, but traditional REITs "
                "feel commoditized and direct real estate is illiquid. Tokenization addresses both issues. "
                "SEC's evolving stance on digital assets and broader accredited investor rules create a regulatory tailwind. "
                "Positions the firm as innovative and forward-looking."
            ),
            "target_client_segment": "Tech-savvy affluent investors (ages 30-50, $100K-$1M investable assets) interested in real assets with modern delivery",
            "dvf_scores": {
                "desirability": {
                    "score": 68,
                    "justification": (
                        "Real estate demand is well-established, and tokenization adds a novelty factor that appeals to younger affluent investors. "
                        "However, the tokenization angle may confuse or alienate more traditional clients. "
                        "Demand is strong but somewhat niche compared to straightforward private credit or PE offerings."
                    )
                },
                "viability": {
                    "score": 65,
                    "justification": (
                        "Low minimum investment and tokenization infrastructure create higher per-dollar costs than traditional real estate funds. "
                        "1.0% management fee is reasonable but margins are thinner. "
                        "Secondary market liquidity feature is a differentiator but requires critical mass of participants to function."
                    )
                },
                "feasibility": {
                    "score": 45,
                    "justification": (
                        "Requires building or partnering for blockchain/tokenization infrastructure. "
                        "Regulatory framework for tokenized securities is still evolving and varies by state. "
                        "Compliance, custody, and technology requirements are significantly higher than traditional fund structures. "
                        "12-18 month build timeline is realistic."
                    )
                }
            },
            "key_risks": [
                "Regulatory uncertainty around tokenized securities could delay or block launch",
                "Technology risk: secondary trading platform needs liquidity to function, creating a chicken-and-egg problem"
            ],
            "suggested_next_steps": [
                "Commission a regulatory feasibility study from external counsel",
                "Evaluate 2-3 tokenization platform partners (e.g., Securitize, tZERO)",
                "Gauge client interest through a targeted survey of digitally-active affluent clients"
            ]
        },
        {
            "id": "S1-005",
            "name": "Structured Yield Enhancement Notes (Buffered Income Series)",
            "category": "Structured Products",
            "description": (
                "A series of principal-buffered structured notes linked to the S&P 500, offering enhanced yield (6-8% annual coupon) "
                "with downside protection (10-15% buffer). Issued quarterly in $1K increments. "
                "Provides a middle ground between fixed income yields and equity market participation."
            ),
            "market_signal_link": (
                "With traditional fixed income yields compressing and equity markets at elevated valuations, "
                "clients need income solutions that offer more than bonds but with less risk than pure equity. "
                "Buffered/defined outcome products have seen 40%+ AUM growth. "
                "Low minimum makes this accessible to the full affluent spectrum."
            ),
            "target_client_segment": "Income-oriented investors across all affluent tiers, particularly pre-retirees (ages 50-65) seeking yield with protection",
            "dvf_scores": {
                "desirability": {
                    "score": 78,
                    "justification": (
                        "Strong demand for income with downside protection in the current environment. "
                        "Buffered outcome products are already proven with fast-growing AUM. "
                        "Broad appeal across wealth segments due to low minimum."
                    )
                },
                "viability": {
                    "score": 72,
                    "justification": (
                        "Structured note economics are well-understood: firm earns distribution fee plus potential spread on issuance. "
                        "Quarterly issuance creates recurring revenue. However, margins depend on issuing bank relationships "
                        "and the firm takes on counterparty concentration risk."
                    )
                },
                "feasibility": {
                    "score": 82,
                    "justification": (
                        "Structured notes are a mature product category with established regulatory and operational frameworks. "
                        "Can partner with existing issuing banks (Goldman, BofA, etc.). "
                        "Advisor training is straightforward since many already sell similar products. Fast time to market (3-4 months)."
                    )
                }
            },
            "key_risks": [
                "Counterparty risk to the issuing bank, which becomes a reputational risk for the firm if the issuer is impaired",
                "Client misunderstanding of buffer mechanics could lead to complaints and regulatory scrutiny"
            ],
            "suggested_next_steps": [
                "Negotiate issuance terms with 2-3 bank partners",
                "Design client-facing educational materials that clearly explain buffer mechanics",
                "Launch pilot series and track advisor adoption rates"
            ]
        },
        {
            "id": "S1-006",
            "name": "Alternatives Education & Certification Hub",
            "category": "Advisory Service",
            "description": (
                "A digital learning platform for both advisors and clients that provides structured education on alternative investments. "
                "For advisors: certification program qualifying them to recommend alts. "
                "For clients: interactive modules explaining private markets, risk, and portfolio fit. "
                "Builds confidence on both sides of the advisory relationship."
            ),
            "market_signal_link": (
                "The biggest bottleneck to alternatives adoption is not product availability but understanding. "
                "65% of clients are asking about alts, but many advisors lack confidence to recommend them. "
                "Competitors are launching products; this firm can differentiate by building the trust and knowledge layer. "
                "Positions the firm as a thought leader, not just a product shelf."
            ),
            "target_client_segment": "Internal advisors (primary) and their affluent client base (secondary)",
            "dvf_scores": {
                "desirability": {
                    "score": 70,
                    "justification": (
                        "Addresses a real but indirect need. Clients don't explicitly ask for education, but lack of understanding "
                        "is a key barrier to alts adoption. Advisor demand for training is high based on internal surveys. "
                        "Not a revenue-generating product itself, but an enabler of product sales."
                    )
                },
                "viability": {
                    "score": 55,
                    "justification": (
                        "No direct revenue stream. Value is measured in increased alt product adoption and AUM growth. "
                        "ROI is real but indirect and harder to quantify. Platform build and content creation require upfront investment. "
                        "Could be positioned as a premium service for top-tier clients."
                    )
                },
                "feasibility": {
                    "score": 92,
                    "justification": (
                        "Low regulatory burden since it is educational, not advisory. Can be built on existing LMS or digital platforms. "
                        "Content can be developed internally with CIO office and compliance input. "
                        "3-month build timeline for MVP. Minimal technology risk."
                    )
                }
            },
            "key_risks": [
                "Advisors may view certification as an extra burden rather than a benefit without proper incentive alignment",
                "Content must be carefully reviewed by compliance to avoid crossing into product recommendation"
            ],
            "suggested_next_steps": [
                "Survey advisor population on preferred learning formats and biggest knowledge gaps",
                "Partner with CIO office to develop curriculum outline",
                "Build MVP with 3-4 modules covering the most-requested alt categories"
            ]
        },
        {
            "id": "S1-007",
            "name": "Gold & Precious Metals Direct Access Account",
            "category": "Real Assets",
            "description": (
                "A dedicated account allowing clients to purchase, hold, and sell physical gold and precious metals "
                "(allocated and stored in insured vaults) directly through their wealth management platform. "
                "Includes options for fractional ownership starting at $500 and automatic rebalancing within a broader portfolio."
            ),
            "market_signal_link": (
                "Gold is at all-time highs with strong momentum driven by geopolitical uncertainty and central bank buying. "
                "Affluent clients are increasingly expressing interest in tangible assets as a hedge. "
                "Most wirehouses offer gold only via ETFs (GLD, IAU), missing clients who want physical ownership. "
                "Fractional access addresses the barrier of high per-ounce cost."
            ),
            "target_client_segment": "Affluent investors (ages 45-70, $500K+) seeking portfolio hedging and tangible asset ownership",
            "dvf_scores": {
                "desirability": {
                    "score": 75,
                    "justification": (
                        "Strong near-term demand driven by gold price momentum and geopolitical anxiety. "
                        "Physical ownership narrative resonates more deeply than ETF exposure for many affluent clients. "
                        "However, gold interest is somewhat cyclical and may cool if macro conditions shift."
                    )
                },
                "viability": {
                    "score": 60,
                    "justification": (
                        "Revenue from custody fees (0.40-0.50% annually) and transaction spreads. "
                        "Lower margin than financial products since there is no performance fee. "
                        "Requires vault storage partnerships and insurance, which add operational cost. "
                        "Economically viable but not a high-margin business."
                    )
                },
                "feasibility": {
                    "score": 58,
                    "justification": (
                        "Requires establishing custody and vault partnerships (e.g., Brink's, Loomis). "
                        "Physical metals have distinct regulatory and tax reporting requirements (collectibles treatment for gold). "
                        "Platform integration for fractional ownership adds technology complexity. "
                        "8-10 month implementation timeline."
                    )
                }
            },
            "key_risks": [
                "Gold price reversal would reduce client interest and could lead to losses on recently purchased positions",
                "Physical custody introduces operational risks (insurance, auditing, vault security) not present in ETF-based solutions"
            ],
            "suggested_next_steps": [
                "Evaluate custody and vault partnerships with 2-3 established providers",
                "Assess platform integration requirements for fractional precious metals trading",
                "Analyze the tax advisory implications of direct gold ownership for clients and advisors"
            ]
        }
    ]
}


# ============================================================
# SCENARIO 2: "The Aging Affluent & Retirement Income Crisis"
# ============================================================

scenario_2 = {
    "scenario_id": "S2",
    "scenario_title": "The Aging Affluent & Retirement Income Crisis",
    "scenario_description": (
        "You are the head of wealth management at a top-5 US wirehouse. "
        "The baby boomer generation is driving the largest wealth transfer in history, with $84 trillion expected to change hands by 2045. "
        "Your client base skews older: 45% of AUM is held by clients aged 60+, and advisor feedback indicates growing anxiety about "
        "retirement income sustainability, long-term care costs, and estate planning complexity. "
        "Interest rates have stabilized but traditional fixed income yields remain below historical averages. "
        "Competitors like Fidelity and Vanguard are heavily marketing low-cost retirement income solutions. "
        "Meanwhile, your firm has limited dedicated retirement income products beyond traditional bond ladders and annuities, "
        "and younger heirs are indicating they plan to consolidate assets elsewhere."
    ),
    "market_signals": [
        "$84 trillion intergenerational wealth transfer underway through 2045",
        "45% of firm AUM held by clients aged 60+",
        "Advisors report rising client anxiety about retirement income sustainability",
        "Long-term care costs rising 5-7% annually, outpacing inflation",
        "Fidelity and Vanguard aggressively marketing low-cost retirement solutions",
        "70% of heirs plan to change financial advisors after inheriting wealth",
        "Fixed income yields below historical averages despite rate stabilization"
    ],
    "ideas": [
        {
            "id": "S2-001",
            "name": "Guaranteed Lifetime Income Bridge Portfolio",
            "category": "Structured Products / Insurance Hybrid",
            "description": (
                "A blended solution combining a partial fixed annuity allocation (covering essential expenses) with a managed "
                "investment portfolio (covering discretionary spending and legacy). Advisors use a proprietary planning tool "
                "to determine the optimal split based on client-specific cash flow needs. Reframes the retirement conversation "
                "from 'how much do I have' to 'how much income do I need.'"
            ),
            "market_signal_link": (
                "Directly addresses the retirement income anxiety reported by advisors. "
                "Positions the firm's offering above low-cost competitors by providing personalized income planning, "
                "not just cheap access to bond funds. Hybrid approach avoids the 'all-in on annuities' stigma."
            ),
            "target_client_segment": "Pre-retirees and early retirees (ages 55-72, $500K-$3M investable assets)",
            "dvf_scores": {
                "desirability": {
                    "score": 90,
                    "justification": (
                        "Retirement income is the top concern for the firm's largest client segment by AUM. "
                        "The hybrid approach is more appealing than pure annuity solutions. "
                        "Advisor feedback consistently ranks income planning tools as their biggest unmet need."
                    )
                },
                "viability": {
                    "score": 78,
                    "justification": (
                        "Multiple revenue streams: managed portfolio fees (0.75-1.0%), annuity placement commissions, "
                        "and planning tool subscription for advisors. High AUM potential given the 45% of firm assets in this demographic. "
                        "Annuity partner revenue sharing adds margin."
                    )
                },
                "feasibility": {
                    "score": 65,
                    "justification": (
                        "The planning tool requires significant development investment. Annuity integration requires partnerships "
                        "with 2-3 insurance carriers. Advisor training is substantial since this reframes their entire retirement planning approach. "
                        "12-month realistic timeline to full launch."
                    )
                }
            },
            "key_risks": [
                "Insurance carrier counterparty risk on the annuity component could erode client trust",
                "Complexity of the hybrid approach may confuse clients or overwhelm advisors without strong training"
            ],
            "suggested_next_steps": [
                "Partner with CIO office to design the asset allocation framework for the managed portfolio component",
                "Negotiate terms with 2-3 annuity carriers for preferential pricing",
                "Prototype the income planning tool with a small advisor focus group"
            ]
        },
        {
            "id": "S2-002",
            "name": "NextGen Wealth Continuity Program",
            "category": "Advisory Service",
            "description": (
                "A structured program that engages the adult children (ages 25-45) of existing high-value clients through "
                "dedicated financial education, personalized onboarding, and a modern digital-first experience. "
                "Each participating heir gets a dedicated junior advisor and access to a curated product set aligned with their "
                "risk profile and financial stage. Goal: retain assets through the generational transfer."
            ),
            "market_signal_link": (
                "70% of heirs plan to leave their parents' advisor. This program directly targets the $84 trillion wealth transfer "
                "risk. Builds the relationship before the transfer happens, not after. "
                "Differentiates from Fidelity/Vanguard's self-service model by providing high-touch onboarding for a digital generation."
            ),
            "target_client_segment": "Adult children (ages 25-45) of existing HNWI/UHNWI clients",
            "dvf_scores": {
                "desirability": {
                    "score": 80,
                    "justification": (
                        "Retention of inherited assets is an existential issue for wealth management firms. "
                        "Next-gen clients want digital experiences and education, not their parents' advisor model. "
                        "Existing clients would appreciate the firm proactively engaging their children."
                    )
                },
                "viability": {
                    "score": 68,
                    "justification": (
                        "Near-term revenue is limited since heirs may have small current portfolios. "
                        "The value is in long-term AUM retention: retaining even 30% of transferred assets represents "
                        "billions across the firm's client base. High upfront cost relative to immediate revenue, "
                        "but massive long-term strategic value."
                    )
                },
                "feasibility": {
                    "score": 78,
                    "justification": (
                        "Can be built largely on existing infrastructure with a modernized digital layer. "
                        "Junior advisor staffing leverages existing talent pipeline. Educational content reusable from other initiatives. "
                        "Low regulatory complexity. 6-month launch timeline for pilot."
                    )
                }
            },
            "key_risks": [
                "Existing advisors may resist sharing client relationships with a next-gen program team",
                "If the digital experience is not genuinely best-in-class, heirs will still leave for fintech competitors"
            ],
            "suggested_next_steps": [
                "Identify the top 200 client households by AUM with adult children aged 25-45",
                "Design a digital-first onboarding experience and test with focus group of 10-15 heirs",
                "Develop an advisor incentive structure that rewards next-gen engagement"
            ]
        },
        {
            "id": "S2-003",
            "name": "Long-Term Care Funding Strategy",
            "category": "Insurance / Advisory Hybrid",
            "description": (
                "An integrated advisory service that combines long-term care insurance analysis, health savings optimization, "
                "and dedicated portfolio carve-outs to fund potential LTC needs. Uses Monte Carlo simulations to model "
                "LTC cost scenarios and recommends a personalized funding strategy that blends insurance, invested assets, "
                "and income streams."
            ),
            "market_signal_link": (
                "LTC costs rising 5-7% annually represent the single largest unplanned expense for retirees. "
                "Most wealth management firms treat LTC as an insurance referral, not an integrated financial planning challenge. "
                "Addressing this proactively builds deep client trust and stickiness."
            ),
            "target_client_segment": "Affluent pre-retirees and retirees (ages 55-75, $500K+) concerned about healthcare costs",
            "dvf_scores": {
                "desirability": {
                    "score": 74,
                    "justification": (
                        "LTC is a top-3 client concern but often avoided because of complexity and emotional discomfort. "
                        "Clients who engage with this service would have very high satisfaction and loyalty. "
                        "Demand exists but is latent; requires proactive advisor initiation rather than client pull."
                    )
                },
                "viability": {
                    "score": 58,
                    "justification": (
                        "Revenue comes from planning fees and increased AUM retention (clients who plan for LTC are less likely to "
                        "draw down or transfer assets). Insurance referral fees add some revenue. "
                        "However, this is more of a retention and differentiation play than a direct profit center."
                    )
                },
                "feasibility": {
                    "score": 72,
                    "justification": (
                        "Monte Carlo modeling tools already exist within most planning platforms. "
                        "LTC insurance partnerships can be established with 2-3 carriers. "
                        "Primary investment is in training advisors on a sensitive topic and building the analytical framework. "
                        "6-8 month build."
                    )
                }
            },
            "key_risks": [
                "LTC conversations are emotionally difficult; advisors may avoid initiating them even with training",
                "LTC insurance market has shrunk significantly, limiting product options for the insurance component"
            ],
            "suggested_next_steps": [
                "Partner with an actuarial consultant to build the LTC cost modeling framework",
                "Train a pilot group of 15-20 advisors on LTC conversation techniques",
                "Develop client-facing materials that normalize LTC planning as part of comprehensive wealth management"
            ]
        },
        {
            "id": "S2-004",
            "name": "Tax-Optimized Charitable Legacy Platform",
            "category": "Advisory Service / Trust",
            "description": (
                "A turnkey platform for establishing donor-advised funds (DAFs), charitable remainder trusts (CRTs), and "
                "structured charitable giving strategies. Integrates with the client's portfolio to identify tax-optimal "
                "assets for gifting (e.g., highly appreciated stock). Provides impact reporting showing how charitable "
                "distributions are used."
            ),
            "market_signal_link": (
                "Wealth transfer and legacy planning are top of mind for the 60+ cohort holding 45% of AUM. "
                "Charitable giving is both a values-driven and tax-optimization opportunity. "
                "Competitors offer basic DAFs, but few provide the integrated tax-optimization and impact reporting layer. "
                "Deepens client relationships by engaging with their values and legacy goals."
            ),
            "target_client_segment": "HNWI/UHNWI clients (ages 55+, $1M+ investable assets) with charitable intent",
            "dvf_scores": {
                "desirability": {
                    "score": 72,
                    "justification": (
                        "Charitable giving is important to a meaningful subset of affluent clients, particularly older ones. "
                        "Tax optimization angle broadens appeal beyond purely philanthropic motivation. "
                        "Not universal demand, but very high engagement and loyalty among participating clients."
                    )
                },
                "viability": {
                    "score": 70,
                    "justification": (
                        "DAF administration fees (0.30-0.60% of assets), trust administration fees, and retained AUM management fees. "
                        "Charitable assets tend to be sticky and long-duration. "
                        "Cross-sell opportunity into estate planning and trust services."
                    )
                },
                "feasibility": {
                    "score": 75,
                    "justification": (
                        "DAF infrastructure can be licensed from existing providers (Schwab Charitable, Fidelity Charitable model). "
                        "CRT structuring requires legal expertise but is well-established. "
                        "Impact reporting is the main technology build. Moderate compliance requirements. "
                        "8-month timeline."
                    )
                }
            },
            "key_risks": [
                "Regulatory and political risk: DAFs face increasing scrutiny over payout timing requirements",
                "Impact reporting accuracy depends on downstream charitable organizations providing data"
            ],
            "suggested_next_steps": [
                "Evaluate build vs. license decision for DAF administration platform",
                "Identify top 100 clients by charitable giving history and conduct outreach",
                "Design the tax-optimization engine that recommends which assets to donate"
            ]
        },
        {
            "id": "S2-005",
            "name": "Private Credit Income Ladder",
            "category": "Private Credit",
            "description": (
                "A structured series of private credit investments with staggered maturities (1, 3, 5, and 7 years) "
                "designed to mimic a bond ladder but with higher yields. Each 'rung' invests in a diversified pool of "
                "senior secured direct loans. Provides predictable income with natural liquidity as rungs mature."
            ),
            "market_signal_link": (
                "Traditional bond ladders deliver inadequate yield in the current environment. "
                "Private credit offers a meaningful yield premium (3-5% above investment grade bonds) with manageable risk in senior secured positions. "
                "Laddered structure solves the liquidity concern that keeps many retirees away from private credit. "
                "Positioned as the next evolution of the bond ladder for sophisticated income investors."
            ),
            "target_client_segment": "Income-focused retirees and pre-retirees (ages 58-75, $500K-$3M) currently holding traditional bond ladders",
            "dvf_scores": {
                "desirability": {
                    "score": 82,
                    "justification": (
                        "Directly addresses the 'yield gap' frustration among income-oriented retirees. "
                        "The ladder concept is familiar and intuitive to clients who already understand bond ladders. "
                        "Strong positioning as an upgrade to, not replacement of, their existing income strategy."
                    )
                },
                "viability": {
                    "score": 74,
                    "justification": (
                        "1.0-1.25% management fee across the ladder generates solid revenue. "
                        "Staggered maturity structure creates natural reinvestment opportunities. "
                        "Higher minimums ($100K per rung, $400K total) limit the addressable market but improve economics per client."
                    )
                },
                "feasibility": {
                    "score": 60,
                    "justification": (
                        "Requires sourcing or partnering for diversified direct lending pools at four different maturity targets. "
                        "Each rung essentially requires a separate fund or sub-fund structure. "
                        "Complexity in portfolio construction and ongoing management. "
                        "10-12 month build timeline."
                    )
                }
            },
            "key_risks": [
                "Credit cycle downturn could impair multiple rungs simultaneously, defeating the diversification benefit",
                "Complexity of managing four synchronized lending pools may lead to operational errors or inconsistent client experience"
            ],
            "suggested_next_steps": [
                "Model the yield curve and credit risk for each rung using historical direct lending data",
                "Evaluate whether to build in-house lending capability or sub-advise to specialist managers",
                "Test the concept with 20 advisors who have large retirement-focused books"
            ]
        },
        {
            "id": "S2-006",
            "name": "Family Governance & Wealth Transfer Advisory",
            "category": "Advisory Service",
            "description": (
                "A premium advisory engagement that guides ultra-high-net-worth families through the governance and "
                "communication challenges of intergenerational wealth transfer. Includes family meeting facilitation, "
                "heir financial readiness assessments, trust structure optimization, and a digital family dashboard "
                "for shared visibility into estate plans and responsibilities."
            ),
            "market_signal_link": (
                "The $84 trillion wealth transfer is not just a financial event but a family governance challenge. "
                "Most wealth management firms focus exclusively on the financial structuring, ignoring the human dynamics "
                "that cause 70% of wealth transfers to fail. "
                "Differentiation through a holistic, family-centered approach that competitors are not offering."
            ),
            "target_client_segment": "UHNWI families ($10M+) with multi-generational wealth transfer needs",
            "dvf_scores": {
                "desirability": {
                    "score": 65,
                    "justification": (
                        "Very high value to the clients who need it, but a niche market within the broader client base. "
                        "Families often do not recognize the need until a crisis occurs (death, family conflict). "
                        "Requires proactive advisor engagement and a consultative sell."
                    )
                },
                "viability": {
                    "score": 72,
                    "justification": (
                        "Premium pricing model: $15K-$50K per engagement depending on family complexity. "
                        "High margins since the primary cost is advisor/consultant time. "
                        "Strong AUM retention value and cross-sell into trust, estate, and next-gen services. "
                        "Small volume but high per-engagement revenue."
                    )
                },
                "feasibility": {
                    "score": 70,
                    "justification": (
                        "Requires specialized talent with family governance and facilitation skills, which is rare in typical wealth management. "
                        "May need to hire or partner with family office consultants. "
                        "Digital family dashboard requires moderate technology build. "
                        "Low regulatory complexity. 6-month pilot timeline."
                    )
                }
            },
            "key_risks": [
                "Family dynamics are sensitive; poor facilitation could damage the client relationship and lead to AUM loss",
                "Recruiting advisors with both financial expertise and family governance skills is difficult"
            ],
            "suggested_next_steps": [
                "Identify 10 UHNWI families with known multi-generational complexity for a pilot",
                "Hire or contract a family governance specialist to design the engagement framework",
                "Build a prototype family dashboard showing estate overview, roles, and action items"
            ]
        }
    ]
}


# ============================================================
# SAVE ALL SCENARIOS
# ============================================================

all_scenarios = [scenario_1, scenario_2]

output_path = "/home/claude/idea_engine_scenarios.json"
with open(output_path, "w") as f:
    json.dump(all_scenarios, f, indent=2)

print(f"Saved {len(all_scenarios)} scenarios with {sum(len(s['ideas']) for s in all_scenarios)} total ideas")
print(f"Output: {output_path}")

# Print summary
for s in all_scenarios:
    print(f"\n{'='*60}")
    print(f"Scenario: {s['scenario_title']}")
    print(f"Ideas: {len(s['ideas'])}")
    for idea in s['ideas']:
        d = idea['dvf_scores']['desirability']['score']
        v = idea['dvf_scores']['viability']['score']
        f_score = idea['dvf_scores']['feasibility']['score']
        composite = 0.40 * d + 0.35 * v + 0.25 * f_score
        print(f"  {idea['id']}: {idea['name']}")
        print(f"    D={d}  V={v}  F={f_score}  Composite={composite:.1f}")
