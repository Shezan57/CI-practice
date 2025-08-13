import streamlit as st

st.title("Basic Streamlit Power Calculator")

st.write("Enter a number to calculate its square, cube and fifth power")


number = st.number_input("Enter a number", value=0, step=1)

# calculate results

squeare = number ** 2
cube = number ** 3
fifth = number ** 5

#display results

st.write(f"The square of {number} is: {squeare}")

st.write(f"The cube of {number} is: {cube}")

st.write(f"The fifth power of {number} is: {fifth}")
