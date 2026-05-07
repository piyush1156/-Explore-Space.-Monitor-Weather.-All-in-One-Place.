import psutil
from shino.core.logger import logger

class SystemMonitor:
    def get_stats(self):
        stats = {
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
            "battery": psutil.sensors_battery().percent if psutil.sensors_battery() else "N/A",
            "is_plugged": psutil.sensors_battery().power_plugged if psutil.sensors_battery() else "N/A"
        }
        return stats

    def check_alerts(self):
        stats = self.get_stats()
        alerts = []
        if isinstance(stats["battery"], (int, float)) and stats["battery"] < 20 and not stats["is_plugged"]:
            alerts.append(f"Sir, battery {stats['battery']}% par aa gayi hai. Please charger connect kijiye.")
        if stats["cpu_usage"] > 90:
            alerts.append("System par kafi load hai, CPU usage high hai.")
        return alerts

system_monitor = SystemMonitor()
