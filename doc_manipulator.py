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


class DocManipulator:
    def __init__(self, document):
        self.document = docx.Document(document)

    def replace_info(self, new_info):
        for p in self.document.paragraphs:
            replace_string('$date', new_info['date'], p)
            replace_string('$name', new_info['name'], p)
            replace_string('$company', new_info['company'], p)
            replace_string('$address', new_info['address'], p)
            replace_string('$city', new_info['city_postal'], p)
            replace_string('$subject', new_info['subject'], p)
            replace_string('$gender', new_info['gender'], p)
            replace_string('$position', new_info['position_title'], p)
        self.document.save(new_info['fileName'])
