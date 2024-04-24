import pandas as pd
import plotly.express as px
from pathlib import Path
import numpy as np
from scipy.stats import f_oneway
from scipy.stats import pearsonr


car_data = pd.read_csv('vehicles.csv') 

def correlation (variable, df,x_axix):
    corr_coefficient, p_value = pearsonr(df['price'], df[variable])
    print("Pearson correlation coefficient:", corr_coefficient)
    print("p-value:", p_value)
      
    #avg_price_by_variable = df.groupby(column)['price'].mean().reset_index()

  #(column_list = list(car_data.columns)
   # column_list[x] = column
    #for column in column_list:
        #if column != 'price':)

def anova(df,column,x_f,x_p,x_axis):            
    if df[column].dtype == 'object':
        groups = [df[df[column] == col]['price'] for col in df[column].unique()]
        f_statistic, p_value = f_oneway(*groups)
    else:
        data1 = df[column] 
        data2 = df['price']
        f_statistic, p_value = f_oneway(data1, data2)
                
        print("F-statistic:", f_statistic)
        print("p-value:", p_value)
            
    if p_value < 0.05:
            print(f"Reject null hypothesis: There are significant differences in mean prices between at least two {column}s.")
    else:
            print(f"Fail to reject null hypothesis: There are no significant differences in mean prices between {column}s.")
                
    fig = px.scatter(df, x=column, y='price', title=f'Price Distribution by {column}')
    fig.update_layout(xaxis=dict(dtick=2))
    fig.update_xaxes(tickvals=x_axis)
    fig.add_annotation(x=x_f, y=350000, text=f'F-statistic: {f_statistic:.2f}', showarrow=False)
    fig.add_annotation(x=x_p, y=350000, text=f'p-value: {p_value:.2f}', showarrow=False)
    return fig


def plot_hist(df):            
    brands = df['brand'].unique()
    histograms = []
    for brand in brands:
        brand_separate = df[df['brand']== brand]
        histogram = px.histogram(brand_separate, x='price', title=f'Histogram of Price for {brand}')
        histograms.append(histogram)   
    return histograms                      