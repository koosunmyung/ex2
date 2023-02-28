import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import plost
import numpy as np
import datetime as dt
from creatdf import df_base
from creatdf import lstday
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="년도별 손익", page_icon=":bar_chart:", layout="centered")



# st.set_page_config(page_title="년도별 손익2", page_icon=":bar_chart:", layout="centered")

st.subheader("최근 3개년 매출 추이")
df_b = df_base.reset_index()
mask = (df_b['수입비용'] == "수입") & (df_b['회계연도'] > 2019)
df_br = df_b.loc[mask]
df_br = df_br.groupby(['회계연도','전기월'])['금액'].sum()
df_br = df_br.reset_index()

# df = df_b
# clist = df['회계연도'].unique().tolist()
# print(clist)

# df_br.to_excel('F:/strea/STREAM/t_f_q/test11.xlsx')
image = Image.open('images/survey.jpg')
st.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)
def plot():
    df = df_br
    clist = df["회계연도"].unique().tolist()
    global countries
    countries = st.multiselect("select 회계연도", clist, default= clist)
    global dfs
    dfs = {country: df[df["회계연도"] == country] for country in countries}
    # print(dfs)
    fig = go.Figure()
    for country, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["전기월"], y=round(df["금액"],1), text=round(df["금액"],1), mode ='lines+text', textposition="top center", name=country))
    st.plotly_chart(fig)
plot()


contries = countries

# print(contries)

# df_b = df_base.reset_index()
# # number_of_result = df[mask].shape[0]
# # st.markdown(f'*Available Results: {number_of_result}*')                                         
# # age_selection = st.slider('Age:',
# #                         min_value= min(ages),
# #                         max_value= max(ages),
# #                         # value=(min(ages),max(ages)))
# #                         value=(min_value, max_value))


# # excel_file = 'F:/strea/STREAM/dbd_ex/finan.xlsx'
# # sheet_name = 'pp'

# # df = pd.read_excel(excel_file,
# #                    sheet_name=sheet_name)
# # #분기표시
# # df.기준일= pd.to_datetime(df.기준일)
# # df['quarter'] = df['기준일'].dt.to_period('Q')

# # #손익 추출
# mask1 = (df_b['대분류'] != "재무상태") & (df_b['중분류'] != "기부금")
# df = df_b.loc[mask1]
# df['수입비용'] =["수입" if s == "매출" else "비용" for s in df["중분류"]]
# for x in df.index: 
#     if df.loc[x,'수입비용'] == "수입":
#         df.loc[x,'매출']=df.loc[x,'금액']
#         # df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
#     else:
#         df.loc[x,'비용']=df.loc[x,'금액']
# df = df.groupby(['회계연도','수입비용', '중분류','보고반영'])[['매출','비용']].sum()

# for x in df.index:         
#   df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
 
# # # df.to_excel('C:/CODING/Streamlit/dashboard_ex/test00.xlsx')
# # # df = df.groupby(df(['회계연도','R','C','중분류','세분류','전기월','보고반영']))
# # # df_b = (df.groupby(['회계연도'])[['매출','비용', '중분류', '수입비용', '보고반영','금액']].sum()/-100000000).round(1)
# # df_b = (df.groupby(['회계연도','수입비용','중분류','보고반영']).sum()/-100000000).round(1)
# # df_base.to_excel('F:/strea/STREAM/dbd_ex/test0.xlsx')
 

# 연도별 손익요약(수입,비용,영업이익) 재구성
# print(countries)
df_b = df_base.reset_index()
df_b = df_b.groupby(['회계연도','분기'])[['매출','비용','금액', '영업이익']].sum()# df_b = (df.groupby(['회계연도'])[['매출','비용', '중분류', '수입비용', '보고반영','금액']].sum()/-100000000).round(1)
df_b = df_b.reset_index()
# print(df_b.columns)
# print(df_b['qrt'].unique().tolist())
global quarters
quarters = df_b['분기'].unique().tolist()
years = df_b['회계연도'].unique().tolist()

# year_selection = st.slider('years:',
#                         min_value= min(years),
#                         max_value= max(years),
#                         value=(min(years),max(years)))



tickers = years
# dropdown = st.multiselect('회계연도', tickers, default=tickers)
# dropdown2 = st.multiselect('분기', quarters, default=quarters)
dropdown2 = st.multiselect('분기', quarters, ['1분기','2분기','3분기','4분기'])
#                         # value=(min_value, max_value))
# quarter_selection = st.slider('분기선택:', 
#                                 min_value= min(quarters),
#                                 max_value= max(quarters),
#                                 value=(min(quarters),max(quarters)))

# print(df_b)
# df_b2 = (df.groupby(['회계연도','매출','비용', '영업이익', '보고반영']).sum()/-100000000).round(1)
# df_c.to_excel('C:/CODING/Streamlit/dashboard_ex/test.xlsx')
# mask = (df_b['qrt'].between(*quarter_selection))




# mask = (df_b['회계연도'].isin(dropdown)) 
mask = (df_b['회계연도'].isin(countries)) & (df_b['분기'].isin(dropdown2)) 
# mask = (df_b['회계연도'].isin(plot.countries)) & (df_b['분기'].isin(dropdown2)) 


df_ann = df_b.loc[mask]
# df_ann = df_b.groupby(['회계연도','전기월'])['매출','비용', '영업이익', '보고반영'].sum()
df_ann = df_ann.reset_index()
df_ann = df_ann.groupby(['회계연도'])['매출','비용','영업이익'].sum()
df_ann = df_ann.reset_index()
df_ann = pd.melt(df_ann,id_vars=['회계연도'],value_vars= ['매출','비용','영업이익'])
# df_ann = df_ann.groupby(['회계연도','분기'])['매출','비용','영업이익'].sum()
# df_ann.to_excel('F:/strea/STREAM/t_f_q/test10.xlsx')



# df_ann = df_ann.groupby(['회계연도', 'variable'])['value'].sum()
# df_ann = df_ann.reindex()
# df_ann.to_excel('F:/strea/STREAM/t_f_q/test12.xlsx')

st.caption(f"기준년월 : {lstday}")
fig = px.bar(df_ann, x="회계연도", y="value", color="variable", barmode='group', text_auto=True , template="plotly_dark",width=400, height=600,
color_discrete_map={
        '매출': 'blue',
        '비용': 'teal',
        '영업이익':'red'})

st.plotly_chart(fig)

# year = df_b['회계연도'].unique().tolist()

# df_anns = df_b.groupby(['전기월'])['매출'].sum()

# chart_data = pd.DataFrame(
#         df_anns,
# #     columns=['a', 'b', 'c'])
#         columns= year.count)
# st.line_chart(df_anns)