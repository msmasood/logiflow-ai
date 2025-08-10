from logiflow.orchestrator import plan_shipments
def main():
    routes = plan_shipments(n_demo=5)
    print('Planned routes:')
    for r in routes:
        print(r)
if __name__ == '__main__':
    main()
