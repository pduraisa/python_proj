
import argparse

parser = argparse.ArgumentParser(description='A simple script demonstrating argparse.')
parser.add_argument('name', type=str, help='Your name to greet.')
parser.add_argument('--age', '-a', type=int, help='Your age (optional).')
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output.')
args = parser.parse_args()
print(f"Hello, {args.name}!")

if args.age:
    print(f"You are {args.age} years old.")

if args.verbose:
    print("Verbose mode is enabled.")



