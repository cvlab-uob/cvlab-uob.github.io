---
layout: page
permalink: /analytics/
title: Analytics
description: Private site analytics dashboard
nav: false
---

<style>
    #login-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(255,255,255,0.97);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    #login-box {
        text-align: center;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.12);
        background: #fff;
        max-width: 360px;
        width: 90%;
    }
    #login-box h3 { margin-bottom: 1.2rem; font-weight: 700; }
    #login-box input[type="password"] {
        width: 100%;
        padding: 0.6rem 1rem;
        border: 1.5px solid #ccc;
        border-radius: 8px;
        font-size: 1rem;
        margin-bottom: 1rem;
        outline: none;
        transition: border 0.2s;
    }
    #login-box input[type="password"]:focus { border-color: #2563eb; }
    #login-box button {
        width: 100%;
        padding: 0.6rem;
        background: #2563eb;
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }
    #login-box button:hover { background: #1d4ed8; }
    #login-error { color: #dc2626; font-size: 0.9rem; margin-top: 0.5rem; display: none; }

    #dashboard { display: none; }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
    }
    .stat-card .stat-label {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 0.3rem;
        font-weight: 500;
    }
    .stat-card .stat-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
    }
    .analytics-section {
        margin-bottom: 2rem;
    }
    .analytics-section h4 {
        font-weight: 700;
        margin-bottom: 1rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #e2e8f0;
    }
    .country-table {
        width: 100%;
        border-collapse: collapse;
    }
    .country-table th, .country-table td {
        padding: 0.5rem 0.8rem;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
    }
    .country-table th {
        font-weight: 600;
        color: #475569;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .country-table tr:hover { background: #f1f5f9; }
    .country-bar {
        height: 8px;
        background: #2563eb;
        border-radius: 4px;
        display: inline-block;
        vertical-align: middle;
        min-width: 4px;
    }
    .pages-table {
        width: 100%;
        border-collapse: collapse;
    }
    .pages-table th, .pages-table td {
        padding: 0.5rem 0.8rem;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
    }
    .pages-table th {
        font-weight: 600;
        color: #475569;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .pages-table tr:hover { background: #f1f5f9; }
    .loading { text-align: center; color: #94a3b8; padding: 2rem; }
    .error-msg { color: #dc2626; text-align: center; padding: 1rem; }
    .dashboard-link {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.5rem 1.2rem;
        background: #f1f5f9;
        border-radius: 8px;
        color: #2563eb;
        text-decoration: none;
        font-weight: 500;
        transition: background 0.2s;
    }
    .dashboard-link:hover { background: #e2e8f0; }
    .refresh-btn {
        background: none;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 0.3rem 0.8rem;
        font-size: 0.85rem;
        color: #475569;
        cursor: pointer;
        float: right;
        transition: all 0.2s;
    }
    .refresh-btn:hover { border-color: #2563eb; color: #2563eb; }
    .date-range {
        margin-bottom: 1.5rem;
    }
    .date-range select {
        padding: 0.4rem 0.8rem;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        font-size: 0.9rem;
        color: #1e293b;
        background: #fff;
        cursor: pointer;
    }
</style>

<div id="login-overlay">
    <div id="login-box">
        <h3>🔒 Analytics Dashboard</h3>
        <p style="color:#64748b; margin-bottom:1.2rem;">Enter password to access</p>
        <input type="password" id="pwd-input" placeholder="Password" onkeydown="if(event.key==='Enter')checkPassword()">
        <button onclick="checkPassword()">Sign In</button>
        <p id="login-error">Incorrect password</p>
    </div>
</div>

<div id="dashboard">
    <div class="date-range">
        <label><strong>Period: </strong></label>
        <select id="date-range" onchange="loadDashboard()">
            <option value="7">Last 7 days</option>
            <option value="30" selected>Last 30 days</option>
            <option value="90">Last 90 days</option>
            <option value="365">Last year</option>
        </select>
        <button class="refresh-btn" onclick="loadDashboard()">↻ Refresh</button>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-label">Total Pageviews</div>
            <div class="stat-value" id="total-pageviews">—</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Unique Visitors</div>
            <div class="stat-value" id="total-visitors">—</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Countries</div>
            <div class="stat-value" id="total-countries">—</div>
        </div>
    </div>

    <div class="analytics-section">
        <h4>🌍 Visitors by Country</h4>
        <div id="country-data"><p class="loading">Loading...</p></div>
    </div>

    <div class="analytics-section">
        <h4>📄 Top Pages</h4>
        <div id="pages-data"><p class="loading">Loading...</p></div>
    </div>

    <p style="text-align:center; margin-top:2rem;">
        <a class="dashboard-link" href="https://{{ site.goatcounter_code }}.goatcounter.com" target="_blank">
            Open Full GoatCounter Dashboard →
        </a>
    </p>
</div>

<script>
const SITE_CODE = "{{ site.goatcounter_code }}";
const API_TOKEN = "{{ site.goatcounter_api_token }}";
const SITE_PASSWORD = "{{ site.analytics_password }}";

function checkPassword() {
    const input = document.getElementById('pwd-input').value;
    if (input === SITE_PASSWORD) {
        document.getElementById('login-overlay').style.display = 'none';
        document.getElementById('dashboard').style.display = 'block';
        sessionStorage.setItem('analytics_auth', 'true');
        loadDashboard();
    } else {
        document.getElementById('login-error').style.display = 'block';
        document.getElementById('pwd-input').value = '';
    }
}

// Auto-login if already authenticated in this session
if (sessionStorage.getItem('analytics_auth') === 'true') {
    document.getElementById('login-overlay').style.display = 'none';
    document.getElementById('dashboard').style.display = 'block';
    document.addEventListener('DOMContentLoaded', loadDashboard);
}

function getDateRange() {
    const days = parseInt(document.getElementById('date-range').value);
    const end = new Date();
    const start = new Date();
    start.setDate(end.getDate() - days);
    return {
        start: start.toISOString().split('T')[0],
        end: end.toISOString().split('T')[0]
    };
}

async function apiGet(endpoint, params = {}) {
    const range = getDateRange();
    const query = new URLSearchParams({ start: range.start, end: range.end, ...params });
    const url = `https://${SITE_CODE}.goatcounter.com/api/v0/${endpoint}?${query}`;
    const resp = await fetch(url, {
        headers: { 'Authorization': `Bearer ${API_TOKEN}` }
    });
    if (!resp.ok) throw new Error(`API error: ${resp.status}`);
    return resp.json();
}

async function loadDashboard() {
    loadTotal();
    loadLocations();
    loadPages();
}

async function loadTotal() {
    try {
        const data = await apiGet('stats/total');
        document.getElementById('total-pageviews').textContent =
            (data.total || 0).toLocaleString();
        document.getElementById('total-visitors').textContent =
            (data.total_unique || data.total_events || data.total || 0).toLocaleString();
    } catch (e) {
        document.getElementById('total-pageviews').textContent = '—';
        document.getElementById('total-visitors').textContent = '—';
        console.error('Total stats error:', e);
    }
}

async function loadLocations() {
    const container = document.getElementById('country-data');
    try {
        const data = await apiGet('stats/locations');
        const locations = data.stats || data.locations || data;
        if (!Array.isArray(locations) || locations.length === 0) {
            container.innerHTML = '<p class="loading">No country data yet</p>';
            document.getElementById('total-countries').textContent = '0';
            return;
        }

        // Sort by count descending
        locations.sort((a, b) => (b.count || 0) - (a.count || 0));
        const maxCount = locations[0].count || 1;
        document.getElementById('total-countries').textContent = locations.length;

        let html = '<table class="country-table"><thead><tr>';
        html += '<th>Country</th><th>Visitors</th><th style="width:40%"></th>';
        html += '</tr></thead><tbody>';

        locations.forEach(loc => {
            const name = loc.name || loc.location || loc.id || 'Unknown';
            const count = loc.count || 0;
            const pct = Math.max((count / maxCount) * 100, 2);
            html += `<tr>
                <td>${escapeHtml(name)}</td>
                <td><strong>${count.toLocaleString()}</strong></td>
                <td><span class="country-bar" style="width:${pct}%"></span></td>
            </tr>`;
        });

        html += '</tbody></table>';
        container.innerHTML = html;
    } catch (e) {
        container.innerHTML = `<p class="error-msg">Failed to load country data. Make sure GoatCounter is configured correctly.</p>`;
        document.getElementById('total-countries').textContent = '—';
        console.error('Locations error:', e);
    }
}

async function loadPages() {
    const container = document.getElementById('pages-data');
    try {
        const data = await apiGet('stats/hits', { limit: 20 });
        const paths = data.stats || data.hits || data.paths || data;
        if (!Array.isArray(paths) || paths.length === 0) {
            container.innerHTML = '<p class="loading">No page data yet</p>';
            return;
        }

        paths.sort((a, b) => (b.count || 0) - (a.count || 0));

        let html = '<table class="pages-table"><thead><tr>';
        html += '<th>Page</th><th>Pageviews</th>';
        html += '</tr></thead><tbody>';

        paths.slice(0, 20).forEach(p => {
            const path = p.path || p.name || p.id || '/';
            const count = p.count || 0;
            html += `<tr>
                <td><code>${escapeHtml(path)}</code></td>
                <td><strong>${count.toLocaleString()}</strong></td>
            </tr>`;
        });

        html += '</tbody></table>';
        container.innerHTML = html;
    } catch (e) {
        container.innerHTML = `<p class="error-msg">Failed to load page data. Make sure GoatCounter is configured correctly.</p>`;
        console.error('Pages error:', e);
    }
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}
</script>
