def percent_to_graph(percent: float, length: int = 20) -> str:
    """
    Converts a percentage (0.0 to 1.0) into a string of hash (#) symbols and spaces.
    """
    if not (0.0 <= percent <= 1.0):
        raise ValueError("Percent must be between 0.0 and 1.0")

    filled_length = int(round(percent * length))
    return '#' * filled_length + ' ' * (length - filled_length)

if __name__ == "__main__":
    print(percent_to_graph(0.5))  # Expected: "##########          "
    print(percent_to_graph(0.75, 10))  # Expected: "#######   "
