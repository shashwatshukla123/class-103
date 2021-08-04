import pandas as pd
import plotly.express as px

df=pd.read_csv("C:/class-python/class-103/data.csv")
fig=px.bar(df,x="Country",y="InternetUsers",title="Population of Internet Users")
fig.show()
