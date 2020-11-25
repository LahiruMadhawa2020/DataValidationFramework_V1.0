import pandas as pd
import pandas_profiling
from datetime import datetime
import datetime


class profilingBase:

    def __init__(self, dataframe_datasource):
        self.df = dataframe_datasource

# To generate both html and json reports
    def sourcedataprofiling(self):
        # run the profile report
        profile = self.df.profile_report(title='Pandas Profiling Report')
        # save the report as html file
        profile.to_file(output_file="reports_profiling_html/pandas_profiling_{}.html".format(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
        # save the report as json file
        profile.to_file(output_file="reports_profiling_json/pandas_profiling_{}.json".format(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))

# To generate only the html report
    def sourcedataprofilingjson(self):
        profile2 = self.df.profile_report(title='Two Pandas Profiling Report')
        # save the report as html file
        profile2.to_file(output_file="reports_profiling_html/pandas_profiling_{}.html".format(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
        # save the report as json file
        # profile2.to_file(output_file="reports_profiling_json/pandas_profiling_{}.json".format(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")))
