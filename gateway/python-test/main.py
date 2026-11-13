
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Simple Itential Gateway test service"
    )

    parser.add_argument(
        "--customer_name",
        required=True,
        help="Customer name"
    )

    args = parser.parse_args()

    print(f"Hello {args.customer_name}, from Itential Gateway!")
    print("Python script service executed successfully.")


if __name__ == "__main__":
    main()
