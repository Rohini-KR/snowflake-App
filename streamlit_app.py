import streamlit

streamlit.title(' MY PARENTS HEALTHY DINER')
streamlit.header(' Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍵Kyle Spinach & Rocket Smoothie')
streamlit.text('🍳Hard-Boiled & Free-Range Egg')

streamlit.header('🍎🍌Buid your own smoothie 🍑🥝')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
