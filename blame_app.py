import os
import random
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Blame-as-a-Service",
    description="A lightweight API that returns funny and ridiculous blame excuses.",
    version="1.0.0"
)

# Configure rate limiter: 120 requests per minute per IP
limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# List of funny blame excuses
BLAME_EXCUSES = [
    "It was the intern who thought 'rm -rf /' was a cleaning command",
    "The office cat walked across the keyboard and accidentally deployed to production",
    "Mercury is in retrograde, which affected our database queries",
    "The code worked on my machine, so it must be the server's fault",
    "The cloud must have been raining on our servers",
    "Our AI became sentient and decided it didn't like that feature",
    "The developer was coding during a full moon",
    "The bug was a feature all along, you just didn't appreciate it",
    "The previous developer left a time bomb in the code",
    "The QA team was on a coffee break when this slipped through",
    "The documentation said it was supposed to work that way",
    "It's not a bug, it's an undocumented feature",
    "The client kept changing requirements faster than we could implement them",
    "The project manager said 'ship it' before we were ready",
    "The CEO's kid suggested that change during 'Bring Your Child to Work Day'",
    "We outsourced that module to a team of monkeys with typewriters",
    "The code was written during a hackathon fueled by energy drinks and pizza",
    "The developer was going through a breakup when they wrote that function",
    "Our most experienced developer was on vacation when that decision was made",
    "The Wi-Fi was spotty that day, so Git commits got mixed up",
    "The server hamsters got tired and needed a break",
    "We followed Stack Overflow advice without reading the comments",
    "The algorithm was designed by throwing darts at a flowchart",
    "The third-party API changed without warning (as they always do)",
    "The developer thought 'temporary fix' meant it would fix itself eventually",
    "The database decided to take a nap at the worst possible moment",
    "The code comments were more aspirational than factual",
    "We inherited that code from a startup we acquired (that went bankrupt)",
    "The developer who wrote that code now works for our competitor",
    "The user didn't follow the instructions that we never wrote",
    "The stars weren't aligned for successful deployment",
    "The office plants weren't watered, affecting the team's oxygen levels and decision-making",
    "The coffee machine broke, causing a 50% decrease in coding ability",
    "We were using the wrong version of the wrong framework",
    "The developer's horoscope said 'take risks' that day",
    "The whiteboard markers were running low, so we couldn't properly design the architecture",
    "The office feng shui was disrupted by a new water cooler placement",
    "We were trying to be 'innovative' and 'disruptive'",
    "The product owner insisted it would be fine without testing",
    "The standup meeting ran long, cutting into actual work time",
    "The team was distracted by a heated debate about tabs vs. spaces",
    "The code review was conducted over lunch when everyone was hangry",
    "The developer was using a keyboard with a sticky spacebar",
    "The version control system was having an existential crisis",
    "The algorithm was inspired by a dream the developer had",
    "We were following the principle of 'move fast and break things' too literally",
    "The user story was written in interpretive dance and something got lost in translation",
    "The sprint planning session was interrupted by a fire drill",
    "The developer was listening to the wrong genre of music for optimal coding",
    "The office thermostat was set too high, melting our logical thinking"
]

# Blame endpoint
@app.get("/blame")
@limiter.limit("120/minute")
async def get_blame(request: Request):
    # Choose a random blame excuse
    blame = random.choice(BLAME_EXCUSES)
    return {"blame": blame}

# Error handler for rate limiting
@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={"error": "Too many requests, please try again later. (120 reqs/min/IP)"}
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"Blame-as-a-Service is running on port {port}")
    uvicorn.run("blame_app:app", host="0.0.0.0", port=port, reload=True)
