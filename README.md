# 🏋️‍♂️ Agentic Coding Fitness @ Rust Tech Bar

Welcome to the repository for the **Agentic Coding Fitness** event series, hosted weekly at Rust Bar, Ban Tad Thong! 

This repository contains all the code, tools, and examples built during our hands-on "Vibe Coding" sessions. It serves as a living codebase demonstrating how to transition from basic AI API calls to building sophisticated, multi-agent systems and real-world IoT integrations.

**Event Details**: [Luma Event Page](https://lu.ma/jy6d10xq)
- **When**: Every Tuesday, 18:00 – 20:00
- **Where**: Rust Bar, Ban Tad Thong (Bangkok)

## 🤖 What is Agentic Coding Fitness?
Think of this as a "fitness center" for your coding brain—but instead of lifting weights, we are building AI muscle muscle memory. We focus on **Agentic AI**: moving beyond simple prompt-and-response mechanisms to build AI that can think, plan, decide, and collaborate using multi-agent systems.

We emphasize a **practice-first** approach (Vibe Coding). No long lectures, just shipping workable solutions that interact with the real world!

## 📂 Repository Contents 

The project is structured week-by-week as our complexity scales up:

### 🔹 Week 2: Claude API Foundations
Understanding how to talk to modern LLMs programmatically.
- `week2/claudeapicall.py`: Basic single-turn API requests.
- `week2/claudestreamingapi.py`: Streaming tokens in real-time for better UX.
- `week2/claudemulti_turn.py`: Managing conversational state and history.

### 🔹 Week 3: Tool Use & Smart Assistants
Teaching our AI agents how to interact with external services.
- `week3/toolsuse.py`: Introduction to function calling (weather, calculator, web search).
- `week3/buildsmartassistant3tools.py`: A fully-fledged assistant script.
- **Tapo Smart Plug Integration**: (`check_tapo.py`, `scan.py`, `tapo_config.json`) Creating a local HTTP wrapper to let Claude natively control TP-Link Tapo L530 smart lights.

### 🔹 Week 4: Autonomous Pipelines & Hardware
Building chains of actions and jumping into IoT physical hardware.
- `week4/pipeline.py`: An autonomous AI Research Pipeline that uses `duckduckgo-search` to browse the web, simulate a multi-agent synthesis process, score its own quality, and output Markdown reports. (With workflows to export findings right into NotebookLM!).
- `week4/dronecontrol.py`: Automating flight patterns and physical tricks using a DJI Tello Drone (`djitellopy`), merging spatial IoT with programmable scripts.

---

## 🛠️ Getting Started

### 1. Requirements
Ensure you have **Python 3.10+** installed on your machine.

Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/your-username/AgenticCoding.git
cd AgenticCoding
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
To authenticate with the models, create a `.env` file in the root directory:
```ini
ANTHROPIC_API_KEY="sk-ant-api03-YourAnthropicKeyHere..."
```

### 4. Hardware Configuration (Optional)
- **Tapo Lights**: Edit `tapo_config.json` with your TP-Link account credentials and local IP address of your light bulb. 
- **Tello Drone**: Connect your computer directly to the Tello's Wi-Fi network before running `week4/dronecontrol.py`.

---

## 🎯 Who is this for?
- **Developers & Programmers** looking to elevate their workflow with AI.
- **Tech, Startup, and Product Innovators**.
- Anyone with basic coding knowledge ready to embrace the future of **AI-native, Agent-based development**.

## 🌟 Our Goal 
- Build **Real Stuff**
- Solve **Real Problems**
- Generate **Real Impact**

Come join us every Tuesday, stretch those brain muscles, and let's craft the future of Agentic AI together! 💪🤖
