# import logging
from utility_readingfiles.testcsv import Testcsv
from config_validation_resultsreport.tablecreation import TbToValidate
from baseconfig_dataProfiling.dataprofiling_base import profilingBase
from validationrules.validation import Validation
from config_validation_resultsreport.testresult import TestResult
from utility_readingfiles.utility_testRunner import utility_testRunner
import pytest
import logging.config


# logging.basicConfig(level='INFO')
# logging.config.fileConfig("config_logging/logging.conf")


# @pytest.fixture
# def csv_source():
#     logging.info('Start reading the csv file')
#     # test_source = TbToValidate(Testcsv(), utils=utility).get_table(Testcsv.test_date)
#     test_source = TbToValidate(Testcsv()).get_table(Testcsv.test_date)
#     # print(test_source)
#     logging.info('Return the csv DataFrame')
#     return test_source


@pytest.fixture()
def csv_source_s1():
    s1_file_location = 'input_filerepository/csv/csv_s1.csv'
    # logging.info('Start reading the csv file')
    test_source = utility_testRunner()
    test_source.read_datasource(s1_file_location)
    return test_source.read_datasource(s1_file_location)


@pytest.mark.run(order=1)
def test_source_profiling_tc01(csv_source_s1):
    # logging.info('started data profiling')
    profiling_tc01 = profilingBase(csv_source_s1)
    profiling_tc01.sourcedataprofiling()


@pytest.mark.run(order=2)
def test_source_csv_general(csv_source_s1):
    # csv_source_selection = csv_source[(csv_source.Age > 75)]
    result = Validation().run_validation_on(csv_source_s1).expect_column_values_to_be_unique("ID", "Test- Unique value")\
                                                          .expect_column_values_to_not_be_null("ID", "Test- Not Null")\
                                                          .expect_column_value_lengths_to_equal("Name", 4, "Length 4 ")\
                                                          .expect_column_values_to_be_of_type("Name", "object", "data type String only")\
                                                          .expect_column_values_to_be_in_set("Gender", ["M", "F"], "Values in List")\
                                                          .expect_column_values_to_match_regex("Email", "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)", "email format check")\
                                                          .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'


@pytest.mark.run(order=3)
def test_source_csv_business_validation(csv_source_s1):
    csv_source_selection = csv_source_s1[(csv_source_s1.Age > 75)]
    result = Validation().run_validation_on(csv_source_selection).expect_table_row_count(0, "More than 75 years old")\
                                                                 .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'


@pytest.fixture()
def csv_source_s2():
    s2_file_location = 'input_filerepository/csv/csv_s2.csv'
    # logging.info('Start reading the csv file')
    test_source = utility_testRunner()
    test_source.read_datasource(s2_file_location)
    return test_source.read_datasource(s2_file_location)


@pytest.mark.run(order=4)
def test_target_profiling_tc02(csv_source_s2):
    # logging.info('started data profiling')
    profiling_tc02 = profilingBase(csv_source_s2)
    profiling_tc02.sourcedataprofiling()


@pytest.mark.run(order=5)
def test_target_csv_general(csv_source_s2):
    # csv_source_selection = csv_source_s2[(csv_source_s2.Age > 75)]
    result = Validation().run_validation_on(csv_source_s2).expect_column_values_to_be_unique("ID", "Test- Unique value")\
                                                          .expect_column_values_to_not_be_null("ID", "Test- Not Null")\
                                                          .expect_column_value_lengths_to_equal("Name", 4, "Length 4 ")\
                                                          .expect_column_values_to_be_of_type("Name", "object", "data type String only")\
                                                          .expect_column_values_to_be_in_set("Gender", ["M", "F"], "Values in List")\
                                                          .expect_column_values_to_match_regex("Email", "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)", "email format check")\
                                                          .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'


@pytest.mark.run(order=6)
def test_target_csv_business_validation(csv_source_s2):
    csv_source_selection = csv_source_s1[(csv_source_s2.Age > 75)]
    result = Validation().run_validation_on(csv_source_selection).expect_table_row_count(0, "More than 75 years old")\
                                                                 .get_results()
    # perform PYTest Assertion
    assert TestResult().is_test_passed(result) == 'True'


# @pytest.mark.run(order=7)
# def test_source_target_comparison(csv_source_s1, csv_source_s2):
#     comparison = Validation().expect_table1_all_rows_overlap_with_table2(csv_source_s1, csv_source_s2, "ID", "csv_s1 comparison with csv_s2")
#     # perform pytest assertion
#     assert TestResult().is_test_passed(comparison) == 'True'


# @pytest.mark.run(order=7)
# def test_source_target_comparison(csv_source_s1, csv_source_s2):
#     comparison = Validation().expect_table1_value_to_be_equal_to_table2_value(csv_source_s1, csv_source_s2, "csv_s1 comparison with csv_s2")
#     # perform pytest assertion
#     assert TestResult().is_test_passed(comparison) == 'True'


@pytest.mark.run(order=7)
def test_source_target_comparison(csv_source_s1, csv_source_s2):
    comparison = Validation().compare_table1_values_with_table2_values(csv_source_s1, csv_source_s2)
    # perform pytest assertion
    assert comparison == 'True'

