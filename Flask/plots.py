import plotly
import plotly.graph_objects  as go
import plotly.express as px
from cleaning_data import data_mpg
import json

def count_type1():
    df = data_mpg()
    df_group= df['mpg'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()

def dist_total():
    df= data_mpg()
    fig = px.box(df,x='mpg' , y='cylinders')
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
