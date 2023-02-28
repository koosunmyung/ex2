import streamlit as st
import pandas as pd  # pip install pandas
import numpy as np
import datetime as dt


excel_file = 'finan.xlsx'
sheet_name = 'pp'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name)
#분기표시
df.기준일= pd.to_datetime(df.기준일)
df['qrt'] = df['기준일'].dt.to_period('Q')


lstday = str(df['기준일'].max(axis=0).year) + "-" + str(df['기준일'].max(axis=0).month)


def quarter_class(x):
  if 1<= x <4:
    return "1분기"
  if 4<= x <7:
    return "2분기"
  if 7<= x <10:
    return "3분기"
  if 10<= x <=12:
    return "4분기"

df['분기'] = df['전기월'].apply(quarter_class)


# print(lstday)
#손익 추출
# mask1 = (df['대분류'] != "재무상태") & (df['중분류'] != "기부금") & (df['quater'] == st.between(*quater_selection))
mask1 = (df['대분류'] != "재무상태") & (df['중분류'] != "기부금") # & (df['회계연도'] > 2018)
df = df.loc[mask1]
df['수입비용'] =["수입" if s == "매출" else "비용" for s in df["중분류"]]
for x in df.index: 
    if df.loc[x,'수입비용'] == "수입":
        df.loc[x,'매출']=df.loc[x,'금액']
        # df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
    else:
        df.loc[x,'비용']=df.loc[x,'금액']
df = df.groupby(['회계연도','수입비용', '중분류','보고반영', '분기', '전기월'])[['매출','비용','금액']].sum()

for x in df.index:         
  df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
 

df_base = (df.groupby(['회계연도','수입비용','중분류','보고반영','분기','전기월']).sum()/-100000000).round(1)
df_base.to_excel('F:/strea/STREAM/t_f_q/test13.xlsx')
# print(df)
