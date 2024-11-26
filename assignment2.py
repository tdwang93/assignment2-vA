#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py
Author: "Tandin Wangmo"
Semester: "Winter 2024"

The python code in this file is original work written by
"Tandin Wangmo". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description:
This script provides a visual representation of memory usage on a Linux system.
It can display the total system memory usage or the memory usage of specific
processes when a program name is provided. The script uses the `/proc` file
system to extract memory-related information and `argparse` for command-line
argument parsing.

Key Features:
- Displays total memory usage with a bar graph.
- Shows memory usage of individual processes when a program name is provided.
- Supports human-readable memory units (e.g., MiB, GiB) with the `-H` option.
- Allows customization of the bar graph length with the `-l` option.
- Adheres to Linux conventions for process and memory information.

Modules Used:
- argparse: Handles command-line arguments.
- os: Interacts with the system to retrieve process IDs.
- sys: Provides access to system-specific parameters and functions.

This script is designed to help users quickly understand memory usage patterns,
making it easier to monitor and debug memory-related issues on a Linux system.


'''


import argparse
import os, sys

# Import functions from external files
from percenttograph import percent_to_graph
from getsysmem import get_sys_mem
from getavailmem import get_avail_mem
from parseargs import parse_command_args
from pidsprog import pids_of_prog
from rssmem import rss_mem_of_pid

# Convert bytes to human-readable format
def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """
    Convert memory size from KiB to a human-readable format.
    """
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes) - 1:
        result /= 1024
        suf_count += 1
    return f"{result:.{decimal_places}f} {suffixes[suf_count]}"

# Main logic
if __name__ == "__main__":
    args = parse_command_args()

    # Total memory usage
    total_mem = get_sys_mem()
    available_mem = get_avail_mem()
    used_mem = total_mem - available_mem
    used_percent = used_mem / total_mem

    if args.program:
        # Process-specific memory usage
        pids = pids_of_prog(args.program)
        total_rss = 0
        for pid in pids:
            rss_mem = rss_mem_of_pid(pid)
            total_rss += rss_mem
            bar = percent_to_graph(rss_mem / total_mem, args.length)
            if args.human_readable:
                print(f"{pid:<10} {bar} {bytes_to_human_r(rss_mem)}/{bytes_to_human_r(total_mem)}")
            else:
                print(f"{pid:<10} {bar} {rss_mem}/{total_mem}")
        # Total for the program
        bar = percent_to_graph(total_rss / total_mem, args.length)
        if args.human_readable:
            print(f"{args.program:<10} {bar} {bytes_to_human_r(total_rss)}/{bytes_to_human_r(total_mem)}")
        else:
            print(f"{args.program:<10} {bar} {total_rss}/{total_mem}")
    else:
        # Total system memory usage
        bar = percent_to_graph(used_percent, args.length)
        if args.human_readable:
            print(f"Memory         [{bar}| {used_percent*100:.0f}%] {bytes_to_human_r(used_mem)}/{bytes_to_human_r(total_mem)}")
        else:
            print(f"Memory         [{bar}| {used_percent*100:.0f}%] {used_mem}/{total_mem}")
