from fastapi import FastAPI
from logiflow.orchestrator import plan_shipments
app = FastAPI(title='LogiFlow AI Demo API')

@app.get('/plan')
def plan(n: int = 5):
    return {'status':'ok', 'routes': plan_shipments(n_demo=n)}
