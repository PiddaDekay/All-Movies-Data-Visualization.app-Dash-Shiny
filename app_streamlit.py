import streamlit as st
st.title("My Simple App")
st.write("""
Controls for my app
""")
fruits = ["Apples", "Oranges","Mangos", "Pomegranate"]
fruit = st.selectbox("Choose a fruit",
        options=fruits)
order = range(0,100)
number = st.select_slider("Order Amount",
        options=order)
button = st.button("Update Order")

if button:
    st.write("""Fruit Chosen:\n\n""",fruit)
    st.write("Order Amount:\n\n",number)