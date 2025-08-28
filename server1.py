# server.py
from flask import Flask, request
import os, requests

app = Flask(__name__)

CLICKUP_TOKEN = os.environ.get("CLICKUP_TOKEN")  # export before running
DAYS_CF_ID = "6bd6d67c-928d-4d5a-b7a6-5e86442a51f8"     # e.g., 6bd6d67c-...

def to_int(x):
    try: return int(float(x))
    except: return None

@app.post("/webhook")
def webhook():
    payload = request.get_json(force=True)
    print("✅ Webhook received:", payload)
    task_id = payload.get("task_id")

    for item in (payload.get("history_items") or []):
        # react only when our number field changed
        if item.get("field") == "custom_field" and item.get("custom_field", {}).get("id") == DAYS_CF_ID:
            before = to_int(item.get("before"))
            after = to_int(item.get("after"))
            print(f"🔔 Days to complete changed on {task_id}: {before} → {after}")

            # visible confirmation back in ClickUp (comment)
            if CLICKUP_TOKEN and task_id is not None:
                r = requests.post(
                    f"https://api.clickup.com/api/v2/task/{task_id}/comment",
                    headers={"Authorization": CLICKUP_TOKEN, "Content-Type": "application/json"},
                    json={"comment_text": f"Days to complete updated: {before} → {after}."}
                )
                print("✅ Comment posted" if r.ok else f"⚠️ Comment failed: {r.text}")
            break
    return "", 200

@app.get("/")
def ok(): return "OK", 200

if __name__ == "__main__":
    # optional: set host="0.0.0.0"
    app.run(port=3000)