import streamlit

streamlit.title(' MY PARENTS HEALTHY DINER')
streamlit.header(' Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍵Kyle Spinach & Rocket Smoothie')
streamlit.text('🍳Hard-Boiled & Free-Range Egg')

streamlit.header('🍎🍌Buid your own smoothie 🍑🥝')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add picklist here to allow user to choose fruits included in their smoothie
fruits_selected = streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_show)
