""" This is the main class implemented with validation functions that tester starts writing test_cp cases
    This class has used main two packages to perform data assertions
    1. Great Expectation
    2. DataComPy
"""

import great_expectations as ge
import pandas as pdf
import json
from utils.globalvariabales import GlobalVariables as gbvar
import datacompy
from utils.utility import Utility
from IPython.display import display_html
import config


class Validation:
    # defining static array to extract results
    __validatedResults = []
    __pdf = pdf.DataFrame(index=None, columns=None)
    pandaFrame = None
    test_case_id = None

    def __init__(self):
        # Initiate test_cp case id
        self.test_case_id = str(Utility.generate_uuid())

    def expect_table_row_count_grater_than(self, count, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_table_row_count_to_be_between(min_value=count, result_format="COMPLETE",
                                                                              catch_exceptions=False,
                                                                              meta={
                                                                                    "validation_id": "expect_table_row_count_grater_than",
                                                                                    "test_case_id": self.test_case_id,
                                                                                    "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))

        return self

    def expect_table_row_count(self, count, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_table_row_count_to_equal(count, result_format="COMPLETE",
                                                                         catch_exceptions=False,
                                                                         meta={
                                                                                "validation_id": "expect_table_row_count",
                                                                                "test_case_id": self.test_case_id,
                                                                                "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expects_column_to_exist(self, column, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_to_exist(column, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expects_column_to_exist",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_values_to_be_unique(self, column, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_values_to_be_unique(column, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_values_to_be_unique",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_values_to_not_be_null(self, column, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_values_to_not_be_null(column, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_values_to_not_be_null",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_value_lengths_to_equal(self, column, value, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_value_lengths_to_equal(column, value, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_value_lengths_to_equal",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_values_to_match_regex(self, column, regex, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_values_to_match_regex(column, regex, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_values_to_match_regex",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_values_to_be_in_set(self, column, datalist, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_values_to_be_in_set(column, datalist, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_values_to_be_in_set",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_column_values_to_be_of_type(self, column, type, test_case_name):

        Validation.pandaFrame = ge.from_pandas(Validation.__pdf)
        geResult = Validation.pandaFrame.expect_column_values_to_be_of_type(column, type, result_format="COMPLETE",
                                                                catch_exceptions=False,
                                                                meta={
                                                                        "validation_id": "expect_column_values_to_be_in_set",
                                                                        "test_case_id": self.test_case_id,
                                                                        "test_case_name": test_case_name})
        gbvar._set_geresult(json.loads(str(geResult)))
        return self

    def expect_table1_all_rows_overlap_with_table2(self, dataset1, dataset2, joincolumn, test_case_name):

        validation_id = "expect_frames_all_raws_overlap"
        # test_cp panda frame
        gePandaFrame = ge.from_pandas(gbvar._get_testpdf())

        try:
            compare = datacompy.Compare(
                dataset1,
                dataset2,
                join_columns=joincolumn,  # You can also specify a list of columns
                df1_name='source',
                df2_name='target')

            status = compare.all_rows_overlap()

            if status is True:

                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)], catch_exceptions=False,result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": ""})
                gbvar._set_geresult(json.loads(str(geResult)))
                print(geResult)
                f = open("reports_comparison/report1a.html", "x")
                g = open("reports_comparison/report1a.html", "a")
                g.write(compare.report())
                # g.close()
                h = open("reports_comparison/report1a.html", "a")
                h.write(str(geResult))
                g.close()
            else:

                mismatch_pdf = compare.report(sample_count=self.sample_row_count)
                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)], catch_exceptions=False,result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": mismatch_pdf})

                gbvar._set_geresult(json.loads(str(geResult)))
                f = open("reports_comparison/report2a.html", "x")
                g = open("reports_comparison/report2a.html", "a")
                g.write(compare.report())
                # g.close()
                h = open("reports_comparison/report2a.html", "a")
                h.write(str(geResult))
                g.close()

        except Exception as error:

            compare = datacompy.Compare(
                    dataset1,
                    dataset2,
                    on_index=True,  # this is for generate report
                    df1_name='source',
                    df2_name='target')

            geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", ["False"], catch_exceptions=False, result_format="COMPLETE",
                                                                      meta={
                                                                          "validation_id": validation_id,
                                                                          "test_case_id": self.test_case_id,
                                                                          "exception": str(error),
                                                                          "test_case_name": self.test_case_name,
                                                                          "comparison_report": compare.report(),
                                                                          "df1_columns_not_in_df2": str(compare.df1_unq_columns()),
                                                                          "df2_columns_not_in_df1": str(compare.df2_unq_columns())})

            gbvar._set_geresult(json.loads(str(geResult)))
            f = open("reports_comparison/report3a.html", "x")
            g = open("reports_comparison/report3a.html", "a")
            g.write(compare.report())
            # g.close()
            h = open("reports_comparison/report3a.html", "a")
            h.write(str(geResult))
            g.close()

        # return self

    def expect_table1_is_subset_of_table2(self, dataset1, dataset2, joincolumn, test_case_name):

        validation_id = "expect_table is subset of"
        # test_cp panda frame
        gePandaFrame = ge.from_pandas(gbvar._get_testpdf())

        try:
            compare = datacompy.Compare(
                dataset1,
                dataset2,
                join_columns=joincolumn,  # You can also specify a list of columns
                df1_name='source',
                df2_name='targer')

            status = compare.subset()

            if status is True:

                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)], catch_exceptions=False,
                                                                          result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": ""})
                gbvar._set_geresult(json.loads(str(geResult)))
                print(geResult)
            else:

                mismatch_pdf = compare.report(sample_count=self.sample_row_count)
                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)], catch_exceptions=False,
                                                                          result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": mismatch_pdf})

                gbvar._set_geresult(json.loads(str(geResult)))

        except Exception as error:

            compare = datacompy.Compare(
                dataset1,
                dataset2,
                on_index=True,  # this is for generate report
                df1_name='source',
                df2_name='targer')

            geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", ["False"], catch_exceptions=False,
                                                                      result_format="COMPLETE",
                                                                      meta={
                                                                          "validation_id": validation_id,
                                                                          "test_case_id": self.test_case_id,
                                                                          "exception": str(error),
                                                                          "test_case_name": test_case_name,
                                                                          "comparison_report": compare.report(),
                                                                          "df1_columns_not_in_df2": str(compare.df1_unq_columns()),
                                                                          "df2_columns_not_in_df1": str(compare.df2_unq_columns())})

            gbvar._set_geresult(json.loads(str(geResult)))

        return self

    def get_results(self):
        repo = pdf.json_normalize(gbvar._get_geresult(), max_level=3, errors='ignore')
        print(repo)
        repo.rename(columns={"meta.test_case_id": "meta_test_case_id"}, inplace=True)

        # seems this is not in proper place to call. this needs to call after all test cases executes
        Utility.generate_report()
        return repo[repo.meta_test_case_id == self.test_case_id]

    def compare_table1_values_with_table2_values(self, value1, value2):
        df1 = value1
        df2 = value2
        compare = datacompy.Compare(
            df1,
            df2,
            # You can also specify a list of columns
            # join_columns='ID',
            # if column names are not matching
            on_index=True,
            # Optional, defaults to 0
            # abs_tol=0,
            # Optional, defaults to 0
            # rel_tol=0,
            # Optional, defaults to 'df1'
            df1_name='Original',
            # Optional, defaults to 'df2'
            df2_name='New'
        )
        compare.matches(ignore_extra_columns=False)
        # False
        compare.all_rows_overlap()
        # This method prints out a human-readable report summarizing and sampling differences
        report = compare.report()
        f = open("reports_comparison/report11a.html", "x")
        g = open("reports_comparison/report11a.html", "a")
        g.write(report)
        g.close()
        return compare.all_rows_overlap()


    def expect_table1_value_to_be_equal_to_table2_value(self, value1, value2, test_case_name):

        validation_id = "comparing values in tables"
        # test_cp panda frame
        gePandaFrame = ge.from_pandas(gbvar._get_testpdf())

        if(isinstance(value1,pdf.core.series.Series) and isinstance(value2,pdf.core.series.Series)):

            # convert serial object back to data frame
            dataset1 = value1.to_frame()
            dataset2 = value2.to_frame()
            print(dataset1)
            print(dataset2)

            try:
                compare = datacompy.Compare(
                    dataset1,
                    dataset2,
                    join_columns=Utility.get_table_columns(dataset1),  # You can also specify a list of columns
                    df1_name='source',
                    df2_name='targer')

                status = compare.all_rows_overlap()

                if status is True:

                    geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)],
                                                                              catch_exceptions=False,
                                                                              result_format="COMPLETE",
                                                                              meta={
                                                                                  "validation_id": validation_id,
                                                                                  "test_case_id": self.test_case_id,
                                                                                  "test_case_name": test_case_name,
                                                                                  "comparison_report": ""})
                    gbvar._set_geresult(json.loads(str(geResult)))
                    f = open("reports_comparison/report7a.html", "x")
                    g = open("reports_comparison/report7a.html", "a")
                    g.write(compare.report())
                    # g.close()
                    h = open("reports_comparison/report7a.html", "a")
                    h.write(str(geResult))
                    h.close()

                else:

                    mismatch_pdf = compare.report(sample_count=self.sample_row_count)
                    geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", [str(status)],
                                                                              catch_exceptions=False,
                                                                              result_format="COMPLETE",
                                                                              meta={
                                                                                  "validation_id": validation_id,
                                                                                  "test_case_id": self.test_case_id,
                                                                                  "test_case_name": test_case_name,
                                                                                  "comparison_report": mismatch_pdf})

                    gbvar._set_geresult(json.loads(str(geResult)))
                    f = open("reports_comparison/report8a.html", "x")
                    g = open("reports_comparison/report8a.html", "a")
                    g.write(compare.report())
                    # g.close()
                    h = open("reports_comparison/report8a.html", "a")
                    h.write(str(geResult))
                    h.close()

            except Exception as error:

                compare = datacompy.Compare(
                    dataset1,
                    dataset2,
                    on_index=True,  # this is for generate report
                    df1_name='source',
                    df2_name='targer')

                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", ["False"], catch_exceptions=False,
                                                                          result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "exception": str(error),
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": compare.report(),
                                                                              "df1_columns_not_in_df2": str(
                                                                                  compare.df1_unq_columns()),
                                                                              "df2_columns_not_in_df1": str(
                                                                                  compare.df2_unq_columns())})

                gbvar._set_geresult(json.loads(str(geResult)))
                f = open("reports_comparison/report9a.html", "x")
                g = open("reports_comparison/report9a.html", "a")
                g.write(compare.report())
                # g. close()
                h = open("reports_comparison/report9a.html", "a")
                h.write(str(geResult))
                h.close()

        else:
                geResult = gePandaFrame.expect_column_values_to_be_in_set("test_cp", ["False"], catch_exceptions=False,
                                                                          result_format="COMPLETE",
                                                                          meta={
                                                                              "validation_id": validation_id,
                                                                              "test_case_id": self.test_case_id,
                                                                              "exception": "",
                                                                              "test_case_name": test_case_name,
                                                                              "comparison_report": "Result data set should be Pandas.core.series.Series"})

                gbvar._set_geresult(json.loads(str(geResult)))
                f = open("reports_comparison/report10a.html", "x")
                g = open("reports_comparison/report10a.html", "a")
                g.write(str(geResult))
                g.close()

        return self

    def run_validation_on(self, pdf):
        Validation.__pdf = pdf
        return self
