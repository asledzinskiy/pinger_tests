import subprocess
from typing import Optional
from settings import pinger_binary_path


def run_pinger(
    config_file: Optional[str] = None,
    report_file: Optional[str] = None,
    expected_exit_code: Optional[int] = None,
) -> str:
    """
    Executes a Pinger binary file with input config and output report files.

    Args:
        config_file: Path to the config file to pass as a system argument. (Optional)
        report_file: Path to the report file to pass as a system argument. (Optional)
        expected_exit_code: Expected exit code of the binary (0 or 1).
                             If provided, the function will check if the
                             actual exit code matches. If not, it will raise
                             a RuntimeError. (Optional)

    Returns:
        The standard output (stdout) of the executed binary as a string.

    Raises:
        FileNotFoundError: If the specified 'binary_path' does not exist.
        RuntimeError: If 'expected_exit_code' is provided and the actual
                      exit code of the binary does not match.
    """

    if not pinger_binary_path:
        raise EnvironmentError("The environment variable PINGER_BINARY must be set.")

    args = [pinger_binary_path]
    if config_file:
        args.append(config_file)
    if report_file:
        args.append(report_file)

    try:
        result = subprocess.run(args, capture_output=True, text=True, check=False)

        if expected_exit_code is not None and result.returncode != expected_exit_code:
            raise RuntimeError(
                f"Binary '{pinger_binary_path}' exited with code {result.returncode}, "
                f"expected {expected_exit_code}.\n"
                f"Stdout: {result.stdout}\n"
                f"Stderr: {result.stderr}"
            )

        return result.stdout.strip()
    except Exception as e:
        raise RuntimeError(f"Error executing binary '{pinger_binary_path}': {e}")
