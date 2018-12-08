import os
from flask import Flask, render_template, url_for, request
from bokeh.plotting import figure, gmap
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, GMapPlot, GMapOptions, DataRange1d, Slider, Select, CustomJS, DateRangeSlider
from bokeh.models import ColorBar, LinearColorMapper
from bokeh.palettes import Viridis256
import math
import numpy as np
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown
# from bokeh.io import curdoc
from bokeh.layouts import column,row
from numpy.random import random 
from bokeh.layouts import gridplot



species_csv=pd.read_csv("species.csv")
species_name=list(species_csv['scientific_name'].values)
base_url='https://raw.githubusercontent.com/IEScoders/EcoclimateTaiwan/master/output_csv/solenopsis_invicta/'


# spec='solenopsis_invicta'
# year='2010'
# month='01'

# # ei_csv=base_url+'{}-{}_{}.csv'.format(year,month,spec)
# appended_data = []
# months=['01','02','03','04','05','06','07','08','09','10','11','12']
# for year in np.arange(2010,2018,1):
#     for month in months:
#         ei_csv=base_url+'{}-{}_solenopsis_invicta.csv'.format(year,month)
#         data = pd.read_csv(ei_csv)
#         appended_data.append(data)
# appended_data = pd.concat(appended_data, axis=0)
# print(appended_data.head())

yeardata_slider = Slider(start=2010, end=2017, value=2010, step=1,title="Year")
monthdata_slider = Slider(start=1, end=12, value=1, step=1,title="Month")


print(str(yeardata_slider.value),'{:02}'.format(monthdata_slider.value))