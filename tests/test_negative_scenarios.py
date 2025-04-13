import pytest

from utils import config_creator, pinger_executor
from test_data import endpoints
from logger import default_logger
from utils import config_creator, pinger_executor
from test_data import endpoints
from logger import default_logger


class TestNegativeScenarios:

    @pytest.mark.negative
    @pytest.mark.regression
    def test_invalid_ip(self, tmp_path):
        """"
        Scenario with 1 invalid endpoint, min_successful_pings - 1, max_pings - 1

        Steps:
        1. Create a config containing 1 invalid endpoint.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   The application should display a validation error message
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, endpoints.invalid_ip)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Endpoint ip is invalid. No checks will be performed"
        assert expected_status in stdout_lines, f"validation message is not present in stdout {stdout_lines}"

    @pytest.mark.negative
    @pytest.mark.regression
    def test_invalid_data_types(self, tmp_path):
        """"
        Scenario with invalid data types

        Steps:
        1. Create a config containing endpoint with invalid data types.
        2. Set `min_successful_pings` to `one`.
        3. Set `max_pings` to `two`.
        4. Run the pinger

        Expected Results:
        -   The application should display a validation error message
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, "one", "two", endpoints.invalid_data_type)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Config data is invalid"
        assert expected_status in stdout_lines, f"validation message is not present in stdout {stdout_lines}"

    @pytest.mark.negative
    @pytest.mark.regression
    def test_negative_ping_numbers(self, tmp_path):
        """"
        Scenario with negative ping numbers

        Steps:
        1. Create a config containing 1 valid endpoint.
        2. Set `min_successful_pings` to `-1`.
        3. Set `max_pings` to `-1`.
        4. Run the pinger

        Expected Results:
        -   The application should display a validation error message
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, -1, -1, endpoints.one_valid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Max and min number of pings can't be negative"
        assert expected_status in stdout_lines, f"validation message is not present in stdout {stdout_lines}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_no_config(self, tmp_path):
        """"
        Scenario with no config

        Steps:
        1. Attempt to execute the pinger application without providing any command-line argument for the configuration file path

        Expected Results:
        -   The application should display a user-friendly message indicating how to provide the configuration file path
        """
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger()
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Usage: [path_to_json_file] [path_to_result_file]"
        assert expected_status in stdout_lines, f"Help message not in the stdout: {stdout_lines}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_non_existent_path(self, tmp_path):
        """"
        Scenario with non-existent config path

        Steps:
        1. Attempt to execute the pinger application without providing any command-line argument for the configuration file path

        Expected Results:
        -   The application should display a user-friendly message indicating how to provide the configuration file path
        """
        path = f"{tmp_path}/404.json"
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Provided config path doesn't exist"
        assert expected_status in stdout_lines, f"Validation message not in the stdout: {stdout_lines}"
