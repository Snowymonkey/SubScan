import argparse
import json
from subdomain_scanner import scan_manager

with open("config.json") as file:
    data = json.load(file)

max_threads = data["max_threads"]

parser = argparse.ArgumentParser(
    prog="SubScan",
    description="A Simple subdomain and fast subdomain scanner",
    epilog="Use --help to view all arguments"
)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument(
    "-s",
    "--small_scan",
    help="Small top 5000 subdomain scan"
)

group.add_argument(
    "-m",
    "--medium_scan",
    help="Medium top 20000 subdomain scan"
)

group.add_argument(
    "-l",
    "--large_scan",
    help="Large top 110000 subdomain scan"
)

args = parser.parse_args()

if args.small_scan:
    print(f"Starting small scan on {args.small_scan}...")
    scan_manager(args.small_scan, "s", max_threads)
    print("Finished scan")

elif args.medium_scan:
    print(f"Starting medium scan on {args.small_scan}...")
    scan_manager(args.medium_scan, "m", max_threads)
    print("Finished scan")

elif args.large_scan:
    print(f"Starting large scan on {args.small_scan}...")
    scan_manager(args.large_scan, "l", max_threads)
    print("Finished scan")

