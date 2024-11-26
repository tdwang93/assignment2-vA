def get_avail_mem() -> int:
    """
    Returns the available memory in kB.
    Handles both standard Linux and WSL scenarios.
    """
    memfree = 0
    swapfree = 0
    memavailable = 0

    with open('/proc/meminfo', 'r') as meminfo:
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
            elif line.startswith("MemFree:"):
                memfree = int(line.split()[1])
            elif line.startswith("SwapFree:"):
                swapfree = int(line.split()[1])

    # Handle WSL scenario
    if memavailable == 0:
        return memfree + swapfree
    return memavailable

if __name__ == "__main__":
    print(get_avail_mem())  # Expected: Available system memory in kB
