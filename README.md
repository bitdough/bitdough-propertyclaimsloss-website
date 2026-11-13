# propertyclaimsloss.com

Website for Property Claims Loss: insurance appraisal services (appraiser and umpire) for property
insurance claims. Plain HTML and CSS, no frameworks, no JavaScript. It loads fast and AI crawlers can
read every page.

## What's where

- `public/` holds everything visitors see.
  - `index.html` is the home page. Each other page lives in its own folder: `appraiser-services/`, `umpire-services/`,
    `insurance-appraisal-process/`, `faq/`, `about/`, `contact/`.
  - `404.html` shows for any missing page.
  - `styles.css` controls the look of every page.
  - `sitemap.xml`, `robots.txt` and `llms.txt` help Google, Bing and AI assistants find and understand the site.
  - `_redirects` sends the old WordPress addresses (/about-us, /contact-us, /blog) to the new pages.
  - `_headers` sets caching and security headers on Cloudflare.
  - `favicon.*`, `apple-touch-icon.png`, `icon-512.png` and `og-image.jpg` are the icons and the image shown when a link is shared.
- `tools/build.py` builds every page. Business name, phone and email are set once at the top.
- `wrangler.jsonc` tells Cloudflare to serve the `public` folder.

## Making changes

Edit `tools/build.py` (the BUSINESS block or a page's text), then run:

```
python3 tools/build.py
```

That rewrites all pages, `sitemap.xml` (with today's date) and `llms.txt`, so the name, phone and email
always match everywhere. Commit and push, and Cloudflare publishes the change.

## SEO / GEO / AEO built in

- **SEO:** unique title, description and canonical URL on every page; one H1 per page; Open Graph and
  Twitter cards; XML sitemap; 301 redirects from the old WordPress URLs; fast static pages.
- **AEO (answer engines, featured snippets, voice):** every page opens with a 40–60 word answer box;
  question-style headings; FAQPage, HowTo, Service and BreadcrumbList structured data.
- **GEO (ChatGPT, Claude, Perplexity, Gemini, Copilot):** `robots.txt` explicitly allows AI crawlers;
  `llms.txt` gives a plain-text fact sheet; every page carries the same ProfessionalService entity
  (`@id https://propertyclaimsloss.com/#business`); no content is hidden behind JavaScript.

---

## 1. Publish on Cloudflare

1. Make sure propertyclaimsloss.com uses Cloudflare nameservers (Cloudflare dashboard → the domain → **Overview** shows "Active").
2. **Workers & Pages → Create → Import a repository** → choose `bitdough-propertyclaimsloss-website`. Leave the build settings
   at their defaults and click **Deploy**. `wrangler.jsonc` already tells Cloudflare to serve `public/`.
3. In **DNS → Records**, delete the old `A`/`CNAME` records for `propertyclaimsloss.com` and `www` that point to the
   old WordPress host. **Do not delete the `mail`, `MX` or `TXT` records** (see step 2 below).
4. Open the new Worker → **Settings → Domains & Routes → Add → Custom domain** → add `propertyclaimsloss.com`,
   then add `www.propertyclaimsloss.com`.
5. Send `www` to the main domain: **Rules → Redirect Rules → Create rule** → *Redirect from WWW to root* template → 301.
6. **SSL/TLS → Overview** → set to **Full (strict)**. Under **Edge Certificates**, turn on *Always Use HTTPS*.

## 2. Email on InMotion Hosting (with DNS on Cloudflare)

The website is on Cloudflare and email stays on InMotion. Because Cloudflare runs the DNS, the email
records must be added **in Cloudflare**. The DNS zone inside InMotion's cPanel is ignored once the
nameservers point to Cloudflare.

**In InMotion (cPanel):**

1. Make sure `propertyclaimsloss.com` is added to the InMotion account (as the primary or an addon domain).
2. **Email Accounts → Create** → `info@propertyclaimsloss.com` (this is the address used on the website), plus any others.
3. **Email Routing** → select the domain → **Local Mail Exchanger**.
4. **Email Deliverability** → select the domain → **Manage**. Copy the exact *SPF* and *DKIM* values shown there.
5. Note the server's **shared IP address** (cPanel sidebar → *General Information*).

**In Cloudflare → DNS → Records → Add record.** Every mail record must be **DNS only (grey cloud)**, because
Cloudflare's proxy only carries web traffic:

| Type  | Name                | Content / value                                              | Proxy     |
|-------|---------------------|--------------------------------------------------------------|-----------|
| A     | `mail`              | InMotion server IP                                           | DNS only  |
| MX    | `@`                 | `mail.propertyclaimsloss.com`, priority `0`                  | (n/a)     |
| A     | `webmail`           | InMotion server IP                                           | DNS only  |
| A     | `autodiscover`      | InMotion server IP (lets Outlook/phones set up automatically)| DNS only  |
| TXT   | `@`                 | SPF value copied from cPanel *Email Deliverability*           | (n/a)     |
| TXT   | `default._domainkey`| DKIM value copied from cPanel *Email Deliverability*          | (n/a)     |
| TXT   | `_dmarc`            | `v=DMARC1; p=none; rua=mailto:info@propertyclaimsloss.com`   | (n/a)     |

- Keep only **one** SPF record on `@`. If Cloudflare already has a `v=spf1` record, replace it.
- After a few weeks of clean reports, tighten DMARC to `p=quarantine`.
- Test: send from Gmail to `info@propertyclaimsloss.com` and back. Then check
  [mail-tester.com](https://www.mail-tester.com) and aim for 9/10 or better.
- Check webmail at `https://webmail.propertyclaimsloss.com` or through InMotion's AMP → *Email*.

## 3. After launch

1. **Google Search Console:** add the domain property, verify with the TXT record it gives you (add it in Cloudflare),
   then submit `https://propertyclaimsloss.com/sitemap.xml`.
2. **Bing Webmaster Tools:** import from Search Console and submit the sitemap. Bing's index powers Copilot and much
   of ChatGPT's web search, so this matters for GEO.
3. **Google Business Profile:** create or claim it, using the same name, phone and website as the site.
4. Test the structured data at <https://search.google.com/test/rich-results> and <https://validator.schema.org>.

## Keep these identical everywhere

Business name **Property Claims Loss** (legal name *Property Claims Loss Inc.*), phone **(773) 497-2856** and email
**info@propertyclaimsloss.com** appear on every page, in the structured data, in `llms.txt` and in your Google and
Bing business listings. Change them only in `tools/build.py`, then rebuild.
