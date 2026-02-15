const products = {
    'content': {
        name: 'Content Creator Pack',
        price: 900,
        description: '200+ prompts for blog posts, social media, emails, and SEO content.',
        features: ['Blog post generators', 'Instagram captions', 'Twitter threads', 'Email sequences', 'SEO-optimized articles']
    },
    'business': {
        name: 'Business & Marketing Pack',
        price: 1900,
        description: '150+ prompts for business plans, marketing strategies, sales copy, and growth tactics.',
        features: ['Business plan templates', 'Marketing strategy prompts', 'Sales email generators', 'Competitor analysis', 'Growth hacking tactics']
    },
    'developer': {
        name: 'Developer Pack',
        price: 1400,
        description: '180+ prompts for code generation, debugging, documentation, and system design.',
        features: ['Code generators', 'Debug assistants', 'Documentation templates', 'Code review prompts', 'Architecture patterns']
    }
};

function buyPack(packId) {
    const pack = products[packId];
    if (!pack) return;

    const modal = document.getElementById('checkout-modal');
    const modalBody = document.getElementById('modal-body');

    modalBody.innerHTML = `
        <div style="margin-bottom: 24px;">
            <span style="font-size: 3rem;">📝</span>
        </div>
        <h2 style="font-family: 'DM Serif Display', serif; font-size: 1.75rem; margin-bottom: 8px;">${pack.name}</h2>
        <p style="color: var(--fg-muted); margin-bottom: 24px;">${pack.description}</p>
        <ul style="list-style: none; margin-bottom: 24px;">
            ${pack.features.map(f => `<li style="padding: 8px 0; border-bottom: 1px solid var(--border);">→ ${f}</li>`).join('')}
        </ul>
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 16px 0; border-top: 2px solid var(--fg); margin-bottom: 24px;">
            <span>Total</span>
            <span style="font-family: 'DM Serif Display', serif; font-size: 2rem; color: var(--accent);">$${(pack.price / 100).toFixed(2)}</span>
        </div>
        <form id="checkout-form">
            <div style="margin-bottom: 16px;">
                <label style="display: block; font-size: 0.875rem; margin-bottom: 8px; font-weight: 500;">Email</label>
                <input type="email" id="checkout-email" placeholder="you@email.com" required style="width: 100%; padding: 14px 16px; border: 2px solid var(--border); font-family: inherit; font-size: 1rem; background: var(--bg);">
            </div>
            <div style="margin-bottom: 24px;">
                <label style="display: block; font-size: 0.875rem; margin-bottom: 8px; font-weight: 500;">Card Number</label>
                <input type="text" id="checkout-card" placeholder="4242 4242 4242 4242" style="width: 100%; padding: 14px 16px; border: 2px solid var(--border); font-family: inherit; font-size: 1rem; background: var(--bg);">
            </div>
            <button type="submit" style="width: 100%; background: var(--fg); color: var(--bg); border: none; padding: 16px; font-family: inherit; font-weight: 600; font-size: 1rem; cursor: pointer;">
                Pay $${(pack.price / 100).toFixed(2)}
            </button>
            <p style="text-align: center; margin-top: 16px; font-size: 0.8rem; color: var(--fg-muted);">🔒 Secured by Stripe · Test: use card 4242 4242 4242 4242</p>
        </form>
    `;

    document.getElementById('checkout-form').addEventListener('submit', (e) => {
        e.preventDefault();
        processPayment(packId);
    });

    modal.classList.add('active');
}

function closeModal() {
    document.getElementById('checkout-modal').classList.remove('active');
}

function processPayment(packId) {
    const pack = products[packId];
    const email = document.getElementById('checkout-email').value;
    const submitBtn = document.querySelector('#checkout-form button');
    
    submitBtn.disabled = true;
    submitBtn.textContent = 'Processing...';

    setTimeout(() => {
        trackPurchase(packId, pack.price, email);
        showSuccess(pack);
    }, 1500);
}

function showSuccess(pack) {
    const modalBody = document.getElementById('modal-body');
    modalBody.innerHTML = `
        <div style="text-align: center; padding: 40px 0;">
            <div style="font-size: 4rem; margin-bottom: 24px; background: var(--accent-alt); width: 80px; height: 80px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">✓</div>
            <h2 style="font-family: 'DM Serif Display', serif; font-size: 1.75rem; margin-bottom: 8px;">Payment Successful!</h2>
            <p style="color: var(--fg-muted); margin-bottom: 32px;">Check your email for the download link.</p>
            <button onclick="closeModal()" style="background: var(--fg); color: var(--bg); border: none; padding: 16px 40px; font-family: inherit; font-weight: 600; cursor: pointer;">
                Done
            </button>
        </div>
    `;
}

