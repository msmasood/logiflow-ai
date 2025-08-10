from logiflow.orchestrator import plan_shipments
def test_plan():
    r = plan_shipments(2)
    assert isinstance(r, list) and len(r)==2
