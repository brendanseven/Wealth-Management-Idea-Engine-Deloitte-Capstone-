import streamlit as st
import json
import pandas as pd

# ── Page Config ──
st.set_page_config(
    page_title="Wealth Management Idea Engine",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }
    
    .sub-header {
        font-size: 1.05rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }
    
    .scenario-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #86BC25;
        padding: 1.2rem 1.5rem;
        border-radius: 0 8px 8px 0;
        margin-bottom: 1rem;
        font-size: 0.95rem;
        line-height: 1.6;
        color: #374151;
    }
    
    .signal-tag {
        display: inline-block;
        background: #f0fdf4;
        color: #166534;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        margin: 3px 4px 3px 0;
        border: 1px solid #bbf7d0;
        font-weight: 500;
    }
    
    .idea-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        transition: box-shadow 0.2s;
    }
    
    .idea-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .idea-rank {
        font-size: 1.6rem;
        font-weight: 700;
        color: #86BC25;
        margin-right: 0.5rem;
    }
    
    .idea-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1a1a2e;
    }
    
    .idea-category {
        display: inline-block;
        background: #eff6ff;
        color: #1e40af;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-left: 0.5rem;
    }
    
    .idea-segment {
        display: inline-block;
        background: #fef3c7;
        color: #92400e;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-left: 0.3rem;
    }
    
    .score-bar-container {
        display: flex;
        align-items: center;
        margin: 6px 0;
    }
    
    .score-label {
        width: 100px;
        font-size: 0.85rem;
        font-weight: 500;
        color: #4b5563;
    }
    
    .score-value {
        width: 40px;
        text-align: right;
        font-size: 0.85rem;
        font-weight: 600;
        margin-left: 8px;
    }
    
    .composite-score {
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        padding: 0.5rem;
        border-radius: 8px;
    }
    
    .composite-label {
        font-size: 0.75rem;
        text-align: center;
        color: #6b7280;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .section-divider {
        border: none;
        border-top: 2px solid #e5e7eb;
        margin: 1.5rem 0;
    }
    
    .risk-item {
        background: #fef2f2;
        border-left: 3px solid #ef4444;
        padding: 8px 12px;
        border-radius: 0 6px 6px 0;
        margin: 4px 0;
        font-size: 0.88rem;
        color: #7f1d1d;
    }
    
    .next-step-item {
        background: #f0fdf4;
        border-left: 3px solid #22c55e;
        padding: 8px 12px;
        border-radius: 0 6px 6px 0;
        margin: 4px 0;
        font-size: 0.88rem;
        color: #14532d;
    }
    
    .weight-display {
        text-align: center;
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 0.3rem;
    }
    
    div[data-testid="stSidebar"] {
        background: #fafbfc;
    }
    
    .dvf-explanation {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.8rem 1rem;
        font-size: 0.85rem;
        color: #4b5563;
        margin-top: 0.5rem;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)


# ── Load Data ──
@st.cache_data
def load_scenarios():
    with open("idea_engine_scenarios.json", "r") as f:
        return json.load(f)

scenarios = load_scenarios()

