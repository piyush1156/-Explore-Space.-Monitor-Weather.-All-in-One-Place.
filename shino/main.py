import asyncio
import sys
from shino.config.config import Config
from shino.core.logger import logger
from shino.ai.router import router
from shino.voice.speaker import speaker
from shino.memory.history import history_db
from shino.monitoring.monitor import system_monitor

class SHINOSystem:
    def __init__(self):
        self.is_running = True
        self.last_interaction_time = asyncio.get_event_loop().time()

    async def main_loop(self):
        logger.info("SHINO System Started.")
        await speaker.speak("Namaste sir, main Shino hoon. Main aapki kaise madad kar sakti hoon?")

        asyncio.create_task(self.monitoring_loop())
        asyncio.create_task(self.inactivity_check())

        while self.is_running:
            try:
                # Use a non-blocking way to get input in a loop
                command = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                command = command.strip()

                if command:
                    if command.lower() in ["exit", "quit", "bye"]:
                        await speaker.speak("Goodbye sir, apna khayal rakhiyega.")
                        self.is_running = False
                        break

                    self.last_interaction_time = asyncio.get_event_loop().time()
                    response = await router.route_and_respond(command, history_db.get_recent())
                    history_db.add_message("user", command)
                    history_db.add_message("assistant", response)
                    await speaker.speak(response)
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
            await asyncio.sleep(0.1)

    async def monitoring_loop(self):
        while self.is_running:
            alerts = system_monitor.check_alerts()
            for alert in alerts:
                await speaker.speak(alert)
            await asyncio.sleep(300)

    async def inactivity_check(self):
        while self.is_running:
            elapsed = asyncio.get_event_loop().time() - self.last_interaction_time
            if elapsed > Config.INACTIVITY_TIMEOUT:
                await speaker.speak("I'm still here, sir.")
                self.last_interaction_time = asyncio.get_event_loop().time()
            await asyncio.sleep(10)

if __name__ == "__main__":
    shino = SHINOSystem()
    try:
        asyncio.run(shino.main_loop())
    except KeyboardInterrupt:
        print("\nSHINO shutting down...")
