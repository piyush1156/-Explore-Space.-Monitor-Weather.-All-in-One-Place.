import os
import subprocess

def run_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
