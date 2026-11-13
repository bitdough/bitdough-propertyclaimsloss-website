#!/usr/bin/env python3
"""Builds every page in public/ from the content below.

Edit the BUSINESS block or a page's content, then run:  python3 tools/build.py
The script rewrites the HTML pages, sitemap.xml and llms.txt so the business
name, phone and email always match everywhere (important for SEO/GEO).
"""
import json
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- business
BUSINESS = {
    "name": "Property Claims Loss",
    "legal_name": "Property Claims Loss Inc.",
    "url": "https://propertyclaimsloss.com",
    "phone_display": "(773) 497-2856",
    "phone_e164": "+1-773-497-2856",
    "email": "info@propertyclaimsloss.com",
    "city": "Chicago",
    "region": "IL",
    "country": "US",
    "tagline": "Insurance Appraisal & Umpire Services",
    "summary": (
        "Property Claims Loss provides insurance appraisal services for property "
        "insurance claims: independent appraiser services and impartial umpire "
        "services under the appraisal clause, a form of insurance alternative "
        "dispute resolution (ADR) used when the policyholder and insurer agree a "
        "loss is covered but disagree on the amount of loss."
    ),
}
B = BUSINESS

CERTS = [
    "AUA Certified Appraiser",
    "AUA Certified Umpire",
    "Attended PLAN training",
    "IAAI member",
    "IICRC Certified",
    "C.F.E.",
    "Xactimate Certified",
    "Xactimate Pricing Specialist / Consultant",
    "Executive General Adjuster",
    "Florida Mold Assessor",
    "Florida Roofing License",
]
LICENSES = [
    ("State of Iowa", "Licensed Appraiser"),
    ("State of Iowa", "Licensed Umpire"),
    ("Louisiana", "Independent Adjuster / Appraiser, LA-853057"),
    ("Florida", "Independent Adjuster / Appraiser, FL-W665562"),
    ("Alabama", "Independent Adjuster / Appraiser, AL-3001617185"),
    ("Mississippi", "Independent Adjuster / Appraiser, MS-10959135"),
    ("Nevada", "Independent Adjuster / Appraiser, NV-3814650"),
    ("Texas", "Independent Adjuster / Appraiser, TX-2558510"),
    ("Florida", "Public Adjuster, G191934"),
    ("Florida", "Independent Adjuster, Lic. # G046520"),
]
LICENSED_STATES = "Iowa, Louisiana, Florida, Alabama, Mississippi, Nevada and Texas"

def creds_html():
    c = "".join(f"<li>{escape(x)}</li>" for x in CERTS)
    l = "".join(f"<li><strong>{escape(a)}:</strong> {escape(b)}</li>" for a, b in LICENSES)
    return f"""<div class="grid-2">
<div class="card"><div class="icon">{ICON['shield']}</div><h3>Certifications &amp; training</h3><ul class="checks">{c}</ul></div>
<div class="card"><div class="icon">{ICON['clip']}</div><h3>State licenses</h3><ul class="checks">{l}</ul></div>
</div>"""
U = B["url"]

# ---------------------------------------------------------------- icons
ICON = {
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M5 21h14M6 7h12M6 7l-3 7a3.5 3.5 0 0 0 6 0L6 7zm12 0l-3 7a3.5 3.5 0 0 0 6 0l-3-7z"/></svg>',
    "clip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/></svg>',
    "hammer": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4l6 6-3 3-6-6zM11 7L3 15l3 3 8-8"/></svg>',
    "brief": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6"/></svg>',
    "calc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M14 12h2M8 16h2M14 16h2"/></svg>',
}

MARK = ('<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#1d4a3c"/>'
        '<path d="M20 8v24M12 32h16M11 13h18" stroke="#b5862f" stroke-width="2.2" stroke-linecap="round"/>'
        '<path d="M11 13l-4 9a4 4 0 0 0 8 0zM29 13l-4 9a4 4 0 0 0 8 0z" fill="none" stroke="#f3e7cc" stroke-width="1.8" stroke-linejoin="round"/></svg>')

NAV = [
    ("/appraiser-services/", "Appraiser Services"),
    ("/umpire-services/", "Umpire Services"),
    ("/insurance-appraisal-process/", "How Appraisal Works"),
    ("/faq/", "FAQ"),
    ("/about/", "About"),
]

