import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="S.C. Reapers",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Session state for navigation ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

def nav_to(page):
    st.session_state.page = page

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background-color: #0a0a0a !important;
    color: #e8e8e8;
    font-family: 'Barlow', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }

/* Remove default streamlit padding */
[data-testid="stMain"] > div { padding-top: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #1a0000 0%, #0a0a0a 55%, #1a0000 100%);
    border-bottom: 3px solid #cc0000;
    padding: 50px 40px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(204,0,0,0.2) 0%, transparent 70%);
    pointer-events: none;
}
.hero-logo {
    margin-bottom: 16px;
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(4.5rem, 13vw, 10rem);
    letter-spacing: 0.1em;
    color: #cc0000;
    text-shadow: 0 0 60px rgba(204,0,0,0.5), 3px 3px 0 #000;
    margin: 0;
    line-height: 0.9;
}
.hero-subtitle {
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #ccc;
    margin-top: 14px;
}
.hero-badge {
    display: inline-block;
    margin-top: 22px;
    padding: 6px 22px;
    border: 1px solid #cc0000;
    color: #cc0000;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
}

/* ── Nav Bar ── */
.nav-bar {
    background: #111111;
    border-bottom: 2px solid #1e1e1e;
    display: flex;
    justify-content: center;
    gap: 6px;
    padding: 10px 20px;
    flex-wrap: wrap;
}

/* ── Streamlit button reset for nav ── */
div[data-testid="stHorizontalBlock"] .stButton > button,
.nav-zone .stButton > button {
    background: transparent !important;
    border: 1px solid #2a2a2a !important;
    color: #bbb !important;
    font-family: 'Barlow', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 10px 22px !important;
    border-radius: 2px !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover,
.nav-zone .stButton > button:hover {
    color: #cc0000 !important;
    border-color: #cc0000 !important;
    background: rgba(204,0,0,0.06) !important;
}

/* ── Section Title ── */
.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    letter-spacing: 0.06em;
    color: #cc0000;
    border-left: 5px solid #cc0000;
    padding-left: 16px;
    margin: 30px 0 20px;
    line-height: 1;
}

