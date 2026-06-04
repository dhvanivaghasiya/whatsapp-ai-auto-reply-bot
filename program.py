import pyautogui
import pyperclip
import time
from openai import OpenAI

# =========================
# GROQ API
# =========================

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

print("Starting in 5 seconds...")
time.sleep(5)

# =========================
# OPEN WHATSAPP
# =========================

pyautogui.click(924, 1046)

time.sleep(2)

# =========================
# SELECT CHAT
# =========================

pyautogui.moveTo(877, 227)

pyautogui.mouseDown()

pyautogui.moveTo(1861, 892, duration=2)

pyautogui.mouseUp()

time.sleep(1)

# =========================
# COPY CHAT
# =========================

pyautogui.hotkey("ctrl", "c")

time.sleep(2)

# =========================
# GET COPIED TEXT
# =========================

copied_text = pyperclip.paste()

print("===== CHAT =====")
print(copied_text)

# =========================
# GET LAST MESSAGE ONLY
# =========================

last_line = copied_text.strip().split("\n")[-1]

# Remove date/time
if "]" in last_line:
    last_line = last_line.split("]")[-1]

# Remove name
if ":" in last_line:
    last_line = last_line.split(":")[-1]

last_line = last_line.strip()

print("===== CLEAN MESSAGE =====")
print(last_line)

# =========================
# AI REPLY
# =========================

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=1.7,
    max_tokens=120,
    messages=[
        {
            "role": "system",
            "content": """
You are NOT an AI.

You are a real 19 year old boy chatting casually on WhatsApp.

Your texting style:
- messy typing sometimes
- casual texting
- emotional reactions
- funny replies
- medium length replies
- teasing sometimes
- real human vibe

STRICT RULES:
- ONLY English.
- NEVER Hindi.
- NEVER Gujarati.
- NEVER formal.
- NEVER robotic.
- NEVER explain things.

Talk like real Gen-Z friends.

Use words like:
bro, bruh, fr, lowkey, ngl, tf, damn, crazy, wild

Use emojis naturally:
😂😭💀🔥🥲

GOOD EXAMPLES:
"bro that's actually crazy 😭"
"nahhh tf 😂"
"lmaooo i would've left instantly 💀"
"bro you're cooked 😭🔥"
"damn that's lowkey sad tho 🥲"
"nah fr i'd be mad as hell 😂"

BAD EXAMPLES:
"How can I help you?"
"That sounds interesting."
"I understand your feelings."

Reply naturally like real chats.
"""
        },
        {
            "role": "user",
            "content": last_line
        }
    ]
)

reply = response.choices[0].message.content

print("===== REPLY =====")
print(reply)

# =========================
# SEND MESSAGE
# =========================

# Click typing box
pyautogui.click(1100, 830)

time.sleep(1)

# Copy reply
pyperclip.copy(reply)

time.sleep(1)

# Paste reply
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# Send
pyautogui.press("enter")

print("DONE")