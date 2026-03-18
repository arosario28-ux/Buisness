import streamlit as st

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="S.C. Reapers",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS injection ─────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ---- Google Font ---- */
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;600&display=swap');

    /* ---- Base Reset ---- */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0a0a0a;
        color: #f0f0f0;
        font-family: 'Barlow', sans-serif;
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header {visibility: hidden;}

    /* ---- Hero Section ---- */
    .hero {
        background: linear-gradient(135deg, #1a0000 0%, #0a0a0a 60%, #1a0000 100%);
        border-bottom: 3px solid #cc0000;
        padding: 60px 40px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(ellipse at center, rgba(204,0,0,0.15) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-title {
        font-family: 'Bebas Neue', sans-serif;
        font-size: clamp(3rem, 8vw, 7rem);
        letter-spacing: 0.08em;
        color: #cc0000;
        text-shadow: 0 0 40px rgba(204,0,0,0.5), 2px 2px 0 #000;
        margin: 0;
        line-height: 1;
    }
    .hero-subtitle {
        font-family: 'Barlow', sans-serif;
        font-size: 1.1rem;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        color: #888;
        margin-top: 10px;
    }
    .hero-badge {
        display: inline-block;
        margin-top: 24px;
        padding: 6px 22px;
        border: 1px solid #cc0000;
        color: #cc0000;
        font-size: 0.75rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
    }

    /* ---- Nav Bar ---- */
    .nav {
        display: flex;
        justify-content: center;
        gap: 40px;
        padding: 18px 0;
        background: #111;
        border-bottom: 2px solid #1e1e1e;
    }
    .nav a {
        color: #aaa;
        text-decoration: none;
        font-size: 0.85rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        transition: color 0.2s;
    }
    .nav a:hover { color: #cc0000; }

    /* ---- Section Title ---- */
    .section-title {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 2.4rem;
        letter-spacing: 0.06em;
        color: #cc0000;
        border-left: 5px solid #cc0000;
        padding-left: 16px;
        margin-bottom: 20px;
        line-height: 1;
    }

    /* ---- Cards ---- */
    .card {
        background: #111;
        border: 1px solid #1e1e1e;
        border-top: 3px solid #cc0000;
        padding: 24px;
        border-radius: 2px;
        height: 100%;
    }
    .card h3 {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 1.5rem;
        color: #cc0000;
        margin: 0 0 8px;
    }
    .card p {
        font-size: 0.9rem;
        color: #999;
        line-height: 1.6;
        margin: 0;
    }

    /* ---- Stat Block ---- */
    .stat-row {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        margin-top: 10px;
    }
    .stat-box {
        flex: 1;
        min-width: 100px;
        background: #111;
        border: 1px solid #1e1e1e;
        border-bottom: 3px solid #cc0000;
        text-align: center;
        padding: 20px 10px;
        border-radius: 2px;
    }
    .stat-num {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 2.5rem;
        color: #cc0000;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.7rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #666;
        margin-top: 4px;
    }

    /* ---- Divider ---- */
    .red-divider {
        border: none;
        border-top: 1px solid #1e1e1e;
        margin: 40px 0;
    }

    /* ---- Footer ---- */
    .site-footer {
        text-align: center;
        padding: 30px;
        color: #333;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        border-top: 1px solid #1a1a1a;
        margin-top: 60px;
    }
    .site-footer span { color: #cc0000; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <p class="hero-title">S.C. REAPERS</p>
        <p class="hero-subtitle">Fear the scythe &nbsp;|&nbsp; Est. 2024</p>
        <span class="hero-badge">⚽ Official Club Website</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Nav (decorative — real navigation uses sidebar or tabs below) ────────────
st.markdown(
    """
    <div class="nav">
        <a href="#">Home</a>
        <a href="#">Roster</a>
        <a href="#">Schedule</a>
        <a href="#">Stats</a>
        <a href="#">News</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ── Season Stats ─────────────────────────────────────────────────────────────
st.markdown('<p class="section-title">Season at a Glance</p>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="stat-row">
        <div class="stat-box">
            <div class="stat-num">8</div>
            <div class="stat-label">Wins</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">2</div>
            <div class="stat-label">Draws</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">1</div>
            <div class="stat-label">Losses</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">24</div>
            <div class="stat-label">Goals For</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">7</div>
            <div class="stat-label">Goals Against</div>
        </div>
        <div class="stat-box">
            <div class="stat-num">1st</div>
            <div class="stat-label">League Rank</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="red-divider">', unsafe_allow_html=True)

# ── News / Highlights ────────────────────────────────────────────────────────
st.markdown('<p class="section-title">Latest News</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Match Report</h3>
            <p>The Reapers sealed a dominant 3–0 victory on home turf, with a brace from the captain and an outstanding long-range strike in the 78th minute.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>New Signing</h3>
            <p>The club is thrilled to announce the addition of a highly-touted midfielder who brings pace, vision, and championship experience to the squad.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Training Camp</h3>
            <p>Pre-season training camp dates have been confirmed. All registered players are expected to report by 8 AM on the opening day. Details via email.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="red-divider">', unsafe_allow_html=True)

# ── Upcoming Fixtures ────────────────────────────────────────────────────────
st.markdown('<p class="section-title">Upcoming Fixtures</p>', unsafe_allow_html=True)

fixtures = [
    ("Mar 22, 2026", "S.C. Reapers", "vs", "FC Iron Wall",    "Home", "3:00 PM"),
    ("Mar 29, 2026", "S.C. Reapers", "vs", "Northgate United","Away", "5:30 PM"),
    ("Apr 05, 2026", "S.C. Reapers", "vs", "Silver Wolves",   "Home", "2:00 PM"),
]

for date, home, _, away, location, time in fixtures:
    loc_color = "#cc0000" if location == "Home" else "#555"
    st.markdown(
        f"""
        <div style="
            background:#111;
            border:1px solid #1e1e1e;
            border-left:4px solid {loc_color};
            padding:16px 24px;
            margin-bottom:10px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            flex-wrap:wrap;
            gap:10px;
        ">
            <span style="color:#666;font-size:0.8rem;letter-spacing:0.1em;">{date}</span>
            <span style="font-family:'Bebas Neue',sans-serif;font-size:1.3rem;color:#f0f0f0;">
                {home} &nbsp;<span style="color:#cc0000">vs</span>&nbsp; {away}
            </span>
            <span style="color:#666;font-size:0.8rem;">{location} &nbsp;·&nbsp; {time}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="site-footer">
        © 2026 <span>S.C. Reapers</span> &nbsp;·&nbsp; All Rights Reserved &nbsp;·&nbsp; Fear the Scythe
    </div>
    """,
    unsafe_allow_html=True,
)