/* ── Cards ── */
.card {
    background: #151515;
    border: 1px solid #2a2a2a;
    border-top: 3px solid #cc0000;
    padding: 26px;
    border-radius: 2px;
    height: 100%;
}
.card h3 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.6rem;
    color: #cc0000;
    margin: 0 0 10px;
}
.card p { font-size: 0.95rem; color: #ccc; line-height: 1.75; margin: 0; }
.card-tag {
    display: inline-block;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #888;
    border: 1px solid #2a2a2a;
    padding: 3px 10px;
    margin-bottom: 12px;
}

/* ── Stat Block ── */
.stat-row { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px; }
.stat-box {
    flex: 1; min-width: 100px;
    background: #151515; border: 1px solid #2a2a2a;
    border-bottom: 3px solid #cc0000;
    text-align: center; padding: 22px 10px; border-radius: 2px;
}
.stat-num { font-family: 'Bebas Neue', sans-serif; font-size: 2.8rem; color: #cc0000; line-height: 1; }
.stat-label { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #aaa; margin-top: 5px; }

/* ── Divider ── */
.red-divider { border: none; border-top: 1px solid #222; margin: 36px 0; }

/* ── Fixture ── */
.fixture-row {
    background: #151515; border: 1px solid #2a2a2a;
    padding: 18px 26px; margin-bottom: 10px;
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 10px;
}
.fixture-date  { color: #bbb; font-size: 0.82rem; letter-spacing: 0.1em; font-weight: 600; }
.fixture-teams { font-family: 'Bebas Neue', sans-serif; font-size: 1.35rem; color: #f0f0f0; }
.fixture-meta  { color: #aaa; font-size: 0.82rem; font-weight: 600; }

/* ── Coming Soon ── */
.coming-soon { text-align: center; padding: 100px 40px; }
.coming-soon-icon { font-size: 4rem; margin-bottom: 20px; }
.coming-soon-title {
    font-family: 'Bebas Neue', sans-serif; font-size: 4.5rem;
    color: #cc0000; letter-spacing: 0.1em;
    text-shadow: 0 0 40px rgba(204,0,0,0.4); margin: 0;
}
.coming-soon-sub {
    font-size: 0.95rem; font-weight: 600; letter-spacing: 0.2em;
    text-transform: uppercase; color: #bbb; margin-top: 14px;
}
.coming-soon-bar { width: 80px; height: 3px; background: #cc0000; margin: 24px auto 0; }

/* ── Leaders Page ── */
.leader-card {
    background: #151515; border: 1px solid #2a2a2a;
    border-left: 5px solid #cc0000;
    padding: 36px 40px; border-radius: 2px; margin-bottom: 20px;
}
.leader-name {
    font-family: 'Bebas Neue', sans-serif; font-size: 2.2rem;
    color: #cc0000; letter-spacing: 0.08em; margin: 0 0 4px;
}
.leader-role {
    font-size: 0.75rem; font-weight: 700; letter-spacing: 0.22em;
    text-transform: uppercase; color: #888; margin-bottom: 18px;
}
.leader-bio { font-size: 0.97rem; color: #ccc; line-height: 1.8; }
.origin-block {
    background: #1a0000; border: 1px solid #3a0000;
    border-left: 5px solid #cc0000;
    padding: 30px 36px; border-radius: 2px; margin-top: 30px;
}
.origin-block h3 {
    font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem;
    color: #cc0000; margin: 0 0 14px; letter-spacing: 0.06em;
}
.origin-block p { font-size: 0.97rem; color: #ccc; line-height: 1.85; margin: 0; }

/* ── Footer ── */
.site-footer {
    text-align: center; padding: 32px; color: #555;
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.1em;
    border-top: 1px solid #1a1a1a; margin-top: 60px;
}
.site-footer span { color: #cc0000; }

/* ── Page wrapper padding ── */
.page-content { padding: 10px 40px 40px; }
</style>
""", unsafe_allow_html=True)

# ── SVG Logo ─────────────────────────────────────────────────────────────────
LOGO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="110" height="110">
  <!-- Outer shield -->
  <path d="M60 8 L104 28 L104 72 Q104 100 60 114 Q16 100 16 72 L16 28 Z"
        fill="#0a0a0a" stroke="#cc0000" stroke-width="3"/>
  <!-- Inner shield glow ring -->
  <path d="M60 16 L96 33 L96 70 Q96 94 60 106 Q24 94 24 70 L24 33 Z"
        fill="none" stroke="#3a0000" stroke-width="1.5"/>
  <!-- Scythe blade -->
  <path d="M38 52 Q42 32 72 38 Q86 42 82 58 Q78 70 60 68"
        fill="none" stroke="#cc0000" stroke-width="4" stroke-linecap="round"/>
  <!-- Scythe handle -->
  <line x1="60" y1="68" x2="48" y2="88" stroke="#cc0000" stroke-width="3.5" stroke-linecap="round"/>
  <!-- Handle tip -->
  <circle cx="46" cy="90" r="3" fill="#cc0000"/>
  <!-- SCR letters -->
  <text x="60" y="105" text-anchor="middle"
        font-family="'Bebas Neue', sans-serif" font-size="11"
        fill="#cc0000" letter-spacing="3">SCR</text>
</svg>
"""

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <div class="hero-logo">{LOGO_SVG}</div>
    <p class="hero-title">S.C. REAPERS</p>
    <p class="hero-subtitle">Fear the Scythe &nbsp;|&nbsp; Est. 2024 &nbsp;|&nbsp; Carolina</p>
    <span class="hero-badge">⚽ Official Club Website</span>
</div>
""", unsafe_allow_html=True)

# ── Navigation (real Streamlit buttons) ──────────────────────────────────────
st.markdown("<div style='background:#111;border-bottom:2px solid #1e1e1e;padding:12px 40px;'>", unsafe_allow_html=True)

cols = st.columns(6)
nav_items = [
    ("🏠 Home",        "Home"),
    ("👥 Roster",      "Roster"),
    ("📅 Schedule",    "Schedule"),
    ("📊 Stats",       "Stats"),
    ("📰 News",        "News"),
    ("🏆 Our Leaders", "Leaders"),
]
for col, (label, page) in zip(cols, nav_items):
    with col:
        if st.button(label, key=f"nav_{page}"):
            nav_to(page)

st.markdown("</div>", unsafe_allow_html=True)

# ── Active page indicator ─────────────────────────────────────────────────────
current = st.session_state.page
st.markdown(f"""
<div style="background:#111;padding:6px 40px 0;display:flex;gap:0;">
    {''.join(
        f'<span style="font-size:0.65rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;'
        f'color:{"#cc0000" if p == current else "transparent"};padding:4px 0;margin-right:20px;'
        f'border-bottom:{"2px solid #cc0000" if p == current else "2px solid transparent"}">{p}</span>'
        for _, p in nav_items
    )}
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────────────────────────────────────
if current == "Home":
    st.markdown('<div class="page-content">', unsafe_allow_html=True)

    st.markdown('<p class="section-title">Season at a Glance</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stat-row">
        <div class="stat-box"><div class="stat-num">8</div><div class="stat-label">Wins</div></div>
        <div class="stat-box"><div class="stat-num">2</div><div class="stat-label">Draws</div></div>
        <div class="stat-box"><div class="stat-num">1</div><div class="stat-label">Losses</div></div>
        <div class="stat-box"><div class="stat-num">24</div><div class="stat-label">Goals For</div></div>
        <div class="stat-box"><div class="stat-num">7</div><div class="stat-label">Goals Against</div></div>
        <div class="stat-box"><div class="stat-num">1st</div><div class="stat-label">League Rank</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="red-divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Upcoming Fixtures</p>', unsafe_allow_html=True)

    fixtures = [
        ("Mar 22, 2026", "S.C. Reapers", "FC Iron Wall",     "Home", "3:00 PM"),
        ("Mar 29, 2026", "S.C. Reapers", "Northgate United", "Away", "5:30 PM"),
        ("Apr 05, 2026", "S.C. Reapers", "Silver Wolves",    "Home", "2:00 PM"),
    ]
    for date, home, away, location, kickoff in fixtures:
        loc_color = "#cc0000" if location == "Home" else "#555"
        st.markdown(f"""
        <div class="fixture-row" style="border-left:4px solid {loc_color};">
            <span class="fixture-date">{date}</span>
            <span class="fixture-teams">{home} <span style="color:#cc0000">vs</span> {away}</span>
            <span class="fixture-meta">{location} · {kickoff}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: ROSTER — COMING SOON
# ─────────────────────────────────────────────────────────────────────────────
elif current == "Roster":
    st.markdown("""
    <div class="coming-soon">
        <div class="coming-soon-icon">👥</div>
        <p class="coming-soon-title">Coming Soon</p>
        <p class="coming-soon-sub">The full Reapers roster is being assembled — check back shortly.</p>
        <div class="coming-soon-bar"></div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: SCHEDULE — COMING SOON
# ─────────────────────────────────────────────────────────────────────────────
elif current == "Schedule":
    st.markdown("""
    <div class="coming-soon">
        <div class="coming-soon-icon">📅</div>
        <p class="coming-soon-title">Coming Soon</p>
        <p class="coming-soon-sub">The full season schedule will be posted here once confirmed.</p>
        <div class="coming-soon-bar"></div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: STATS — COMING SOON
# ─────────────────────────────────────────────────────────────────────────────
elif current == "Stats":
    st.markdown("""
    <div class="coming-soon">
        <div class="coming-soon-icon">📊</div>
        <p class="coming-soon-title">Coming Soon</p>
        <p class="coming-soon-sub">Detailed player and team stats are on the way — stay tuned.</p>
        <div class="coming-soon-bar"></div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: NEWS
# ─────────────────────────────────────────────────────────────────────────────
elif current == "News":
    st.markdown('<div class="page-content">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Latest News</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card">
            <span class="card-tag">🌟 Club News</span>
            <h3>Welcome to S.C. Reapers</h3>
            <p>S.C. Reapers is a newly formed soccer club proudly based in Carolina.
            Founded in 2024, the club was built from the ground up by passionate players
            and coaches committed to bringing competitive, hard-nosed soccer to the region.
            From day one, the Reapers have set out to build a winning culture — on and off the pitch.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <span class="card-tag">⚽ Match Report</span>
            <h3>Strong Start to the Season</h3>
            <p>The Reapers have hit the ground running in their debut season, posting
            an impressive 8 wins from their first 11 matches. The squad has shown
            quality across all positions, and early signs suggest this club is already
            one to watch in the Carolina soccer scene.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <span class="card-tag">📣 Announcement</span>
            <h3>Growing the Community</h3>
            <p>As a brand new club, S.C. Reapers is actively looking to grow its
            fanbase and community presence across Carolina. Follow us for updates
            on tryouts, training sessions, and upcoming matches. The Reapers are
            just getting started — and the best is yet to come.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: OUR LEADERS
# ─────────────────────────────────────────────────────────────────────────────
elif current == "Leaders":
    st.markdown('<div class="page-content">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Our Leaders</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="leader-card">
        <p class="leader-name">Adrielle Rosario</p>
        <p class="leader-role">⚽ Founder &amp; Club President · Age 16</p>
        <p class="leader-bio">
            Adrielle Rosario is the visionary behind S.C. Reapers — founding the club at just 16 years old
            with an ambition that far exceeds his age. Born and raised in Carolina, Adrielle saw a gap in
            the local soccer community and decided not to wait for someone else to fill it. With zero backing
            and everything to prove, he built the Reapers from the ground up: recruiting players, organizing
            training sessions, and establishing the club's identity around grit, unity, and relentless drive.
            <br><br>
            His leadership philosophy is simple — work harder than everyone else and never let your teammates
            down. At an age when most people are still figuring things out, Adrielle is already running a
            competitive soccer organization and setting a standard for what young leaders in Carolina can achieve.
            The Reapers are his vision, and he intends to see it through.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="origin-block">
        <h3>The Story of S.C. Reapers</h3>
        <p>
            S.C. Reapers was founded in 2024 in Carolina by Adrielle Rosario, a 16-year-old with a
            burning passion for soccer and an even stronger belief that his community deserved a real,
            competitive club to rally behind. The name "Reapers" was chosen deliberately — it represents
            relentlessness, the harvesting of hard work, and the idea that greatness doesn't come without
            sacrifice. The scythe in the club's crest isn't a symbol of fear; it's a symbol of what happens
            when you outwork everyone around you.
            <br><br>
            In their debut season, the Reapers have already made their presence known across the Carolina
            soccer circuit — sitting first in the league standings and drawing attention from fans and
            opponents alike. What started as one teenager's idea is quickly becoming something much bigger.
            <br><br>
            This is just the beginning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-footer">
    © 2026 <span>S.C. Reapers</span> &nbsp;·&nbsp; Carolina &nbsp;·&nbsp;
    Founded by Adrielle Rosario &nbsp;·&nbsp; Fear the Scythe
</div>
""", unsafe_allow_html=True)
