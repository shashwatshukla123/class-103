#pip3 install pandas
import pandas as pd

# do deel data frame we need pandas liberary it helps in data manipulation and anaylsis
df = pd.DataFrame()
#print(df)
# it's create a empty data frame

data=[1,2,3,4,5,6]
df = pd.DataFrame(data)
#print(df)

data=[['S101','shashwat',20],['S102','shukla',10],['S103','amar',30]]
df=pd.DataFrame(data,columns=['ID','name','marks'])
#print(df)

df=df.append(df,ignore_index=True)
print(df)

#...............................................................................................

#plotly.express:- is used to draw graphs and charts
#pip3 install plotly-express
#read_csv("filename"):- is used to read the csv file