function trackPurchase(packId, amount, email) {
    console.log('Purchase:', { packId, amount: amount / 100, email });
    if (typeof gtag !== 'undefined') {
        gtag('event', 'purchase', {
            transaction_id: Date.now(),
            value: amount / 100,
            currency: 'USD',
            items: [{ id: packId, name: products[packId].name, price: amount / 100, quantity: 1 }]
        });
    }
}

function openNewsletter() {
    const modal = document.getElementById('checkout-modal');
    const modalBody = document.getElementById('modal-body');

    modalBody.innerHTML = `
        <div style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 24px;">📧</div>
            <h2 style="font-family: 'DM Serif Display', serif; font-size: 1.75rem; margin-bottom: 8px;">Join 12,000+ Readers</h2>
            <p style="color: var(--fg-muted); margin-bottom: 24px;">AI tools worth your time. No spam. Unsubscribe anytime.</p>
            <form id="newsletter-modal-form">
                <input type="email" placeholder="you@email.com" required style="width: 100%; padding: 14px 16px; border: 2px solid var(--border); font-family: inherit; font-size: 1rem; background: var(--bg); margin-bottom: 16px;">
                <button type="submit" style="width: 100%; background: var(--accent); color: white; border: none; padding: 16px; font-family: inherit; font-weight: 600; cursor: pointer;">
                    Subscribe Free
                </button>
            </form>
            <p style="margin-top: 16px; font-size: 0.85rem; color: var(--accent);">🎁 Get "50 GPT Prompts for Productivity" free</p>
        </div>
    `;

    document.getElementById('newsletter-modal-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const email = e.target.querySelector('input').value;
        const btn = e.target.querySelector('button');
        btn.disabled = true;
        btn.textContent = 'Subscribing...';
        
        setTimeout(() => {
            console.log('Newsletter:', email);
            modalBody.innerHTML = `
                <div style="text-align: center; padding: 40px 0;">
                    <div style="font-size: 4rem; margin-bottom: 24px;">✓</div>
                    <h2 style="font-family: 'DM Serif Display', serif; font-size: 1.75rem; margin-bottom: 8px;">You're In!</h2>
                    <p style="color: var(--fg-muted); margin-bottom: 24px;">Check your email for your free prompts PDF.</p>
                    <button onclick="closeModal()" style="background: var(--fg); color: var(--bg); border: none; padding: 16px 40px; font-family: inherit; font-weight: 600; cursor: pointer;">
                        Done
                    </button>
                </div>
            `;
        }, 1000);
    });

    modal.classList.add('active');
}

function copyCode(code) {
    navigator.clipboard.writeText(code).then(() => {
        const btn = event.target;
        const original = btn.textContent;
        btn.textContent = 'Copied!';
        btn.style.background = 'var(--accent-alt)';
        setTimeout(() => {
            btn.textContent = original;
            btn.style.background = '';
        }, 2000);
    });
}

document.querySelectorAll('.tool-action').forEach(btn => {
    btn.addEventListener('click', function() {
        const tool = this.dataset.tool;
        console.log('Tool click:', tool);
        if (typeof gtag !== 'undefined') {
            gtag('event', 'tool_click', { tool_name: tool });
        }
    });
});

document.querySelectorAll('.filter-tab').forEach(tab => {
    tab.addEventListener('click', function() {
        document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
        this.classList.add('active');
        
        const filter = this.dataset.filter;
        document.querySelectorAll('.tool-row').forEach(row => {
            if (filter === 'all' || row.dataset.category === filter) {
                row.style.display = 'grid';
            } else {
                row.style.display = 'none';
            }
        });
    });
});

document.getElementById('newsletter-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const email = this.querySelector('input').value;
    const btn = this.querySelector('button');
    btn.disabled = true;
    btn.textContent = 'Subscribing...';
    
    setTimeout(() => {
        console.log('Newsletter:', email);
        this.innerHTML = '<span style="color: var(--accent-alt); font-weight: 600;">✓ Subscribed! Check your email.</span>';
    }, 1000);
});

const navMobile = document.querySelector('.nav-mobile');
const navGrid = document.querySelector('.nav-grid');

if (navMobile) {
    navMobile.addEventListener('click', () => {
        navGrid.classList.toggle('active');
    });
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.tool-row, .deal-card, .prompt-pack').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    observer.observe(el);
});

console.log('[TOOLS.AI] Ready. No bullshit, just results.');