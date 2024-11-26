def rss_mem_of_pid(proc_id: str) -> int:
    """
    Given a process ID, return the resident memory used (RSS) in kB.

    Args:
        proc_id (str): The process ID.

    Returns:
        int: RSS memory in kB, or 0 if not found.
    """
    try:
        with open(f"/proc/{proc_id}/status", "r") as status_file:
            for line in status_file:
                if line.startswith("VmRSS:"):
                    return int(line.split()[1])  # Memory value in kB
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    print(rss_mem_of_pid("1"))  # For manual testing
