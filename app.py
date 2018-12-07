import os
from flask import Flask, render_template, url_for, request
from bokeh.plotting import figure, gmap
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import components
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, GMapPlot, GMapOptions, DataRange1d, Slider
from bokeh.models import ColorBar, LinearColorMapper
from bokeh.palettes import Viridis256
import math
import numpy as np
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown
from bokeh.io import curdoc
from bokeh.layouts import column,row
from numpy.random import random 





feature_names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]
df=pd.read_csv('EI_result/2010-01_achatina_fulica.csv')
# df.columns=["id","name","ele","x","y","city","address","資料起始日期","撤站日期","備註","原站號","新站號"]
df.columns=["Index","EI","id","x","y"]
# psource = ColumnDataSource(df)

x=df['x'].values
y=df['y'].values
EIvals=df['EI'].values
psource=ColumnDataSource(
    data=dict(
        x=x,
        y=y,
        EIvals=EIvals,
    )
)

# low=math.floor(np.min(df['EI'].values))
# high=math.ceil(np.max(df['EI'].values))
mapper=LinearColorMapper(palette=Viridis256,low=0, high=1)
color_bar=ColorBar(color_mapper=mapper,location=(0,0))
# lat_vals=df["lat"].values
# long_vals=df["long"].values

# def create_google_map(plotsource=psource):
#     map_options = GMapOptions(lat=23.5, lng=121.0, map_type="terrain", zoom=7)
#     p = gmap("AIzaSyDqpIUEhtFIX53RPKR5QX0gi8QdyRZh0NQ", map_options, title="EI Plot",plot_width=500, plot_height=500)
#     # p=GMapPlot(map_options=map_options,api_key='AIzaSyDqpIUEhtFIX53RPKR5QX0gi8QdyRZh0NQ')
#     # p.title.text="EI Plot"
#     # p = figure(plot_width=500, plot_height=500,title="EI Plot", toolbar_location="right",tools="pan,box_zoom,reset")
#     my_hover = HoverTool()
#     my_hover.tooltips = [('EI Value', '@EI'), ('Latitude', '@lat'), ('City', '@city'),('Address of the station', '@address')]
#     p.circle('x', 'y',source=plotsource, size=5, line_color="black", fill_color={'field':'ele','transform':mapper}, fill_alpha=0.5)
#     p.add_tools(my_hover)
#     # p.add_layout(color_bar, 'right')
#     return p


# Create the main plot
def create_scatter_circle(plotsource=psource,color_bar=color_bar):
    p = figure(plot_width=500, plot_height=500,title="EI Plot", toolbar_location="right",tools="pan,box_zoom,reset")
    my_hover = HoverTool()
    my_hover.tooltips = [('Name', '@name'), ('Elevation', '@ele'), ('City', '@city'),('Address of the station', '@address')]
    p.circle('x', 'y',source=plotsource, size=10, line_color="navy", fill_color="orange", fill_alpha=0.5)
    p.add_tools(my_hover)
    return p



app = Flask(__name__)


posts_data = [
    {
        'bug': 'Red Mite',
        'predator': 'Birdy Bird',
        'crops_affected': "really can't say",
        'ei_val': '-999999'
    }#,
    # {
    #     'author': 'Jane Doe',
    #     'title': 'Blog Post 2',
    #     'content': 'Second post content',
    #     'date_posted': 'April 21, 2018'
    # }
]
app_title="BioZone"
## Home page Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts_data, app_title=app_title)

# # # Analysis Page Route
@app.route('/analysis')
def analysis():
    current_feature_name = request.args.get("feature_name")
    if current_feature_name == None:
        current_feature_name = "Sepal Length"


    map_options = GMapOptions(lat=23.5, lng=121.0, map_type="terrain", zoom=7)
    p = gmap("AIzaSyDqpIUEhtFIX53RPKR5QX0gi8QdyRZh0NQ", map_options, title="EI Plot",plot_width=500, plot_height=500)
    my_hover = HoverTool()
    my_hover.tooltips = [('EI Value', '@EIvals'), ('Latitude', '@y'), ('Longitude', '@x')]
    p.circle('x', 'y',source=psource, size=5, line_color="black", fill_color={'field':'EIvals','transform':mapper}, fill_alpha=0.5)
    p.add_tools(my_hover)

    N = 0.5
    slider = Slider(start=0, end=1, value=N,step=0.1, title='Number of points')
    # Add callback to widgets
    def callback(attr, old, new):
        N = slider.value
        psource.data={'x': df['x'].values, 'y': df['y'].values}
    slider.on_change('value', callback) 
    # Arrange plots and widgets in layouts
    layout = row(slider, p) 

    # script1, div1 = components(drop)
    script, div = components(layout)	
    return render_template("analysis.html", script=script, div=div, app_title=app_title,feature_names=feature_names,  current_feature_name=current_feature_name)


if __name__=="__main__":
    app.run(debug=True)