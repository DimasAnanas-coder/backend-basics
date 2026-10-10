import argparse
import sys
import json

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
    p.add_argument(
        "--json",
        nargs="?",
        const="default.json",
        default=None,
        help="Output the result in JSON format.",

    )
    return p.parse_args()


def main() -> int:
    try:
        args = parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        return 2

    try:
        city_summary = service.build_city_summary(args.city, args.currency)
    except BadApiArgument as e:
        print(f"Currency or city not found: {e}")
        return 3
    except ApiRequestError as e:
        print(f"Error making API request: {e}")
        return 4
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    if args.json:
        with open(args.json, "w") as f:
            json.dump(city_summary, f, indent=4)
    else:
        print(city_summary)


if __name__ == "__main__":
    status_code: int = main()
    sys.exit(status_code)
