Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> # Define holidays
>>> def get_easter_date(year):
...     a = year % 19
...     b = year // 100
...     c = year % 100
...     d = b // 4
...     e = b % 4
...     f = (b + 8) // 25
...     g = (b - f + 1) // 3
...     h = (19 * a + b - d - g + 15) % 30
...     i = c // 4
...     k = c % 4
...     l = (32 + 2 * e + 2 * i - h - k) % 7
...     m = (a + 11 * h + 22 * l) // 451
...     month = (h + l - 7 * m + 114) // 31
...     day = ((h + l - 7 * m + 114) % 31) + 1
...     return pd.Timestamp(year, month, day)
... 
>>> def is_holiday_season(date):
...     year = date.year
...     valentine = pd.Timestamp(year=year, month=2, day=14)
...     halloween = pd.Timestamp(year=year, month=10, day=31)
...     christmas = pd.Timestamp(year=year, month=12, day=25)
...     easter = get_easter_date(year)
...     holidays = [valentine, easter, halloween, christmas]
...     for holiday in holidays:
...         if (date - holiday).days in range(-7, 8):  # Within a week of the holiday
...             return True
...         return False
... 
...     
>>> def seasonal_factor(date):
...     if is_holiday_season(date):
...         return 1.5  # Higher demand during holiday seasons
...     elif date.month in [11, 12]:
...         return 1.2  # Higher demand in November and December
...     elif date.month in [6, 7, 8]:
...         return 0.8  # Lower demand in summer months
    else:
        return 1.0  # Normal demand for other months

    
# Example order data
data = {
    'order_date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'order_quantity': np.random.randint(100, 200, size=365)
    }
# Create DataFrame
df = pd.DataFrame(data)
# Apply seasonal factor
df['seasonal_factor'] = df['order_date'].apply(seasonal_factor)
# Feature engineering
df['month'] = df['order_date'].dt.month
df['day_of_week'] = df['order_date'].dt.dayofweek
df['previous_order_quantity'] = df['order_quantity'].shift(1).fillna(method='bfill')

Warning (from warnings module):
  File "<pyshell#55>", line 
FutureWarning: Series.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
df['previous_order_quantity'] = df['order_quantity'].shift(1).fillna('bfill')
df['future_demand'] = df['order_quantity'].shift(-1).fillna('ffill')
# Features and target
features = ['order_quantity', 'seasonal_factor', 'month', 'day_of_week', 'previous_order_quantity']
target = 'future_demand'
# Export DataFrame with predictions to Excel
output_file = 'seasonal_demand_predictions.xlsx'
df.to_excel(output_file, index=False)
print(f'Data with predictions exported to {output_file}')
Data with predictions exported to seasonal_demand_predictions.xlsx
SyntaxError: invalid syntax
print(f'Data with predictions exported to {output_file}')
Data with predictions exported to seasonal_demand_predictions.xlsx