# ── Sidebar ──
with st.sidebar:
    st.markdown("### 🎯 Scenario Selection")
    scenario_names = [s["scenario_title"] for s in scenarios]
    selected_scenario_name = st.selectbox(
        "Choose a market scenario",
        scenario_names,
        label_visibility="collapsed"
    )
    selected_scenario = next(s for s in scenarios if s["scenario_title"] == selected_scenario_name)
    
    st.markdown("---")
    st.markdown("### ⚖️ DVF Dimension Weights")
    st.markdown(
        '<div class="dvf-explanation">'
        "Adjust how much each dimension matters in the composite ranking. "
        "Weights are automatically normalized to sum to 100%."
        "</div>",
        unsafe_allow_html=True
    )
    
    st.markdown("")
    
    w_d = st.slider("**Desirability** (market demand)", 0, 100, 40, key="w_d")
    w_v = st.slider("**Viability** (business economics)", 0, 100, 35, key="w_v")
    w_f = st.slider("**Feasibility** (implementation)", 0, 100, 25, key="w_f")
    
    total = w_d + w_v + w_f
    if total == 0:
        norm_d, norm_v, norm_f = 1/3, 1/3, 1/3
    else:
        norm_d = w_d / total
        norm_v = w_v / total
        norm_f = w_f / total
    
    st.markdown(
        f'<div class="weight-display">'
        f'Normalized: D={norm_d:.0%} / V={norm_v:.0%} / F={norm_f:.0%}'
        f'</div>',
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### 🔍 Filters")
    
    all_categories = sorted(set(idea["category"] for idea in selected_scenario["ideas"]))
    selected_categories = st.multiselect(
        "Asset Class / Category",
        all_categories,
        default=all_categories
    )
    
    min_composite = st.slider("Minimum Composite Score", 0, 100, 0)

    st.markdown("---")
    st.markdown(
        '<div style="text-align:center; color:#9ca3af; font-size:0.78rem;">'
        "Deloitte Group 2 | MSBA Capstone 2026"
        "</div>",
        unsafe_allow_html=True
    )


# ── Main Content ──
st.markdown('<div class="main-header">💡 Wealth Management Idea Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">'
    "AI-powered ideation and DVF prioritization for wealth management product strategy"
    "</div>",
    unsafe_allow_html=True
)

# Scenario Context
st.markdown(f"### 📋 Scenario: {selected_scenario['scenario_title']}")
st.markdown(
    f'<div class="scenario-box">{selected_scenario["scenario_description"]}</div>',
    unsafe_allow_html=True
)

# Market Signals
signals_html = "".join(
    f'<span class="signal-tag">📡 {signal}</span>'
    for signal in selected_scenario["market_signals"]
)
st.markdown(f"**Market Signals:**\n\n{signals_html}", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── Score and Rank Ideas ──
ideas_with_scores = []
for idea in selected_scenario["ideas"]:
    d = idea["dvf_scores"]["desirability"]["score"]
    v = idea["dvf_scores"]["viability"]["score"]
    f_score = idea["dvf_scores"]["feasibility"]["score"]
    composite = norm_d * d + norm_v * v + norm_f * f_score
    
    if idea["category"] in selected_categories and composite >= min_composite:
        ideas_with_scores.append({
            **idea,
            "d_score": d,
            "v_score": v,
            "f_score": f_score,
            "composite": round(composite, 1)
        })

ideas_with_scores.sort(key=lambda x: x["composite"], reverse=True)

# ── Summary Chart ──
if ideas_with_scores:
    st.markdown(f"### 📊 Ranked Ideas ({len(ideas_with_scores)} results)")
    
    chart_data = pd.DataFrame([
        {
            "Idea": idea["name"][:40] + ("..." if len(idea["name"]) > 40 else ""),
            "Desirability": idea["d_score"] * norm_d,
            "Viability": idea["v_score"] * norm_v,
            "Feasibility": idea["f_score"] * norm_f,
        }
        for idea in ideas_with_scores
    ])
    chart_data = chart_data.set_index("Idea")
    
    st.bar_chart(
        chart_data,
        color=["#86BC25", "#1A4F8B", "#D35400"],
        horizontal=True,
        height=max(250, len(ideas_with_scores) * 50)
    )
    
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # ── Idea Cards ──
    for rank, idea in enumerate(ideas_with_scores, 1):
        
        def get_score_color(score):
            if score >= 80:
                return "#16a34a"
            elif score >= 65:
                return "#ca8a04"
            elif score >= 50:
                return "#ea580c"
            else:
                return "#dc2626"
        
        composite_color = get_score_color(idea["composite"])
        
        with st.container():
            st.markdown(
                f'<div class="idea-card">'
                f'<span class="idea-rank">#{rank}</span>'
                f'<span class="idea-name">{idea["name"]}</span>'
                f'<span class="idea-category">{idea["category"]}</span>'
                f'<span class="idea-segment">{idea["target_client_segment"][:50]}</span>'
                f'</div>',
                unsafe_allow_html=True
            )
            
            col_scores, col_composite, col_desc = st.columns([2, 1, 3])
            
            with col_scores:
                st.markdown("**DVF Scores**")
                
                for label, score, color, weight_pct in [
                    ("Desirability", idea["d_score"], "#86BC25", f"{norm_d:.0%}"),
                    ("Viability", idea["v_score"], "#1A4F8B", f"{norm_v:.0%}"),
                    ("Feasibility", idea["f_score"], "#D35400", f"{norm_f:.0%}")
                ]:
                    st.markdown(
                        f'<div class="score-bar-container">'
                        f'<span class="score-label">{label} <span style="color:#9ca3af;">({weight_pct})</span></span>'
                        f'<div style="flex:1; background:#e5e7eb; border-radius:4px; height:20px; margin:0 8px;">'
                        f'<div style="width:{score}%; background:{color}; height:100%; border-radius:4px; '
                        f'transition:width 0.3s;"></div></div>'
                        f'<span class="score-value" style="color:{color};">{score}</span>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
            
            with col_composite:
                st.markdown(
                    f'<div class="composite-label">Composite</div>'
                    f'<div class="composite-score" style="color:{composite_color};">{idea["composite"]}</div>',
                    unsafe_allow_html=True
                )
            
            with col_desc:
                st.markdown("**Description**")
                st.markdown(f'<div style="font-size:0.9rem; color:#374151; line-height:1.6;">{idea["description"]}</div>', unsafe_allow_html=True)
            
            # Expandable details
            with st.expander("View full analysis", expanded=False):
                detail_col1, detail_col2 = st.columns(2)
                
                with detail_col1:
                    st.markdown("**📡 Market Signal Link**")
                    st.markdown(f'<div style="font-size:0.9rem; line-height:1.6;">{idea["market_signal_link"]}</div>', unsafe_allow_html=True)
                    
                    st.markdown("")
                    st.markdown("**⚠️ Key Risks**")
                    for risk in idea["key_risks"]:
                        st.markdown(f'<div class="risk-item">{risk}</div>', unsafe_allow_html=True)
                
                with detail_col2:
                    st.markdown("**📊 Score Justifications**")
                    for dim_name, dim_key in [("Desirability", "desirability"), ("Viability", "viability"), ("Feasibility", "feasibility")]:
                        st.markdown(f"*{dim_name}:* {idea['dvf_scores'][dim_key]['justification']}")
                    
                    st.markdown("")
                    st.markdown("**✅ Suggested Next Steps**")
                    for step in idea["suggested_next_steps"]:
                        st.markdown(f'<div class="next-step-item">{step}</div>', unsafe_allow_html=True)
            
            st.markdown("")

else:
    st.warning("No ideas match the current filters. Try adjusting the category filter or lowering the minimum composite score.")


# ── Footer ──
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center; color:#9ca3af; font-size:0.82rem; padding:1rem 0;">'
    "Wealth Management Idea Engine | Deloitte Capstone Project | Prototype v1.0<br>"
    "DVF Framework: Desirability (market demand) · Viability (business economics) · Feasibility (implementation readiness)"
    "</div>",
    unsafe_allow_html=True
)
