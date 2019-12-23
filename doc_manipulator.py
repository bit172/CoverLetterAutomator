import docx
import os


class DocManipulator:
    def __init__(self, document):
        self.document = docx.Document(document)

    def replace_info(self, new_info):
        pass
