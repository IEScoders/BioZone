import os
from flask import Flask, render_template, url_for, request
from bokeh.plotting import figure, save
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components
import pandas as pd



df=pd.read_csv('CWB_Stations_171226.csv')
df.columns=["id","name","ele","x","y","city","address","資料起始日期","撤站日期","備註","原站號","新站號"]
lat_vals=df["y"].values
long_vals=df["x"].values
print(lat_vals)