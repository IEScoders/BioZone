import os
from flask import Flask, render_template, url_for, request
from bokeh.plotting import figure, gmap
# from bokeh.resources import CDN
# from bokeh.embed import file_html
from bokeh.embed import components
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, GMapOptions, Slider, Select, CustomJS
from bokeh.models import ColorBar, LinearColorMapper
# from bokeh.palettes import Viridis256
# import math
import numpy as np
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown, TextInput, Div, Button
# from bokeh.io import curdoc
from bokeh.layouts import column,row
# from numpy.random import random 
# from bokeh.layouts import gridplot


# species_csv=pd.read_csv("species.csv")
# species_name=list(species_csv['scientific_name'].values)
# base_url='https://raw.githubusercontent.com/IEScoders/EcoclimateTaiwan/master/output_csv/solenopsis_invicta/'


# spec='solenopsis_invicta'
# year='2010'
# month='01'

# ei_csv=base_url+'{}-{}_{}.csv'.format(year,month,spec)

# months=['01','02','03','04','05','06','07','08','09','10','11','12']
# for year in np.arange(2010,2018,1):
#     for month in months:
#         ei_csv=base_url+'{}-{}_solenopsis_invicta.csv'.format(year,month)

# def read_data(year='2015',month='01',spec='solenopsis_invicta'):
#     ei_csv=base_url+'{}-{}_{}.csv'.format(year,month,spec)
#     df=pd.read_csv(ei_csv)
#     df.columns=["Index","EI","id","x","y"]
#     x=df['x'].values
#     y=df['y'].values
#     EIvals=df['EI'].values
#     psource=ColumnDataSource(
#         data=dict(
#             x=x,
#             y=y,
#             EIvals=EIvals,
#         )
#     )
#     return psource
# source=read_data()
# low=math.floor(np.min(df['EI'].values))
# high=math.ceil(np.max(df['EI'].values))
# mapper=LinearColorMapper(palette=Viridis256,low=0, high=1)
# color_bar=ColorBar(color_mapper=mapper,location=(0,0))




app = Flask(__name__)


# posts_data = [
#     {
#         'bug': 'Red Mite',
#         'predator': 'Birdy Bird',
#         'crops_affected': "really can't say",
#         'ei_val': '-999999'
#     }#,
#     # {
#     #     'author': 'Jane Doe',
#     #     'title': 'Blog Post 2',
#     #     'content': 'Second post content',
#     #     'date_posted': 'April 21, 2018'
#     # }
# ]
port = int(os.getenv('PORT', 8000))
app_title="BioZone"
## Home page Route
@app.route('/')
def home():
     return render_template('home.html', app_title=app_title)

@app.route('/about')
def about():
    return render_template('about.html', app_title=app_title)

@app.route('/ei_explain')
def whatisei():
    return render_template('whatisei.html', app_title=app_title)

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html', app_title=app_title)

@app.route('/links')
def links():
    return render_template('links.html', app_title=app_title)

# # # Analysis Page Route
@app.route('/analysis')
def analysis():
    species_csv=pd.read_csv("species.csv")
    pest_index=species_csv.index[species_csv['scientific_name']==request.values['pest']]
    pest_name=species_csv['common_name_c'][pest_index].values[0]
    pest_image=species_csv['image'][pest_index].values[0]
    pest_desc=species_csv['desc'][pest_index].values[0]
    pest_latin=species_csv['scientific_name'][pest_index].values[0].replace('_',' ')
    if request.values['crop']:
        crops_csv=pd.read_csv("CropsPests.csv")
        crop_index=crops_csv.index[crops_csv['CropCommon']==request.values['crop']]
        crop_name=crops_csv['CropChinese'][crop_index].values[0]
        crop_yield=crops_csv['KiloPerHectare'][crop_index].values[0]
        crop_price=crops_csv['PricePerKilo'][crop_index].values[0]
    else:
        crop_name=''
        crop_yield=''
        crop_price=''
    

    htmlfile="%s.html" % request.values['pest']
    # pest_name=request.values['pest'].title()
    # crop_name=request.values['crop'].title()
    
    return render_template("analysis.html", app_title=app_title,pest_name=pest_name,pest_latin=pest_latin,pest_image=pest_image,pest_desc=pest_desc,crop_name=crop_name,crop_yield=crop_yield,crop_price=crop_price,htmlfile=htmlfile)

# # # Analysis Page Route
# @app.route('/analysis_old')
# def analysis2():

#     def slider_callback(attr, old, new):
#         year=yeardata_slider.value
#         species=menu.value
#         # month=monthdata_slider.value
#         ei_csv=base_url+'{}-{}_{}.csv'.format(year,'{:02}'.format(4),species)
#         df=pd.read_csv(ei_csv)
#         df.columns=["Index","EI","id","x","y"]
#         x=df['x'].values
#         y=df['y'].values
#         EIvals=df['EI'].values
#         new1=ColumnDataSource(
#             data=dict(
#                 x=x,
#                 y=y,
#                 EIvals=EIvals,
#             )
#         )
#         source.data = new1.data

#     # scientific_name=request.values['pest'] 
#     pest_name=request.values['pest'].title()
#     menu = Select(options=species_name,value="solenopsis_invicta", title='Select Bugs') 
#     menu.on_change('value', slider_callback)
#     yeardata_slider = Slider(start=2010, end=2017, value=2010, step=1,title="Year")
#     yeardata_slider.on_change('value', slider_callback) 
#     monthdata_slider = Slider(start=1, end=12, value=1, step=1,title="Month")
#     monthdata_slider.on_change('value', slider_callback)
#     crop =  Div(text="""<hr><p><h5>Possible Loss for <b>%s</b>:</h5></p>""" % request.values['crop'].title()) 
#     damage_slider = Slider(start=0, end=100, value=50, step=1,title="Loss Percentage")
#     # damage_slider.on_change('value', price_callback) 
#     croparea=TextInput(id="area", value="10", title="Farm Area (ha)")
#     cropyield=TextInput(id="yield", value="20000", title="Yield (kg/ha)")
#     cropprice=TextInput(id="price", value="50", title="Price (NT$/kg)")
#     loss=float(damage_slider.value)/100*float(croparea.value)*float(cropyield.value)*float(cropprice.value)
#     estimation = Div(text="""<p align="right" style="font-size:16px"><b>%s</b></p>""" % 'NT${:,.0f}'.format(loss))

#     map_options = GMapOptions(lat=23.5, lng=121.0, map_type="terrain", zoom=7)
#     p = gmap("AIzaSyDqpIUEhtFIX53RPKR5QX0gi8QdyRZh0NQ", map_options, title="EI Plot",plot_width=500, plot_height=500)
#     my_hover = HoverTool()
#     my_hover.tooltips = [('EI Value', '@EIvals'), ('Latitude', '@y'), ('Longitude', '@x')]
#     p.circle('x', 'y',source=source, size=8, line_color="black", fill_color={'field':'EIvals','transform':mapper}, fill_alpha=0.5)
#     p.add_tools(my_hover)
#     layout = row(widgetbox(menu, yeardata_slider,monthdata_slider,crop,damage_slider,croparea,cropyield,cropprice,estimation),p)

#     script, div = components(layout)	
#     return render_template("analysis_old.html", script=script, div=div, app_title=app_title,species_name=pest_name)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=port, debug=True)