"""Command-line helper to run individual steps of the pipeline."""

import argparse


def main(step: str):
    if step == "preprocessing":
        print("Run preprocessing (implement logic here).")
    elif step == "embeddings":
        print("Run visibility graph and embedding step (implement logic here).")
    elif step == "barycenter":
        print("Run Wasserstein barycenter and GMM fit (implement logic here).")
    elif step == "joint_model":
        print("Run joint model calibration (implement logic here).")
    else:
        raise ValueError(f"Unknown step: {step}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", type=str, required=True)
    args = parser.parse_args()
    main(args.step)
