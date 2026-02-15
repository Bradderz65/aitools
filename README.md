# [TOOLS.AI] — The Unboring AI Directory

A completely unique AI tools directory website with bold design, honest positioning, and multiple monetization channels.

## Design Philosophy

This is **not** another generic AI website. We went for:
- **Cream/warm background** — No more dark mode everywhere
- **Brutalist borders** — 2px solid black, box shadows
- **Serif headlines** — DM Serif Display for editorial feel
- **Coral accent** — #FF4D4D as the primary action color
- **Honest copy** — "No bullshit" tone, human-written
- **Floating cards** — Animated visual elements
- **Marquee category strip** — Dynamic scrolling categories

## Monetization

1. **Affiliate Links** — Each tool link can be an affiliate link (15-30% commissions)
2. **Digital Products** — AI prompt packs ($9-$19) sold via Stripe
3. **Newsletter** — Build email list for future monetization
4. **Sponsored Deals** — The "Deals" section can feature paid placements

## Quick Start

```bash
# Just open in browser
open index.html

# Or serve locally
npx serve .
```

## Configuration

### 1. Affiliate Links

Replace placeholder URLs with your affiliate links:

| Tool | Affiliate Program |
|------|-------------------|
| ChatGPT | https://partner.openai.com |
| Jasper | https://jasper.ai/affiliate-program |
| Notion | https://notion.so/affiliates |
| Cursor | https://cursor.sh |
| Midjourney | https://midjourney.com |

### 2. Stripe Integration

For real payments, add your Stripe keys:

```javascript
// In script.js, replace processPayment with:
const stripe = Stripe('YOUR_PUBLISHABLE_KEY');

const response = await fetch('/create-checkout-session', {
    method: 'POST',
    body: JSON.stringify({ pack_id: packId })
});

const session = await response.json();
stripe.redirectToCheckout({ sessionId: session.id });
```

### 3. Analytics

Add Google Analytics before `</head>`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_ID');
</script>
```

### 4. Email Collection

Connect to any email service (ConvertKit, Mailchimp, etc.):

```javascript
// In newsletter form submit:
await fetch('https://api.convertkit.com/v3/forms/YOUR_FORM/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, api_key: 'YOUR_KEY' })
});
```

## File Structure

```
ai-tools-hub/
├── index.html    — Main page with all content
├── styles.css    — Unique brutalist/editorial styling
├── script.js     — Payments, tracking, interactions
└── README.md     — This file
```

## Deployment

Free options:

```bash
# Netlify
npx netlify deploy --prod

# Vercel
npx vercel --prod

# GitHub Pages
git push && enable Pages in repo settings
```

## Revenue Potential

| Channel | Potential |
|---------|-----------|
| Affiliate commissions | $500-5000/mo |
| Prompt pack sales | $200-2000/mo |
| Newsletter sponsorships | $100-500/email |
| Sponsored tool placements | $50-500/placement |

## Customization

### Colors
Edit CSS variables at the top of `styles.css`:
```css
:root {
    --bg: #F5F2EB;           /* Cream background */
    --accent: #FF4D4D;       /* Coral/red */
    --highlight: #FFE156;    /* Yellow */
    --accent-alt: #00C2A8;   /* Teal */
}
```

### Typography
The site uses:
- **DM Serif Display** — Headlines (Google Fonts)
- **Space Grotesk** — Body text (Google Fonts)

### Adding Tools
Copy a `.tool-row` block and edit:
```html
<article class="tool-row" data-category="writing">
    <div class="tool-rank">#9</div>
    ...
</article>
```

---

Built with 🧠 by humans. No AI-generated fluff.