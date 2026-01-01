import os
import random
from typing import Optional, List
from fastapi import FastAPI, Request, Response, status, Query
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import uvicorn

# Import our blame data and visualizer
from blame_data import (
    ALL_EXCUSES, BLAME_EXCUSES, CATEGORIES,
    SEVERITY_INFO
)
from blame_visualizer import (
    format_blame_ascii, format_blame_rich,
    create_blame_meter, create_multi_blame_display
)

# Initialize FastAPI app
app = FastAPI(
    title="🎯 Blame-as-a-Service",
    description="""
    ## Because it's NEVER your fault. Ever.

    The ultimate API for creative accountability evasion. Get professional-grade blame excuses
    with categorization, severity ratings, and epic ASCII art formatting.

    ### Features
    - 🎨 **ASCII Art Display**: Multiple visual styles for maximum dramatic effect
    - 📊 **Severity Levels**: From "Minor Oopsie" to "Catastrophic Disaster"
    - 🗂️ **10+ Categories**: Cosmic, Technical, Management, AI/ML, and more
    - 🎰 **Randomization**: Never get the same excuse twice (probably)
    - 🎭 **100+ Excuses**: Carefully crafted for maximum believability

    Built by developers who definitely didn't break the build, for developers who definitely won't.
    """,
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure rate limiter: 120 requests per minute per IP
limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Mount static files for demo page
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except:
    pass  # Static directory might not exist yet


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root():
    """Redirect to demo page or docs"""
    return """
    <html>
        <head>
            <title>Blame-as-a-Service</title>
            <style>
                body {
                    font-family: 'Courier New', monospace;
                    background: #1a1a1a;
                    color: #00ff00;
                    padding: 50px;
                    text-align: center;
                }
                h1 { font-size: 3em; margin-bottom: 20px; }
                a { color: #00ff00; text-decoration: none; padding: 10px 20px;
                    border: 2px solid #00ff00; margin: 10px; display: inline-block; }
                a:hover { background: #00ff00; color: #1a1a1a; }
                .blame { background: #2a2a2a; padding: 20px; margin: 30px auto;
                         max-width: 600px; border: 2px solid #00ff00; }
            </style>
        </head>
        <body>
            <h1>🎯 BLAME-AS-A-SERVICE 🎯</h1>
            <p style="font-size: 1.2em;">Because it's NEVER your fault. Ever.</p>
            <div class="blame">
                <p>"The developer was coding during a full moon while Mercury was in retrograde
                   during a solar eclipse on Thursday the 13th"</p>
            </div>
            <div>
                <a href="/docs">📚 API Documentation</a>
                <a href="/demo">🎨 Live Demo</a>
                <a href="/blame">🎲 Random Blame</a>
            </div>
        </body>
    </html>
    """


@app.get("/demo", response_class=HTMLResponse, include_in_schema=False)
async def demo_page():
    """Serve the interactive demo page"""
    try:
        with open("static/demo.html", "r") as f:
            return f.read()
    except:
        return "<h1>Demo page not found. Make sure static/demo.html exists.</h1>"


@app.get("/blame",
         summary="Get a random blame excuse",
         description="Returns a random blame excuse from our extensive library")
@limiter.limit("120/minute")
async def get_blame(request: Request):
    """Get a random blame excuse (simple format)"""
    excuse = random.choice(ALL_EXCUSES)
    return {
        "blame": excuse["blame"],
        "category": excuse["category"],
        "severity": excuse["severity"]
    }


@app.get("/blame/rich",
         summary="Get a blame excuse with rich details",
         description="Returns a blame excuse with severity info, quality scores, and visual elements")
@limiter.limit("120/minute")
async def get_blame_rich(request: Request):
    """Get a blame excuse with full visual details"""
    excuse = random.choice(ALL_EXCUSES)
    return format_blame_rich(excuse)


@app.get("/blame/ascii",
         response_class=PlainTextResponse,
         summary="Get a blame excuse in epic ASCII art",
         description="Returns a blame excuse formatted as beautiful ASCII art")
@limiter.limit("120/minute")
async def get_blame_ascii(
    request: Request,
    style: str = Query("box", description="ASCII style: box, banner, simple, dramatic")
):
    """Get a blame excuse as ASCII art"""
    excuse = random.choice(ALL_EXCUSES)
    return format_blame_ascii(excuse, style=style)


@app.get("/blame/category/{category}",
         summary="Get a blame excuse from a specific category",
         description="Returns a random blame excuse from the specified category")
@limiter.limit("120/minute")
async def get_blame_by_category(request: Request, category: str):
    """Get a blame excuse from a specific category"""
    category = category.lower()

    if category not in CATEGORIES:
        return JSONResponse(
            status_code=404,
            content={
                "error": f"Category '{category}' not found",
                "available_categories": CATEGORIES
            }
        )

    # Get all excuses from this category
    category_excuses = []
    for severity, excuses in BLAME_EXCUSES[category].items():
        for excuse in excuses:
            category_excuses.append({
                "blame": excuse,
                "category": category,
                "severity": severity
            })

    excuse = random.choice(category_excuses)
    return excuse


@app.get("/blame/severity/{severity}",
         summary="Get a blame excuse by severity level",
         description="Returns a random blame excuse of the specified severity (minor, moderate, catastrophic)")
@limiter.limit("120/minute")
async def get_blame_by_severity(request: Request, severity: str):
    """Get a blame excuse by severity level"""
    severity = severity.lower()

    if severity not in ["minor", "moderate", "catastrophic"]:
        return JSONResponse(
            status_code=404,
            content={
                "error": f"Severity '{severity}' not found",
                "available_severities": ["minor", "moderate", "catastrophic"]
            }
        )

    # Filter excuses by severity
    severity_excuses = [e for e in ALL_EXCUSES if e["severity"] == severity]
    excuse = random.choice(severity_excuses)

    return excuse


@app.get("/blame/multiple",
         summary="Get multiple random blame excuses",
         description="Returns multiple blame excuses for extra coverage")
@limiter.limit("120/minute")
async def get_multiple_blames(
    request: Request,
    count: int = Query(3, ge=1, le=10, description="Number of excuses (1-10)")
):
    """Get multiple random blame excuses"""
    excuses = random.sample(ALL_EXCUSES, min(count, len(ALL_EXCUSES)))
    return {
        "count": len(excuses),
        "blames": excuses
    }


@app.get("/blame/multiple/ascii",
         response_class=PlainTextResponse,
         summary="Get multiple blame excuses in ASCII format",
         description="Returns multiple blame excuses as a formatted ASCII display")
@limiter.limit("120/minute")
async def get_multiple_blames_ascii(
    request: Request,
    count: int = Query(3, ge=1, le=10, description="Number of excuses (1-10)")
):
    """Get multiple random blame excuses as ASCII art"""
    excuses = random.sample(ALL_EXCUSES, min(count, len(ALL_EXCUSES)))
    return create_multi_blame_display(excuses)


@app.get("/categories",
         summary="List all available blame categories",
         description="Returns a list of all excuse categories available")
async def get_categories():
    """Get all available categories"""
    return {
        "categories": CATEGORIES,
        "count": len(CATEGORIES)
    }


@app.get("/severity-info",
         summary="Get information about severity levels",
         description="Returns details about all severity levels and their meanings")
async def get_severity_info():
    """Get information about severity levels"""
    return {
        "severity_levels": SEVERITY_INFO,
        "description": "Severity indicates how bad your situation is, from Minor Oopsie to Catastrophic Disaster"
    }


@app.get("/stats",
         summary="Get API statistics",
         description="Returns statistics about the excuse database")
async def get_stats():
    """Get API statistics"""
    category_counts = {}
    severity_counts = {"minor": 0, "moderate": 0, "catastrophic": 0}

    for excuse in ALL_EXCUSES:
        category = excuse["category"]
        severity = excuse["severity"]

        category_counts[category] = category_counts.get(category, 0) + 1
        severity_counts[severity] += 1

    return {
        "total_excuses": len(ALL_EXCUSES),
        "categories": len(CATEGORIES),
        "category_breakdown": category_counts,
        "severity_breakdown": severity_counts,
        "rate_limit": "120 requests per minute per IP",
        "version": "2.0.0"
    }


@app.get("/health",
         summary="Health check endpoint",
         description="Check if the API is running")
async def health_check():
    """Health check"""
    return {
        "status": "operational",
        "message": "Blame service is running smoothly (unlike your code)",
        "version": "2.0.0"
    }


# Error handler for rate limiting
@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={
            "error": "Too many requests, please try again later",
            "blame": "You're making too many mistakes too quickly. Even we can't keep up.",
            "rate_limit": "120 requests per minute per IP"
        }
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"""
    ╔═══════════════════════════════════════════════════════════════╗
    ║          🎯 BLAME-AS-A-SERVICE v2.0.0 🎯                      ║
    ║                                                               ║
    ║  Running on: http://localhost:{port:<43} ║
    ║  Docs: http://localhost:{port}/docs{' ' * 35} ║
    ║  Demo: http://localhost:{port}/demo{' ' * 35} ║
    ║                                                               ║
    ║  Because it's NEVER your fault. Ever.                        ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    uvicorn.run("blame_app:app", host="0.0.0.0", port=port, reload=True)
