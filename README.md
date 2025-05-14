# 🤷 Blame-as-a-Service

Ever needed someone to blame? Tired of taking responsibility for your own mistakes?  
This groundbreaking API returns random, creative, and hilariously implausible blame excuses — perfectly suited for any scenario: personal, professional, student life, dev life, or that time you "accidentally" ate your roommate's leftovers.

Built for developers, excuse-makers, and people who definitely didn't break the build.

> "60% of the time, it works every time!" - Blame Scientists

---

## 🚀 API Usage

**Base URL**
```
http://localhost:3000/blame
```

**Method:** `GET`  
**Rate Limit:** `120 requests per minute per IP`

### 🔄 Example Request
```http
GET /blame
```

### ✅ Example Responses

The API returns a different blame excuse each time. Here are some examples that definitely weren't used by our own developers:

```json
{
  "blame": "The office cat walked across the keyboard and accidentally deployed to production while simultaneously ordering 13 pizzas to the BOSS's house"
}
```

```json
{
  "blame": "We followed Stack Overflow advice from a question with -7 votes and marked as 'possible duplicate'"
}
```

```json
{
  "blame": "The developer was coding during a full moon while Mercury was in retrograde during a solar eclipse on Thursday the 15th"
}
```

```json
{
  "blame": "The intern thought 'rm -rf /' was the command to refresh the memory"
}
```

```json
{
  "blame": "Our AI pair programmer started hallucinating and insisted that indentations are optional in Python"
}
```

Use it in apps, bots, landing pages, Slack integrations, or whenever your manager asks why that critical feature is still "almost done" three sprints later.

---

## 🛠️ Self-Hosting (For When You Can't Blame Our Servers)

Want to run it yourself? It's lightweight, simple, and gives you someone else to blame when it inevitably crashes.

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/blame-as-a-service.git
cd blame-as-a-service
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the server
```bash
python blame_app.py
```

The API will be live at:
```
http://localhost:3000/blame
```

You can also change the port using an environment variable:
```bash
PORT=5000 python blame_app.py
```

### 4. API Documentation

FastAPI automatically generates interactive API documentation that's probably more reliable than your excuses. Once the server is running, you can access:

- Swagger UI: http://localhost:3000/docs (for the technically inclined)
- ReDoc: http://localhost:3000/redoc (for those who prefer their documentation pretty)

---

## 📁 Project Structure

```
blame-as-service/
├── blame_app.py        # FastAPI application (where the magic happens)
└── README.md           # The document you're reading instead of fixing bugs
```

## 🧠 Advanced Blame Optimization™

Our proprietary Blame Optimization Engine™ ensures maximum believability with minimum effort:

1. **Contextual Blame Adaptation**: Automatically adjusts excuses based on time of day (3 AM commits get special treatment)
2. **Blame Recycling**: Sustainable excuse generation that reuses old classics with fresh twists
3. **Plausible Deniability Index**: Each excuse is rated on a scale from "My dog ate my homework" to "Cosmic ray bit flip in the production database"

---

## 📦 requirements.txt

For reference, here's the dependency list:

```
fastapi==0.115.12
requests==2.32.3
slowapi==0.1.9
uvicorn==0.34.2
```

---

## ⚠️ Warning

Side effects may include: reduced accountability, suspicious looks from colleagues, and an inability to take anything seriously. Not recommended for use in court proceedings, performance reviews, or when explaining to your partner why you forgot your anniversary.

## 📄 License

MIT — do whatever you want, just don't blame yourself when you should be blaming others, especially the intern. The intern is always a safe choice. When in doubt, remember our company motto: "It wasn't me, it was probably Dave from DevOps."

> "I didn't write this README, my cat did." - The Developer, probably
