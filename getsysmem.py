def get_sys_mem() -> int:
    """
    Returns the total system memory (MemTotal) in kB.
    """
    with open('/proc/meminfo', 'r') as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])  # Extract the memory value as an integer
    raise ValueError("Could not find MemTotal in /proc/meminfo")

if __name__ == "__main__":
    print(get_sys_mem())  # Expected: Total system memory in kB
