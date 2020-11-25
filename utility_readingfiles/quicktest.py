import pandas as pdf
from utility_readingfiles.localfilereader import LocalFileReader
from utility_readingfiles.flattningfiles import FlatteningFiles


class QuickTest(FlatteningFiles):

    question_master = None;
    question_items = None;

    def convert_to_pdf(self, **kwargs):
        json_content = LocalFileReader().read_json("input_filerepository/json")
        QuickTest.question_master = pdf.json_normalize(json_content, max_level=5, errors='ignore')
        QuickTest.question_items = pdf.json_normalize(json_content, 'itemResults', ['id'], errors='ignore', max_level=5,
                                                      record_prefix='items.')


