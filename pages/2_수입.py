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
from creatdf import df_base
from PIL import Image
from annually_p import countries
from annually_p import dropdown2
from annually_p import dfs


# print(countries)


st.caption(f"기준년월 : {lstday}")

df_s = df_base.reset_index()

mask = (df_s['회계연도'].isin(countries)) & (df_s['수입비용'] == "수입")


df_s = df_s.loc[mask]
df_s.to_excel('F:/strea/STREAM/t_f_q/pages/df_test0.xlsx')
df_s = df_s.reset_index()
df_s = df_s.groupby(['회계연도','보고반영'])['매출'].sum()
df_s.to_excel('F:/strea/STREAM/t_f_q/pages/df_test1.xlsx')