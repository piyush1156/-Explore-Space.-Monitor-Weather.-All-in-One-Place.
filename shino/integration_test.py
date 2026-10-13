import asyncio
import os
from shino.ai.router import router
from shino.memory.history import history_db
from shino.monitoring.monitor import system_monitor

async def test_integration():
    print("Starting SHINO Integration Test...")

    # 1. Test Router
    print("Testing AI Router...")
    is_coding = router.is_coding_task("Write a python function to add two numbers")
    print(f"Is coding task detection: {is_coding}")

    # 2. Test Memory
    print("Testing Memory System...")
    history_db.add_message("user", "Hello Shino")
    history_db.add_message("assistant", "Hello! Main aapki kaise madad kar sakti hoon?")
    recent = history_db.get_recent(limit=2)
    print(f"Memory retrieval: {len(recent)} messages found.")

    # 3. Test Monitoring
    print("Testing System Monitor...")
    stats = system_monitor.get_stats()
    print(f"System Stats: CPU {stats['cpu_usage']}%, RAM {stats['memory_usage']}%")

    print("Integration test finished (Desktop Automation skipped due to headless env).")

if __name__ == "__main__":
    asyncio.run(test_integration())
