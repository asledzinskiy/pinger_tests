import pytest

from utils import config_creator, pinger_executor
from test_data import endpoints
from logger import default_logger


class TestPinging:

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_2min_3max_pings(self, tmp_path):
        """"
        Scenario with 1 valid endpoint, min_successful_pings - 2, max_pings - 3

        Steps:
        1. Create a config containing 1 valid endpoint.
        2. Set `min_successful_pings` to `2`.
        3. Set `max_pings` to `3`.
        4. Run the pinger

        Expected Results:
        -   The application should execute ping exactly 2 times, not 3
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 2, 3, endpoints.one_valid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_description = "Checking availability of 1.1.1.1 [Cloudflare DNS]..."
        expected_status = "OK [2/2]"
        errors = []
        if not stdout_lines[-1] == expected_status:
            errors.append(f"Expected status is {expected_status}, got - {stdout_lines[-1]}")
        if not stdout_lines[-2] == expected_description:
            errors.append(f"Expected desc is {expected_description}, got - {stdout_lines[-2]}")
        assert not errors, f"Next checks failed: {errors}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_2min_2max_pings(self, tmp_path):
        """"
        Scenario with 3 valid endpoint, min_successful_pings - 2, max_pings - 2

        Steps:
        1. Create a config containing three valid endpoints.
        2. Set `min_successful_pings` to `2`.
        3. Set `max_pings` to `2`.
        4. Run the pinger

        Expected Results:
        -   The application should execute ping exactly 1 time, not 2
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 2, 2, endpoints.three_valid_endpoints)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "OK [1/1]"
        assert stdout_lines[-1] == expected_status, f"Expected status is {expected_status}," \
                                                    f" got - {stdout_lines[-1]}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_1min_2max_pings(self, tmp_path):
        """"
        Scenario with 1 unreachable endpoint, min_successful_pings - 1, max_pings - 2

        Steps:
        1. Create a config containing 1 unreachable endpoint.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `2`.
        4. Run the pinger

        Expected Results:
        -   The application should execute ping exactly 2 times
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 2, endpoints.one_invalid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "NOT OK [0/2]"
        assert stdout_lines[-1] == expected_status, f"Expected status is {expected_status}," \
                                                    f" got - {stdout_lines[-1]}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_0min_0max_pings(self, tmp_path):
        """"
        Scenario with 1 unreachable endpoint, min_successful_pings - 0, max_pings - 0

        Steps:
        1. Create a config containing 1 unreachable endpoint.
        2. Set `min_successful_pings` to `0`.
        3. Set `max_pings` to `0`.
        4. Run the pinger

        Expected Results:
        -   The endpoint should be effectively ignored; no ping attempts should be made
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 0, 0, endpoints.one_invalid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Checking availability of 191.111.1.1 [Cloudflare DNS]..."
        assert expected_status not in stdout_lines, f"191.111.1.1 endpoint is present in stdout {stdout_lines}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_0min_1max_pings(self, tmp_path):
        """"
        Scenario with 1 unreachable endpoint, min_successful_pings - 0, max_pings - 1

        Steps:
        1. Create a config containing 1 unreachable endpoint.
        2. Set `min_successful_pings` to `0`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   The status for this endpoint in the report should be 'ok'
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 0, 1, endpoints.one_invalid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "OK [0/0]"
        assert stdout_lines[-1] == expected_status, f"Expected status is {expected_status}," \
                                                    f" got - {stdout_lines[-1]}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_1min_0max_pings(self, tmp_path):
        """"
        Scenario with 1 unreachable endpoint, min_successful_pings - 1, max_pings - 0

        Steps:
        1. Create a config containing 1 unreachable endpoint.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `0`.
        4. Run the pinger

        Expected Results:
        -   The status for this endpoint in the report should NOT be 'ok'
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 0, endpoints.one_invalid_endpoint)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "NOT OK [0/1]"
        assert stdout_lines[-1] == expected_status, f"Expected status is {expected_status}," \
                                                    f" got - {stdout_lines[-1]}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_check_non_zero_exit_code(self, tmp_path):
        """"
        Scenario with 2 valid, 1 unreachable endpoints, min_successful_pings - 1, max_pings - 1

        Steps:
        1. Create a config containing 2 valid, 1 unreachable endpoints.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   The application should exit with a non-zero exit code (failure) because at least one endpoint is unreachable
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, endpoints.two_valid_one_invalid_endpoints)
        default_logger.info("Executing Pinger")
        pinger_executor.run_pinger(config_path, expected_exit_code=123)

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_check_zero_exit_code(self, tmp_path):
        """"
        Scenario with 1 valid endpoint, min_successful_pings - 1, max_pings - 1

        Steps:
        1. Create a config containing 1 valid endpoints.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   The application should exit with 0 exit code
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, endpoints.one_valid_endpoint)
        default_logger.info("Executing Pinger")
        with pytest.raises(RuntimeError) as exc_info:
            pinger_executor.run_pinger(config_path, expected_exit_code=0)
        assert exc_info.value is None, f"Code was executed with non-zero exit code." \
                                       f"Next exception was raised - {exc_info.value}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_ignore_field(self, tmp_path):
        """"
        Scenario with 2 valid endpoints, min_successful_pings - 1, max_pings - 1 and one is ignored

        Steps:
        1. Create a config containing 2 valid endpoints.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Set one endpoint 'ignore' field to True
        5. Run the pinger

        Expected Results:
        -   The ignored endpoint shouldn't be executed
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, endpoints.two_valid_ignored)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Checking availability of 8.8.8.8 [Google DNS]..."
        assert expected_status not in stdout_lines, f"8.8.8.8 endpoint is present in stdout {stdout_lines}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_many_endpoints(self, tmp_path):
        """"
        Scenario with 12 valid endpoints, min_successful_pings - 1, max_pings - 1

        Steps:
        1. Create a config containing 12 valid endpoints.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   All 12 endpoints are executed
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, endpoints.twelve_valid_endpoints)
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Checking availability of 8.8.8.8 [12th DNS]..."
        assert expected_status in stdout_lines, f"8.8.8.8 12th DNS endpoint is not present in stdout {stdout_lines}"

    @pytest.mark.pinging
    @pytest.mark.regression
    def test_empty_endpoints(self, tmp_path):
        """"
        Scenario with empty endpoints list, min_successful_pings - 1, max_pings - 1

        Steps:
        1. Create a config containing empty endpoints list.
        2. Set `min_successful_pings` to `1`.
        3. Set `max_pings` to `1`.
        4. Run the pinger

        Expected Results:
        -   The application should display a user-friendly message indicating that the endpoints list is empty and no pings will be performed.
        """
        default_logger.info("Creating configuration file")
        config_path = config_creator.create_config(tmp_path, 1, 1, [])
        default_logger.info("Executing Pinger")
        stdout = pinger_executor.run_pinger(config_path)
        default_logger.info("Checking Pinger output")
        stdout_lines = stdout.split("\n")
        expected_status = "Endpoint list is empty. No checks will be performed"
        assert expected_status in stdout_lines, f"validation message is not present in stdout {stdout_lines}"
