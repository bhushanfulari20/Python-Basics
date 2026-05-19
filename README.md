<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Python Basic Programs – Bhushan Fulari</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<style>
  :root {
    --bg: #0b0f1a;
    --surface: #111827;
    --card: #161d2e;
    --border: #1f2d45;
    --accent: #3ddcf7;
    --accent2: #f7c948;
    --accent3: #7cf7a0;
    --accent4: #f76c8a;
    --accent5: #b57cf7;
    --text: #e2eaf7;
    --muted: #5b7499;
    --snake: #3dda7c;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Space Grotesk', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
  }

  /* ── Animated grid background ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(61,220,124,.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(61,220,124,.04) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridShift 20s linear infinite;
    pointer-events: none;
    z-index: 0;
  }

  @keyframes gridShift {
    0%   { background-position: 0 0; }
    100% { background-position: 40px 40px; }
  }

  /* ── Floating code particles ── */
  .particles {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
  }

  .particle {
    position: absolute;
    font-family: 'Fira Code', monospace;
    font-size: 11px;
    color: var(--snake);
    opacity: 0;
    animation: floatUp var(--dur, 12s) var(--delay, 0s) linear infinite;
    left: var(--x, 50%);
    white-space: nowrap;
  }

  @keyframes floatUp {
    0%   { transform: translateY(110vh); opacity: 0; }
    5%   { opacity: .25; }
    90%  { opacity: .15; }
    100% { transform: translateY(-10vh); opacity: 0; }
  }

  /* ── Wrapper ── */
  .wrapper {
    position: relative;
    z-index: 1;
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 24px 100px;
  }

  /* ── Hero ── */
  .hero {
    text-align: center;
    margin-bottom: 64px;
    animation: fadeDown .8s ease both;
  }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-30px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .snake-icon {
    font-size: 72px;
    display: inline-block;
    animation: snakeWiggle 3s ease-in-out infinite;
    filter: drop-shadow(0 0 24px rgba(61,220,124,.6));
    margin-bottom: 16px;
  }

  @keyframes snakeWiggle {
    0%, 100% { transform: rotate(-6deg) scale(1); }
    50%       { transform: rotate(6deg) scale(1.08); }
  }

  .hero-title {
    font-family: 'Fira Code', monospace;
    font-size: clamp(2rem, 6vw, 3.4rem);
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-bottom: 12px;
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent3) 60%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-subtitle {
    font-size: 1.05rem;
    color: var(--muted);
    font-weight: 400;
    letter-spacing: .5px;
  }

  .badge-row {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 20px;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 14px;
    border-radius: 999px;
    font-family: 'Fira Code', monospace;
    font-size: .72rem;
    font-weight: 500;
    letter-spacing: .5px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--accent3);
    animation: fadePop .5s ease both;
  }

  .badge:nth-child(2) { animation-delay: .1s; }
  .badge:nth-child(3) { animation-delay: .2s; }

  @keyframes fadePop {
    from { opacity: 0; transform: scale(.8); }
    to   { opacity: 1; transform: scale(1); }
  }

  /* ── Section labels ── */
  .section-label {
    font-family: 'Fira Code', monospace;
    font-size: .72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ── Programs grid ── */
  .programs-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 18px;
    margin-bottom: 56px;
  }

  /* ── Program card ── */
  .prog-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    opacity: 0;
    transform: translateY(24px);
    transition: transform .35s ease, border-color .3s, box-shadow .3s;
    animation: cardReveal .5s ease forwards;
  }

  .prog-card:nth-child(1) { animation-delay: .1s; }
  .prog-card:nth-child(2) { animation-delay: .2s; }
  .prog-card:nth-child(3) { animation-delay: .3s; }
  .prog-card:nth-child(4) { animation-delay: .4s; }
  .prog-card:nth-child(5) { animation-delay: .5s; }

  @keyframes cardReveal {
    to { opacity: 1; transform: translateY(0); }
  }

  .prog-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at var(--mx,50%) var(--my,50%), var(--glow,.2) 0%, transparent 60%);
    opacity: 0;
    transition: opacity .4s;
    pointer-events: none;
  }

  .prog-card:hover::before { opacity: 1; }
  .prog-card:hover {
    transform: translateY(-4px);
    border-color: var(--clr, var(--accent));
    box-shadow: 0 16px 40px rgba(0,0,0,.35), 0 0 0 1px var(--clr, var(--accent));
  }

  /* scanning line on hover */
  .prog-card::after {
    content: '';
    position: absolute;
    left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--clr, var(--accent)), transparent);
    top: -2px;
    transition: top .0s;
  }

  .prog-card:hover::after {
    animation: scanLine 1.2s ease forwards;
  }

  @keyframes scanLine {
    from { top: 0%; opacity: 1; }
    to   { top: 100%; opacity: 0; }
  }

  .prog-icon {
    font-size: 32px;
    margin-bottom: 12px;
    display: inline-block;
    animation: none;
    transition: transform .3s;
  }

  .prog-card:hover .prog-icon { transform: scale(1.2) rotate(-5deg); }

  .prog-name {
    font-family: 'Fira Code', monospace;
    font-size: .92rem;
    font-weight: 600;
    color: var(--clr, var(--accent));
    margin-bottom: 6px;
    letter-spacing: .3px;
  }

  .prog-desc {
    font-size: .82rem;
    color: var(--muted);
    line-height: 1.55;
    margin-bottom: 16px;
  }

  /* code snippet */
  .code-snippet {
    background: #090d16;
    border-radius: 10px;
    padding: 12px 14px;
    font-family: 'Fira Code', monospace;
    font-size: .72rem;
    line-height: 1.7;
    color: #768aad;
    border: 1px solid #1a2540;
    overflow: hidden;
    max-height: 0;
    opacity: 0;
    transition: max-height .4s ease, opacity .3s ease, padding .3s;
  }

  .prog-card:hover .code-snippet {
    max-height: 160px;
    opacity: 1;
  }

  .kw  { color: var(--accent5); }
  .fn  { color: var(--accent2); }
  .str { color: var(--accent3); }
  .num { color: var(--accent4); }
  .cm  { color: #3a4f70; }
  .op  { color: var(--accent); }

  .check-tag {
    position: absolute;
    top: 16px; right: 16px;
    width: 22px; height: 22px;
    border-radius: 50%;
    background: var(--clr, var(--accent));
    display: flex; align-items: center; justify-content: center;
    font-size: 11px;
    box-shadow: 0 0 12px var(--clr, var(--accent));
  }

  /* ── Tech stack ── */
  .tech-row {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 56px;
    animation: fadeIn 1s .7s ease both;
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }

  .tech-chip {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    font-family: 'Fira Code', monospace;
    font-size: .8rem;
    font-weight: 500;
    color: var(--accent2);
    position: relative;
    overflow: hidden;
  }

  .tech-chip .pip {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--accent3);
    box-shadow: 0 0 8px var(--accent3);
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: .5; transform: scale(.7); }
  }

  /* ── How to run ── */
  .steps {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 56px;
    animation: fadeIn 1s .9s ease both;
  }

  .step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 18px 20px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    transition: border-color .3s, transform .3s;
  }

  .step:hover {
    border-color: var(--accent);
    transform: translateX(6px);
  }

  .step-num {
    font-family: 'Fira Code', monospace;
    font-size: .75rem;
    font-weight: 700;
    color: var(--bg);
    background: var(--accent3);
    width: 26px; height: 26px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }

  .step-text {
    font-size: .88rem;
    color: var(--muted);
    line-height: 1.5;
    padding-top: 2px;
  }

  .step-text code {
    font-family: 'Fira Code', monospace;
    color: var(--accent);
    background: #0d1525;
    padding: 2px 7px;
    border-radius: 5px;
    font-size: .8rem;
  }

  /* ── Author card ── */
  .author-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 32px;
    display: flex;
    align-items: center;
    gap: 24px;
    flex-wrap: wrap;
    animation: fadeIn 1s 1.1s ease both;
    position: relative;
    overflow: hidden;
  }

  .author-card::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(61,220,124,.12) 0%, transparent 70%);
  }

  .avatar {
    width: 72px; height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent3), var(--accent));
    display: flex; align-items: center; justify-content: center;
    font-size: 28px;
    flex-shrink: 0;
    box-shadow: 0 0 24px rgba(61,220,124,.4);
    animation: avatarPulse 3s ease-in-out infinite;
  }

  @keyframes avatarPulse {
    0%, 100% { box-shadow: 0 0 24px rgba(61,220,124,.4); }
    50%       { box-shadow: 0 0 40px rgba(61,220,124,.7); }
  }

  .author-info { flex: 1; min-width: 180px; }

  .author-name {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 4px;
    background: linear-gradient(90deg, var(--text), var(--accent3));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .author-role {
    font-size: .82rem;
    color: var(--muted);
    margin-bottom: 14px;
  }

  .social-links {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }

  .social-link {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 16px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: var(--surface);
    font-family: 'Fira Code', monospace;
    font-size: .75rem;
    color: var(--text);
    text-decoration: none;
    transition: all .25s;
  }

  .social-link:hover {
    border-color: var(--accent);
    color: var(--accent);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(61,220,124,.2);
  }

  /* ── Typewriter cursor ── */
  @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
  .cursor {
    display: inline-block;
    width: 3px; height: 1em;
    background: var(--accent);
    vertical-align: text-bottom;
    border-radius: 2px;
    animation: blink .8s step-end infinite;
    margin-left: 3px;
  }

  /* ── Footer ── */
  .footer {
    text-align: center;
    margin-top: 64px;
    font-family: 'Fira Code', monospace;
    font-size: .75rem;
    color: var(--muted);
    animation: fadeIn 1s 1.4s ease both;
  }

  /* ── Terminal prompt header ── */
  .terminal-bar {
    background: #0a0e1a;
    border: 1px solid var(--border);
    border-radius: 12px 12px 0 0;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: -1px;
  }

  .dot { width: 11px; height: 11px; border-radius: 50%; }
  .dot-r { background: #f76c8a; }
  .dot-y { background: #f7c948; }
  .dot-g { background: var(--accent3); }

  .terminal-title {
    font-family: 'Fira Code', monospace;
    font-size: .72rem;
    color: var(--muted);
    margin-left: 8px;
  }
</style>
</head>
<body>

<!-- Floating code particles -->
<div class="particles" id="particles"></div>

<div class="wrapper">

  <!-- Hero -->
  <div class="hero">
    <div class="snake-icon">🐍</div>
    <h1 class="hero-title">Python Basic Programs<span class="cursor"></span></h1>
    <p class="hero-subtitle">A collection of beginner programs built with if-else conditions</p>
    <div class="badge-row">
      <span class="badge">🟢 Python 3</span>
      <span class="badge">⚡ Beginner Friendly</span>
      <span class="badge">✅ 5 Programs</span>
    </div>
  </div>

  <!-- Programs -->
  <div class="section-label">// programs included</div>
  <div class="programs-grid" id="prog-grid">

    <div class="prog-card" style="--clr:#3ddcf7;--glow:rgba(61,220,247,.12);" data-idx="0">
      <div class="check-tag">✓</div>
      <div class="prog-icon">📅</div>
      <div class="prog-name">Leap Year Checker</div>
      <div class="prog-desc">Determines if a given year is a leap year using divisibility rules.</div>
      <div class="code-snippet">
<span class="kw">def</span> <span class="fn">is_leap</span>(year):<br>
&nbsp;&nbsp;<span class="kw">if</span> year <span class="op">%</span> <span class="num">400</span> <span class="op">==</span> <span class="num">0</span>: <span class="kw">return</span> <span class="str">True</span><br>
&nbsp;&nbsp;<span class="kw">if</span> year <span class="op">%</span> <span class="num">100</span> <span class="op">==</span> <span class="num">0</span>: <span class="kw">return</span> <span class="str">False</span><br>
&nbsp;&nbsp;<span class="kw">return</span> year <span class="op">%</span> <span class="num">4</span> <span class="op">==</span> <span class="num">0</span>
      </div>
    </div>

    <div class="prog-card" style="--clr:#7cf7a0;--glow:rgba(124,247,160,.12);" data-idx="1">
      <div class="check-tag">✓</div>
      <div class="prog-icon">📝</div>
      <div class="prog-name">Pass or Fail Checker</div>
      <div class="prog-desc">Evaluates student marks and outputs pass/fail based on a threshold.</div>
      <div class="code-snippet">
<span class="kw">def</span> <span class="fn">result</span>(marks):<br>
&nbsp;&nbsp;<span class="kw">if</span> marks <span class="op">>=</span> <span class="num">40</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Pass 🎉"</span>)<br>
&nbsp;&nbsp;<span class="kw">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Fail 😢"</span>)
      </div>
    </div>

    <div class="prog-card" style="--clr:#f7c948;--glow:rgba(247,201,72,.12);" data-idx="2">
      <div class="check-tag">✓</div>
      <div class="prog-icon">🗳️</div>
      <div class="prog-name">Voter Eligibility</div>
      <div class="prog-desc">Checks if a person meets the minimum age requirement to vote.</div>
      <div class="code-snippet">
<span class="kw">def</span> <span class="fn">can_vote</span>(age):<br>
&nbsp;&nbsp;<span class="kw">if</span> age <span class="op">>=</span> <span class="num">18</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Eligible ✅"</span>)<br>
&nbsp;&nbsp;<span class="kw">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Not eligible ❌"</span>)
      </div>
    </div>

    <div class="prog-card" style="--clr:#f76c8a;--glow:rgba(247,108,138,.12);" data-idx="3">
      <div class="check-tag">✓</div>
      <div class="prog-icon">🌡️</div>
      <div class="prog-name">Temperature Checker</div>
      <div class="prog-desc">Classifies temperature as hot, warm, cool, or cold based on input.</div>
      <div class="code-snippet">
<span class="kw">def</span> <span class="fn">temp_check</span>(t):<br>
&nbsp;&nbsp;<span class="kw">if</span> t <span class="op">></span> <span class="num">35</span>: <span class="fn">print</span>(<span class="str">"Hot 🔥"</span>)<br>
&nbsp;&nbsp;<span class="kw">elif</span> t <span class="op">></span> <span class="num">20</span>: <span class="fn">print</span>(<span class="str">"Warm ☀️"</span>)<br>
&nbsp;&nbsp;<span class="kw">elif</span> t <span class="op">></span> <span class="num">10</span>: <span class="fn">print</span>(<span class="str">"Cool 🌤️"</span>)<br>
&nbsp;&nbsp;<span class="kw">else</span>: <span class="fn">print</span>(<span class="str">"Cold ❄️"</span>)
      </div>
    </div>

    <div class="prog-card" style="--clr:#b57cf7;--glow:rgba(181,124,247,.12);" data-idx="4">
      <div class="check-tag">✓</div>
      <div class="prog-icon">🔢</div>
      <div class="prog-name">Even or Odd Checker</div>
      <div class="prog-desc">Determines whether a given integer is even or odd using modulus.</div>
      <div class="code-snippet">
<span class="kw">def</span> <span class="fn">even_odd</span>(n):<br>
&nbsp;&nbsp;<span class="kw">if</span> n <span class="op">%</span> <span class="num">2</span> <span class="op">==</span> <span class="num">0</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Even 🟢"</span>)<br>
&nbsp;&nbsp;<span class="kw">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">print</span>(<span class="str">"Odd 🔵"</span>)
      </div>
    </div>

  </div>

  <!-- Technologies -->
  <div class="section-label">// technologies used</div>
  <div class="tech-row">
    <div class="tech-chip"><span class="pip"></span>Python 3</div>
    <div class="tech-chip" style="color:var(--accent5)"><span class="pip" style="background:var(--accent5);box-shadow:0 0 8px var(--accent5)"></span>if-else logic</div>
    <div class="tech-chip" style="color:var(--accent)"><span class="pip" style="background:var(--accent);box-shadow:0 0 8px var(--accent)"></span>Standard I/O</div>
  </div>

  <!-- How to run -->
  <div class="section-label">// how to run</div>

  <div class="terminal-bar">
    <div class="dot dot-r"></div>
    <div class="dot dot-y"></div>
    <div class="dot dot-g"></div>
    <span class="terminal-title">terminal</span>
  </div>

  <div class="steps" style="margin-top:0; border-top:1px solid var(--border); background:var(--card); border-radius:0 0 12px 12px; padding:16px; gap:10px;">
    <div class="step" style="background:#090d16;">
      <div class="step-num">1</div>
      <div class="step-text">Install Python 3 from <code>python.org</code></div>
    </div>
    <div class="step" style="background:#090d16;">
      <div class="step-num">2</div>
      <div class="step-text">Download the file <code>python_programs.py</code></div>
    </div>
    <div class="step" style="background:#090d16;">
      <div class="step-num">3</div>
      <div class="step-text">Run the script: <code>python python_programs.py</code></div>
    </div>
  </div>

  <!-- Author -->
  <div class="section-label" style="margin-top:48px;">// author</div>
  <div class="author-card">
    <div class="avatar">👨‍💻</div>
    <div class="author-info">
      <div class="author-name">Bhushan Fulari</div>
      <div class="author-role">Python Developer · Ope