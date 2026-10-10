import argparse
import sys

from processing import service


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="A simple command-line tool for getting city summary.")
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
    args = parse_args()
    print(service.build_city_summary(args.city, args.currency))
    return 0


if __name__ == "__main__":
    status_code: int = main()
    sys.exit(status_code)
