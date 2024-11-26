import os

def pids_of_prog(app_name: str) -> list:
    """
    Given an app name, return all process IDs associated with it.

    Args:
        app_name (str): The name of the application.

    Returns:
        list: A list of process IDs as strings.
    """
    try:
        output = os.popen(f"pidof {app_name}").read().strip()
        return output.split() if output else []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    print(pids_of_prog("bash"))  # For manual testing
