# 🎯 Blame-as-a-Service (BaaS) v2.0

![Blame-as-a-Service](./media/Blame-as-a-Service.png)

<div align="center">

### Because it's NEVER your fault. Ever.

[![API Status](https://img.shields.io/badge/API-Operational-success?style=for-the-badge)](https://baas.budhathokisagar.com.np)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-00C7B7?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

**100+ Excuses** • **10 Categories** • **ASCII Art** • **Severity Ratings** • **Interactive Demo**

[Live Demo](https://baas.budhathokisagar.com.np/demo) • [API Docs](https://baas.budhathokisagar.com.np/docs) • [Report Bug](https://github.com/sbmagar13/blame-as-a-service/issues)

</div>

---

## 🌟 What's New in v2.0

- 🎨 **ASCII Art Display** - 4 visualization styles (Box, Banner, Simple, Dramatic)
- 📊 **Severity Levels** - Minor 🟢, Moderate 🟡, Catastrophic 🔴
- 🗂️ **10 Categories** - Cosmic, Technical, Management, AI/ML, Cloud, Security & more
- 💎 **Rich Details** - Quality scores, believability ratings, visual elements
- 🎭 **100+ Excuses** - Carefully crafted blame excuses
- 🎰 **Blame Roulette** - Get multiple excuses at once
- 🌐 **Interactive Demo** - Web UI with animations and confetti

---

## 🚀 Quick Start

```bash
# Random blame excuse
curl https://baas.budhathokisagar.com.np/blame

# Epic ASCII art format
curl https://baas.budhathokisagar.com.np/blame/ascii?style=dramatic

# Blame from specific category
curl https://baas.budhathokisagar.com.np/blame/category/cosmic

# Multiple blames
curl https://baas.budhathokisagar.com.np/blame/multiple?count=5
```

---

## 📖 API Reference

**Base URL:** `https://baas.budhathokisagar.com.np`  
**Rate Limit:** 120 requests/minute/IP

### Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /blame` | Random blame excuse with category & severity |
| `GET /blame/rich` | Excuse with quality scores & detailed severity info |
| `GET /blame/ascii` | ASCII art format (`?style=box\|banner\|simple\|dramatic`) |
| `GET /blame/category/{category}` | Blame from specific category |
| `GET /blame/severity/{severity}` | Blame by severity (minor, moderate, catastrophic) |
| `GET /blame/multiple` | Multiple excuses (`?count=3`, max 10) |
| `GET /categories` | List all categories |
| `GET /severity-info` | Severity level details |
| `GET /stats` | API statistics |
| `GET /health` | Health check |

### Example Responses

**`GET /blame`**
```json
{
  "blame": "The developer was coding during a full moon while Mercury was in retrograde",
  "category": "cosmic",
  "severity": "catastrophic"
}
```

**`GET /blame/rich`**
```json
{
  "blame": "Our AI pair programmer started hallucinating...",
  "category": "ai_modern",
  "severity": {
    "level": "catastrophic",
    "emoji": "🔴",
    "name": "CATASTROPHIC DISASTER",
    "bar": "▓▓▓▓▓▓▓▓▓▓ 100% 🔥💀🔥"
  },
  "quality_score": 9,
  "believability": 7
}
```

---

## 📂 Categories

| Category | Description |
|----------|-------------|
| 🌌 `cosmic` | Mercury retrograde, solar eclipses, cosmic rays |
| 💻 `technical` | Stack Overflow, database naps, race conditions |
| 👔 `management` | Pivots, CEO dreams, TED talks |
| 👥 `team` | Interns, breakups, coffee breaks |
| 🌍 `environmental` | Office cats, thermostat, feng shui |
| 📜 `legacy` | COBOL scripts, time bombs from 2008 |
| 👤 `user` | Bobby Tables, refresh enthusiasts |
| 🤖 `ai_modern` | Hallucinating models, sentient deployments |
| ☁️ `cloud` | AWS surprises, serverless rebellion |
| 🔐 `security` | password123, ROT13 encryption |

---

## 🛠️ Self-Hosting

```bash
git clone https://github.com/sbmagar13/blame-as-a-service.git
cd blame-as-a-service
pip install -r requirements.txt
python blame_app.py
```

**Endpoints:** `http://localhost:3000/blame` • `/demo` • `/docs`

```
blame-as-a-service/
├── blame_app.py          # FastAPI application
├── blame_data.py         # 100+ excuses by category & severity
├── blame_visualizer.py   # ASCII art generators
├── static/demo.html      # Interactive web demo
└── requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Add excuses to `blame_data.py`
3. Test with `python blame_app.py`
4. Submit PR (bonus: blame someone in the description)

---

## 📄 License

MIT — Do whatever you want, just don't blame yourself.

> "It wasn't me, it was probably Dave from DevOps."

---

<div align="center">

**Made with 💀 by developers who definitely didn't break production**

[Live Demo](https://baas.budhathokisagar.com.np/demo) • [API Docs](https://baas.budhathokisagar.com.np/docs) • [GitHub](https://github.com/sbmagar13/blame-as-a-service)

</div>
