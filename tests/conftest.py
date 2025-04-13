import pytest

from utils import config_creator, pinger_executor, report_reader
from test_data import endpoints
from logger import default_logger


@pytest.fixture(scope="class")
def get_pinger_report(tmp_path_factory, request):
    """
    A fixture to execute pinger and return generated report as a dict.
    """
    config_temp_dir = tmp_path_factory.mktemp("pinger_conf")
    default_logger.info("Creating configuration file")
    config_path = config_creator.create_config(config_temp_dir, request.cls.min_pings,
                                               request.cls.max_pings, request.cls.data)
    report_path = f"{config_temp_dir}/reporting.json"
    default_logger.info("Executing Pinger")
    pinger_executor.run_pinger(config_path, report_path)
    return report_reader.read_json_report(report_path)
