import sys
import os
import argparse

# Ensure project root is in import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your modules
from modules.weather_time import get_weather, get_local_time
from system_metrics import get_system_metrics
from modules.docker_health import get_container_health
from colorama import Fore, Style

def show_weather_time():
    print(Fore.CYAN + "\n🕒 Local Time:" + Style.RESET_ALL, get_local_time())
    print(Fore.BLUE + "🌦 Weather:" + Style.RESET_ALL, get_weather())

def show_system_metrics():
    metrics = get_system_metrics()
    print(Fore.GREEN + "\n📊 System Metrics:" + Style.RESET_ALL)
    for key, value in metrics.items():
        print(f"  {key}: {value}")

def show_docker_health():
    containers = get_container_health()
    print(Fore.MAGENTA + "\n🐳 Docker Container Health Check:" + Style.RESET_ALL)
    for info in containers:
        print(f"  {info['Name']} ({info['Image']}): Status={info['Status']}, Health={info['Health']}")

# CLI entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Monitor Dashboard")
    parser.add_argument("--weather", action="store_true", help="Show weather and local time")
    parser.add_argument("--metrics", action="store_true", help="Show system metrics")
    parser.add_argument("--docker", action="store_true", help="Show Docker container health")
    parser.add_argument("--all", action="store_true", help="Show full dashboard: weather, metrics, and Docker health")

    args = parser.parse_args()

    if args.all:
        show_weather_time()
        show_system_metrics()
        show_docker_health()
    else:
        if args.weather:
            show_weather_time()
        if args.metrics:
            show_system_metrics()
        if args.docker:
            show_docker_health()
