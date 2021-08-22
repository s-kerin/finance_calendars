import requests
from datetime import datetime, date
import pandas as pd

# headers and params used to bypass NASDAQ's anti-scraping mechanism in function __exchange2df
headers = {
    'authority': 'api.nasdaq.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'origin': 'https://www.nasdaq.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nasdaq.com/',
    'accept-language': 'en-US,en;q=0.9',
}

def get_earnings_today():
    return get_earnings_by_date()

def get_earnings_by_date(date:datetime = None):
    url = 'https://api.nasdaq.com/api/calendar/earnings'
    return __get_calendar_query(url, date=date)

def get_dividends_today():
    return get_dividends_by_date()

def get_dividends_by_date(date:datetime = None):
    url = 'https://api.nasdaq.com/api/calendar/dividends'
    return __get_calendar_query(url, date=date, subcolumn=['calendar'])

def get_priced_ipos_this_month():
    return get_priced_ipos_by_month()

def get_priced_ipos_by_month(date:datetime = None):
    url = 'https://api.nasdaq.com/api/ipo/calendar'
    return __get_calendar_query(url, date=date, subcolumn=['priced'], date_is_month=True, symbolcol='proposedTickerSymbol')

def get_filed_ipos_this_month():
    return get_filed_ipos_by_month()

def get_filed_ipos_by_month(date:datetime = None):
    url = 'https://api.nasdaq.com/api/ipo/calendar'
    return __get_calendar_query(url, date=date, subcolumn=['filed'], date_is_month=True, symbolcol='proposedTickerSymbol')

def get_upcoming_ipos_this_month():
    return get_upcoming_ipos_by_month()

def get_upcoming_ipos_by_month(date:datetime = None):
    url = 'https://api.nasdaq.com/api/ipo/calendar'
    return __get_calendar_query(url, date=date, subcolumn=['upcoming', 'upcomingTable'], date_is_month=True, symbolcol='proposedTickerSymbol')

def get_withdrawn_ipos_this_month():
    return get_withdrawn_ipos_by_month()

def get_withdrawn_ipos_by_month(date:datetime = None):
    url = 'https://api.nasdaq.com/api/ipo/calendar'
    return __get_calendar_query(url, date=date, subcolumn=['withdrawn'], date_is_month=True, symbolcol='proposedTickerSymbol')

def get_splits_today():
    return get_splits_by_date()

def get_splits_by_date(date:datetime = None):
    url = 'https://api.nasdaq.com/api/calendar/splits'
    return __get_calendar_query(url, date=date)

def get_div_hist_per_stock(symbol:str):
    url = 'https://api.nasdaq.com/api/quote/' + symbol + '/dividends'
    params = {'assetclass' : 'stocks'}
    return __get_calendar_query(url, subcolumn=['dividends'], paramsin=params, symbolcol='exOrEffDate')

def get_div_hist_per_etf(symbol:str):
    url = 'https://api.nasdaq.com/api/quote/' + symbol + '/dividends'
    params = {'assetclass' : 'etf'}
    return __get_calendar_query(url, subcolumn=['dividends'], paramsin=params, symbolcol='exOrEffDate')


def __get_calendar_query(url:str, date:datetime = None, subcolumn:[str] = None, symbolcol:str = 'symbol', date_is_month:bool = False, paramsin=None):
    if paramsin is None:
        if date is None:
            if date_is_month:
                datestr = datetime.today().strftime('%Y-%m')
            else:
                datestr = datetime.today().strftime('%Y-%m-%d')
        else:
            if date_is_month:
                datestr = date.strftime('%Y-%m')
            else:
                datestr = date.strftime('%Y-%m-%d')

        params = {'date': datestr}
    else:
        params = paramsin

    response = requests.get(url, headers=headers, params=params)
    data = response.json()['data']
    if subcolumn is not None:
        for s in subcolumn:
           data = data[s]
    df = pd.DataFrame(data['rows'], columns=data['headers'])
    if len(df) > 0:
        df = df.set_index(symbolcol)
    return df

if __name__ == '__main__':

    earnings = get_earnings_today()
    print(earnings[:5])

    earnings = get_earnings_by_date(datetime(2021, 8, 16, 0, 0))
    print(earnings[:5])

    dividends = get_dividends_today()
    print(dividends[:5])

    dividends = get_dividends_by_date(datetime(2021, 8, 16, 0, 0))
    print(dividends[:5])

    ipos = get_priced_ipos_this_month()
    print(ipos[:5])

    ipos = get_priced_ipos_by_month(datetime(2021, 7, 1, 0, 0))
    print(ipos[:5])

    ipos = get_filed_ipos_this_month()
    print(ipos[:5])

    ipos = get_filed_ipos_by_month(datetime(2021, 7, 1, 0, 0))
    print(ipos[:5])

    ipos = get_withdrawn_ipos_this_month()
    print(ipos[:5])

    ipos = get_withdrawn_ipos_by_month(datetime(2021, 7, 1, 0, 0))
    print(ipos[:5])

    ipos = get_upcoming_ipos_this_month()
    print(ipos[:5])

    ipos = get_upcoming_ipos_by_month(datetime(2021, 7, 1, 0, 0))
    print(ipos[:5])

    splits = get_splits_today()
    print(splits[:5])

    splits = get_splits_by_date(datetime(2021, 8, 16, 0, 0))
    print(splits[:5])

    div_hist = get_div_hist_per_stock('AAPL')
    print(div_hist)

    div_hist = get_div_hist_per_etf('VIG')
    print(div_hist)
