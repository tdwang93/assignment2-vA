import argparse

def parse_command_args():
    """
    Parse command-line arguments using argparse.
    Returns an argparse.Namespace object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )
    parser.add_argument(
        "-H", "--human-readable", action="store_true",
        help="Prints sizes in human readable format"
    )
    parser.add_argument(
        "-l", "--length", type=int, default=20,
        help="Specify the length of the graph. Default is 20."
    )
    parser.add_argument(
        "program", type=str, nargs='?', 
        help="if a program is specified, show memory use of all associated processes. Show only total use if not."
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_command_args()
    print(args)  # For manual testing
