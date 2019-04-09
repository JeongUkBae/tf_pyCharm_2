import pandas as pd
import folium

ctx = '../data/'
xls = ctx + '01. population_in_Seoul.xls'
csv = ctx +'01. CCTV_in_Seoul.csv'
pop_data = pd.read_excel(xls)
cctv_data = pd.read_csv(csv)

print(cctv_data.head())
print(pop_data.head())
