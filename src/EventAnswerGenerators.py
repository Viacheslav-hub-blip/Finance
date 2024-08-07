from src.GROQ import Model
from typing import NamedTuple
import ast
from src.PeriodGetter import Period_Getter, Period


class Event_Type(NamedTuple):
    company: str
    event: str
    description: str
    change_stock_price: str
    semantic: str


class EventCreator():
    ''''
    создает список обьектов Event из словаря ответов языковой модели
    '''

    def __init__(self, answers_dict):
        self.answers_dict = answers_dict

    def _create_events_from_dict(self, answers_dict: [{}]) -> [Event_Type]:
        """из словаря создаем массив Event"""
        Events = []

        for answer in answers_dict:
            print(answer)
            dict = answer[0]
            ev = Event_Type('error', 'error', 'error', 'error', 'error')
            try:
                ev = Event_Type(dict['COMPANY'], dict['EVENT'], dict['DESCRIPTION'],
                                dict['CHANGE_STOCK_PRICE'],
                                dict['SEMANTIC'])
            except:
                print("неправильный формат ответа")

            Events.append(ev)

        return Events

    def get_events(self) -> [Event_Type]:
        return self._create_events_from_dict(self.answers_dict)


class AnswerGenerator():
    '''
    Получает периоды изменения курса акций -> возвращает список с ответами модели(обьяснение изменения)
    '''
    model_key_api: str
    periods: []
    question: str

    def __init__(self, model_key_api, periods, prompt):
        self.model_key_api = model_key_api
        self.periods = periods
        self.question = prompt

    def _get_answer_on_periods(self, all_periods: [Period]) -> []:
        """получает список обьектов Period и преобразует в список ответов языковой модели"""
        answers = []
        for i in all_periods:
            question = self.question.format(i.company, i.start_date, i.end_date, i.change)
            model = Model(key=self.model_key_api)
            answer = model.get_answer(question)
            answers.append(answer)
        return answers

    def _parse_answer(self, answer: str) -> []:
        """Получает список ответов языковой модели и удаляет лишние слова, строки -> преобразует в сьроковый формат dict"""
        res = []

        answer = answer.replace("{", "*{")
        answer = answer.replace("}", "}*")
        print('parse_answer', answer)
        x = answer.split("*")
        print('x', x)

        for i in x:
            if i.startswith("{") and i.endswith("}"):
                res.append(i)

        print('res', res)
        return res

    def _get_dict_after_parse(self, parsed_answers: []) -> []:
        """Получает обработанный ответ языковой модели и преобразует в dict"""
        res_dict = []
        for i in parsed_answers:
            result = ast.literal_eval(i)
            res_dict.append(result)

        print('get_dict', res_dict)

        return res_dict

    def get_answers_on_periods(self) -> [{}]:
        answers = self._get_answer_on_periods(self.periods)
        answers_dicts = []
        for answer in answers:
            parsed_answer = self._parse_answer(answer)
            mapped_answer_to_dict = self._get_dict_after_parse(parsed_answer)
            answers_dicts.append(mapped_answer_to_dict)
        return answers_dicts


