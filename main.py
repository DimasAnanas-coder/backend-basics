import argparse
import sys

from exceptions import ApiRequestError, BadApiArgument
from processing import service


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="A simple command-line tool for getting city summary."
    )
    p.add_argument(
        "--city",
        action="store",
        help="The city for which to display information.",
        default="Moscow",
    )
    p.add_argument(
        "--currency",
        action="store",
        help="The currency in which to display information.",
        default="USD",
    )
    return p.parse_args()


def main() -> int:
    try:
        args = parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        return 2

    try:
        print(service.build_city_summary(args.city, args.currency))
        return 0
    except BadApiArgument as e:
        print(f"Currency or city not found: {e}")
        return 3
    except ApiRequestError as e:
        print(f"Error making API request: {e}")
        return 4
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1


if __name__ == "__main__":
    status_code: int = main()
    sys.exit(status_code)
