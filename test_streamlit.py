import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("Simple Streamlit App")
st.write("This is a basic Streamlit app created to demonstrate functionality.")

# User input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Welcome to this Streamlit app.")

# Display a sample chart
st.write("Here's a sample line chart:")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(data)