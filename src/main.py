import datetime
from random import shuffle

from src.AnswerBuilder import AnswerBuilder
from src.PeriodBuilder_v2 import PeriodBuilder
from src.GROQ import Model
from src.CompanyStockPrice import get_data_company
from src.AnswerLoaderFile import AnswerLoader

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    companies = [
        'ORCL',
        'TM',
        'MCD',
        'BA',
        'BK',
        'JPM',
        'BAC',
        'CVX',
        'DIS',
        'MS',
        'RY',
        'NKE',
        'AMZN',
        'META',
        'TSM',
        'V',
        'LLY',
        'SSNLF'
        'KO',
        'CSCO',
        'UNH',
        'HD',
        'MA',
        'ADBE',
    ]
    # company = 'TSLA'
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

    #companies = ['AAPL']

    prompt_rise = 'What is the reason for the growth of the companys shares <{0}> in the period from <{1}> to <{2}> by {3}?Answer in JSON format with the fields COMPANY(COMPANY TIKER), EVENT (the event that occurred), DESCRIPTION (How it affected the development of the company?), SEMANTIC(NEGATIVE OR POSITIVE). Do not respond in other formats and do not add words in parentheses.'
    prompt_decline = 'What is the reason decline of the companys shares <{0}> in the period from <{1}> to <{2}> by {3}?Answer in JSON format with the ONLY THIS fields COMPANY(COMPANY TIKER), EVENT (the event that occurred), DESCRIPTION (How it affected the development of the company? ),  SEMANTIC(NEGATIVE OR POSITIVE). Do not respond in other formats and do not add words in parentheses.'

    model_key = "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"

    period_builder = PeriodBuilder()
    model = Model(model_key)

    for comp in companies:
        prices  = get_data_company(comp, 2500, '2016-01-01', 1)
        decline_periods = period_builder.all_decline_periods(ar_data)
        decline_periods = period_builder.choose_periods_by_length_and_change(decline_periods, 3, 6)
        decline_periods = period_builder.create_Periods_list(comp, decline_periods)

        rise_periods = period_builder.all_rise_period(ar_data)
        rise_periods = period_builder.choose_periods_by_length_and_change(rise_periods, 3, 6)
        rise_periods = period_builder.create_Periods_list(comp, rise_periods)

        answer_builder_decline = AnswerBuilder(model, decline_periods, prompt_decline)
        answers_decline = answer_builder_decline.get_answer_list()

        answer_builder_rise = AnswerBuilder(model, rise_periods, prompt_rise)
        answers_rise = answer_builder_rise.get_answer_list()

        answers = []

        for ans in answers_rise:
            try:
                if comp == ans['COMPANY']:
                    answers.append(ans)
            except:
                pass

        for ans in answers_decline:
            try:
                if (comp == ans['COMPANY']):
                    answers.append(ans)
            except:
                pass

        shuffle(answers)
        print()
        for ans in answers:
            print(ans)

        answer_loader = AnswerLoader(answers, f'{comp}.jsonl')
        answer_loader.create_jsonl_file()

    t2 = datetime.datetime.now()
    print(t2 - t1)
