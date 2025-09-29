import requests
from datetime import datetime
import pytz

def get_weather(location="Indore"):
    try:
        response = requests.get(f"https://wttr.in/{location}?format=3")
        return response.text.strip()
    except Exception as e:
        return f"Weather fetch failed: {e}"

def get_local_time(timezone="Asia/Kolkata"):
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return f"Time fetch failed: {e}"

if __name__ == "__main__":
    print("🕒 Local Time:", get_local_time())
    print("🌦 Weather:", get_weather())
