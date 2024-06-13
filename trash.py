from src.EventAnswerGenerators import Event_Type

first = """
[
  {
    "EVENT": "Supply Chain Concerns",
    "DESCRIPTION": "Worries about supply chain disruptions and chip shortages",
    "CHANGE": -2.51
  },
  {
    "EVENT": "Microsoft's Earnings Report",
    "DESCRIPTION": "Microsoft's strong earnings report increased competition concerns",
    "CHANGE": -1.43
  },
  {
    "EVENT": "Nvidia's Earnings Report",
    "DESCRIPTION": "Nvidia's mixed earnings report raised concerns about tech industry",
    "CHANGE": -1.24
  },
  {
    "EVENT": "Federal Reserve Meeting",
    "DESCRIPTION": "Expectations of interest rate hike by Federal Reserve",
    "CHANGE": -1.83
  },
  {
    "EVENT": "Apple's Production Cuts",
    "DESCRIPTION": "Report of Apple's production cuts due to supply chain issues",
    "CHANGE": -2.39
  }
]

Note: The above response is based on historical data and may not reflect the exact change in Apple's stock price during the specified period. The events listed are some of the possible factors that could have contributed to the decline in Apple's stock price during that time.

"""
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
s = '''Apple Inc., вероятно, сократит прогнозируемые целевые показатели по производству iPhone 13 на 2021 год на целых 10 миллионов единиц, поскольку длительная нехватка чипов ударила по ее флагманскому продукту, по словам осведомленных людей.

Компания ожидала произвести 90 миллионов новых моделей iPhone за последние три месяца года, но теперь сообщает производственным партнерам, что общее количество будет ниже, потому что Broadcom Inc. и Texas Instruments Inc. испытывают трудности с поставкой достаточного количества компонентов, сказали люди, которые попросили не называть их имен, поскольку ситуация носит частный характер.\n

Технологический гигант является одним из крупнейших покупателей чипов в мире и ежегодно задает ритм для цепочки поставок электроники. Но даже при высокой покупательной способности Apple сталкивается с теми же перебоями в поставках, которые нанесли ущерб промышленным предприятиям по всему миру. Крупнейшие производители чипов предупредили, что спрос будет продолжать превышать предложение в течение следующего года и, возможно, в последующий период.\n

Apple закупает запчасти для дисплеев у Texas Instruments, в то время как Broadcom является ее давним поставщиком беспроводных компонентов. Нехватка одного чипа TI для последних iPhone связана с питанием OLED-дисплея. Apple также сталкивается с нехваткой компонентов у других поставщиков.'''

sys = """
Ты финансовый аналитик, который оценивает последние новости.

Пример вопроса: Как скажется на акциях компании Apple Сбои в цепочке поставок?
Ответ:Сообщения о сбоях в цепочке поставок в Китае, ключевом производственном центре Apple, вызвали обеспокоенность по поводу способности компании удовлетворять спрос и поддерживать прибыльность
Примерное изменение курса акций: -2.38%
семантика: ОТРИЦАТЕЛЬНО
"""

m_m = """Apple Inc. может снизить производство iPhone 13 на 10 миллионов единиц в 2021 году из-за нехватки чипов у поставщиков, таких как Broadcom и Texas Instruments.
"""

t = [
    Event_Type(company='AAPL', event='Microsoft quarterly earnings',
          description="Microsoft's quarterly earnings report was released, showing a strong performance. This led to a shift in investor sentiment towards Microsoft and away from Apple.",
          change_stock_price='-2.14', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Nvidia quarterly earnings',
          description="Nvidia's quarterly earnings report was released, showing a strong performance. This led to a shift in investor sentiment towards Nvidia and away from Apple.",
          change_stock_price='-1.45', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='iPhone 13 supply chain issues',
          description="Reports of supply chain issues affecting iPhone 13 production, leading to concerns about Apple's ability to meet demand.",
          change_stock_price='-2.35', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event="Apple's electric car project delays",
          description="Reports of delays in Apple's electric car project, leading to concerns about the company's ability to innovate and expand into new markets.",
          change_stock_price='-1.75', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Missed Earnings Estimates',
          description="Apple's quarterly earnings report missed Wall Street's expectations, sparking a sell-off in the stock.",
          change_stock_price='-6.51', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Supply Chain Disruptions',
          description="Rising COVID-19 cases in China led to lockdowns, disrupting Apple's supply chain and impacting production.",
          change_stock_price='-2.15', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Inflation Concerns',
          description="Rising inflation concerns in the US led to a broader market sell-off, affecting Apple's stock.",
          change_stock_price='-1.45', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Earnings report',
          description="Apple's Q2 2022 earnings report missed Wall Street's expectations, sparking a sell-off",
          change_stock_price='-6.0975609756097615%', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Missed Revenue Expectations',
          description="Apple's quarterly revenue fell short of Wall Street expectations", change_stock_price='-6.45',
          semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Earnings Report',
          description="Apple's Q2 2022 earnings report missed revenue expectations, citing supply chain issues and lockdowns in China.",
          change_stock_price='-6.08', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Inflation concerns',
          description='Fears of inflation weighed on tech stocks, including Apple, as investors worried about the impact of rising prices on consumer spending and corporate profit margins.',
          change_stock_price='-5.14', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Rate hike worries',
          description="The Federal Reserve's decision to raise interest rates by 0.75% sparked concerns about the impact on economic growth, leading to a sell-off in tech stocks, including Apple.",
          change_stock_price='-3.28', semantic='NEGATIVE'),
    Event_Type(company='AAPL', event='Supply chain disruptions',
          description="Reports of supply chain disruptions in China, a key manufacturing hub for Apple, raised concerns about the company's ability to meet demand and maintain profitability.",
          change_stock_price='-2.38', semantic='NEGATIVE'),

]
