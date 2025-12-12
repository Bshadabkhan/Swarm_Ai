<div align="center">

# 🐝 Swarm Framework  
### **A Lightweight, Modular Multi-Agent Orchestration Engine for Python**

<img src="https://img.shields.io/badge/Agents-Modular-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Orchestration-Dynamic-purple?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.9%2B-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" />

</div>

---

## 🌟 Overview

**Swarm Framework** is a minimal and flexible **multi-agent orchestration system** inspired by OpenAI Swarm.  
It enables developers to create **coordinating AI agents** that can:

- 🤝 Collaborate  
- 🔄 Handoff tasks  
- 🧠 Maintain shared memory  
- 🎛️ Act with tools  
- ⚡ Run dynamic reasoning chains

Ideal for **AI assistants**, **RAG systems**, **DevOps bots**, **workflow automation**, and more.

---

## 📌 Features

### 🐝 Modular Agents  
Define agents with their own **name, instructions, model**, and **toolset**.

### 🔄 Agent Handoff  
Agents can transfer conversations or tasks using the `handoff()` function.

### 🧰 Tool Support  
Register Python functions as tools that agents can call autonomously.

### 🧵 Conversation Continuity  
Automatic propagation of `messages` across handoffs.

### ⚡ Minimal Boilerplate  
No heavy classes, no configs — just simple Python functions.

---

## 🧠 Architecture Diagram

┌───────────────┐ handoff() ┌───────────────┐
│ Agent A │ ─────────────────────────▶ │ Agent B │
│ (Planner) │ │ (Executor) │
└───────▲────────┘ └───────▲───────┘
│ │
│ actions / calls │ actions / next agent
▼ ▼
┌────────────────┐ ┌──────────────────┐
│ Tools / API │ │ Memory / Context │
└────────────────┘ └──────────────────┘

---

## 🚀 Installation

```bash
pip install swarm-framework

git clone https://github.com/yourusername/swarm-framework.git
cd swarm-framework

🐝 Quick Start Example

Below is a minimal example showing two agents handing off a task.

from swarm import Swarm, Agent, handoff

# Define Agents
planner = Agent(
    name="planner",
    instructions="Break tasks into steps and assign to executor.",
)

executor = Agent(
    name="executor",
    instructions="Execute steps received from planner.",
)

# Agent logic
def planner_agent(state):
    return handoff(executor, "Please execute this task.")

def executor_agent(state):
    return "Task executed successfully."

# Run
client = Swarm()
response = client.run(
    agent=planner,
    context={"input": "Process a user request."},
)
print(response.messages[-1]["content"])

⚙️ Defining Agents
agent = Agent(
    name="researcher",
    instructions="Search, analyze, and summarize information.",
    functions=[search_tool, summarize_tool],
    model="gpt-4o-mini",
    parallel_tool_calls=True,
)

🔧 Adding Tools
from swarm import tool

@tool
def get_weather(city: str):
    """Fetches weather for a given city."""
    return {"city": city, "temp": "27°C", "condition": "Sunny"}


Use it inside an agent:

agent = Agent(
    name="weather_agent",
    instructions="Provide weather updates.",
    functions=[get_weather],
)

🔄 Agent Handoff
return handoff(
    agent=executor_agent,
    message="Here are the steps. Please execute them."
)


Handoff transfers:

Messages

Context

Memory

State

🧵 Conversation Workflow
User → Agent A → Handoff → Agent B → Response → User


The user interacts with one system, not multiple agents.

🔥 Advanced Features
🔹 State Injection
def agent_handler(state):
    user_query = state["input"]
    return f"Processed: {user_query}"

🔹 Parallel Tool Calls
Agent(..., parallel_tool_calls=True)

🔹 Tools with JSON Schema

Tools auto-generate schema for the model.

🔹 Context Propagation

All prior messages automatically flow through agents.

📁 Project Structure
swarm-framework/
│
├── swarm/
│   ├── core.py
│   ├── agent.py
│   ├── client.py
│   ├── tools.py
│   └── utils.py
│
├── examples/
│   └── basic_handoff.py
│
└── README.md

🛠️ Example Use Cases

🔍 Multi-agent RAG pipeline

👩‍💻 AI coding assistants

📊 Research + analysis bots

🧾 Document analyzers

🎧 AI podcast workflow automation

🤖 Agentic task executors

📜 License

Licensed under the MIT License.

<div align="center">
⭐ If you like this project, consider giving it a star!
</div> ```
