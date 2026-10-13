import os
import subprocess
import sys

def install_dependencies():
    print("Installing SHINO dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_environment():
    if not os.path.exists(".env"):
        print("Creating .env from .env.example...")
        with open(".env.example", "r") as f_in:
            with open(".env", "w") as f_out:
                f_out.write(f_in.read())
        print("Please update .env with your actual API keys.")

def main():
    try:
        install_dependencies()
        setup_environment()
        print("SHINO setup complete successfully!")
    except Exception as e:
        print(f"Setup failed: {e}")

if __name__ == "__main__":
    main()
