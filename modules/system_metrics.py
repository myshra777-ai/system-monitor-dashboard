import psutil
import time
import os

def get_system_metrics():
    uptime = time.time() - psutil.boot_time()
    load_avg = os.getloadavg() if hasattr(os, 'getloadavg') else (0, 0, 0)

    metrics = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Uptime (hrs)": round(uptime / 3600, 2),
        "Load Avg (1/5/15 min)": load_avg
    }
    return metrics

if __name__ == "__main__":
    print("Running system metrics...")
    for key, value in get_system_metrics().items():
        print(f"{key}: {value}")
