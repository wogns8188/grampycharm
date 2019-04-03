import pandas as pd
from libs.naverShopping.excelSaver import save


df = pd.read_json('./naverShopping.json')
df['price']=df['price'].str.replace(',','').astype(float)

dfSorted = df.sort_values(['price'])
dfPriceTop5 = dfSorted.head(10)
dfPriceReverseTop5 = df.sort_values(['price'], ascending=[0]).head(10)

dfs=[
    {'df':dfSorted, "sheetName":'sorted'},
    {'df':dfPriceTop5, 'sheetName':'priceTop5'},
    {'df':dfPriceReverseTop5, 'sheetName':'priceReverseTop5'}
]
save(dfs, 'priceAnalyze.xlsx')

