import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module
import altair as alt
import plost
from vega_datasets import data
import datetime as dt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from annually_p import lstday
from annually_p import df_b
from PIL import Image

# from annually import quarter_selection
# import annually
st.caption(f"기준년월 : {lstday}")
# sys.path.append('..')
# st.set_page_config2(page_title="연도별 수입내역", page_icon=":bar_chart:", layout="centered")

# excel_file = 'C:/CODING/Streamlit/dashboard_ex/finan.xlsx'
# # excel_file = 'C:/Users/KSM/바탕 화면/P2/STREAM/str11/test/finan.xlsx'
# sheet_name = 'pp'

# df = pd.read_excel(excel_file,
#                    sheet_name=sheet_name)
# df['금액'] = df['금액']/-100000000


# #손익 추출
# mask1 = (df['대분류'] != "재무상태") & (df['중분류'] != "기부금")
# df = df.loc[mask1]
# # df.to_excel('C:/CODING/Streamlit/dashboard_ex/df_test0.xlsx')

# #분기표시
# df.기준일= pd.to_datetime(df.기준일)
# df['quarter'] = df['기준일'].dt.to_period('Q')

# # df = df.groupby(['회계연도','quarter','대분류','중분류','보고반영','전기월','계정코드']).sum()
# # df = df.loc['회계연도','quarter','대분류','중분류','보고반영','전기월','계정코드']
# df = df[df['금액'] != 0]
# df.to_excel('C:/CODING/Streamlit/dashboard_ex/df_test1.xlsx')


# df['수입비용'] =["수입" if s == "매출" else "비용" for s in df["중분류"]]

# for x in df.index: 
#     if df.loc[x,'수입비용'] == "수입":
#         df.loc[x,'매출']=df.loc[x,'금액']
#     else:
#         df.loc[x,'비용']=df.loc[x,'금액']
# # df = df.groupby(df(['회계연도','R','C','중분류','세분류','전기월','보고반영']))
# # df = (df.groupby(['회계연도'])[['매출','비용']].sum()/-100000000).round(1)
# # for x in df.index: 
# #     df.loc[x,'영업이익']=df.loc[x,'매출']+df.loc[x,'비용'] 

# df.to_excel('C:/CODING/Streamlit/dashboard_ex/df_test.xlsx')
# df = df_b
# df_매출 = df_b.groupby(['회계연도', '중분류','보고반영']).sum()[['금액']]
# df_매출 = df_b.groupby(['회계연도', '중분류','보고반영']).sum()[['금액']].unstack()
# mask1 = (df['중분류'] == "매출") & (df['금액'] != 0)
# df1 = df.loc[mask1].sort_values(by="금액", ascending=True).round()
# df1 = df.loc[(df['수입비용'] == "매출")]

# df_b.reset_index()
# quarters = df_b['분기'].unique().tolist()

# quarters_selection = st.multiselect('분기선택:',
#                                     quarters,
#                                     default=quarters)




# print(quarters)
# # ages = df['Age'].unique().tolist()

# quarters_selection = st.slider('분기:',
#                 min_value= min(quarters),
#                 max_value= max(quarters),
#                 value=(min(quarters),max(quarters)))
                # value=('1분기','2분기','3분기','4분기'))
# mask = (df_b['분기'].between(*quarters_selection))
# & (df['Department'].isin(department_selection))

# number_of_result = df_b[mask].shape[0]
# df_b = df_b[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')

# age_selection = st.slider('Age:',
#                         # min_value= min(ages),
#                         # max_value= max(ages),
#                         # value=(min(ages),max(ages)))
#                         value=(min_value, max_value))
# # mask22 = (df['quarter'].between(*quarter_selection)) & (df['회계연도'] == 2022)

# df_t = df_b.groupby(['회계연도'])['금액'].sum()
# df_t = df_b[df_b['금액'] != 0]

# df_b = df_b.reset_index()
# mask22 = (df_b['회계연도'] == 2022) & (df_b['수입비용'] == "수입") & (df_b['분기'].between(*quarters_selection)) 
mask22 = (df_b['회계연도'] == 2022) & (df_b['수입비용'] == "수입") & (df_b['분기'].isin(quarters_selection))
# & (df_b['quarter'].between(*quarter_selection))
# df1 = df_b[mask22].groupby(by=["보고반영"]).sum()[["금액"]].sort_values(by="금액", ascending=False).round()
df1 = df_b.loc[mask22]
# df_b.to_excel('F:/strea/STREAM/dbd_ex/test3.xlsx')
df1 = df_b[mask22].groupby(by=["보고반영"]).sum()[['매출']].sort_values(by="매출", ascending=False).round()
# df1 = df_b[mask22].groupby(by=["회계연도"]).sum()[['매출','비용']].sort_values(by="금액", ascending=False).round()

col1, col2 = st.columns(2)
with col1:
    total_sales = df1["매출"].sum().round()
    st.subheader(f"매출액계 {total_sales:,}")
    fig_product_sales22 = px.bar(
    df1,

    # x=df_selection.index,
    x = df1.index,
    y= '매출',
    # y = df_sales_by_product_line['금액'] / 100000000
    width= 300,
    height= 500,
    text = "매출",
    title="<b>유형별 매출 현황(2022)</b>",
    color_discrete_sequence=["#F63366"] * len(df1),
    template="plotly_white",
    )
    fig_product_sales22.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_product_sales22)


# mask22 = (df_b['회계연도'] == 2022) & (df_b['수입비용'] == "비용") & (df_b['분기'].between(*quarters_selection)) 
mask22 = (df_b['회계연도'] == 2022) & (df_b['수입비용'] == "비용") & (df_b['분기'].isin(quarters_selection))
# df1 = df_b[mask22].groupby(by=["보고반영"]).sum()[["금액"]].sort_values(by="금액", ascending=False).round()
df2 = df_b.loc[mask22]
# df_b.to_excel('C:/CODING/Streamlit/dashboard_ex/test3.xlsx')
df2 = df_b[mask22].groupby(by=["중분류"]).sum()[['비용']].sort_values(by="비용", ascending=False).round()
df2s = df_b[mask22].groupby(by=["중분류"]).sum()[['비용']].sort_values(by="비용", ascending=False).round()

with col2:

    # df2 = df.loc[(df['수입비용'] == "비용")]

    # mask22 = (df_t['quarter'].between(*quarter_selection)) & (df_t['회계연도'] == 2022)
    # mask22 = (df2['회계연도'] == 2022)
    # df2 = df2[mask22].groupby(by=["중분류"]).sum()[["금액"]].sort_values(by="금액", ascending=False).round()
    total_Cost = df2["비용"].sum()
    st.subheader(f"비용계 {total_Cost:,}")


    fig_product_sales21 = px.bar(
    df2,
    # x=df_selection.index,
    x = df2.index,
    y= '비용',
    # y = df_sales_by_product_line['금액'] / 100000000
    width= 300,
    height= 500,
    text = "비용",
    title="<b>유형별 비용 현황(2022)</b>",
    color_discrete_sequence=["#F63366"] * len(df2),
    template="plotly_white",
    )
    fig_product_sales22.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_product_sales21)




col1, col2 = st.columns(2)
image = Image.open('images/survey.jpg')
col1.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)
col2.dataframe(df2)

