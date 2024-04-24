import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import numpy as np
from scipy.stats import f_oneway
from scipy.stats import pearsonr

car_data = pd.read_csv('vehicles.csv') 
(car_data
 .isna()
.mean()
.sort_values(ascending=False)
.reset_index()
.rename(columns={'index':'Coluna', 0 : 'Missing Data'})
)
car_data = car_data.dropna()
car_data['model_year'] = car_data['model_year'].astype(str)
car_data['model_year'].dtype
car_data['brand'] = car_data['model'].apply(lambda x: 'dodge ram' if 'dodge' in x.lower() or 'ram' in x.lower() else x.split()[0])
car_data = car_data .sort_values(by='model_year') 
from functions import anova
from functions import plot_hist
y_odometer = [i*100000 for i in range(10)]
y_model_year = [i*1 for i in range(45)]
y_model = [i*2 for i in range(100)]
y_condition= [i*1 for i in range(6)]
y_cylinders= [i*2 for i in range(10)]
y_transmission= [i*1 for i in range(3)]
y_type= [i*1 for i in range(12)]
y_fuel= [i*1 for i in range(5)]
y_paint_color= [i*1 for i in range(12)]
y_brand= [i*1 for i in range(18)]

st.header('Pre-owned car advertisement in the US market :car:')


option = st.selectbox(
    'Comparison between the Price and the other characteristics',
    ('Price x Model', 'Price x Model Year','Price x Condition','Price x Cylinders', 'Price x Fuel','Price x Odometer','Price x Transmissions','Price x Type','Price x Paint Color','Price x Brand')
)
st.write('You selected:', option)

if option == 'Price x Model':
    fig1 = anova(car_data, 'model', 50,70,y_model )
    st.plotly_chart(fig1)
elif option == 'Price x Model Year':
    fig2 = anova(car_data, 'model_year', 20,30,y_model_year)
    st.plotly_chart(fig2)
elif option == 'Price x Condition':
    fig3 = anova(car_data, 'condition', 2,4,y_condition)
    st.plotly_chart(fig3)
elif option == 'Price x Cylinders':
    fig4 = anova(car_data, 'cylinders', 7,10,y_cylinders)
    st.plotly_chart(fig4)
elif option == 'Price x Fuel':
    fig5 = anova(car_data, 'fuel', 2,3,y_fuel)
    st.plotly_chart(fig5)
elif option == 'Price x Odometer':
    fig6 = anova(car_data, 'odometer', 400000,700000,y_odometer)
    st.plotly_chart(fig6)
elif option == 'Price x Transmissions':
    fig7 = anova(car_data, 'transmission', 1,1.5,y_transmission)
    st.plotly_chart(fig7)
elif option == 'Price x Type':
    fig8 = anova(car_data, 'type', 5,8,y_type)
    st.plotly_chart(fig8)
elif option == 'Price x Paint Color':
    fig9 = anova(car_data, 'paint_color', 5,8,y_paint_color)
    st.plotly_chart(fig9)
elif option == 'Price x Brand':
    fig10 = anova(car_data, 'brand', 5,10,y_brand)
    st.plotly_chart(fig10)

def plot_histograms(histograms):
    for histogram in histograms:
        st.plotly_chart(histogram, use_container_width=True)
hist_button = st.button('Create histogram')
if hist_button: 
    st.write('Creating histograms for the car sales dataset by brand')
    histograms = plot_hist(car_data)
    plot_histograms(histograms)








