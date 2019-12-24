import docx
import os


def replace_string(old_text, new_text, p):
    if old_text in p.text:
        inline = p.runs
        # Loop added to work with runs (strings with same style)
        for i in range(len(inline)):
            if old_text in inline[i].text:
                text = inline[i].text.replace(old_text, new_text)
                inline[i].text = text
        print(p.text)


class DocManipulator:
    def __init__(self, document):
        self.document = docx.Document(document)

    def replace_info(self, new_info):
        for p in self.document.paragraphs:
            replace_string('$name', 'John Doe', p)
        self.document.save('dest1.docx')


if __name__ == '__main__':
    manipulator = DocManipulator("Cover Letter.docx")
    manipulator.replace_info(1)
    pass
