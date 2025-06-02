import flwr as fl
from flwr.server.strategy import FedAvg
import time

def run_stage(stage_num):
    print(f'Stage {stage_num}')
    strategy = FedAvg(
        fraction_fit=1.0,
        fraction_evaluate=1.0,
        min_fit_clients=1,
        min_evaluate_clients=1,
        min_available_clients=1,
    )

    fl.server.start_server(
        server_address="0.0.0.0:5000",
        config=fl.server.ServerConfig(num_rounds=5),
        strategy=strategy,
    )

if __name__ == "__main__":
    stage = 1
    while True:
        run_stage(stage)
        stage += 1