# ---------------------------------------------------------------- schema
def org_node():
    return {
        "@type": "ProfessionalService",
        "@id": f"{U}/#business",
        "name": B["name"],
        "legalName": B["legal_name"],
        "url": f"{U}/",
        "telephone": B["phone_e164"],
        "email": B["email"],
        "logo": f"{U}/icon-512.png",
        "image": f"{U}/og-image.jpg",
        "description": B["summary"],
        "slogan": B["tagline"],
        "address": {"@type": "PostalAddress", "addressLocality": B["city"],
                    "addressRegion": B["region"], "addressCountry": B["country"]},
        "areaServed": {"@type": "Country", "name": "United States"},
        "knowsAbout": [
            "Insurance appraisal", "Appraisal clause", "Insurance umpire",
            "Alternative dispute resolution", "Property insurance claims",
            "Amount of loss disputes", "Actual cash value", "Replacement cost value",
            "Xactimate estimating", "Hail and wind damage", "Water damage", "Fire damage",
        ],
        "contactPoint": {"@type": "ContactPoint", "telephone": B["phone_e164"],
                         "email": B["email"], "contactType": "customer service",
                         "areaServed": "US", "availableLanguage": "English"},
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": x} for x in CERTS]
            + [{"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                "name": f"{a} {b}", "recognizedBy": {"@type": "Organization", "name": a}} for a, b in LICENSES],
        "memberOf": {"@type": "Organization", "name": "International Association of Arson Investigators (IAAI)"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Insurance appraisal services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@id": f"{U}/appraiser-services/#service"}},
                {"@type": "Offer", "itemOffered": {"@id": f"{U}/umpire-services/#service"}},
            ],
        },
    }

def website_node():
    return {"@type": "WebSite", "@id": f"{U}/#website", "url": f"{U}/", "name": B["name"],
            "publisher": {"@id": f"{U}/#business"}, "inLanguage": "en-US"}

def webpage_node(path, title, desc, kind="WebPage"):
    return {"@type": kind, "@id": f"{U}{path}#webpage", "url": f"{U}{path}", "name": title,
            "description": desc, "isPartOf": {"@id": f"{U}/#website"},
            "about": {"@id": f"{U}/#business"}, "inLanguage": "en-US", "dateModified": TODAY}

def crumbs_node(path, label):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{U}/"}]
    if path != "/":
        items.append({"@type": "ListItem", "position": 2, "name": label, "item": f"{U}{path}"})
    return {"@type": "BreadcrumbList", "@id": f"{U}{path}#breadcrumb", "itemListElement": items}

def faq_node(path, qa):
    return {"@type": "FAQPage", "@id": f"{U}{path}#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qa]}

def service_node(path, name, stype, desc, audience):
    return {"@type": "Service", "@id": f"{U}{path}#service", "name": name, "serviceType": stype,
            "description": desc, "provider": {"@id": f"{U}/#business"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "audience": [{"@type": "Audience", "audienceType": a} for a in audience],
            "url": f"{U}{path}"}

def strip(html):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()

# ---------------------------------------------------------------- layout
def head(path, title, desc, graph):
    t, d = escape(title), escape(desc)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{U}{path}">
<meta name="theme-color" content="#1d4a3c">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/styles.css">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{escape(B['name'])}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{U}{path}">
<meta property="og:image" content="{U}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(B['name'])}: insurance appraisal and umpire services">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{U}/og-image.jpg">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(path):
    cur = ' aria-current="page"'
    links = "".join(
        f'<li><a href="{h}"{cur if h == path else ""}>{escape(l)}</a></li>' for h, l in NAV)
    mlinks = "".join(f'<li><a href="{h}">{escape(l)}</a></li>' for h, l in NAV + [("/contact/", "Contact")])
    return f"""<div class="topbar"><div class="wrap">
<span class="hide-sm">Insurance alternative dispute resolution for property claims</span>
<span>Call <a href="tel:{B['phone_e164']}">{B['phone_display']}</a> &nbsp;·&nbsp; <a href="mailto:{B['email']}">{B['email']}</a></span>
</div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="/" aria-label="{escape(B['name'])} home">{MARK}<span class="brand-name">{escape(B['name'])}<small>{escape(B['tagline'])}</small></span></a>
<nav class="nav" aria-label="Main"><ul>{links}<li><a class="btn" href="/contact/">Request Appraisal</a></li></ul></nav>
<details class="menu"><summary aria-label="Open menu">Menu</summary><ul>{mlinks}</ul></details>
</div></header>
<main id="main">
"""

def footer():
    nav = "".join(f'<li><a href="{h}">{escape(l)}</a></li>' for h, l in NAV)
    return f"""</main>
<section class="cta-band" aria-label="Contact"><div class="wrap">
<div><h2>Disagree with the amount of your claim?</h2>
<p>Talk with us about whether appraisal fits your dispute, or retain an appraiser or umpire today.</p></div>
<div class="hero-actions" style="margin:0"><a class="btn btn-primary" href="tel:{B['phone_e164']}">Call {B['phone_display']}</a><a class="btn btn-ghost" href="/contact/">Request an Appraisal</a></div>
</div></section>
<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><a class="brand" href="/">{MARK}<span class="brand-name">{escape(B['name'])}<small>{escape(B['tagline'])}</small></span></a>
<p>Independent appraisers and impartial umpires for property insurance claims, resolving amount-of-loss disputes outside of court.</p></div>
<div><h2>Services</h2><ul>
<li><a href="/appraiser-services/">Appraiser Services</a></li>
<li><a href="/umpire-services/">Umpire Services</a></li>
<li><a href="/insurance-appraisal-process/">The Appraisal Process</a></li></ul></div>
<div><h2>Company</h2><ul>
<li><a href="/about/">About</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact</a></li></ul></div>
<div><h2>Contact</h2><ul>
<li><a href="tel:{B['phone_e164']}">{B['phone_display']}</a></li>
<li><a href="mailto:{B['email']}">{B['email']}</a></li>
<li>{B['city']}, Illinois</li></ul></div>
</div>
<div class="legal">
<p>{escape(B['legal_name'])} provides insurance appraisal and umpire services. We are not a law firm and do not give legal advice. Appraisal determines the amount of loss; it does not decide coverage. When serving as umpire, we act impartially and do not advocate for either party.</p>
<p>© {date.today().year} {escape(B['legal_name'])} · <a href="/llms.txt">llms.txt</a> · <a href="/sitemap.xml">Sitemap</a></p>
</div>
</div></footer>
</body>
</html>
"""

def page_hero(path, label, h1, lead):
    crumb = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {escape(label)}</nav>'
    return f"""<div class="page-hero"><div class="wrap">{crumb}
<h1>{h1}</h1><p class="lead">{lead}</p></div></div>
"""

def faq_html(qa, open_first=False):
    out = []
    for i, (q, a) in enumerate(qa):
        o = " open" if (open_first and i == 0) else ""
        out.append(f'<details{o}><summary>{escape(q)}</summary><div class="a">{a}</div></details>')
    return "\n".join(out)

def aside_contact():
    return f"""<aside class="aside">
<div class="card"><h2>Talk to an appraiser</h2>
<p>Tell us about the claim, the carrier's position and where the numbers differ.</p>
<p><a class="btn btn-dark" href="tel:{B['phone_e164']}" style="width:100%;text-align:center">Call {B['phone_display']}</a></p>
<p style="margin:0"><a href="mailto:{B['email']}">{B['email']}</a></p></div>
<div class="card"><h2>Have these ready</h2><ul class="checks" style="margin:0">
<li>Full policy with declarations page</li><li>Claim number and carrier</li>
<li>Carrier's estimate and payments to date</li><li>Your estimate or contractor bid</li><li>Photos and any denial or partial-denial letters</li></ul></div>
</aside>"""

PAGES = []  # (path, label, priority)

def write(path, label, priority, html):
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    PAGES.append((path, label, priority))

# ================================================================ HOME
HOME_FAQ = [
    ("What is insurance appraisal?",
     "<p>Insurance appraisal is a dispute-resolution process written into most property insurance policies. When the policyholder and the insurer agree the loss is covered but disagree on how much it is worth, either side can demand appraisal. Each side hires its own appraiser, the two appraisers choose an umpire, and an agreement signed by any two of the three sets the amount of loss.</p>"),
    ("What is the difference between an appraiser and an umpire?",
     "<p>An appraiser is selected by one party, investigates the loss and works to reach an agreed amount with the other side's appraiser. An umpire is a neutral third person chosen by the two appraisers, or appointed by a court, who decides only the items the appraisers cannot agree on.</p>"),
    ("Does appraisal decide whether my claim is covered?",
     "<p>No. Appraisal decides the amount of loss. Questions about whether the policy covers a loss, or whether a policy condition was met, are coverage questions that are generally handled by the insurer, by negotiation, or in court.</p>"),
    ("Who can hire Property Claims Loss?",
     "<p>Policyholders, public adjusters, contractors, attorneys and insurance carriers retain us as appraisers. Appraisers on both sides, or a court, may select us as umpire.</p>"),
]
HOME_DESC = ("Insurance appraisal services for property claim disputes: independent appraisers and impartial "
             "umpires under the appraisal clause. Call (773) 497-2856.")
HOME_TITLE = "Insurance Appraisal & Umpire Services | Property Claims Loss"

home = head("/", HOME_TITLE, HOME_DESC, [
    org_node(), website_node(), webpage_node("/", HOME_TITLE, HOME_DESC), faq_node("/", HOME_FAQ)])
home += header("/")
home += f"""<div class="hero"><div class="wrap">
<div>
<span class="eyebrow">Insurance alternative dispute resolution</span>
<h1>Settle the amount of your property claim without going to court.</h1>
<p class="lead">{escape(B['name'])} provides <strong>insurance appraisal services</strong> for property claims: experienced <strong>appraisers</strong> who build and defend the number, and impartial <strong>umpires</strong> who resolve what the appraisers cannot agree on.</p>
<div class="hero-actions"><a class="btn btn-primary" href="/contact/">Request an Appraisal</a><a class="btn btn-ghost" href="tel:{B['phone_e164']}">Call {B['phone_display']}</a></div>
</div>
<div class="hero-card"><h2>How appraisal works</h2><ol>
<li><strong>Written demand</strong>Either side invokes the policy's appraisal clause.</li>
<li><strong>Appraisers selected</strong>Each side names a competent, disinterested appraiser.</li>
<li><strong>Umpire chosen</strong>The appraisers select a neutral umpire.</li>
<li><strong>Award signed</strong>Any two of the three sign, setting the amount of loss.</li>
</ol></div>
</div></div>

<section class="section-tight"><div class="wrap">
<div class="answer"><h2>What is insurance appraisal?</h2>
<p><strong>Insurance appraisal is a policy-based form of alternative dispute resolution for property claims.</strong> It is used when the insured and the insurance company agree that a loss is covered but disagree on the <em>amount of loss</em>. Each side selects an appraiser, the appraisers select an umpire, and a written award signed by any two of the three determines the amount. It is typically faster and less expensive than litigation.</p></div>
</div></section>

<section class="section-alt"><div class="wrap">
<div class="section-head"><span class="eyebrow">Our services</span><h2>Two roles in the appraisal process</h2>
<p>We serve either as a party's appraiser or as the neutral umpire. We never serve both roles on the same claim.</p></div>
<div class="grid-2">
<article class="card card-feature"><div class="icon">{ICON['clip']}</div><span class="tag">Appraiser services</span><h3>Your appraiser</h3>
<p>We investigate the loss, prepare a detailed line-item estimate, and work with the other side's appraiser to reach an agreed amount, presenting any unresolved items to the umpire.</p>
<ul class="checks"><li>Policy and appraisal-clause review</li><li>On-site inspection and documentation</li><li>Xactimate line-item estimating</li><li>Negotiation with the opposing appraiser</li><li>Umpire submissions and signed award</li></ul>
<a class="btn btn-dark" href="/appraiser-services/">Appraiser services</a></article>
<article class="card card-feature"><div class="icon">{ICON['scale']}</div><span class="tag">Umpire services</span><h3>A neutral umpire</h3>
<p>When the appraisers cannot agree, the umpire decides the items in dispute. We review both positions, inspect the property where needed and issue a clear, itemized award.</p>
<ul class="checks"><li>Conflict check and written disclosures</li><li>Review of both appraisers' estimates</li><li>Property inspection and umpire meetings</li><li>Item-by-item decisions on disputed amounts</li><li>Itemized award with ACV and RCV</li></ul>
<a class="btn btn-dark" href="/umpire-services/">Umpire services</a></article>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><span class="eyebrow">The process</span><h2>From demand to award in five steps</h2>
<p>Most residential and commercial property policies follow the same basic appraisal sequence. Your policy wording and state law control the details.</p></div>
<ol class="steps">
<li><h3>Demand</h3><p>Either party makes a written demand for appraisal after a disagreement on the amount of loss.</p></li>
<li><h3>Select appraisers</h3><p>Each side names its own competent, disinterested appraiser, commonly within 20 days.</p></li>
<li><h3>Select umpire</h3><p>The appraisers agree on an umpire, commonly within 15 days, or ask a court to appoint one.</p></li>
<li><h3>Evaluate</h3><p>The appraisers inspect, compare estimates and resolve as many items as possible.</p></li>
<li><h3>Award</h3><p>Disputed items go to the umpire. An award signed by any two sets the amount of loss.</p></li>
</ol>
<p style="margin-top:24px"><a href="/insurance-appraisal-process/">Read the full guide to the insurance appraisal process →</a></p>
</div></section>

<section class="section-alt"><div class="wrap">
<div class="section-head"><span class="eyebrow">Who we work with</span><h2>Built for everyone on a property claim</h2></div>
<div class="grid-3">
<div class="card"><div class="icon">{ICON['home']}</div><h3>Policyholders</h3><p>Homeowners and business owners whose claim payment does not cover the real cost of repair.</p></div>
<div class="card"><div class="icon">{ICON['brief']}</div><h3>Public adjusters &amp; attorneys</h3><p>Professionals who need an appraiser to carry a disputed claim through the appraisal clause.</p></div>
<div class="card"><div class="icon">{ICON['hammer']}</div><h3>Contractors &amp; roofers</h3><p>Restoration and roofing contractors whose scope or pricing differs from the carrier's estimate.</p></div>
<div class="card"><div class="icon">{ICON['shield']}</div><h3>Insurance carriers</h3><p>Carriers and claim departments that want a qualified appraiser or a neutral umpire.</p></div>
<div class="card"><div class="icon">{ICON['calc']}</div><h3>Independent adjusters</h3><p>Adjusting firms that need appraisal support on large or complex losses.</p></div>
<div class="card"><div class="icon">{ICON['user']}</div><h3>Opposing appraisers</h3><p>Appraisers on both sides who need to agree on a qualified, impartial umpire.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><span class="eyebrow">Compare your options</span><h2>Appraisal vs. mediation vs. litigation</h2>
<p>Appraisal is one of several ways to resolve a property claim dispute. Here is how it compares on the questions policyholders and carriers ask most.</p></div>
<div class="table-wrap"><table>
<thead><tr><th scope="col"></th><th scope="col">Appraisal</th><th scope="col">Mediation</th><th scope="col">Litigation</th></tr></thead>
<tbody>
<tr><th scope="row">What it resolves</th><td>Amount of loss</td><td>Amount and some coverage issues, by agreement</td><td>Coverage, amount, bad faith and other claims</td></tr>
<tr><th scope="row">Who decides</th><td>Two appraisers, with an umpire for disputed items</td><td>The parties themselves; the mediator only facilitates</td><td>Judge or jury</td></tr>
<tr><th scope="row">Is it binding?</th><td>An award signed by two of three generally sets the amount</td><td>Only if the parties sign a settlement</td><td>Yes, subject to appeal</td></tr>
<tr><th scope="row">Typical timeline</th><td>Weeks to a few months</td><td>Often a single session</td><td>Often a year or more</td></tr>
<tr><th scope="row">Typical cost</th><td>Each side pays its appraiser; umpire cost is usually shared</td><td>Mediator fee, often shared or paid by insurer under state programs</td><td>Attorney fees, expert fees and court costs</td></tr>
</tbody></table></div>
</div></section>

<section class="section-alt"><div class="wrap faq">
<div class="section-head"><span class="eyebrow">Quick answers</span><h2>Common questions about appraisal</h2></div>
{faq_html(HOME_FAQ, open_first=True)}
<p style="margin-top:22px"><a href="/faq/">See all frequently asked questions →</a></p>
</div></section>
"""
home += footer()
write("/", "Home", "1.0", home)

# ================================================================ APPRAISER
AP_PATH = "/appraiser-services/"
AP_TITLE = "Insurance Appraiser Services | Property Claims Loss"
AP_DESC = ("Hire an experienced insurance appraiser for your property claim dispute. Policy review, inspection, "
           "Xactimate estimates and umpire submissions. Call (773) 497-2856.")
AP_FAQ = [
    ("When should I hire an insurance appraiser?",
     "<p>Consider appraisal once the insurer has made a determination you disagree with on price or scope, you have tried to resolve the difference directly, and the dispute is about how much the covered loss is worth rather than whether it is covered. Check your policy for any deadline to demand appraisal or to file suit.</p>"),
    ("Can my contractor or public adjuster be my appraiser?",
     "<p>Most policies require each appraiser to be \"competent and disinterested\" (some say \"impartial\" or \"independent\"). Someone with a financial stake in the claim outcome, such as the contractor doing the repairs, may be challenged. An independent appraiser avoids that risk.</p>"),
    ("What does an insurance appraiser need from me?",
     "<p>The full policy, the claim number, the insurer's estimates and payment letters, any estimates or bids you have, photos and videos of the damage, and the written appraisal demand if one has been sent.</p>"),
]
ap = head(AP_PATH, AP_TITLE, AP_DESC, [
    org_node(), website_node(), webpage_node(AP_PATH, AP_TITLE, AP_DESC), crumbs_node(AP_PATH, "Appraiser Services"),
    service_node(AP_PATH, "Insurance Appraiser Services", "Insurance appraisal",
                 "Party-appointed appraiser services for property insurance claims under the policy appraisal clause: policy review, inspection, line-item estimating, negotiation with the opposing appraiser, umpire submissions and award.",
                 ["Policyholders", "Public adjusters", "Attorneys", "Contractors", "Insurance carriers"]),
    faq_node(AP_PATH, AP_FAQ)])
ap += header(AP_PATH)
ap += page_hero(AP_PATH, "Appraiser Services", "Insurance appraiser services",
                "When you and the insurance company agree the loss is covered but not on what it is worth, an experienced appraiser builds the documented number and gets it into a signed award.")
ap += f"""<section><div class="wrap layout"><div class="prose">
<div class="answer"><h2>What does an insurance appraiser do?</h2>
<p>An insurance appraiser is the person each party selects under the appraisal clause to determine the amount of loss. The appraiser inspects the damage, prices the repairs line by line, separates actual cash value from replacement cost, and negotiates with the other side's appraiser. Items they cannot agree on are presented to the umpire.</p></div>

<h2>What's included</h2>
<h3>1. Claim and policy review</h3>
<p>We read the policy, the appraisal clause, the declarations and endorsements, the carrier's estimate and the claim correspondence, so the appraisal is built on the right valuation basis, limits and deductibles.</p>
<h3>2. Inspection and documentation</h3>
<p>We inspect the property and document the damage with measurements and photographs, covering roofing, siding, interiors, contents, and the matching and code-upgrade issues that drive many disputes.</p>
<h3>3. Line-item estimate</h3>
<p>We prepare a detailed Xactimate estimate with pricing for the loss location and date, showing replacement cost value (RCV), depreciation and actual cash value (ACV) separately.</p>
<h3>4. Negotiation with the opposing appraiser</h3>
<p>We compare estimates item by item and work to agree on as much as possible. Agreed items narrow the dispute and keep the umpire's work, and cost, to a minimum.</p>
<h3>5. Umpire submission and award</h3>
<p>Remaining differences go to the umpire with clear documentation. Once two of the three sign, we deliver the signed award and explain what it means for payment.</p>

<h2>Common disputes we handle</h2>
<ul class="checks">
<li>Hail and wind damage to roofs, siding, gutters and windows</li>
<li>Water and plumbing losses, including mold remediation scope</li>
<li>Fire and smoke damage, cleaning versus replacement</li>
<li>Matching of undamaged materials and line-of-sight issues</li>
<li>Code upgrades, overhead and profit, and depreciation</li>
<li>Commercial property, multi-family and large losses</li>
</ul>

<h2>Questions about hiring an appraiser</h2>
<div class="faq">{faq_html(AP_FAQ)}</div>
<p class="updated">Last updated {TODAY}.</p>
</div>{aside_contact()}</div></section>
"""
ap += footer()
write(AP_PATH, "Appraiser Services", "0.9", ap)

# ================================================================ UMPIRE
UM_PATH = "/umpire-services/"
UM_TITLE = "Insurance Umpire Services | Property Claims Loss"
UM_DESC = ("Impartial insurance umpire services for property claim appraisals. Conflict checks, review of both "
           "estimates, inspection, and itemized awards. Call (773) 497-2856.")
UM_FAQ = [
    ("How is an umpire selected?",
     "<p>Under most policies, the two appraisers agree on an umpire, often within 15 days after both appraisers are named. If they cannot agree, either party can usually ask a court in the state where the property is located to appoint one.</p>"),
    ("Does the umpire decide the entire claim?",
     "<p>No. The umpire decides only the items the two appraisers submit as disagreements. Items the appraisers already agree on are carried into the award as agreed.</p>"),
    ("Who pays the umpire?",
     "<p>Under the typical appraisal clause, the policyholder and the insurer share the umpire's fees and the other costs of appraisal equally. Your policy and state law control.</p>"),
    ("Is the umpire's decision final?",
     "<p>An award signed by the umpire and at least one appraiser generally determines the amount of loss. Courts may set an award aside only in limited situations, such as fraud, a lack of impartiality, or deciding issues outside the appraisal.</p>"),
]
um = head(UM_PATH, UM_TITLE, UM_DESC, [
    org_node(), website_node(), webpage_node(UM_PATH, UM_TITLE, UM_DESC), crumbs_node(UM_PATH, "Umpire Services"),
    service_node(UM_PATH, "Insurance Umpire Services", "Insurance appraisal umpire",
                 "Impartial umpire services for property insurance appraisals: conflict disclosure, review of both appraisers' positions, inspection, umpire meetings, and an itemized award of the disputed amounts.",
                 ["Party-appointed appraisers", "Insurance carriers", "Policyholders", "Courts"]),
    faq_node(UM_PATH, UM_FAQ)])
um += header(UM_PATH)
um += page_hero(UM_PATH, "Umpire Services", "Insurance umpire services",
                "A neutral, qualified umpire who gives both appraisers a fair hearing and decides the disputed items with a clear, itemized award.")
um += f"""<section><div class="wrap layout"><div class="prose">
<div class="answer"><h2>What does an insurance umpire do?</h2>
<p>An insurance umpire is the neutral third member of an appraisal panel. When the two party-appointed appraisers cannot agree on the amount of loss, they submit their differences to the umpire, who reviews both positions and decides the disputed items. An award signed by the umpire and either appraiser sets the amount of loss.</p></div>

<h2>Our umpire commitments</h2>
<ul class="checks">
<li><strong>Impartiality.</strong> We do not advocate for either side. We disclose any prior relationship with the parties, appraisers or counsel before accepting an assignment.</li>
<li><strong>No dual roles.</strong> We never act as umpire on a claim where we have acted as an appraiser, adjuster or consultant.</li>
<li><strong>Equal access.</strong> Communications go to both appraisers. We do not hold one-sided discussions about the merits.</li>
<li><strong>Clear awards.</strong> Every disputed item is decided and explained, with RCV and ACV shown where the policy requires it.</li>
</ul>

<h2>How our umpire process works</h2>
<ol>
<li><strong>Selection and disclosure.</strong> Both appraisers confirm our selection, we complete a conflict check and send written disclosures and fee terms to both sides.</li>
<li><strong>Submissions.</strong> Each appraiser provides an estimate, photos and a list of the items still in dispute.</li>
<li><strong>Inspection and meeting.</strong> Where the dispute calls for it, we inspect the property with both appraisers and hold an umpire meeting to hear each position.</li>
<li><strong>Decision.</strong> We decide each disputed line item based on the evidence, the policy's valuation terms and local pricing.</li>
<li><strong>Award.</strong> We prepare the award for signature by the umpire and at least one appraiser, with an itemized attachment.</li>
</ol>

<h2>Questions about umpires</h2>
<div class="faq">{faq_html(UM_FAQ)}</div>
<p class="updated">Last updated {TODAY}.</p>
</div>{aside_contact()}</div></section>
"""
um += footer()
write(UM_PATH, "Umpire Services", "0.9", um)

# ================================================================ PROCESS GUIDE
PR_PATH = "/insurance-appraisal-process/"
PR_TITLE = "How Insurance Appraisal Works: A Step-by-Step Guide"
PR_DESC = ("A plain-English guide to the insurance appraisal clause: when to invoke it, how appraisers and "
           "umpires are chosen, timelines, costs, the award and what happens after.")
PR_STEPS = [
    ("Confirm the dispute is about the amount of loss",
     "Appraisal resolves disagreements over price and scope of a covered loss. Coverage disputes generally belong elsewhere."),
    ("Send a written demand for appraisal",
     "Either the policyholder or the insurer may demand appraisal in writing, following any notice requirements in the policy."),
    ("Each party selects an appraiser",
     "Each side names a competent and disinterested appraiser, commonly within 20 days of the demand, and notifies the other side."),
    ("The appraisers select an umpire",
     "The two appraisers agree on an umpire, commonly within 15 days. If they cannot, a court where the property is located may appoint one."),
    ("The appraisers evaluate the loss",
     "Each appraiser inspects and estimates the loss, stating actual cash value and amount of loss separately for each item, and they resolve what they can."),
    ("Disagreements go to the umpire",
     "The appraisers submit only their differences to the umpire, who reviews the evidence and decides those items."),
    ("The award is signed",
     "A written award signed by any two of the three sets the amount of loss, and the insurer issues payment under the policy's terms."),
]
pr = head(PR_PATH, PR_TITLE, PR_DESC, [
    org_node(), website_node(), webpage_node(PR_PATH, PR_TITLE, PR_DESC), crumbs_node(PR_PATH, "How Appraisal Works"),
    {"@type": "Article", "@id": f"{U}{PR_PATH}#article", "headline": "How the insurance appraisal process works",
     "description": PR_DESC, "author": {"@id": f"{U}/#business"}, "publisher": {"@id": f"{U}/#business"},
     "mainEntityOfPage": {"@id": f"{U}{PR_PATH}#webpage"}, "dateModified": TODAY, "datePublished": "2026-11-13",
     "image": f"{U}/og-image.jpg", "inLanguage": "en-US"},
    {"@type": "HowTo", "@id": f"{U}{PR_PATH}#howto", "name": "How to resolve a property claim dispute through insurance appraisal",
     "description": "The standard steps of the appraisal clause found in most property insurance policies.",
     "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t, "url": f"{U}{PR_PATH}#step-{i+1}"}
              for i, (n, t) in enumerate(PR_STEPS)]}])
pr += header(PR_PATH)
pr += page_hero(PR_PATH, "How Appraisal Works", "How the insurance appraisal process works",
                "A step-by-step guide to the appraisal clause in property insurance policies: what it covers, who is involved, how long it takes and what it costs.")
steps_html = "\n".join(f'<li id="step-{i+1}"><strong>{escape(n)}.</strong> {escape(t)}</li>' for i, (n, t) in enumerate(PR_STEPS))
pr += f"""<section><div class="wrap layout"><article class="prose">
<div class="answer"><h2>The short answer</h2>
<p>Insurance appraisal is a contractual dispute-resolution process in most property policies. If you and your insurer disagree on the amount of a covered loss, either side may demand appraisal in writing. Each side selects an appraiser, the appraisers select an umpire, and an award signed by any two of the three determines the amount of loss. It is usually faster and less costly than a lawsuit.</p></div>

<h2 id="what">What the appraisal clause says</h2>
<p>Most homeowners and commercial property policies contain an appraisal provision modeled on standard industry wording. While the exact language varies, the typical clause provides that:</p>
<ul>
<li>If the insured and insurer fail to agree on the amount of loss, either may demand appraisal in writing.</li>
<li>Each party chooses a competent and disinterested (or impartial) appraiser within a set time, commonly 20 days.</li>
<li>The appraisers choose an umpire, commonly within 15 days, or ask a court of record in the state where the property is located to select one.</li>
<li>The appraisers separately state the actual cash value and the amount of loss.</li>
<li>Agreement in writing by any two of the three sets the amount of loss.</li>
<li>Each party pays its own appraiser and shares the umpire and other appraisal expenses equally.</li>
</ul>
<p>Always read your own policy. Some policies add conditions, some states regulate appraisal by statute, and some policies have no appraisal clause at all.</p>

<h2 id="steps">The appraisal process, step by step</h2>
<ol>{steps_html}</ol>

<h2 id="when">When appraisal makes sense</h2>
<ul class="checks">
<li>The insurer accepts the claim but its estimate is far below the cost to repair.</li>
<li>There is a disagreement over scope, such as repair versus replacement, or matching.</li>
<li>The dispute is over pricing, depreciation, overhead and profit, or code items.</li>
<li>Both sides want a faster, lower-cost resolution than litigation.</li>
</ul>
<h3>When appraisal may not fit</h3>
<p>If the insurer has denied the claim outright, or the disagreement is about whether a cause of loss is covered, appraisal may not resolve the issue. Some courts allow appraisers to decide causation as part of the amount of loss; others do not. Talk to a licensed attorney about coverage questions.</p>

<h2 id="time">How long does insurance appraisal take?</h2>
<p>Many appraisals conclude within a few weeks to a few months after the umpire is chosen. Timing depends on how quickly appraisers are named, the size and complexity of the loss, access to the property and how many items go to the umpire.</p>

<h2 id="cost">How much does insurance appraisal cost?</h2>
<p>Under the typical clause, each party pays its own appraiser, and the umpire's fee and other appraisal expenses are split equally. Appraiser fee structures vary by firm, claim size and state rules, so ask for the fee arrangement in writing before you sign an engagement agreement.</p>

<h2 id="after">What happens after the award</h2>
<p>The signed award sets the amount of loss. The insurer then pays according to the policy, applying the deductible, prior payments, limits and any holdback for replacement cost until repairs are completed. The award generally does not resolve coverage defenses the insurer has reserved.</p>

<h2 id="terms">Key terms</h2>
<dl>
<dt><strong>Amount of loss</strong></dt><dd>The dollar value of the covered damage, as determined in appraisal.</dd>
<dt><strong>Replacement cost value (RCV)</strong></dt><dd>The cost to repair or replace damaged property with like kind and quality, without deducting depreciation.</dd>
<dt><strong>Actual cash value (ACV)</strong></dt><dd>Generally replacement cost minus depreciation, though state law defines it differently in some places.</dd>
<dt><strong>Disinterested appraiser</strong></dt><dd>An appraiser without a financial stake or bias in the outcome of the claim.</dd>
<dt><strong>Umpire</strong></dt><dd>The neutral third person who decides items the appraisers cannot agree on.</dd>
<dt><strong>Award</strong></dt><dd>The written, signed determination of the amount of loss.</dd>
</dl>
<p class="note">This guide is general information, not legal advice. Policy language and state law control how appraisal works on your claim. Last updated {TODAY}.</p>
</article>{aside_contact()}</div></section>
"""
pr += footer()
write(PR_PATH, "How Appraisal Works", "0.9", pr)

# ================================================================ FAQ
FAQ_PATH = "/faq/"
FAQ_TITLE = "Insurance Appraisal FAQ | Property Claims Loss"
FAQ_DESC = ("Answers to common questions about insurance appraisal: what it is, when to demand it, who pays, "
            "how long it takes, appraisers vs. umpires, and binding awards.")
FAQ_GROUPS = [
    ("Understanding appraisal", [
        ("What is insurance appraisal?", HOME_FAQ[0][1]),
        ("Is appraisal the same as arbitration?",
         "<p>No. Appraisal is narrower. It decides only the amount of loss, uses appraisers and an umpire rather than an arbitrator, and usually involves no formal hearing or legal rulings. Arbitration can decide broader legal issues.</p>"),
        ("Does appraisal decide coverage?", HOME_FAQ[2][1]),
        ("Is insurance appraisal a form of alternative dispute resolution?",
         "<p>Yes. Appraisal is a policy-based form of alternative dispute resolution (ADR). Like mediation and arbitration, it resolves a disagreement outside of court, but it is limited to the value of a covered loss.</p>"),
    ]),
    ("Starting appraisal", [
        ("Who can demand appraisal?",
         "<p>Under the typical clause, either the policyholder or the insurance company can demand appraisal in writing once they disagree on the amount of loss.</p>"),
        ("How do I demand appraisal?",
         "<p>Send the insurer a written demand that identifies the claim, states that you disagree with the amount of loss and invokes the appraisal provision, and name your appraiser within the time the policy allows. Keep proof of delivery.</p>"),
        ("Is there a deadline to demand appraisal?",
         "<p>Policies and state laws vary. Some set no specific deadline, while the policy's suit-limitation period and any reasonableness requirements may still apply. Review your policy promptly and do not wait.</p>"),
        ("Can the insurance company refuse appraisal?",
         "<p>If the policy contains an appraisal clause and the dispute is over the amount of loss, the insurer is generally bound by it. Insurers sometimes object that the dispute involves coverage. In that case a court may decide whether appraisal goes forward.</p>"),
    ]),
    ("Appraisers and umpires", [
        ("What is the difference between an appraiser and an umpire?", HOME_FAQ[1][1]),
        ("What does \"competent and disinterested\" mean?",
         "<p>It generally means the appraiser has the knowledge to value the loss and no financial interest or bias that would compromise their judgment. Requirements and court interpretations vary by state.</p>"),
        ("Can I choose any appraiser I want?",
         "<p>Yes, within the policy's requirements. Each side picks its own appraiser, but either side can object if an appraiser is not competent or not disinterested.</p>"),
        ("What happens if the appraisers cannot agree on an umpire?",
         "<p>Either party can usually ask a court in the state where the property is located to appoint one.</p>"),
    ]),
    ("Cost, time and outcome", [
        ("Who pays for insurance appraisal?",
         "<p>Typically each party pays its own appraiser, and the umpire's fee and other appraisal costs are divided equally between the policyholder and the insurer, subject to the policy and state law.</p>"),
        ("How long does appraisal take?",
         "<p>Many appraisals finish within a few weeks to a few months. Larger or more complex losses, or disputes about the process itself, take longer.</p>"),
        ("Is the appraisal award binding?",
         "<p>An award signed by any two of the three generally sets the amount of loss. Courts may vacate an award only in narrow cases, such as fraud, partiality or an award outside the scope of appraisal.</p>"),
        ("Will appraisal get me more money?",
         "<p>No outcome is guaranteed. The award can come in higher, lower or close to the insurer's estimate, depending on the evidence. A well-documented estimate gives you the best chance of a fair number.</p>"),
    ]),
]
ALL_FAQ = [qa for _, g in FAQ_GROUPS for qa in g]
fq = head(FAQ_PATH, FAQ_TITLE, FAQ_DESC, [
    org_node(), website_node(), webpage_node(FAQ_PATH, FAQ_TITLE, FAQ_DESC), crumbs_node(FAQ_PATH, "FAQ"),
    faq_node(FAQ_PATH, ALL_FAQ)])
fq += header(FAQ_PATH)
fq += page_hero(FAQ_PATH, "FAQ", "Insurance appraisal: frequently asked questions",
                "Straight answers about the appraisal clause, appraisers, umpires, costs, timelines and awards.")
groups = "".join(f"<h2>{escape(t)}</h2>{faq_html(g)}" for t, g in FAQ_GROUPS)
fq += f"""<section><div class="wrap layout"><div class="faq">{groups}
<p class="note">These answers are general information, not legal advice. Your policy and state law control. Last updated {TODAY}.</p></div>{aside_contact()}</div></section>
"""
fq += footer()
write(FAQ_PATH, "FAQ", "0.8", fq)

# ================================================================ ABOUT
AB_PATH = "/about/"
AB_TITLE = "About Property Claims Loss | Insurance Appraisal Firm"
AB_DESC = ("Property Claims Loss is an insurance appraisal firm providing appraiser and umpire services to resolve "
           "property claim disputes through the appraisal clause.")
ab = head(AB_PATH, AB_TITLE, AB_DESC, [
    org_node(), website_node(), webpage_node(AB_PATH, AB_TITLE, AB_DESC, "AboutPage"), crumbs_node(AB_PATH, "About")])
ab += header(AB_PATH)
ab += page_hero(AB_PATH, "About", "About Property Claims Loss",
                "An insurance appraisal firm focused on one thing: resolving disagreements over the amount of a property loss fairly and on the record.")
ab += f"""<section><div class="wrap layout"><div class="prose">
<h2>Who we are</h2>
<p>{escape(B['legal_name'])} is an insurance appraisal firm based in {B['city']}, Illinois. We provide <a href="/appraiser-services/">appraiser services</a> and <a href="/umpire-services/">umpire services</a> for residential and commercial property claims, using the appraisal clause in the insurance policy to resolve disputes over the amount of loss without litigation.</p>

<h2>What we believe</h2>
<ul class="checks">
<li><strong>The number should be documented.</strong> Every figure we present is backed by inspection, measurement, photos and line-item pricing.</li>
<li><strong>Appraisal is not litigation.</strong> The goal is an accurate amount of loss, reached efficiently, not a prolonged fight.</li>
<li><strong>Roles must stay clean.</strong> As an appraiser we present our client's position honestly. As an umpire we are neutral. We never mix the two on one claim.</li>
<li><strong>Plain language.</strong> Policyholders deserve to understand the process, the costs and the likely outcomes before they commit.</li>
</ul>

<h2>Credentials on staff</h2>
<p>Our staff holds appraiser and umpire certifications, adjuster licenses in {LICENSED_STATES}, and experience as an Executive General Adjuster.</p>
</div></div></section>
<section class="section-alt"><div class="wrap">{creds_html()}
<p style="margin-top:24px"><strong>We stand ready to assist with your insurance appraisal needs.</strong></p></div></section>
<section><div class="wrap layout"><div class="prose">

<h2>What we do not do</h2>
<p>We are not a law firm and do not give legal advice. Appraisal decides the amount of loss, not coverage. If your claim was denied or involves coverage questions, we recommend speaking with a licensed attorney in your state.</p>
<p class="updated">Last updated {TODAY}.</p>
</div>{aside_contact()}</div></section>
"""
ab += footer()
write(AB_PATH, "About", "0.6", ab)

# ================================================================ CONTACT
CT_PATH = "/contact/"
CT_TITLE = "Contact Property Claims Loss | Request an Appraiser or Umpire"
CT_DESC = ("Request an insurance appraiser or umpire. Call (773) 497-2856 or email info@propertyclaimsloss.com "
           "with your claim details.")
subject = "Appraisal%20request"
body = ("Name%3A%0APhone%3A%0AProperty%20address%3A%0AInsurance%20carrier%20and%20claim%20number%3A%0A"
        "Date%20of%20loss%3A%0AType%20of%20damage%3A%0AService%20needed%20(appraiser%20or%20umpire)%3A%0A"
        "Has%20appraisal%20been%20demanded%3F%3A%0ABrief%20description%20of%20the%20dispute%3A%0A")
ct = head(CT_PATH, CT_TITLE, CT_DESC, [
    org_node(), website_node(), webpage_node(CT_PATH, CT_TITLE, CT_DESC, "ContactPage"), crumbs_node(CT_PATH, "Contact")])
ct += header(CT_PATH)
ct += page_hero(CT_PATH, "Contact", "Request an appraiser or umpire",
                "Tell us about the claim and where the numbers differ. We will let you know whether appraisal fits and what the next steps are.")
ct += f"""<section><div class="wrap grid-2">
<div class="card"><h2>Get in touch</h2>
<ul class="contact-list">
<li><strong>Phone</strong><a href="tel:{B['phone_e164']}">{B['phone_display']}</a></li>
<li><strong>Email</strong><a href="mailto:{B['email']}">{B['email']}</a></li>
<li><strong>Based in</strong>{B['city']}, Illinois</li>
</ul>
<p style="margin-top:20px"><a class="btn btn-dark" href="mailto:{B['email']}?subject={subject}&amp;body={body}">Email an appraisal request</a></p>
<p class="updated">The button opens a pre-filled email with the details we need.</p></div>
<div class="card"><h2>What to include</h2>
<ul class="checks">
<li>Your name, phone and the property address</li>
<li>Insurance carrier and claim number</li>
<li>Date and type of loss (hail, wind, water, fire, other)</li>
<li>Whether you need an appraiser or an umpire</li>
<li>Whether appraisal has already been demanded, and by whom</li>
<li>The carrier's estimate and your estimate or contractor bid</li>
</ul>
<p class="note" style="margin-bottom:0">For umpire assignments, please copy both appraisers so we can run a conflict check and keep communications equal.</p></div>
</div></section>
"""
ct += footer()
write(CT_PATH, "Contact", "0.7", ct)

# ================================================================ 404
nf = head("/404.html", "Page Not Found | Property Claims Loss", "The page you requested could not be found.",
          [org_node(), website_node()]).replace('content="index, follow, max-image-preview:large, max-snippet:-1"', 'content="noindex"')
nf += header("")
nf += f"""<div class="page-hero"><div class="wrap"><h1>Page not found</h1>
<p class="lead">That page has moved or doesn't exist. Try one of these instead.</p></div></div>
<section><div class="wrap grid-3">
<a class="card" href="/appraiser-services/"><h3>Appraiser Services</h3><p>Hire an appraiser for your claim.</p></a>
<a class="card" href="/umpire-services/"><h3>Umpire Services</h3><p>Retain a neutral umpire.</p></a>
<a class="card" href="/insurance-appraisal-process/"><h3>How Appraisal Works</h3><p>The step-by-step guide.</p></a>
</div></section>
"""
nf += footer()
(ROOT / "404.html").write_text(nf, encoding="utf-8")

# ================================================================ sitemap
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, _, pri in PAGES:
    sm.append(f"  <url><loc>{U}{path}</loc><lastmod>{TODAY}</lastmod><priority>{pri}</priority></url>")
sm.append("</urlset>\n")
(ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

# ================================================================ llms.txt
llms = f"""# {B['name']}

> {B['summary']}

## Key facts

- Business name: {B['name']} (legal name: {B['legal_name']})
- Website: {U}/
- Phone: {B['phone_display']}
- Email: {B['email']}
- Based in: {B['city']}, Illinois, United States
- Services: insurance appraiser services (party-appointed appraiser for policyholders or insurers); insurance umpire services (neutral umpire selected by the appraisers or appointed by a court)
- Category: insurance alternative dispute resolution (ADR) for property insurance claims
- Works with: policyholders, public adjusters, attorneys, contractors and roofers, insurance carriers, independent adjusters, opposing appraisers
- Claim types: hail, wind, water, fire and smoke, residential and commercial property, large losses
- Credentials on staff: {"; ".join(CERTS)}
- Licenses: {"; ".join(f"{a} {b}" for a, b in LICENSES)}
- Not a law firm; does not give legal advice; appraisal determines amount of loss, not coverage

## Pages

- [Home]({U}/): overview of appraisal, the two service roles, process, comparison with mediation and litigation
- [Appraiser Services]({U}/appraiser-services/): what an insurance appraiser does and what is included
- [Umpire Services]({U}/umpire-services/): what an insurance umpire does, impartiality commitments, umpire process
- [How Appraisal Works]({U}/insurance-appraisal-process/): step-by-step guide to the appraisal clause, timelines, costs, key terms
- [FAQ]({U}/faq/): questions on demanding appraisal, appraisers vs. umpires, cost, timing, binding awards
- [About]({U}/about/): who we are and how we work
- [Contact]({U}/contact/): phone, email and what to include in a request

## Insurance appraisal in brief

- Appraisal resolves disagreements about the amount of a covered property loss, not coverage.
- Either the insured or the insurer may demand appraisal in writing.
- Each side selects a competent, disinterested appraiser (commonly within 20 days); the appraisers select an umpire (commonly within 15 days) or a court appoints one.
- Appraisers state actual cash value and amount of loss separately; disagreements go to the umpire.
- A written award signed by any two of the three sets the amount of loss.
- Typically each side pays its own appraiser and the umpire and other expenses are shared equally, subject to policy wording and state law.

Last updated: {TODAY}
"""
(ROOT / "llms.txt").write_text(llms, encoding="utf-8")

print("Built", len(PAGES), "pages + 404, sitemap.xml, llms.txt")
