# finance_calendars
Simple wrapper of NASDAQ public API for Financial Calendars.  This returns calendar data on *ALL* US stocks.

## Features
* Earnings Calendar
* IPO Calendar
* Dividends Calendar
* Dividends History per symbol
* Splits History

### Install
Use the following pip command:
```
pip install finance-calendars
```

## Methods & Classes
```
get_earnings_today()
```
Returns all US earnings reports due on today's date.

```
get_earnings_by_date(date:datetime = None)
```
Returns all US earnings reports due on the specified date.

```
get_priced_ipos_this_month()
```
Returns all US IPOs *priced* for the current month.  IPO data is reported by NASDAQ on a per month basis.

```
get_priced_ipos_by_month(date:datetime = None)
```
Returns all US IPOs *priced* for the specifed month.  IPO data is reported by NASDAQ on a per month basis.

```
get_filed_ipos_this_month()
```
Returns all US IPOs *filed* for the current month.  IPO data is reported by NASDAQ on a per month basis.

```
get_filed_ipos_by_month(date:datetime = None)
```
Returns all US IPOs *filed* for the specifed month.  IPO data is reported by NASDAQ on a per month basis.

```
get_upcoming_ipos_this_month()
```
Returns all *upcoming* US IPOs for the current month.  IPO data is reported by NASDAQ on a per month basis.

```
get_upcoming_ipos_by_month(date:datetime = None)
```
Returns all *upcoming* US IPOs for the specifed month.  IPO data is reported by NASDAQ on a per month basis.

```
get_withdrawn_ipos_this_month()
```
Returns all *withdrawn* US IPOs for the current month.  IPO data is reported by NASDAQ on a per month basis.

```
get_withdrawn_ipos_by_month(date:datetime = None)
```
Returns all *withdrawn* US IPOs for the specifed month.  IPO data is reported by NASDAQ on a per month basis.

```
get_dividends_today()
```
Returns all US stocks with an ex-dividends date today.

```
get_splits_by_date(date:datetime = None)
```
Returns all US stock with an ex-dividends date on the specified date.

```
get_splits_today()
```
Returns all US stock splits due on today's date.

```
get_splits_by_date(date:datetime = None)
```
Returns all US stock splits on the specified date.

```
get_div_hist_per_stock(symbol:str)
```
Returns all dividend history for the given stock.

```
get_div_hist_per_etf(symbol:str)
```
Returns all dividend history for the given ETF.

## Examples

```
from finance_calendars import finance_calendars as fc
from datetime import datetime, date
import pandas as pd

earnings =fc.get_earnings_today()
print(earnings[:5])

earnings = fc.get_earnings_by_date(datetime(2021, 8, 16, 0, 0))
print(earnings[:5])

dividends = fc.get_dividends_today()
print(dividends[:5])

dividends = fc.get_dividends_by_date(datetime(2021, 8, 16, 0, 0))
print(dividends[:5])

ipos = fc.get_priced_ipos_this_month()
print(ipos[:5])

ipos = fc.get_priced_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_filed_ipos_this_month()
print(ipos[:5])

ipos = fc.get_filed_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_withdrawn_ipos_this_month()
print(ipos[:5])

ipos = fc.get_withdrawn_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

ipos = fc.get_upcoming_ipos_this_month()
print(ipos[:5])

ipos = fc.get_upcoming_ipos_by_month(datetime(2021, 7, 1, 0, 0))
print(ipos[:5])

splits = fc.get_splits_today()
print(splits[:5])

splits = fc.get_splits_by_date(datetime(2021, 8, 16, 0, 0))
print(splits[:5])

div_hist = fc.get_div_hist_per_stock('AAPL')
print(div_hist)

div_hist = fc.get_div_hist_per_etf('VIG')
print(div_hist)
```

