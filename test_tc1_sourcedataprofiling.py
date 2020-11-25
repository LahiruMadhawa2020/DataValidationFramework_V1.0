import logging
from utility_readingfiles.testcsv import Testcsv
from config_validation_resultsreport.tablecreation import TbToValidate
from baseconfig_dataProfiling.dataprofiling_base import profilingBase
import pytest


@pytest.fixture
def csv_source_tc01():
    # test_source = TbToValidate(Testcsv(), utils=utility).get_table(Testcsv.test_date)
    test_source = TbToValidate(Testcsv()).get_table(Testcsv.test_date)
    return test_source


@pytest.mark.run(order=1)
def test_source_profiling_tc01(csv_source_tc01):
    profiling_tc01 = profilingBase(csv_source_tc01)
    profiling_tc01.sourcedataprofiling()


