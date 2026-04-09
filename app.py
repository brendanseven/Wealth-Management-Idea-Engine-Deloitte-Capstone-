import streamlit as st
import json
import pandas as pd

# ── Page Config ──
st.set_page_config(
    page_title="Wealth Management Idea Engine",
    page_icon="IE",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──
st.markdown("""
<style>
    /* Fix broken Material Symbols icons */
    [data-testid="stIconMaterial"] {
        font-size: 0 !important;
        width: 0;
        height: 0;
        display: inline-block;
        vertical-align: middle;
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        border-left: 7px solid #6b7280;
        margin-right: 6px;
    }
    
    [data-testid="stExpander"][open] [data-testid="stIconMaterial"] {
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 7px solid #6b7280;
        border-bottom: none;
    }
    
    [data-testid="baseButton-headerNoPadding"] [data-testid="stIconMaterial"] {
        font-size: 0 !important;
        width: 0;
        height: 0;
        display: inline-block;
        vertical-align: middle;
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        border-left: 7px solid #6b7280;
        margin-right: 6px;
    }
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0.2rem; }
    .sub-header { font-size: 1.05rem; color: #6b7280; margin-bottom: 1.5rem; font-weight: 400; }
    .scenario-box { background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-left: 4px solid #86BC25; padding: 1.2rem 1.5rem; border-radius: 0 8px 8px 0; margin-bottom: 1rem; font-size: 0.95rem; line-height: 1.6; color: #374151; }
    .signal-tag { display: inline-block; background: #f0fdf4; color: #166534; padding: 4px 12px; border-radius: 20px; font-size: 0.82rem; margin: 3px 4px 3px 0; border: 1px solid #bbf7d0; font-weight: 500; }
    .idea-card { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
    .idea-rank { font-size: 1.6rem; font-weight: 700; color: #86BC25; margin-right: 0.5rem; }
    .idea-name { font-size: 1.2rem; font-weight: 600; color: #1a1a2e; }
    .idea-category { display: inline-block; background: #eff6ff; color: #1e40af; padding: 3px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 500; margin-left: 0.5rem; }
    .idea-segment { display: inline-block; background: #fef3c7; color: #92400e; padding: 3px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 500; margin-left: 0.3rem; }
    .score-bar-container { display: flex; align-items: center; margin: 6px 0; }
    .score-label { width: 100px; font-size: 0.85rem; font-weight: 500; color: #4b5563; }
    .score-value { width: 40px; text-align: right; font-size: 0.85rem; font-weight: 600; margin-left: 8px; }
    .composite-score { font-size: 2rem; font-weight: 700; text-align: center; padding: 0.5rem; border-radius: 8px; }
    .composite-label { font-size: 0.75rem; text-align: center; color: #6b7280; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
    .section-divider { border: none; border-top: 2px solid #e5e7eb; margin: 1.5rem 0; }
    .risk-item { background: #fef2f2; border-left: 3px solid #ef4444; padding: 8px 12px; border-radius: 0 6px 6px 0; margin: 4px 0; font-size: 0.88rem; color: #7f1d1d; }
    .next-step-item { background: #f0fdf4; border-left: 3px solid #22c55e; padding: 8px 12px; border-radius: 0 6px 6px 0; margin: 4px 0; font-size: 0.88rem; color: #14532d; }
    .weight-display { text-align: center; font-size: 0.9rem; color: #6b7280; margin-top: 0.3rem; }
    div[data-testid="stSidebar"] { background: #fafbfc; }
    .dvf-explanation { background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 0.8rem 1rem; font-size: 0.85rem; color: #4b5563; margin-top: 0.5rem; line-height: 1.5; }
    .theme-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; border-left: 4px solid #86BC25; }
    .theme-title { font-size: 1.1rem; font-weight: 600; color: #1a1a2e; }
    .theme-desc { font-size: 0.85rem; color: #6b7280; margin-top: 0.3rem; line-height: 1.4; }
    .subcat-label { font-size: 0.9rem; font-weight: 500; color: #1A4F8B; margin: 0.5rem 0 0.3rem 0.5rem; }
    .variation-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.8rem 1rem; margin: 0.4rem 0; }
    .variation-name { font-size: 0.95rem; font-weight: 600; color: #1a1a2e; }
    .variation-desc { font-size: 0.85rem; color: #4b5563; margin-top: 0.3rem; line-height: 1.4; }
    .dvf-shift { font-size: 0.8rem; color: #86BC25; font-style: italic; margin-top: 0.3rem; }
    .segment-card { background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 0.8rem 1rem; margin: 0.4rem 0; }
    .impl-card { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 0.8rem 1rem; margin: 0.4rem 0; }
</style>
""", unsafe_allow_html=True)


# ── Load Data ──
@st.cache_data
def load_scenarios():
    with open("idea_engine_scenarios.json", "r") as f:
        return json.load(f)

@st.cache_data
def load_hierarchy_and_feedback():
    try:
        with open("hierarchy_and_feedback.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"hierarchies": [], "feedback": {}}

scenarios = load_scenarios()
hf_data = load_hierarchy_and_feedback()


# ── Helper: Get idea by ID ──
def get_idea_by_id(ideas, idea_id):
    for idea in ideas:
        if idea.get("id") == idea_id:
            return idea
    return None

def get_score_color(score):
    if score >= 80: return "#16a34a"
    elif score >= 65: return "#ca8a04"
    elif score >= 50: return "#ea580c"
    else: return "#dc2626"


# ── Helper: Render an idea card ──
def render_idea_card(idea, rank, norm_d, norm_v, norm_f, show_feedback=True):
    dvf = idea.get("dvf_scores", {})
    d = dvf.get("desirability", {})
    v = dvf.get("viability", {})
    f_dim = dvf.get("feasibility", {})
    d_score = d.get("score", 0)
    v_score = v.get("score", 0)
    f_score = f_dim.get("score", 0)
    composite = round(norm_d * d_score + norm_v * v_score + norm_f * f_score, 1)
    composite_color = get_score_color(composite)
    target = idea.get("target_client_segment", "")

    st.markdown(
        f'<div class="idea-card">'
        f'<span class="idea-rank">#{rank}</span>'
        f'<span class="idea-name">{idea["name"]}</span>'
        f'<span class="idea-category">{idea.get("category", "")}</span>'
        f'<span class="idea-segment">{str(target)[:50]}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

    col_scores, col_composite, col_desc = st.columns([2, 1, 3])

    with col_scores:
        st.markdown("**DVF Scores**")
        for label, score, color, weight_pct in [
            ("Desirability", d_score, "#86BC25", f"{norm_d:.0%}"),
            ("Viability", v_score, "#1A4F8B", f"{norm_v:.0%}"),
            ("Feasibility", f_score, "#D35400", f"{norm_f:.0%}")
        ]:
            st.markdown(
                f'<div class="score-bar-container">'
                f'<span class="score-label">{label} <span style="color:#9ca3af;">({weight_pct})</span></span>'
                f'<div style="flex:1; background:#e5e7eb; border-radius:4px; height:20px; margin:0 8px;">'
                f'<div style="width:{score}%; background:{color}; height:100%; border-radius:4px;"></div></div>'
                f'<span class="score-value" style="color:{color};">{score}</span>'
                f'</div>',
                unsafe_allow_html=True
            )

    with col_composite:
        st.markdown(
            f'<div class="composite-label">Composite</div>'
            f'<div class="composite-score" style="color:{composite_color};">{composite}</div>',
            unsafe_allow_html=True
        )

    with col_desc:
        st.markdown("**Description**")
        st.markdown(f'<div style="font-size:0.9rem; color:#374151; line-height:1.6;">{idea["description"]}</div>', unsafe_allow_html=True)

    # Analysis expander
    with st.expander("View full analysis", expanded=False):
        dc1, dc2 = st.columns(2)
        with dc1:
            st.markdown("**Market Signal Link**")
            st.markdown(f'<div style="font-size:0.9rem; line-height:1.6;">{idea.get("market_signal_link", "")}</div>', unsafe_allow_html=True)
            st.markdown("")
            st.markdown("**Key Risks**")
            for risk in idea.get("key_risks", []):
                st.markdown(f'<div class="risk-item">{risk}</div>', unsafe_allow_html=True)
        with dc2:
            st.markdown("**Score Justifications**")
            for dim_name, dim_key in [("Desirability", "desirability"), ("Viability", "viability"), ("Feasibility", "feasibility")]:
                dim_data = dvf.get(dim_key, {})
                st.markdown(f"*{dim_name}:* {dim_data.get('justification', '')}")
            st.markdown("")
            st.markdown("**Suggested Next Steps**")
            for step in idea.get("suggested_next_steps", []):
                st.markdown(f'<div class="next-step-item">{step}</div>', unsafe_allow_html=True)

    # Feedback loop expander
    idea_id = idea.get("id", "")
    feedback = hf_data.get("feedback", {}).get(idea_id)
    if show_feedback and feedback:
        with st.expander("Explore further: variations, segments, and implementation", expanded=False):
            tab1, tab2, tab3 = st.tabs(["Product Variations", "Segment Adaptations", "Implementation Deep Dive"])

            with tab1:
                st.markdown("**How could this idea be modified or extended?**")
                for var in feedback.get("variations", []):
                    st.markdown(
                        f'<div class="variation-card">'
                        f'<div class="variation-name">{var["name"]}</div>'
                        f'<div class="variation-desc">{var["description"]}</div>'
                        f'<div class="dvf-shift">DVF Impact: {var["dvf_shift"]}</div>'
                        f'</div>',
                        unsafe_allow_html=True
                    )

            with tab2:
                st.markdown("**How would this idea change for different client segments?**")
                for seg in feedback.get("segment_adaptations", []):
                    st.markdown(
                        f'<div class="segment-card">'
                        f'<div class="variation-name">Target: {seg["segment"]}</div>'
                        f'<div class="variation-desc">{seg["adaptation"]}</div>'
                        f'<div class="dvf-shift">DVF Impact: {seg["dvf_impact"]}</div>'
                        f'</div>',
                        unsafe_allow_html=True
                    )

            with tab3:
                impl = feedback.get("implementation_deep_dive", {})
                st.markdown("**Critical Path to Launch**")
                for step in impl.get("critical_path", []):
                    st.markdown(f'<div class="impl-card">{step}</div>', unsafe_allow_html=True)

                st.markdown("")
                st.markdown("**Key Decisions**")
                for decision in impl.get("key_decisions", []):
                    st.markdown(f"- {decision}")

                if impl.get("estimated_cost"):
                    st.markdown("")
                    st.markdown(f"**Estimated Cost:** {impl['estimated_cost']}")

    st.markdown("")
    return composite


# ── Sidebar ──
with st.sidebar:
    st.markdown("### Scenario Selection")
    scenario_names = [s["scenario_title"] for s in scenarios]
    selected_scenario_name = st.selectbox("Choose a market scenario", scenario_names, label_visibility="collapsed")
    selected_scenario = next(s for s in scenarios if s["scenario_title"] == selected_scenario_name)

    st.markdown("---")
    st.markdown("### View Mode")
    view_mode = st.radio(
        "How to display ideas",
        ["Ranked List", "Thematic Hierarchy"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### DVF Dimension Weights")
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
        norm_d, norm_v, norm_f = w_d/total, w_v/total, w_f/total

    st.markdown(
        f'<div class="weight-display">Normalized: D={norm_d:.0%} / V={norm_v:.0%} / F={norm_f:.0%}</div>',
        unsafe_allow_html=True
    )

    if view_mode == "Ranked List":
        st.markdown("---")
        st.markdown("### Filters")
        all_categories = sorted(set(idea["category"] for idea in selected_scenario["ideas"]))
        selected_categories = st.multiselect("Asset Class / Category", all_categories, default=all_categories)
        min_composite = st.slider("Minimum Composite Score", 0, 100, 0)

    st.markdown("---")
    st.markdown(
        '<div style="text-align:center; color:#9ca3af; font-size:0.78rem;">'
        "Deloitte Group 2 | MSBA Capstone 2026"
        "</div>",
        unsafe_allow_html=True
    )


# ── Main Content ──
st.markdown('<div class="main-header">Wealth Management Idea Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">'
    "AI-powered ideation and DVF prioritization for wealth management product strategy"
    "</div>",
    unsafe_allow_html=True
)

# Scenario Context
st.markdown(f"### Scenario: {selected_scenario['scenario_title']}")
st.markdown(f'<div class="scenario-box">{selected_scenario["scenario_description"]}</div>', unsafe_allow_html=True)

signals_html = "".join(f'<span class="signal-tag">{s}</span>' for s in selected_scenario.get("market_signals", []))
if signals_html:
    st.markdown(f"**Market Signals:**\n\n{signals_html}", unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# VIEW MODE: RANKED LIST
# ═══════════════════════════════════════════════════════
if view_mode == "Ranked List":
    ideas_with_scores = []
    for idea in selected_scenario["ideas"]:
        dvf = idea.get("dvf_scores", {})
        d = dvf.get("desirability", {}).get("score", 0)
        v = dvf.get("viability", {}).get("score", 0)
        f_score = dvf.get("feasibility", {}).get("score", 0)
        composite = round(norm_d * d + norm_v * v + norm_f * f_score, 1)
        if idea["category"] in selected_categories and composite >= min_composite:
            ideas_with_scores.append({**idea, "composite": composite})

    ideas_with_scores.sort(key=lambda x: x["composite"], reverse=True)

    if ideas_with_scores:
        st.markdown(f"### Ranked Ideas ({len(ideas_with_scores)} results)")

        chart_data = pd.DataFrame([
            {
                "Idea": idea["name"][:40] + ("..." if len(idea["name"]) > 40 else ""),
                "Desirability": idea["dvf_scores"]["desirability"]["score"] * norm_d,
                "Viability": idea["dvf_scores"]["viability"]["score"] * norm_v,
                "Feasibility": idea["dvf_scores"]["feasibility"]["score"] * norm_f,
            }
            for idea in ideas_with_scores
        ])
        chart_data = chart_data.set_index("Idea")
        st.bar_chart(chart_data, color=["#86BC25", "#1A4F8B", "#D35400"], horizontal=True, height=max(250, len(ideas_with_scores) * 50))

        st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

        for rank, idea in enumerate(ideas_with_scores, 1):
            render_idea_card(idea, rank, norm_d, norm_v, norm_f)
    else:
        st.warning("No ideas match the current filters.")


# ═══════════════════════════════════════════════════════
# VIEW MODE: THEMATIC HIERARCHY
# ═══════════════════════════════════════════════════════
elif view_mode == "Thematic Hierarchy":
    # Find the hierarchy for this scenario
    scenario_id = selected_scenario.get("scenario_id", selected_scenario.get("scenario_title", "")[:2].upper())
    hierarchy = None
    for h in hf_data.get("hierarchies", []):
        if h["scenario_id"] == scenario_id:
            hierarchy = h
            break

    if hierarchy:
        st.markdown("### Thematic Idea Hierarchy")
        st.markdown(
            '<div class="dvf-explanation">'
            "Ideas are organized into strategic themes. Expand a theme to explore its sub-categories "
            "and individual product ideas. This view helps you identify which strategic direction to pursue "
            "before drilling into specific products. Inspired by hierarchical mechanism trees from AI-assisted ideation research."
            "</div>",
            unsafe_allow_html=True
        )
        st.markdown("")

        for theme in hierarchy["themes"]:
            # Calculate aggregate stats for the theme
            theme_ideas = [get_idea_by_id(selected_scenario["ideas"], iid) for iid in theme["idea_ids"]]
            theme_ideas = [i for i in theme_ideas if i is not None]
            
            if not theme_ideas:
                continue

            avg_d = sum(i["dvf_scores"]["desirability"]["score"] for i in theme_ideas) / len(theme_ideas)
            avg_v = sum(i["dvf_scores"]["viability"]["score"] for i in theme_ideas) / len(theme_ideas)
            avg_f = sum(i["dvf_scores"]["feasibility"]["score"] for i in theme_ideas) / len(theme_ideas)
            avg_composite = round(norm_d * avg_d + norm_v * avg_v + norm_f * avg_f, 1)
            composite_color = get_score_color(avg_composite)

            with st.expander(f"{theme['theme']} ({len(theme_ideas)} ideas, avg composite: {avg_composite})", expanded=False):
                st.markdown(f'<div class="theme-desc">{theme["description"]}</div>', unsafe_allow_html=True)
                st.markdown("")

                # Theme-level aggregate scores
                tcol1, tcol2, tcol3, tcol4 = st.columns(4)
                with tcol1:
                    st.metric("Avg Desirability", f"{avg_d:.0f}")
                with tcol2:
                    st.metric("Avg Viability", f"{avg_v:.0f}")
                with tcol3:
                    st.metric("Avg Feasibility", f"{avg_f:.0f}")
                with tcol4:
                    st.metric("Avg Composite", avg_composite)

                st.markdown("")

                # Sub-categories
                for subcat in theme.get("sub_categories", []):
                    st.markdown(f'<div class="subcat-label">{subcat["name"]}</div>', unsafe_allow_html=True)
                    
                    subcat_ideas = [get_idea_by_id(selected_scenario["ideas"], iid) for iid in subcat["idea_ids"]]
                    subcat_ideas = [i for i in subcat_ideas if i is not None]
                    
                    # Sort by composite within sub-category
                    for idea in subcat_ideas:
                        dvf = idea["dvf_scores"]
                        idea["_composite"] = round(
                            norm_d * dvf["desirability"]["score"] +
                            norm_v * dvf["viability"]["score"] +
                            norm_f * dvf["feasibility"]["score"], 1
                        )
                    subcat_ideas.sort(key=lambda x: x["_composite"], reverse=True)

                    for rank_in_sub, idea in enumerate(subcat_ideas, 1):
                        render_idea_card(idea, rank_in_sub, norm_d, norm_v, norm_f)

    else:
        st.warning("No hierarchical organization available for this scenario. Showing ranked list instead.")
        # Fallback to ranked list
        ideas_sorted = sorted(
            selected_scenario["ideas"],
            key=lambda i: norm_d * i["dvf_scores"]["desirability"]["score"] + norm_v * i["dvf_scores"]["viability"]["score"] + norm_f * i["dvf_scores"]["feasibility"]["score"],
            reverse=True
        )
        for rank, idea in enumerate(ideas_sorted, 1):
            render_idea_card(idea, rank, norm_d, norm_v, norm_f)


# ── Footer ──
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center; color:#9ca3af; font-size:0.82rem; padding:1rem 0;">'
    "Wealth Management Idea Engine | Deloitte Capstone Project | Prototype v3.0<br>"
    "DVF Framework: Desirability (market demand) · Viability (business economics) · Feasibility (implementation readiness)<br>"
    "Hierarchical organization inspired by AI-assisted creative ideation research (Yang et al., CMU 2025)"
    "</div>",
    unsafe_allow_html=True
)
