# 🤷 Blame-as-a-Service (BaaS)

Because it's NEVER your fault. Ever.

Tired of taking responsibility for your own mistakes? Need a scapegoat that isn't "the dog ate my homework" or "my grandmother died" (for the fifth time this year)? Our groundbreaking API returns random, creative, and hilariously implausible blame excuses — perfectly suited for any scenario where accountability is an inconvenience you'd rather avoid.

Built by developers who definitely didn't break the build, for developers who definitely won't break the build (but absolutely will).

> "I would've written a better quote, but my keyboard doesn't have the right keys for profound thoughts." - Blame Scientists

---

## 🚀 API Usage (For When You Need Someone to Blame ASAP)

**Base URL** (Point your finger here)
```
https://blame-as-a-service.onrender.com/blame
```

**Method:** `GET` (As in "GET me out of this situation")  
**Rate Limit:** `120 requests per minute per IP` (We know you mess up a lot, but come on)

### 🔄 Example Request
```http
GET /blame
```

### ✅ Example Responses (That We've Definitely Used Ourselves)

The API returns a different blame excuse each time, carefully crafted to maximize believability while minimizing your personal responsibility:

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

Use it whenever your manager asks why that critical feature is still "almost done" three sprints later, or when you need to explain why production is down at 3 AM (hint: it wasn't you, it was probably Dave from DevOps).

---

## 🛠️ Self-Hosting (For When You Can't Even Blame Our Servers)

Want to run it yourself? It's lightweight, simple, and gives you someone else to blame when it inevitably crashes. Plus, you can customize it to include your coworkers' names for extra realism!

### 1. Clone this repository (Blame Git if it fails)
```bash
git clone https://github.com/yourusername/blame-as-a-service.git
cd blame-as-a-service  # If you get lost here, blame your terminal
```

### 2. Install dependencies (Blame pip if anything breaks)
```bash
pip install -r requirements.txt  # If this fails, it's pip's fault, not yours
```

### 3. Start the server (And prepare your first excuse for when it crashes)
```bash
python blame_app.py  # If this fails, Python is clearly having a bad day
```

The API will be live at:
```
http://localhost:3000/blame  # If this doesn't work, blame your router
```

You can also change the port using an environment variable:
```bash
PORT=5000 python blame_app.py  # If this fails, blame environment variables for being too environmental
```

### 4. API Documentation (That Nobody Will Read Anyway)

FastAPI automatically generates interactive API documentation that's more reliable than your excuses:

- Swagger UI: http://localhost:3000/docs (for people who pretend to understand what they're looking at)
- ReDoc: http://localhost:3000/redoc (for those who prefer their documentation pretty but still won't read it)

---

## 📁 Project Structure (Simpler Than Your Excuses)

```
blame-as-service/
├── blame_app.py        # FastAPI application (where the magic happens)
└── README.md           # The document you're reading instead of fixing bugs
```

## 🧠 Advanced Blame Optimization™ (Patent Pending)

Our proprietary Blame Optimization Engine™ ensures maximum believability with minimum effort:

1. **Contextual Blame Adaptation**: Automatically adjusts excuses based on time of day (3 AM commits get special treatment because "I was tired" isn't creative enough)
2. **Blame Recycling**: Sustainable excuse generation that reuses old classics with fresh twists (environmentally friendly blaming)
3. **Plausible Deniability Index**: Each excuse is rated on a scale from "My dog ate my homework" to "Cosmic ray bit flip in the production database"
4. **Blame Deflection Technology**: Automatically identifies the most blame-worthy person in your organization (usually the intern or Dave from DevOps)
5. **Excuse Believability Algorithm**: Uses machine learning to generate excuses that sound just plausible enough that people might not question them

---

## 📦 requirements.txt (Things We Blame When Our Code Doesn't Work)

For reference, here's the dependency list:

```
fastapi==0.115.12      # We blame FastAPI when our routes don't work
requests==2.32.3       # We blame Requests when APIs don't respond
slowapi==0.1.9         # We blame SlowAPI when rate limiting breaks
uvicorn==0.34.2        # We blame Uvicorn when the server crashes
```

---

## ⚠️ Warning (The Only Time We Take Responsibility)

Side effects may include: reduced accountability, suspicious looks from colleagues, an inability to take anything seriously, and a strange compulsion to blame inanimate objects for your problems. Not recommended for use in court proceedings, performance reviews, or when explaining to your partner why you forgot your anniversary (though we've tried).

## 📄 License

MIT — do whatever you want with this code, just don't blame yourself when you should be blaming others. When in doubt, remember our company motto: "It wasn't me, it was probably Dave from DevOps." The intern is always a safe choice too. Or Mercury being in retrograde. Or cosmic rays. Or that weird bug that only happens on Tuesdays.

> "I didn't write this README, my cat did while Mercury was in retrograde during a solar eclipse on a Thursday." - The Developer, definitely not taking responsibility
