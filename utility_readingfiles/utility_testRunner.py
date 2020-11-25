from datetime import datetime
import pandas as pd
import datetime
import json
# import utility_readingfiles.read_files as rf
# import logging
# import datacompy
# import db_dw_connect as dbc


class utility_testRunner:
    def __init__(self):
        # logging.info('Start utility_testRunner')
        # self.file_location = file_location
        print('Start utility_testRunner')

    def read_datasource(self, file_location):
        data_set = pd.read_csv(file_location)
        return data_set
