import yfinance as yf
import datetime
import warnings


def get_data_company(company: str, period: int, current_date: str, time_delta: int) -> dict:
    #получаем курс акций от какого то дня(current day) и на определенный период вперед
    company = yf.Ticker(company)
    current_date = [current_date]
    delta_time = datetime.timedelta(days=time_delta)
    ar_data = {}
    for i in range(period):
        next_date = str(([datetime.datetime.strptime(i, '%Y-%m-%d') + delta_time for i in current_date])[0])[0:10]
        print(next_date)
        data = company.history(start=current_date[0], end=next_date)
        try:
            key = str(data.iloc[0].name)[0:10]
            value = data.iloc[0]['High']
            ar_data[key] = value
        except:
            pass
        current_date = [next_date]
    return ar_data


if __name__ == '__main__':
    data = get_data_company('AAPL', 180, '2022-01-01', 1)
    print(data)
