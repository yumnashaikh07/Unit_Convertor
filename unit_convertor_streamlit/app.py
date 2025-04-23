import streamlit as st
from time import sleep

st.set_page_config(page_title="Unit Convertor", page_icon=":bar_chart:")
st.title("Unit Convertor")
selected_value = st.selectbox("Select Value To Convert ",[ 'Temperature', 'Length', 'Weight'])


if selected_value == 'Temperature':
    from_unit = st.selectbox("Select From Unit",['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox("Select To Unit",['Celsius', 'Fahrenheit', 'Kelvin'])
    input_value  = st.number_input("Enter Value")

    result = None
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (input_value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = input_value + 273.15
        else:
            result = input_value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (input_value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (input_value - 32) * 5/9 + 273.15
        else:
            result = input_value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = input_value - 273.15
        elif to_unit == "Fahrenheit":
            result = (input_value - 273.15) * 9/5 + 32
        else:
            result = input_value

    if result is not None:
        st.spinner()
        sleep(3)
        st.success(f"{input_value:} {from_unit:} = {result:.1f} {to_unit}")

elif selected_value == 'Length':
    from_length_unit = st.selectbox("Select From Unit",['Meter', 'Kilometer', 'Centimeter'])
    to_length_unit = st.selectbox("Select To Unit",['Meter', 'Kilometer', 'Centimeter'])
    input_value  = st.number_input("Enter Value")
    if from_length_unit == "Meter":
        if to_length_unit == "Kilometer":
            result = input_value / 1000
        elif to_length_unit == "Centimeter":
            result = input_value * 100
        else:
            result = input_value
    elif from_length_unit == "Kilometer":   
        if to_length_unit == "Meter":
            result = input_value * 1000
        elif to_length_unit == "Centimeter":
            result = input_value * 100000
        else:
            result = input_value
    elif from_length_unit == "Centimeter":
        if to_length_unit == "Meter":
            result = input_value / 100
        elif to_length_unit == "Kilometer":
            result = input_value / 100000
        else:
            result = input_value
    if result is not None:
        st.spinner()
        sleep(3)
        st.success(f"{input_value:} {from_length_unit:} = {result:.1f} {to_length_unit}")

elif selected_value == 'Weight':            
    from_weight_value = st.selectbox("Select From Unit",['Gram', 'Kilogram'])
    to_weight_value = st.selectbox("Select To Unit",['Gram', 'Kilogram'])
    input_value  = st.number_input("Enter Value")
    if from_weight_value == "Gram":
        if to_weight_value == "Kilogram":
            result = input_value / 1000
        else:
            result = input_value
    elif from_weight_value == "Kilogram":
        if to_weight_value == "Gram":
            result = input_value * 1000
        else:
            result = input_value
    if result is not None:
        st.spinner("Calculating")
        sleep(3)
        st.success(f"{input_value:} {from_weight_value:} = {result:.1f} {to_weight_value}")