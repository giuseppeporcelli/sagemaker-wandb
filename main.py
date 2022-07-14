import os
import wandb

def train():
    run = wandb.init(reinit=True, project="sagemaker-wandb")
    for y in range (100):
        wandb.log({"metric": y})
    run.finish()

if __name__ == "__main__":
    train()
