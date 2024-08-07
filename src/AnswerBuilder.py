import ast

from src.GROQ import Model
from src.PeriodBuilder_v2 import Period
from src.AnswerLoaderFile import AnswerLoader


class AnswerBuilder:
    def __init__(self, model, periods: [Period], question: str):
        self.model = model
        self.periods = periods
        self.question = question

    def get_answer_list(self) -> []:
        answers = []
        for period in self.periods:
            answer = self.model.get_answer(self.question.format(
                period.company,
                period.start_date,
                period.end_date,
                period.change))
            #print('ans', answer)
            answer = self.format_answer(answer)
            answer = self.answer_to_dict(answer)
            answers.append(answer)
        return answers

    def format_answer(self, answer: str):
        '''
        parse_answer [
        *{
        "COMPANY": "APPL",
        "EVENT": "Apple WWDC 2022",
        "DESCRIPTION": ...
         "CHANGE_STOCK_PRICE": 6.67,
        "SEMANTIC": "POSITIVE"
        }*
        ]
        elements ['[\n    ', '{\n        "COMPANY": "APPL",\n
         "EVENT": "Apple WWDC 2022",\n
          "DESCRIPTION": ...
           "CHANGE_STOCK_PRICE": 6.67,\n
            "SEMANTIC": "POSITIVE"\n    }', '\n]']
        '''

        answer = answer.replace("{", "*{")
        answer = answer.replace("}", "}*")
        elements = answer.split("*")

        for element in elements:
            if element.startswith("{") and element.endswith("}"):
                answer = element

        return answer

    def answer_to_dict(self, answer: str):
        answer = ast.literal_eval(answer)
        return answer


if __name__ == "__main__":
    test_periods = [Period(company='APPL', start_date='2022-01-27', end_date='2022-01-31', start_value=161.56357070593663,
                           end_value=172.56850696964707, change=6.812),
                    Period(company='APPL', start_date='2022-03-14', end_date='2022-03-30', start_value=152.1722594446784,
                           end_value=177.34011923441986, change=16.539),
                    Period(company='APPL', start_date='2022-05-25', end_date='2022-06-01', start_value=140.20376421597848,
                           end_value=150.04245773889076, change=7.017),
                    Period(company='APPL', start_date='2022-06-16', end_date='2022-06-27', start_value=130.90893145837705,
                           end_value=141.8847550770621, change=8.384)]

    key = "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"
    prompt_rise = 'What is the reason for the growth of the companys shares <{0}> in the period from <{1}> to <{2}> by {3}?Answer in JSON format with the fields COMPANY, EVENT (the event that occurred), DESCRIPTION (How it affected the development of the company? Use your knowledge of the company to draw a conclusion),SEMANTIC(NEGATIVE OR POSITIVE).Take into account only the nearest events to these dates. Do not respond in other formats and do not add words in parentheses.'

    model = Model(key)
    answer_builder = AnswerBuilder(model, test_periods, prompt_rise)
    answers  = answer_builder.get_answer_list()
    for answer in answers:
        print(answer)

    answer_loader = AnswerLoader(answers, 'test.jsonl')
    answer_loader.create_jsonl_file()
