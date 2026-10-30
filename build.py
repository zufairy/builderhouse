from pathlib import Path
import shutil
root = Path(__file__).parent
site = root / 'site'
(site / 'assets').mkdir(parents=True, exist_ok=True)

def pic(name, alt, cls=''):
    shutil.copyfile(root / 'assets' / name, site / 'assets' / name)
    return f'<img class="{cls}" src="assets/{name}" alt="{alt}" loading="lazy">'

hero = pic('haven.jpg', 'Concept illustration of the proposed Kajang builder haven: shared desks, a workshop corner, lounge and rest pods', 'heroimg')
news = pic('softbank-news.jpg', 'Screenshot of The Star Malaysia, 26 Oct 2026: "SoftBank\'s Son plans US$50bil Malaysia tech outlay, PM says"', 'newsimg')

perks = [
    ('people-0.jpg', '01', 'A desk that is actually yours', 'Workspace access',
     'Lot 90, Kajang. A seat, fast wifi, and a room full of people mid-build instead of mid-scroll. Come in whenever you need to focus — this is the base, not a vibe.'),
    ('people-1.jpg', '02', 'A reason to ship something every week', 'Weekly hands-on workshops',
     'No slide decks. Bring your laptop and leave with something running — an AI agent, an automation, a faceless content pipeline, a landing page. See a sample week below.'),
    ('people-3.jpg', '03', 'People who will actually check on your idea', 'A circle of 30, not 300',
     'Capped on purpose. Small enough that people remember what you are building and ask how it is going. You will know everyone’s name by week two.'),
    ('people-2.jpg', '04', 'A clearer shot at being fundable', 'VC network & fundraising guidance',
     'Intros to relevant investors when there is real fit, plus hands-on help tightening your pitch, your numbers and your story. Introductions depend on stage and fit — not a guarantee of funding.'),
]
perk_cards = ''.join(
    f'<article class="feature"><div class="fnum">{n}</div>{pic(img, title)}<div><small>{n} / {sub.upper()}</small><h3>{title}</h3><p>{body}</p></div></article>'
    for img, n, title, sub, body in perks
)

schedule = [
    ('MON', 'Build Night', 'Open floor. Bring whatever you’re stuck on — code, ads, pitch deck. Peer help + quiet focus blocks.'),
    ('WED', 'Workshop', 'Hands-on session: AI agents one week, content automation the next, fundraising prep after that. Rotating, announced 2 weeks ahead.'),
    ('FRI', 'Demo & Kopi', 'Show what you shipped this week, even if it’s small. Feedback from the room. Then everyone just hangs out.'),
    ('SAT', 'Open House', 'Weekend access for deep work. No programming — just the room, the wifi, and the pods if you need a reset.'),
]
schedule_cards = ''.join(
    f'<article class="day"><small>{d}</small><h3>{t}</h3><p>{desc}</p></article>' for d, t, desc in schedule
)

expectations = [
    ('Come with something to build', 'An idea, a side project, a business you’re trying to grow — not just curiosity. This keeps the room productive for everyone.'),
    ('Show up at least weekly', 'The value compounds with consistency. Ghosts don’t get the benefit of the circle — or the network.'),
    ('Respect the quiet hours', 'Calls in the call corner, headphones during focus blocks. It’s a workspace first.'),
    ('No cold-pitching other members', 'Build relationships like a normal human. Selling to the room without consent gets you a warning, then a refund of your remaining month.'),
]
expect_cards = ''.join(
    f'<article class="exp"><h3>{t}</h3><p>{d}</p></article>' for t, d in expectations
)

html = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Builder House Kajang — Malaysia’s first AI builder house</title><style>
:root{--cream:#f6f1e7;--green:#173e30;--muted:#5e6b60;--lime:#d6f282;--line:#ccd4c5;--ember:#bd5c39;--ember2:#e8795a}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--cream);color:var(--green);font:16px/1.65 Arial,sans-serif;overflow-x:hidden}
button,a{font:inherit;color:inherit}a{text-decoration:none}button{cursor:pointer;font-family:inherit}
button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--ember);outline-offset:5px}
.wrap{max-width:1240px;padding:0 34px;margin:auto}
.marquee{background:var(--green);color:var(--lime);overflow:hidden;white-space:nowrap;padding:10px 0;position:relative}
.marquee div{display:inline-block;padding-left:100%;animation:scroll 26s linear infinite;font:11px/1.6 monospace;letter-spacing:1.5px}
.marquee div:hover{animation-play-state:paused}
@keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-100%)}}
nav{display:flex;justify-content:space-between;align-items:center;padding:25px 0;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:17px;line-height:1.1;letter-spacing:-.6px}
.mark{width:43px;height:43px}
.navlinks{display:flex;gap:25px;align-items:center;font-size:13px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:15px 23px;background:var(--green);color:#fff;border:0;border-radius:6px;font-weight:700;transition:transform .15s cubic-bezier(0,0,.2,1),box-shadow .15s cubic-bezier(0,0,.2,1)}
.btn:hover{transform:translateY(-3px);box-shadow:0 10px 24px -8px rgba(23,62,48,.5)}
.btn:active{transform:translateY(-1px) scale(.98);transition-duration:.05s}
.btn.lime{background:var(--lime);color:var(--green)}
.btn.ember{background:var(--ember);color:#fff}
small,.eyebrow{font:11px/1.6 monospace;letter-spacing:1.2px;text-transform:uppercase}
.badge{display:inline-flex;align-items:center;gap:7px;background:#fde7de;color:var(--ember);padding:7px 13px;border-radius:999px;font:11px/1 monospace;letter-spacing:1px;text-transform:uppercase;animation:pulse 2.4s ease-in-out infinite}
.badge i{width:7px;height:7px;border-radius:50%;background:var(--ember);display:inline-block;animation:dot 1.2s ease-in-out infinite}
@keyframes dot{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(189,92,57,.25)}50%{box-shadow:0 0 0 7px rgba(189,92,57,0)}}
.hero{padding:55px 0 0;text-align:center}
.hero h1{font-size:clamp(42px,6vw,78px);line-height:1.03;letter-spacing:-4px;max-width:1020px;margin:22px auto}
.hero h1 em{font-family:Georgia,serif;font-weight:400;color:#6b8141;font-style:normal}
.intro{max-width:660px;margin:22px auto;color:var(--muted);font-size:18px}
.actions{display:flex;justify-content:center;gap:16px;align-items:center;flex-wrap:wrap}
.fine{font-size:12px;color:var(--muted)}
.art{position:relative;margin-top:35px}
.heroimg{display:block;width:100%;max-height:640px;object-fit:cover;border-radius:12px}
.caption{font:11px/1.6 monospace;color:var(--muted);margin:12px 0}
.stamp{position:absolute;right:20px;top:25px;background:var(--lime);border-radius:50%;width:116px;height:116px;display:grid;place-content:center;text-align:center;transform:rotate(8deg);font:12px monospace;transition:transform .25s cubic-bezier(.4,0,.2,1)}
.art:hover .stamp{transform:rotate(0) scale(1.05)}
.stamp b{font-size:38px;display:block}
.promise{display:grid;grid-template-columns:repeat(4,1fr);gap:25px;padding:28px 0;border-block:1px solid var(--line);margin-top:25px}
.promise b{display:block}.promise span{font-size:13px;color:var(--muted)}
section{padding:78px 0}
h2{font-size:clamp(32px,4.2vw,52px);letter-spacing:-2.1px;line-height:1.08;margin:16px 0 25px;font-weight:600}
h3{font-size:25px;line-height:1.15;letter-spacing:-.8px;margin:13px 0 16px}
p{margin:0 0 20px}
.heading{display:flex;justify-content:space-between;gap:40px;align-items:end;margin-bottom:28px}
.heading p{max-width:380px;color:var(--muted)}
/* why now */
.whynow{background:var(--green);border-radius:16px;padding:46px;display:grid;grid-template-columns:1fr 1fr;gap:46px;align-items:center;color:var(--cream)}
.whynow .copy small{color:var(--lime)}
.whynow p{color:#c4d2c3}
.newsimg{width:100%;border-radius:10px;box-shadow:0 20px 50px -20px rgba(0,0,0,.6)}
.srcline{font:11px/1.5 monospace;color:#9fb49b;margin-top:10px}
.srcline a{color:var(--lime);text-decoration:underline}
/* features */
.features{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.feature{position:relative;background:#fffcf5;border:1px solid var(--line);border-radius:10px;overflow:hidden;transition:transform .2s cubic-bezier(0,0,.2,1)}
.feature:hover{transform:translateY(-5px)}
.feature img{display:block;width:100%;aspect-ratio:1.8;object-fit:cover}
.feature>div{padding:27px}
.feature p{color:var(--muted);font-size:15px;margin:0}
.fnum{position:absolute;top:14px;left:14px;background:rgba(23,62,48,.85);color:var(--lime);font:11px monospace;padding:5px 10px;border-radius:6px;z-index:2}
/* schedule */
.schedule{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.day{background:#fffcf5;border:1px solid var(--line);border-left:3px solid var(--ember2);border-radius:8px;padding:22px}
.day small{color:var(--ember)}
.day h3{font-size:19px;margin:8px 0 10px}
.day p{color:var(--muted);font-size:14px;margin:0}
/* expectations */
.expect{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
.exp{border-top:2px solid #789354;padding-top:16px}
.exp h3{font-size:18px}
.exp p{color:var(--muted);font-size:14px;margin:0}
/* pods */
.reset{background:var(--green);color:var(--cream);border-radius:12px;padding:32px;display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}
.reset img{width:100%;border-radius:8px}
.reset p{color:#c4d2c3}
.tag{display:inline-block;background:var(--lime);color:var(--green);padding:7px 12px;border-radius:4px;font:10px monospace;letter-spacing:1px}
/* pricing */
.pricing{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}
.pricecard{background:var(--green);padding:38px;border-radius:12px;color:var(--cream)}
.price{font-size:72px;line-height:1.3;letter-spacing:-4px}
.price span{font-size:15px;letter-spacing:0}
ul{list-style:none;padding:0;margin:20px 0}
li{padding:12px 0;border-bottom:1px solid #587360}
li:before{content:'↗';color:var(--lime);margin-right:12px}
.pricecard .btn{width:100%}
.pricecard .fine{color:#cad6c4;margin-top:18px}
.seats{display:grid;grid-template-columns:repeat(10,1fr);gap:7px;margin:20px 0}
.seats i{aspect-ratio:1;border-radius:4px;border:1px solid #849c75;background:#e1eacb;transition:background .3s cubic-bezier(0,0,.2,1),transform .3s cubic-bezier(0,0,.2,1)}
.seats i.taken{background:var(--ember);border-color:var(--ember);transform:scale(.9)}
.status{font-size:13px;color:var(--muted);display:flex;align-items:center;gap:8px}
.status b{color:var(--ember)}
/* apply form */
.applyform{background:#fffcf5;border:1px solid var(--line);border-radius:12px;padding:30px}
.applyform label{display:block;font:11px monospace;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin:16px 0 6px}
.applyform input,.applyform textarea{width:100%;padding:13px 14px;border:1px solid var(--line);border-radius:7px;font:15px/1.4 Arial,sans-serif;background:#fff;color:var(--green)}
.applyform textarea{resize:vertical;min-height:70px}
.applyform .btn{margin-top:20px;width:100%}
details{padding:20px 0;border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:700}
details p{margin:15px 0 0;color:var(--muted);max-width:800px}
.final{text-align:center;padding:65px 25px;background:#e1e9ce;border-radius:12px;margin-bottom:30px}
.final p{color:var(--muted)}
footer{padding:25px 0 40px;display:flex;justify-content:space-between;font-size:12px;color:var(--muted)}
.success{border-top:2px solid var(--lime);padding-top:18px;margin-top:20px}
.success b{display:block;margin-bottom:4px}
.fade{animation:rise .45s cubic-bezier(0,0,.2,1) both}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
[data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .45s cubic-bezier(0,0,.2,1),transform .45s cubic-bezier(0,0,.2,1)}
[data-reveal].in{opacity:1;transform:none}
@media(max-width:860px){.whynow,.schedule,.expect{grid-template-columns:1fr 1fr}.pricing{grid-template-columns:1fr}}
@media(max-width:720px){.wrap{padding:0 20px}.navlinks>a:not(.btn){display:none}.brand{font-size:14px}.hero{padding-top:40px}.hero h1{letter-spacing:-2.2px}.intro{font-size:16px}.heroimg{min-height:280px}.stamp{width:78px;height:78px;right:10px;top:12px;font-size:9px}.stamp b{font-size:24px}.promise,.schedule,.expect,.whynow{grid-template-columns:1fr 1fr}.features,.reset,.pricing{grid-template-columns:1fr;gap:25px}.heading{display:block}section{padding:48px 0}.pricecard{padding:26px}.reset,.whynow{padding:22px}.feature>div{padding:22px}footer{display:block}.navlinks .btn{font-size:12px;padding:12px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}.marquee div{animation:none}}
</style>
<div class="marquee"><div>● MALAYSIA’S FIRST AI BUILDER HOUSE ● ONLY 30 FOUNDING SPOTS ● LOT 90, KAJANG ● WEEKLY WORKSHOPS ● TARGET OPENING DECEMBER 2026 ● APPLICATIONS OPEN NOW ● MALAYSIA’S FIRST AI BUILDER HOUSE ● ONLY 30 FOUNDING SPOTS ● LOT 90, KAJANG ● WEEKLY WORKSHOPS ● TARGET OPENING DECEMBER 2026 ● APPLICATIONS OPEN NOW ●</div></div>
<div class="wrap"><nav><a class="brand" href="#"><svg class="mark" viewBox="0 0 48 48" fill="none" aria-hidden="true"><path d="M5 22 24 6l19 16v20H5Z" stroke="currentColor" stroke-width="3"/><path d="m19 24-6 6 6 6m10-12 6 6-6 6" stroke="currentColor" stroke-width="3"/><path d="m26 21-4 18" stroke="currentColor" stroke-width="2"/></svg>builder house<br>/ kajang</a><div class="navlinks"><a href="#why">Why now</a><a href="#perks">What you get</a><a href="#week">Workshops</a><a class="btn ember" href="#join">Claim a spot ↗</a></div></nav>
<main>
<header class="hero fade">
<div class="badge"><i aria-hidden="true"></i>ONLY 30 FOUNDING SPOTS · FIRST BATCH</div>
<h1>Malaysia’s first<br><em>AI builder house.</em></h1>
<p class="intro">Everyone’s talking about Malaysia’s AI moment. We built the room where you actually do something about it — a desk, a weekly workshop, and 29 other people who are building, not just watching.</p>
<div class="actions"><a class="btn ember" href="#join">Claim your founding spot ↗</a><a class="btn lime" href="#why">See why now ↓</a></div>
<p class="fine" style="margin-top:14px">RM500/month · Lot 90, Kajang · Target opening December 2026</p>
<div class="art" data-reveal>HEROVISUAL<div class="stamp"><b id="seatsLeft">30</b>SPOTS LEFT</div></div>
<p class="caption">THE VISION / Generated concept of the proposed space — shared desks, workshop corner, lounge and rest pods. Not a photo of the current office.</p>
</header>
<div class="promise"><div><b>A place to build</b><span>Lot 90, Kajang</span></div><div><b>A weekly push forward</b><span>Hands-on AI workshops</span></div><div><b>A circle of 30</b><span>Not 300. Curated on purpose</span></div><div><b>A way into the room</b><span>VC network & fundraising guidance</span></div></div>

<section id="why" data-reveal>
<div class="heading"><div><small>Why this, why now</small><h2>Malaysia just became<br>an AI headline. Be inside it.</h2></div><p>SoftBank’s Masayoshi Son has reportedly picked Malaysia — Sarawak and the peninsula — for close to US$50 billion in AI and data-centre investment. That’s a proposal, not a signed cheque. But the direction is clear: the jobs, the tools and the attention are landing here.</p></div>
<div class="whynow"><div>NEWSIMG<p class="srcline">Source: <a href="https://www.thestar.com.my/business/business-news/2026/10/26/softbanks-son-plans-us50bil-malaysia-tech-outlay-pm-says" target="_blank" rel="noopener">The Star Malaysia, 26 Oct 2026</a>. Figure attributed to PM Anwar Ibrahim; SoftBank has not confirmed the amount.</p></div><div class="copy"><small>The honest version</small><h3>A proposal isn’t a job. Your skills are.</h3><p>Big capital announcements don’t teach you to build an AI agent, ship a faceless channel, or close your first client. That part is still on you — we just make sure you’re not doing it alone, in your bedroom, with no deadline forcing you to finish.</p><p class="fine">We are not affiliated with SoftBank, the Malaysian government, or this investment in any way. It’s context for why the timing matters — not a claim of funding or endorsement.</p></div></div>
</section>

<section id="perks" data-reveal>
<div class="heading"><div><small>Your membership, made tangible</small><h2>Here’s exactly<br>what RM500 buys you.</h2></div><p>No vague “community vibes.” Four concrete things, explained plainly, with the honest limits included.</p></div>
<div class="features">FEATURES</div>
<p class="caption">Images above are generated concepts of the community and space. Guest sessions, specific workshop topics and individual investor introductions depend on availability and fit.</p>
</section>

<section id="week" data-reveal>
<div class="heading"><div><small>A sample week in the house</small><h2>What showing up<br>actually looks like.</h2></div><p>An illustrative week, not a fixed roster — topics rotate and will be confirmed before opening.</p></div>
<div class="schedule">SCHEDULE</div>
</section>

<section data-reveal style="padding-top:0">
<div class="heading"><div><small>What we expect from you</small><h2>This is selective<br>on both sides.</h2></div><p>RM500 doesn’t buy a passive seat. It buys entry into a room that stays useful because everyone pulls their weight.</p></div>
<div class="expect">EXPECT</div>
</section>

<section id="pods" data-reveal style="padding-top:0"><div class="reset">PODVISUAL<div><span class="tag">THE HAVEN / PROPOSED REST AREA</span><h2>Build mode.<br>Chill mode.<br>Reset mode.</h2><p>Deep-work pods for when you need to disappear into a problem, a lounge for when you need to talk it out with someone, and a room worth coming back to on a Tuesday night for no reason at all.</p><p class="fine">Sleeping pods are part of the vision for the space. Installation, hours and use terms will be confirmed before they’re offered. This is an office community, not residential accommodation.</p><a class="btn lime" href="#join">Find your people ↗</a></div></div></section>

<section id="join" data-reveal>
<div class="pricing">
<div><small>Small by choice. Ambitious by nature.</small><h2>30 people.<br>First batch.<br>No second chances<br>on founding pricing.</h2><p>Lock this rate as one of the first 30. After the founding cohort fills, pricing and terms for later batches may change.</p><div class="seats" id="seatsGrid" aria-hidden="true"></div><p class="status" role="status"><span id="statusText">30 of 30 spots open.</span> <b id="statusUrgent"></b></p><p class="fine">Demo counter for this preview — it resets on reload and does not reflect real applications yet. Live availability needs shared registration data before launch.</p></div>
<div class="pricecard"><small>Your monthly commitment</small><div class="price">RM500<span> / month</span></div><p>Locked for as long as you stay, as one of the founding 30.</p><ul><li>Workspace access in Lot 90, Kajang</li><li>Weekly hands-on AI workshops</li><li>A curated circle of 30 builders</li><li>Demo nights + peer feedback</li><li>VC network access, subject to fit</li><li>Fundraising prep & pitch guidance</li></ul><a class="btn lime" href="#applyform">I’m ready to build my next chapter ↗</a><p class="fine">Target opening December 2026. Hours, programme and membership terms shared before any payment. VC introductions depend on fit and availability — no funding guarantee. Pods are proposed, not yet confirmed.</p></div>
</div>
<div id="applyform" class="applyform" style="margin-top:40px"><small>Reserve your spot</small><h3>Tell us what you’re building.</h3><form id="appForm" onsubmit="submitApp(event)"><label for="nm">Name</label><input id="nm" name="name" autocomplete="name" required placeholder="Your name"><label for="ph">Phone / WhatsApp</label><input id="ph" name="tel" type="tel" autocomplete="tel" required placeholder="01X-XXX XXXX"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email" required placeholder="you@email.com"><label for="pj">What are you building, or trying to build?</label><textarea id="pj" name="project" required placeholder="A product, a business, a skill — be specific"></textarea><button class="btn ember" type="submit">Submit my application ↗</button><p class="fine" style="margin-top:14px">This sends your interest to Along directly. No payment is collected here — approved applicants get payment details once the gateway is confirmed and opening terms are final.</p></form><div id="appSuccess" class="success" role="status" hidden><b id="appSuccessTitle">Got it.</b><span id="appSuccessBody">We'll follow up on your application soon.</span></div></div>
</section>

<section data-reveal style="padding-top:0"><small>A few honest answers</small><h2>Before your first day.</h2>
<details><summary>Do I need a startup or coding experience?</summary><p>No. Bring curiosity and a project or problem you want to work on. Each workshop will state its prerequisites ahead of time.</p></details>
<details><summary>How do the VC connections actually work?</summary><p>We offer access to our VC network through relevant introductions, based on your stage, fit and mutual interest, plus guidance on your pitch, numbers and fundraising narrative. Membership does not guarantee an introduction to a specific investor, or any investment.</p></details>
<details><summary>How will I pay, and when?</summary><p>No payment is collected on this page. Once your application is reviewed and the payment gateway is live, you’ll get a secure link to pay your first month and lock your founding spot.</p></details>
<details><summary>Are these pictures of the actual office?</summary><p>These are generated concept images that show the vision, plus one real news screenshot (credited above) for context on timing. The address is Lot 90, Kajang. Final layout, pods, access hours and workshop calendar will be confirmed before opening.</p></details>
<details><summary>Can I visit before committing?</summary><p>Yes — mention it in your application and we’ll arrange a time. No payment is required to visit.</p></details>
</section>

<div class="final" data-reveal><small>Your future needs more than a saved tutorial.</small><h2>Put yourself in the room.</h2><p>Your people. Your next idea. Your commitment to begin.<br>RM500 / month · 30 founding spots · Kajang</p><a class="btn ember" href="#applyform">Count me in for the founding circle ↗</a></div>
</main>
<footer><span>builder house / kajang · Build in good company.</span><span>Concept preview · December 2026 target opening</span></footer>
</div>
<script>
(function(){
var grid=document.getElementById('seatsGrid');
for(var i=0;i<30;i++){var s=document.createElement('i');grid.appendChild(s)}
var taken=0,max=11; // demo only: simulate early interest, capped well under 30
function tick(){
 if(taken>=max)return;
 taken++;
 var cells=grid.querySelectorAll('i');
 cells[taken-1].classList.add('taken');
 document.getElementById('seatsLeft').textContent=30-taken;
 document.getElementById('statusText').textContent=(30-taken)+' of 30 spots open.';
 document.getElementById('statusUrgent').textContent= (30-taken)<=15 ? '— moving fast.' : '';
 setTimeout(tick, 1400+Math.random()*2600);
}
setTimeout(tick, 1200);
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('in')})},{threshold:.12});
document.querySelectorAll('[data-reveal]').forEach(function(el){io.observe(el)});
})();
function submitApp(e){
 e.preventDefault();
 var nm=document.getElementById('nm').value,ph=document.getElementById('ph').value,em=document.getElementById('em').value,pj=document.getElementById('pj').value;
 var msg='Builder House Kajang application — Name: '+nm+' | Phone: '+ph+' | Email: '+em+' | Building: '+pj;
 var live=window.mausbot&&typeof window.mausbot.send==='function';
 if(live){window.mausbot.send(msg)}
 document.getElementById('appForm').hidden=true;
 document.getElementById('appSuccessTitle').textContent=live?'Application sent.':'Preview only.';
 document.getElementById('appSuccessBody').textContent=live?'Thanks, '+nm+' — we review applications and follow up by phone or email within a few days.':'This would send your application to Along. Open this page inside the chat app to actually submit it.';
 document.getElementById('appSuccess').hidden=false;
}
</script>
</html>'''

html = (html.replace('HEROVISUAL', hero)
            .replace('NEWSIMG', news)
            .replace('FEATURES', perk_cards)
            .replace('SCHEDULE', schedule_cards)
            .replace('EXPECT', expect_cards)
            .replace('PODVISUAL', pic('space-2.jpg', 'Generated concept of rest pods with pillows, mattresses and soft lighting')))

(site / 'index.html').write_text(html)
print('Built:', len(html.encode()), 'bytes; <img> tags:', html.count('<img'))
