import pandas as pd

mini_df = pd.DataFrame(
    {'country': ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Greece', 'Turkey', 'Belgium', 'Hungary'],
     'capital': ['Berlin', 'Paris', 'Rome', 'Madrid', 'Warsaw', 'Athens', 'Ankara', 'Brussels', 'Budapest']})

for idx, row in mini_df.iterrows():
    if 'ar' in row['country'] or 'ar' in row['capital']:
        print(f"{row['country']} - {row['capital']}")

for t in mini_df.itertuples():
    if 'ar' in t.country or 'ar' in t.capital:
        print(f"{t.country} - {t.capital}")

from pprint import pprint
capitals = {i.country: i.capital for i in mini_df.itertuples()}
pprint(capitals)

# {'Belgium': 'Brussels',
#  'France': 'Paris',
#  'Germany': 'Berlin',
#  'Greece': 'Athens',
#  'Hungary': 'Budapest',
#  'Italy': 'Rome',
#  'Poland': 'Warsaw',
#  'Spain': 'Madrid',
#  'Turkey': 'Ankara'}
