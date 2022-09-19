import streamlit as st
import pandas as pd
from metrics import *
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('randomdata.csv')
df = pd.DataFrame()

# Create Pie Charts using Matplotlib
def pie_chart(df):
    labels = list(df.index)
    values = list(df['Percentage'])


    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    return fig

# Header and Spacer
st.markdown("<h1 style='text-align: center; color: white;'>My Dashboard</h1>", unsafe_allow_html=True)
st.markdown('***')

# Search Box
buffer, col2, col3 = st.columns([1,5,15])

with col2:
    key = st.selectbox("Key", ['Name', 'Email', 'Age', 'Gender', 'State', 'Profession', 'Salary' ])

# Set input to search, use title case, use search function to get data
with col3:
    search_term = st.text_input("Search")
    search_term = search_term.title()
    if key != '' and search_term != '':
        df = search(data, key, search_term)

buffer, col2 = st.columns([1,20])

# Display search results
with col2:
    if len(df) < 1 and len(search_term) > 0:
        st.write("Did not find any matches.")
    elif not df.empty:
        st.dataframe(df)
    else:
        st.write('')
    

st.markdown('***')
buffer, col2, buffer, col3, buffer = st.columns([1,7, 1, 7, 1])

# Use gender dist function to display % male and female
with col2:
    st.markdown("<h5 style='text-align: center; color: white;'>Gender Distribution</h1>", unsafe_allow_html=True)
    st.markdown('')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(pie_chart(gender_distribution(data, 'Gender')))

# Use salary dist function to display average salary by profession
with col3:
   st.markdown("<h5 style='text-align: center; color: white;'>Average Salary Per Profession</h1>", unsafe_allow_html=True)
   st.markdown('')
   st.set_option('deprecation.showPyplotGlobalUse', False)
   st.bar_chart(salary_distribution(data, 'Profession', 'Salary'))