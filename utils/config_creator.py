import json
import os
import random
from typing import List, Dict


def create_config(
    dir_path: str,
    min_successful_pings: int,
    max_pings: int,
    endpoints: List[Dict[str, any]]
) -> str:
    """
    Generates a config configuration and saves it to a file in the provided directory.

    Args:
        dir_path: Path to the directory where the JSON file should be saved. (Required)
        min_successful_pings: Minimum number of successful pings required. (Required)
        max_pings: Maximum number of ping attempts to make. (Required)
        endpoints: A list of dictionaries, where each dictionary represents an
                   endpoint to ping. Each dictionary is expected to have at
                   least a key specifying the endpoint address (e.g., 'url', 'ip').
                   (Required)

    Returns:
        The full path to the generated configuration file in the format
        '{dir_name}/input_config_{random_integer}'.

    Raises:
        FileNotFoundError: If the provided 'dir_path' does not exist.
    """
    if not os.path.isdir(dir_path):
        raise FileNotFoundError(f"Directory not found: {dir_path}")

    config_data = {
        "min_successful_pings": min_successful_pings,
        "max_pings": max_pings,
        "endpoints": endpoints,
    }

    rand_int = random.randint(1000, 9999)
    file_name = f"input_config_{rand_int}.json"
    file_path = os.path.join(dir_path, file_name)

    try:
        with open(file_path, 'w') as f:
            json.dump(config_data, f, indent=4)
        return file_path
    except IOError as e:
        raise IOError(f"Error writing config file to {file_path}: {e}")
