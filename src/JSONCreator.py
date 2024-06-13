import random

import jsonlines


class JSONLCreator():
    variable_answer = [
        'how can it affect',
        'how can people react to',
        'what happens after',
        'is it worth buying shares of the company after'
    ]
    events: []
    output_file: str

    def __init__(self, events, output_file):
        self.events = events
        self.output_file = output_file

    def create_jsonl_file(self):
        with open(self.output_file, 'w') as output_file:
            json_writer = jsonlines.Writer(output_file)
            for event in self.events:
                format = f"<s>[INST] <<SYS>> You are a respectful, helpful and honest stock market analysis assistant. You should give a forecast of the stock market's reaction to events that occur in the world or with a certain company. <</SYS>>" \
                         f" {self.variable_answer[random.randint(0, len(self.variable_answer) - 1)]} {event.event} with company {event.company}? [/INST] " \
                         f"{event.description} " \
                         f"stock_price_change : {event.change_stock_price} " \
                         f"semantic: {event.semantic} " \
                         f"company: {event.company} "
                json_writer.write({"text": format})
