import asyncio
from shino.coding_agent.agent import coding_agent
from shino.utils.helpers import run_command
from shino.core.logger import logger
from shino.vision.screen import screen_analyzer

class DebugLoop:
    def __init__(self):
        self.max_retries = 5

    async def run_and_fix(self, run_command_str: str, file_to_fix: str):
        retries = 0
        while retries < self.max_retries:
            logger.info(f"Running attempt {retries + 1}: {run_command_str}")
            output = run_command(run_command_str)

            if "Error" not in output and "Exception" not in output:
                logger.info("Project ran successfully!")
                return True

            logger.warn(f"Error detected: {output}")

            # Request fix from Laguna
            fix_prompt = f"The following error occurred while running '{run_command_str}':\n\n{output}\n\nPlease provide the corrected code for {file_to_fix}."
            new_code = await coding_agent.generate_code(fix_prompt)

            if new_code:
                coding_agent.write_to_file(file_to_fix, new_code)
                logger.info(f"Applied fix to {file_to_fix}")

            retries += 1
            await asyncio.sleep(1)

        logger.error("Failed to fix after maximum retries.")
        return False

debug_loop = DebugLoop()
