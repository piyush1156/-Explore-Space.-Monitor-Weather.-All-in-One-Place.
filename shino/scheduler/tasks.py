import asyncio
from datetime import datetime
from shino.core.logger import logger

class ShinoScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, execution_time: datetime, action):
        self.tasks.append({"name": name, "time": execution_time, "action": action})
        logger.info(f"Task '{name}' scheduled for {execution_time}")

    async def run_scheduler(self):
        while True:
            now = datetime.now()
            for task in self.tasks[:]:
                if now >= task["time"]:
                    logger.info(f"Executing task: {task['name']}")
                    await task["action"]()
                    self.tasks.remove(task)
            await asyncio.sleep(60)

scheduler = ShinoScheduler()
