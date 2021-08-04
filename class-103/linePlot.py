import pandas as pd
import plotly.express as px

df=pd.read_csv("C:/class-python/class-103/line_chart.csv")
fig=px.line(df,x="Year",y="Per capita",color="Country",title="Per capita income")
fig.show()
