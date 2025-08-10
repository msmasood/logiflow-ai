# LogiFlow AI — Autonomous Logistics Optimization Agent (Demo)

LogiFlow AI demonstrates routing optimization and simple inventory rebalancing using OR-Tools and a multi-agent orchestration demo.

Quickstart:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/logiflow/orchestrator_demo.py
uvicorn src.api.app:app --reload --port 8300
```
