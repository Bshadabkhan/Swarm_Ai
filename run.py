import sys
import os
# import swarm # added afterwards\\\\
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swarm.repl import run_demo_loop
from triage_agent.agents import triage_agent

if __name__ == "__main__":
    print("Starting live interaction. Press Ctrl+C to stop.")
    run_demo_loop(triage_agent)




