import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def generate_random_data(num_points):
    # Generate random dataset
    data = {
        'X': np.random.rand(num_points),
        'Y': np.random.rand(num_points),
    }
    return pd.DataFrame(data)

def main():
    st.set_page_config(page_title='Fun Data Science App', page_icon=':chart_with_upwards_trend:')

    # Add title and description
    st.title('Fun Data Science App')
    st.write("Generate a random dataset and customize the appearance of your chart!")

    # Sidebar for customization options
    st.sidebar.subheader("Customization Options")
    num_points = st.sidebar.slider("Number of Data Points", 10, 100, 50)
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Scatter Plot", "Bar Chart", "Line Chart"])

    # Generate random data
    data = generate_random_data(num_points)

    # Customize chart appearance
    st.sidebar.subheader("Chart Appearance")
    color = st.sidebar.color_picker("Choose a Color", "#3498db")
    size = st.sidebar.slider("Marker Size", 5, 20, 10)

    # Create chart based on user selection
    if chart_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        fig = px.scatter(data, x='X', y='Y', color_discrete_sequence=[color], size_max=size)
        st.plotly_chart(fig)

    elif chart_type == "Bar Chart":
        st.subheader("Bar Chart")
        fig = px.bar(data, x='X', y='Y', color_discrete_sequence=[color])
        st.plotly_chart(fig)

    elif chart_type == "Line Chart":
        st.subheader("Line Chart")
        fig = px.line(data, x='X', y='Y', line_shape='linear', line_dash=[color])
        st.plotly_chart(fig)

  
    st.plotly_chart(fig)
if __name__ == "__main__":
    main()
