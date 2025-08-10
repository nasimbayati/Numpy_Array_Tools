"""
NumPy Array Tools
-----------------
This script demonstrates two useful NumPy operations:
1. Finding the intersection of two arrays.
2. Performing addition using broadcasting rules.

The script can run in demo mode or accept command-line input.
"""

import numpy as np
import argparse
import ast
import os

def array_intersection(a, b):
    """
    Returns the unique, sorted intersection of two NumPy arrays.
    """
    return np.intersect1d(a, b)

def broadcast_addition(a, b):
    """
    Returns the result of adding two arrays using NumPy broadcasting.
    """
    return a + b

def run_demo():
    """
    Runs both features with example data.
    """
    # Intersection example
    arr_a = np.array([
        ['joe', 'Joe', 'harry'],
        ['frank', 'alice', 'jim'],
        ['Will', 'sam', 'tom']
    ])
    arr_b = np.array([
        ['joe', 'Joe', 'heather'],
        ['frank', 'alice', 'frank'],
        ['Will', 'bill', 'martha']
    ])
    print("Intersection (unique sorted 1-D):")
    print(array_intersection(arr_a, arr_b))

    # Broadcasting addition example
    arr1 = np.array([[33, 59, 24], [16, 12, 18]])
    arr2 = np.array([13, 16, 47])
    print("\nBroadcast addition result:")
    print(broadcast_addition(arr1, arr2))

def parse_array_input(value):
    """
    Parses array input from a string or loads from a file if ending with .npy.
    """
    if os.path.isfile(value) and value.endswith(".npy"):
        return np.load(value, allow_pickle=True)
    try:
        return np.array(ast.literal_eval(value))
    except Exception:
        raise argparse.ArgumentTypeError("Invalid array format. Use Python list syntax or a .npy file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NumPy Array Tools")
    subparsers = parser.add_subparsers(dest="command", help="Choose a function to run")

    # Intersection command
    parser_intersect = subparsers.add_parser("intersect", help="Find intersection of two arrays")
    parser_intersect.add_argument("--a", type=parse_array_input, help="First array (inline or .npy file)")
    parser_intersect.add_argument("--b", type=parse_array_input, help="Second array (inline or .npy file)")

    # Broadcasting addition command
    parser_add = subparsers.add_parser("add", help="Perform broadcasting addition")
    parser_add.add_argument("--a", type=parse_array_input, help="First array (inline or .npy file)")
    parser_add.add_argument("--b", type=parse_array_input, help="Second array (inline or .npy file)")

    args = parser.parse_args()

    if args.command == "intersect":
        if args.a is None or args.b is None:
            parser.error("Both --a and --b are required for intersect")
        print(array_intersection(args.a, args.b))

    elif args.command == "add":
        if args.a is None or args.b is None:
            parser.error("Both --a and --b are required for add")
        print(broadcast_addition(args.a, args.b))

    else:
        run_demo()
