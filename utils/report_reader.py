import json
from typing import Dict


def read_json_report(report_path: str) -> Dict:
    """
    Reads report file from the specified path and returns its content as a dictionary.

    Args:
        report_path: The path to the JSON report file to be read. (Required)

    Returns:
        A dictionary representing the data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the specified 'report_path' does not exist.
        json.JSONDecodeError: If the content of the file is not valid JSON.
        IOError: If there is an error reading the file.
    """
    try:
        with open(report_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Report file not found at: {report_path}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in file: {report_path}. Error: {e.msg}", e.doc, e.pos)
    except IOError as e:
        raise IOError(f"Error reading file: {report_path}. Error: {e}")
