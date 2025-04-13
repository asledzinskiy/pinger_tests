import pytest

from dateutil import parser
from test_data import endpoints

class TestReporting:
    min_pings = 2
    max_pings = 3
    data = endpoints.two_valid_one_invalid_endpoints


    @pytest.mark.reporting
    @pytest.mark.regression
    def test_start_end_time(self, get_pinger_report):
        """"
        Scenario to check start time is earlier than end time

        Steps:
        1. Prepare report
        2. Check start and end time

        Expected Results:
        -   The 'start_time' value in the report should be chronologically earlier than the 'end_time' value.
        """
        start_time = parser.isoparse(get_pinger_report['start_time'])
        end_time = parser.isoparse(get_pinger_report['end_time'])
        assert start_time < end_time, f"Start time is not earlier than end time," \
                                      f"start time is {start_time}, end time is {end_time}"

    @pytest.mark.reporting
    @pytest.mark.regression
    def test_min_max_pings(self, get_pinger_report):
        """"
        Scenario to check min/max pings equal to config values

        Steps:
        1. Prepare report
        2. Inspect the 'min_successful_pings' and 'max_pings' values in the generated report

        Expected Results:
        -   The 'min_successful_pings' value in the report should be 2.
        -   The 'max_pings' value should be 3, matching the configuration.
        """
        min_pings = get_pinger_report['min_successful_pings']
        max_pings = get_pinger_report['max_pings']
        assert min_pings == 2, f"Min pings value should be 2," \
                               f"actual value is {min_pings}"
        assert max_pings == 3, f"Max pings value should be 3," \
                               f"actual value is {max_pings}"

    @pytest.mark.reporting
    @pytest.mark.regression
    def test_check_entries_len(self, get_pinger_report):
        """"
        Check number of entries equals number of config endpoints

        Steps:
        1. Prepare report
        2. Inspect the 'entries' array in the generated report.

        Expected Results:
        -   The 'entries' array in the report should contain 3 elements
        """
        actual_len = len(get_pinger_report['entries'])
        expected_len = len(self.data)
        assert expected_len == actual_len, f"Not all Entries are in the report ," \
                                           f"actual entries are {get_pinger_report['entries']}"

    @pytest.mark.reporting
    @pytest.mark.regression
    def test_check_entries(self, get_pinger_report):
        """"
        Check report entries equals to config endpoints

        Steps:
        1. Prepare report
        2. Inspect the 'entries' array in the generated report.

        Expected Results:
        -   The 'entries' array in the report should contain 3 elements
        """
        actual_len = len(get_pinger_report['entries'])
        expected_len = len(self.data)
        assert expected_len == actual_len, f"Not all Entries are in the report ," \
                                           f"actual entries are {get_pinger_report['entries']}"
        report_entries = [item['endpoint'] for item in get_pinger_report['entries']]
        assert report_entries == self.data, f"Entries don't match, expected entries are {self.data}," \
                                            f"actual entries are {report_entries}"

    @pytest.mark.reporting
    @pytest.mark.regression
    def test_total_successful_pings(self, get_pinger_report):
        """"
        Check entries are correct - total/successful pings

        Steps:
        1. Prepare report
        2. Inspect the 'entries' array in the generated report.

        Expected Results:
        -   'total_pings' should be 2, and 'successful_pings' should be 2
        -   For the invalid endpoint, 'total_pings' should be 3, and 'successful_pings' should be 0.
        """
        valid_endpoints_total_pings = get_pinger_report['entries'][0]['total_pings']
        valid_endpoints_success_pings = get_pinger_report['entries'][0]['successful_pings']
        invalid_endpoints_total_pings = get_pinger_report['entries'][2]['total_pings']
        invalid_endpoints_success_pings = get_pinger_report['entries'][2]['successful_pings']

        assert invalid_endpoints_total_pings == 3, f"Invalid endpoints is expected to be pinged 3 times ," \
                                                   f"actual result is {invalid_endpoints_total_pings}"
        assert invalid_endpoints_success_pings == 0, f"Invalid endpoints is expected to be successfully pinged 0 times ," \
                                                     f"actual result is {invalid_endpoints_success_pings}"
        assert valid_endpoints_total_pings == 2, f"Valid endpoints is expected to be pinged 2 times ," \
                                                 f"actual result is {valid_endpoints_total_pings}"
        assert valid_endpoints_success_pings == 2, f"Valid endpoints is expected to be successfully pinged 2 times ," \
                                                   f"actual result is {valid_endpoints_success_pings}"
