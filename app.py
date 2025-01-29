# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:23:15 2025

@author: Dr OxMAN
"""
#import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# """Introduction to Streamlit"""
# st.title("Streamlit is Amazing")

# st.header("Hello, Streamlit")
# st.header("Number Selection")

# number = st.slider("Pick a number", 1, 100, SliderValue=True)
# st.write(f"**You picked**: {number}")


# """Visualisation of Data"""

# st.title("Title heading")

# st.write("Hello, Streamlit!")

# st.header("Sample Data")

# data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
# st.write(data)

# Create a Plotly figure
# fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
# st.plotly_chart(fig)


# """Building a Researcher Profile Page"""


#uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png"])

#if uploaded_file is not None:
    #st.sidebar.image(uploaded_file, width=256, caption="Dr OxMAN")
st.sidebar.image("OXMAN.jpg",
                 width=256, caption="Dr OxMAN")

name = "Dr. OxMAN"
field = "Materials Science"
institution = "University of the Witwatersrand"
email = "droxman@wits.ac.za"
number = "081 234 5678"

st.sidebar.subheader("Contact Information")
# Add a contact section
# Collect basic information

st.sidebar.text(f"You can reach {name} at {email}")
st.sidebar.text(f"Mobile number : {number}")

st.sidebar.subheader("Area of Interest")
st.sidebar.write(f"**Name:** {name}")
st.sidebar.write(f"**Expertise:** {field}")
st.sidebar.write(f"**Institution:** {institution}")

# Title of the app
st.title("Researcher Profile Page")

# Display basic profile information
st.header("Dr Oxman's Research Areas")
st.write(f"Ultra High Resolution Electron Microscopy. Image Simulation and Processing. The investigation of new approaches to quantitative microscopy (theory and experiment). Structural Studies of inorganic oxides and surfaces. The development of new detectors for imaging with high energy electrons. Aberration Corrected Electron Optics. Imaging radiation sensitive materials. Nanocrystalline metal and metal oxide catalysts. Diffractive imaging without lenses.")

# Add a section for publications
st.header("Publications")

st.write("For more information on Publications refer to link below:")

st.page_link("https://www.researchgate.net/profile/Arthur-Moya",
             label="Research publications", icon="🔥")

uploaded_file = st.file_uploader(
    "Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower()
                               in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

    # Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

# Set Streamlit page layout
#st.set_page_config(page_title="Citations Growth", layout="wide")

# Title
st.title("Exponential Growth of Citations (2015 - 2024)")

# Years from 2015 to 2024
years = np.arange(2015, 2025)

# Generate exponential growth data for citations
citations = np.round(10 * np.exp(0.5 * (years - 2015))).astype(int)

# Create a DataFrame
df = pd.DataFrame({"Year": years, "Citations": citations})

# Create Plotly bar chart
fig = px.bar(
    df,
    x="Year",
    y="Citations",
    text="Citations",
    title="Publication Trends",
    labels={"Year": "Year", "Citations": "Number of Citations"},
    color="Citations",
    color_continuous_scale="Blues"
)

# Customize layout
fig.update_traces(textposition="outside")  # Show citation values above bars
fig.update_layout(
    xaxis=dict(tickmode="linear"),
    yaxis=dict(showgrid=True, gridcolor="lightgray"),
    plot_bgcolor="white"
)

# Display Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
