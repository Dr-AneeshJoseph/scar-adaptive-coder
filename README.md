# ⚡ S.C.A.R. (Self-Correction & Adaptive Retention)

> **The Autonomous Coder that Never Makes the Same Mistake Twice.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## ⚠️ The Problem
AI Coding Agents are amnesiacs. If they fail to solve a bug, they often retry the exact same solution in the next session, wasting tokens and time.

## 🛡️ The Solution
**S.C.A.R.** implements **Loop 10 (Memory Anvil)**. It maintains a persistent JSON file of "Traumas" (failures). Before writing any code, it consults this file to ensure it avoids previously known bad paths.

## 🚀 Quick Start
```python
from scar.agent import ScarAgent
agent = ScarAgent()

# If the agent fails:
agent.report_failure("task", "bad_code()", "Error: Function not found")

# Next time, the agent knows better.
