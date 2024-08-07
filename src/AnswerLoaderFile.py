import random

import jsonlines


class AnswerLoader():
    output_file: str

    def __init__(self, events, output_file):
        self.answers = events
        self.output_file = output_file

    def create_jsonl_file(self):
        with open(self.output_file, 'w') as output_file:
            json_writer = jsonlines.Writer(output_file)
            for answer in self.answers:
                try:
                    json_writer.write(answer)
                except:
                    print('ошибка записи в фаил')
