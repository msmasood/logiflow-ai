# src/logiflow/orchestrator.py
from typing import List, Dict
import random
def plan_shipments(n_demo=5):
    # simple placeholder: create demo routes with cost estimates
    routes = []
    for i in range(n_demo):
        routes.append({'shipment_id': i, 'route': f'WH{i}->CUST{i}', 'est_distance_km': round(random.uniform(10,200),1), 'est_cost_usd': int(random.uniform(50,800))})
    return routes
