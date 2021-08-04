import pandas as pd
import plotly.express as px

df=pd.read_csv("C:/class-python/class-103/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",color="Country",title="Per capita income",size="Percentage",size_max=60)
fig.show()