if __name__ == "__main__":
    # ВКЛЮЧИТЬ VPN!!!!!!!!!!!!!!!!!!
    s = "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"
    ar_data = {'2022-01-03': 180.33904722092433, '2022-01-04': 180.3982048932326, '2022-01-05': 177.6666794522193,
               '2022-01-06': 172.86432004724844, '2022-01-07': 171.7204462075955, '2022-01-10': 170.1032520387883,
               '2022-01-11': 172.74603198621736, '2022-01-12': 174.7182092125996, '2022-01-13': 174.16600315657104,
               '2022-01-14': 171.36550159833055, '2022-01-18': 170.14268560308685, '2022-01-19': 168.70301497913653,
               '2022-01-20': 167.32243930012962, '2022-01-21': 164.018975211671, '2022-01-24': 160.04499528082962,
               '2022-01-25': 160.4986044346938, '2022-01-26': 162.10594712858335, '2022-01-27': 161.56357070593663,
               '2022-01-28': 167.983135753714, '2022-01-31': 172.56850696964707, '2022-02-01': 172.41076011558698,
               '2022-02-02': 173.43627272196204, '2022-02-03': 173.79126979950706, '2022-02-04': 171.89976069436705,
               '2022-02-07': 171.75163795549324, '2022-02-08': 173.13396171924924, '2022-02-09': 174.41751949539008,
               '2022-02-10': 173.2623316210006, '2022-02-11': 170.89266472448745, '2022-02-14': 167.43686272054998,
               '2022-02-15': 170.76430482421443, '2022-02-16': 171.14936377362403, '2022-02-17': 169.7374492315471,
               '2022-02-18': 168.38472780193263, '2022-02-22': 164.5834059978904, '2022-02-23': 164.0502222358277,
               '2022-02-24': 160.7919447982649, '2022-02-25': 163.03322425695418, '2022-02-28': 163.32946058774525,
               '2022-03-01': 164.4945683903717, '2022-03-02': 165.24494039015102, '2022-03-03': 166.77534990993806,
               '2022-03-04': 163.45779088712348, '2022-03-07': 162.93451728637865, '2022-03-08': 160.82155472792724,
               '2022-03-09': 161.344879328565, '2022-03-10': 158.36300968048798, '2022-03-11': 157.2670524854861,
               '2022-03-14': 152.1722594446784, '2022-03-15': 153.6039342954496, '2022-03-16': 157.9779575079191,
               '2022-03-17': 158.96530558618755, '2022-03-18': 162.40133492222668, '2022-03-21': 164.24772064034795,
               '2022-03-22': 167.2789011970964, '2022-03-23': 170.45821239699626, '2022-03-24': 171.93923996079144,
               '2022-03-25': 173.06483751110625, '2022-03-28': 173.5091604436738, '2022-03-29': 176.74767453101398,
               '2022-03-30': 177.34011923441986, '2022-03-31': 175.78008178782005, '2022-04-01': 172.66988981337443,
               '2022-04-04': 176.23426186391876, '2022-04-05': 176.0466847102787, '2022-04-06': 171.43568680584949,
               '2022-04-07': 171.1691063679234, '2022-04-08': 169.60907418331664, '2022-04-11': 166.89383558708428,
               '2022-04-12': 167.7232150172138, '2022-04-13': 168.87841691593871, '2022-04-14': 169.1055167246455,
               '2022-04-18': 164.49454968997628, '2022-04-19': 165.6991139070027, '2022-04-20': 166.74573382452937,
               '2022-04-21': 169.36222403818198, '2022-04-22': 165.74847922912687, '2022-04-25': 161.10790742234119,
               '2022-04-26': 160.28836963672174, '2022-04-27': 157.770616624801, '2022-04-28': 162.44081338187044,
               '2022-04-29': 164.09957194748955, '2022-05-02': 156.23030678802172, '2022-05-03': 158.67897432234906,
               '2022-05-04': 164.37603786939437, '2022-05-05': 162.00637171026727, '2022-05-06': 157.6563011138173,
               '2022-05-09': 154.08671556547696, '2022-05-10': 154.98655803651522, '2022-05-11': 153.71093987243302,
               '2022-05-12': 144.56442687779335, '2022-05-13': 146.443178741056, '2022-05-16': 145.86967981759375,
               '2022-05-17': 148.094519484629, '2022-05-18': 145.71147409406072, '2022-05-19': 140.07524259698587,
               '2022-05-20': 139.12597477479417, '2022-05-23': 141.65733384747773, '2022-05-24': 140.381753606561,
               '2022-05-25': 140.20376421597848, '2022-05-26': 142.72522624660758, '2022-05-27': 148.0054882548772,
               '2022-05-31': 148.97457370239113, '2022-06-01': 150.04245773889076, '2022-06-02': 149.57772845826625,
               '2022-06-03': 146.31462245154594, '2022-06-06': 146.9079503180405, '2022-06-07': 147.33312055920365,
               '2022-06-08': 148.1933849720813, '2022-06-09': 146.29484379276224, '2022-06-10': 139.18528162445682,
               '2022-06-13': 133.68749875262418, '2022-06-14': 132.39214355181187, '2022-06-15': 135.80358410422494,
               '2022-06-16': 130.90893145837705, '2022-06-17': 131.59119532254587, '2022-06-21': 135.52666510309132,
               '2022-06-22': 136.21888934724515, '2022-06-23': 137.03957206270437, '2022-06-24': 140.32244431749157,
               '2022-06-27': 141.8847550770621, '2022-06-28': 141.81554761684743, '2022-06-29': 139.0963173941443}

    period_getter = Period_Getter(ar_data, 6, 'APPL')

    decline_periods = period_getter.get_decline_periods()
    rise_period = period_getter.get_rise_periods()

    print('decline', decline_periods)
    print('rise', rise_period)

    prompt_decline = 'What is the reason for the fall in the company shares <{0}> in the period from <{1}> to <{2}> by {3}?Answer in JSON format with the fields COMPANY, EVENT (the event that occurred), DESCRIPTION (how it affected the development of the company), CHANGE_STOCK_PRICE (as a percentage), SEMANTIC(NEGATIVE OR POSITIVE).Take into account only the nearest events to these dates. Do not respond in other formats and do not add words in parentheses.'
    prompt_rise = 'What is the reason for the growth of the companys shares <{0}> in the period from <{1}> to <{2}> by {3}?Answer in JSON format with the fields COMPANY, EVENT (the event that occurred), DESCRIPTION (how it affected the development of the company), CHANGE_STOCK_PRICE (as a percentage), SEMANTIC(NEGATIVE OR POSITIVE).Take into account only the nearest events to these dates. Do not respond in other formats and do not add words in parentheses.'

    answer_generator_decline = AnswerGenerator(s, decline_periods, prompt_decline)
    answer_decline_dict = answer_generator_decline.get_answers_on_periods()

    print('decline answer', answer_generator_decline)

    answer_generator_rise = AnswerGenerator(s, rise_period, prompt_rise)
    answer_rise_dict = answer_generator_rise.get_answers_on_periods()

    print('rise answer', answer_generator_rise)

    all_answers = [answer_decline_dict, answer_rise_dict]

    for ans in all_answers:
        print(ans)
