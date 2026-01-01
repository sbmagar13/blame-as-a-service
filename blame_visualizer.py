"""
ASCII art and visual formatters for blame excuses
"""
import random
from blame_data import SEVERITY_INFO

# ASCII Art Templates
ASCII_TEMPLATES = {
    "box": """
╔═══════════════════════════════════════════════════════════════════════╗
║                         ⚠️  BLAME REPORT ⚠️                            ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  {blame}
║                                                                       ║
╠═══════════════════════════════════════════════════════════════════════╣
║  Severity: {severity_emoji} {severity_name:<20}  Category: {category:<15} ║
╚═══════════════════════════════════════════════════════════════════════╝
""",
    "banner": """
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                    🚨 OFFICIAL BLAME CERTIFICATE 🚨
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

  {blame}

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Severity: {severity_emoji} {severity_name}
  Category: {category}
  Excuse Quality: {quality}/10 ⭐
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

           This excuse has been officially certified by
                   🏢 Blame-as-a-Service Inc. 🏢
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
""",
    "simple": """
┌─────────────────────────────────────────────────────────────────┐
│ 🎯 BLAME: {blame_short}...
│
│ {severity_emoji} Severity: {severity_name}
│ 📁 Category: {category}
└─────────────────────────────────────────────────────────────────┘
""",
    "dramatic": """
██████╗ ██╗      █████╗ ███╗   ███╗███████╗
██╔══██╗██║     ██╔══██╗████╗ ████║██╔════╝
██████╔╝██║     ███████║██╔████╔██║█████╗
██╔══██╗██║     ██╔══██║██║╚██╔╝██║██╔══╝
██████╔╝███████╗██║  ██║██║ ╚═╝ ██║███████╗
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {blame}
┃
┃  {severity_emoji} {severity_name} | 📂 {category}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
}

# Severity indicators
SEVERITY_BARS = {
    "minor": "▓░░░░░░░░░ 10%",
    "moderate": "▓▓▓▓▓░░░░░ 50%",
    "catastrophic": "▓▓▓▓▓▓▓▓▓▓ 100% 🔥💀🔥"
}


def wrap_text(text, width=60):
    """Wrap text to specified width"""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def format_blame_ascii(blame_data, style="box"):
    """
    Format blame data as ASCII art

    Args:
        blame_data: Dict with 'blame', 'category', 'severity'
        style: ASCII style (box, banner, simple, dramatic)

    Returns:
        Formatted ASCII art string
    """
    blame = blame_data["blame"]
    category = blame_data["category"].upper()
    severity = blame_data["severity"]

    severity_info = SEVERITY_INFO[severity]
    severity_emoji = severity_info["emoji"]
    severity_name = severity_info["name"]
    quality = random.randint(6, 10)  # All excuses are quality!

    # Wrap the blame text
    wrapped_lines = wrap_text(blame, 60)

    if style == "box":
        # Format wrapped lines with proper padding
        formatted_blame = "\n".join([f"║  {line:<69}║" for line in wrapped_lines])
        return ASCII_TEMPLATES["box"].format(
            blame=formatted_blame,
            severity_emoji=severity_emoji,
            severity_name=severity_name,
            category=category
        )

    elif style == "banner":
        formatted_blame = "\n  ".join(wrapped_lines)
        return ASCII_TEMPLATES["banner"].format(
            blame=formatted_blame,
            severity_emoji=severity_emoji,
            severity_name=severity_name,
            category=category,
            quality=quality
        )

    elif style == "simple":
        blame_short = blame[:50] if len(blame) > 50 else blame
        return ASCII_TEMPLATES["simple"].format(
            blame_short=blame_short,
            severity_emoji=severity_emoji,
            severity_name=severity_name,
            category=category
        )

    elif style == "dramatic":
        formatted_blame = "\n┃  ".join(wrapped_lines)
        return ASCII_TEMPLATES["dramatic"].format(
            blame=formatted_blame,
            severity_emoji=severity_emoji,
            severity_name=severity_name,
            category=category
        )

    return blame


def get_severity_bar(severity):
    """Get visual severity bar"""
    return SEVERITY_BARS.get(severity, "░░░░░░░░░░")


def format_blame_rich(blame_data):
    """
    Format blame data with rich details

    Returns JSON-compatible dict with all visual elements
    """
    severity_info = SEVERITY_INFO[blame_data["severity"]]

    return {
        "blame": blame_data["blame"],
        "category": blame_data["category"],
        "severity": {
            "level": blame_data["severity"],
            "emoji": severity_info["emoji"],
            "name": severity_info["name"],
            "description": severity_info["description"],
            "numeric": severity_info["level"],
            "bar": get_severity_bar(blame_data["severity"])
        },
        "quality_score": random.randint(6, 10),
        "believability": random.randint(1, 10),
        "disclaimer": "This excuse is certified 100% not your fault™"
    }


def create_blame_meter(severity):
    """Create a visual blame meter"""
    severity_info = SEVERITY_INFO[severity]
    level = severity_info["level"]

    meter = ""
    meter += "\n┌─────────── BLAME METER ───────────┐\n"
    meter += "│                                   │\n"
    meter += "│  🟢 Minor      "
    if level >= 1:
        meter += "●"
    else:
        meter += "○"
    meter += "                  │\n"

    meter += "│       ↓                           │\n"
    meter += "│  🟡 Moderate   "
    if level >= 2:
        meter += "●"
    else:
        meter += "○"
    meter += "                  │\n"

    meter += "│       ↓                           │\n"
    meter += "│  🔴 Catastrophic "
    if level >= 3:
        meter += "●"
    else:
        meter += "○"
    meter += "               │\n"

    meter += "│                                   │\n"
    meter += f"│  Current: {severity_info['emoji']} {severity_info['name']:<18} │\n"
    meter += "└───────────────────────────────────┘\n"

    return meter


def create_multi_blame_display(blames):
    """Create a display for multiple blames"""
    output = "\n"
    output += "╔═══════════════════════════════════════════════════════════════════════╗\n"
    output += "║                    🎰 BLAME ROULETTE RESULTS 🎰                       ║\n"
    output += "╚═══════════════════════════════════════════════════════════════════════╝\n\n"

    for i, blame_data in enumerate(blames, 1):
        severity_info = SEVERITY_INFO[blame_data["severity"]]
        output += f"  {i}. {severity_info['emoji']} [{blame_data['category'].upper()}] {blame_data['blame']}\n\n"

    return output
