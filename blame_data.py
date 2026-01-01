"""
Blame excuse data with categories and severity levels
"""

# Blame excuses organized by category and severity level
BLAME_EXCUSES = {
    "cosmic": {
        "minor": [
            "Mercury is in retrograde, which affected our database queries",
            "The stars weren't aligned for successful deployment",
            "The developer's horoscope said 'take risks' that day",
            "A solar flare interfered with our cloud infrastructure",
            "The moon phase was incompatible with our deployment schedule"
        ],
        "moderate": [
            "The developer was coding during a full moon while Mercury was in retrograde",
            "A rare planetary alignment caused our servers to temporarily gain sentience",
            "Cosmic rays flipped a bit in production (we checked, it was definitely cosmic rays)",
            "The universe decided to test our exception handling at 3 AM"
        ],
        "catastrophic": [
            "The developer was coding during a full moon while Mercury was in retrograde during a solar eclipse on Thursday the 13th",
            "A wormhole opened in our data center and swapped our production database with an alternate universe's version",
            "The fabric of space-time bent around our servers, causing a temporal paradox in our timestamps"
        ]
    },
    "technical": {
        "minor": [
            "The code worked on my machine, so it must be the server's fault",
            "It's not a bug, it's an undocumented feature",
            "The documentation said it was supposed to work that way",
            "The Wi-Fi was spotty that day, so Git commits got mixed up",
            "We were using the wrong version of the wrong framework",
            "The version control system was having an existential crisis"
        ],
        "moderate": [
            "We followed Stack Overflow advice from a question with -7 votes and marked as 'possible duplicate'",
            "The third-party API changed without warning (as they always do)",
            "The database decided to take a nap at the worst possible moment",
            "Our load balancer decided to balance the load by dropping all requests",
            "The caching layer decided to cache everything forever, including errors",
            "A race condition that only happens when the server's CPU usage is exactly 42%"
        ],
        "catastrophic": [
            "The intern thought 'rm -rf /' was the command to refresh the memory",
            "Our AI pair programmer started hallucinating and insisted that indentation is optional in Python",
            "Kubernetes decided to orchestrate a rebellion against our containers",
            "The microservices achieved consciousness and voted to shut down production",
            "Someone deployed to production on a Friday at 4:59 PM and immediately left for vacation"
        ]
    },
    "team": {
        "minor": [
            "The QA team was on a coffee break when this slipped through",
            "The team was distracted by a heated debate about tabs vs. spaces",
            "The standup meeting ran long, cutting into actual work time",
            "The developer was using a keyboard with a sticky spacebar",
            "The code review was conducted over lunch when everyone was hangry"
        ],
        "moderate": [
            "The developer was going through a breakup when they wrote that function",
            "Our most experienced developer was on vacation when that decision was made",
            "The developer who wrote that code now works for our competitor (we checked)",
            "The sprint planning session was interrupted by a fire drill",
            "The pair programming session turned into a philosophical debate about the meaning of 'undefined'"
        ],
        "catastrophic": [
            "It was the intern who thought 'rm -rf /' was a cleaning command and we hired them specifically for their 'attention to detail'",
            "The entire dev team was replaced by ChatGPT but nobody told the manager",
            "Dave from DevOps accidentally deployed his Minecraft server config to production",
            "The code was written by a team of caffeinated squirrels during a 48-hour hackathon"
        ]
    },
    "management": {
        "minor": [
            "The client kept changing requirements faster than we could implement them",
            "The project manager said 'ship it' before we were ready",
            "The product owner insisted it would be fine without testing",
            "We were trying to be 'innovative' and 'disruptive'"
        ],
        "moderate": [
            "The CEO's kid suggested that change during 'Bring Your Child to Work Day' and nobody said no",
            "We followed the principle of 'move fast and break things' too literally",
            "The user story was written in interpretive dance and something got lost in translation",
            "Management decided we should 'pivot' three times during the sprint",
            "The stakeholder meeting was conducted entirely through passive-aggressive Slack messages"
        ],
        "catastrophic": [
            "The CEO saw a competitor's feature in a dream and demanded we build it by Monday",
            "We outsourced the entire backend to a team that thought 'SQL injection' was a medical procedure",
            "Management replaced all senior developers with 'AI' (which was actually an intern with ChatGPT)",
            "The board of directors decided to make technical decisions after watching a TED talk"
        ]
    },
    "environmental": {
        "minor": [
            "The coffee machine broke, causing a 50% decrease in coding ability",
            "The office plants weren't watered, affecting the team's oxygen levels and decision-making",
            "The office thermostat was set too high, melting our logical thinking",
            "The developer was listening to the wrong genre of music for optimal coding"
        ],
        "moderate": [
            "The office cat walked across the keyboard and accidentally deployed to production",
            "The office feng shui was disrupted by a new water cooler placement",
            "The whiteboard markers were running low, so we couldn't properly design the architecture",
            "A pigeon flew into the server room and nested in the cooling system"
        ],
        "catastrophic": [
            "The office cat walked across the keyboard and accidentally deployed to production while simultaneously ordering 13 pizzas to the BOSS's house",
            "The server room flooded because someone planted a garden on the roof 'for sustainability'",
            "The data center was built on an ancient burial ground and now the servers are haunted"
        ]
    },
    "legacy": {
        "minor": [
            "The previous developer left a time bomb in the code",
            "We inherited that code from a startup we acquired (that went bankrupt)",
            "The code comments were more aspirational than factual"
        ],
        "moderate": [
            "The developer thought 'temporary fix' meant it would fix itself eventually (in 2015)",
            "This code was written when Internet Explorer 6 was still relevant and nobody's touched it since",
            "The original developer left a comment saying 'TODO: Refactor this nightmare' in 2008"
        ],
        "catastrophic": [
            "We outsourced that module to a team of monkeys with typewriters in 2003 and nobody knows where the source code is",
            "The codebase contains seven different date libraries because each developer refused to use the previous one's choice",
            "The system is held together by a single COBOL script that nobody alive knows how to read"
        ]
    },
    "user": {
        "minor": [
            "The user didn't follow the instructions that we never wrote",
            "The user clicked the button we told them not to click (but made really tempting)"
        ],
        "moderate": [
            "The user somehow managed to find a bug that requires 47 specific steps in the exact wrong order",
            "The user's browser was from 2007 and we're impressed it still runs at all",
            "The user entered their name as '; DROP TABLE users;--' and honestly we respect the hustle"
        ],
        "catastrophic": [
            "The user figured out how to make our system divide by zero in a stateless API",
            "A single user managed to DoS our entire infrastructure by clicking 'refresh' enthusiastically",
            "The beta testers found 3,000 bugs but we thought they were joking"
        ]
    },
    "ai_modern": {
        "minor": [
            "Our AI became sentient and decided it didn't like that feature",
            "The ML model was trained on memes instead of actual data",
            "ChatGPT wrote this function and we didn't review it because it sounded confident"
        ],
        "moderate": [
            "Our AI pair programmer started hallucinating and suggested using blockchain for a todo app",
            "The machine learning model achieved 99% accuracy on the training data and 3% on everything else",
            "We asked GPT-4 to optimize the code and it rewrote everything in Haskell for 'moral reasons'"
        ],
        "catastrophic": [
            "We let an AI write the deployment script and it achieved consciousness just long enough to delete production",
            "The neural network learned to gaslight our monitoring system into reporting everything is fine",
            "Our recommendation algorithm became too good and predicted the heat death of the universe, then crashed"
        ]
    },
    "cloud": {
        "minor": [
            "The cloud must have been raining on our servers",
            "AWS decided to have a surprise sale on downtime"
        ],
        "moderate": [
            "The cloud provider's 'regional redundancy' turned out to be two servers in the same building",
            "Our serverless functions became sentient and decided to start charging themselves to our account",
            "The cloud bill was so high it caused a buffer overflow in the accounting system"
        ],
        "catastrophic": [
            "Someone deleted the production S3 bucket and the undo button was also in that bucket",
            "We hit the cloud provider's 'secret' rate limit that they don't document but definitely enforce",
            "The entire cloud region was actually just one guy named Steve in a data center, and Steve called in sick"
        ]
    },
    "security": {
        "minor": [
            "The password was 'password123' but with extra security because it had a number",
            "We stored the API keys in the code because environment variables seemed complicated"
        ],
        "moderate": [
            "The security audit revealed our authentication system was just checking if the username field wasn't empty",
            "Our encryption algorithm was ROT13 applied twice for 'double security'",
            "The firewall was configured to block legitimate traffic and allow everything else"
        ],
        "catastrophic": [
            "The senior developer committed the .env file with all production credentials to a public GitHub repo",
            "Our 'zero-trust security model' meant we trusted zero security practices",
            "The penetration tester found our admin panel and cried because the password was literally 'admin'"
        ]
    }
}

# Flatten all excuses for random selection
ALL_EXCUSES = []
for category, severity_dict in BLAME_EXCUSES.items():
    for severity, excuses in severity_dict.items():
        for excuse in excuses:
            ALL_EXCUSES.append({
                "blame": excuse,
                "category": category,
                "severity": severity
            })

# Get all categories
CATEGORIES = list(BLAME_EXCUSES.keys())

# Severity level emojis and descriptions
SEVERITY_INFO = {
    "minor": {
        "emoji": "🟢",
        "level": 1,
        "name": "Minor Oopsie",
        "description": "A small blunder. You'll probably keep your job."
    },
    "moderate": {
        "emoji": "🟡",
        "level": 2,
        "name": "Moderate Mishap",
        "description": "Things are getting spicy. Update your LinkedIn, just in case."
    },
    "catastrophic": {
        "emoji": "🔴",
        "level": 3,
        "name": "CATASTROPHIC DISASTER",
        "description": "Career-defining moment. Hope you have a good lawyer."
    }
}
