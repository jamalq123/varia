import streamlit as st
import numpy as np
import numpy_financial as npf

# Function to calculate material price variance
def price_var(actual_price_material, standard_price_material, actual_quantity_material):
    mpv = ((actual_price_material-standard_price_material) * actual_quantity_material)
    return mpv

# Function to calculate material quantity variance
def quantity_var(actual_quantity_material, standard_quantity_material, standard_price_material):
    mqv = ((actual_quantity_material-standard_quantity_material) * standard_price_material)
    return mqv

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, num_years):
    cagr = ((ending_value / beginning_value) ** (1 / num_years)) - 1
    return cagr

# Define a function to calculate IRR
def calculate_irr(cash_flows):
    try:
        irr = npf.irr(cash_flows)
        return irr
    except ValueError:
        return None
   
# Create a select box for function selection
st.sidebar.header('User Input Parameters')

selected_function = st.sidebar.selectbox("Select a function", ["Price Variance", "Quantity Variance","Sales Variance", 'CAGR', 'IRR' ])

# Use conditional statements to call the selected function
if selected_function == "Price Variance":
         actual_price_materaial = st.number_input('Enter Material Actual Price:')
         standard_price_material = st.number_input('Enter Material Standard Price:')
         actual_quantity_material = st.number_input('Enter Material Actual Quantity:')
         
         if st.button('Calculate mpv'):
              try:
                   mpv = ((actual_price_materaial-standard_price_material) * actual_quantity_material)
                   st.success(f'CAGR: {mpv}')
              except ZeroDivisionError:
                  st.error("Number of years cannot be zero.")
              except Exception as e:
                   st.error(f"An error occurred: {e}")
                   

if selected_function == "Quantity Variance":
     actual_quantity_materaial = st.number_input('Enter Material Actual Qty:')
     standard_quantity_material = st.number_input('Enter Material Standard Qty:')
     standard_price_material = st.number_input('Enter Material Std Price:')
     
     if st.button('Calculate mqv'):
              try:
                   mqv = ((actual_quantity_material-standard_quantity_material) * standard_price_material)
                   st.success(f'CAGR: {mqv}')
              except ZeroDivisionError:
                  st.error("Number of years cannot be zero.")
              except Exception as e:
                   st.error(f"An error occurred: {e}")


if selected_function == "CAGR":
            beginning_value = st.number_input('Enter Beginning Value:')
            ending_value = st.number_input('Enter Ending Value:')
            num_years = st.number_input('Enter Number of Years:', min_value=1, step=1)

            if st.button('Calculate CAGR'):
                  try:
                          cagr = calculate_cagr(beginning_value, ending_value, num_years)
                          st.success(f'CAGR: {cagr:.2%}')
                  except ZeroDivisionError:
                      st.error("Number of years cannot be zero.")
                  except Exception as e:
                         st.error(f"An error occurred: {e}")

if selected_function == 'IRR':
     # Create a Streamlit app
     st.title('IRR Calculator')
     st.write('Enter your cash flows (negative for investments, positive for returns) and calculate IRR.')

     # Create a text input for cash flows
     cash_flows_text = st.text_area('Enter cash flows (comma-separated)', '0, 200, 300, 400, 500')

     # Convert the input string to a list of floats
     cash_flows = [float(cf.strip()) for cf in cash_flows_text.split(',')]

     # Calculate IRR when a button is clicked
     if st.button('Calculate IRR'):
     # Call the calculate_irr function
      irr = calculate_irr(cash_flows)
    
      if irr is not None:
        st.write(f'IRR: {irr:.2%}')
      else:
        st.write('Invalid input. Ensure cash flows are properly formatted.')

# Display cash flows for reference
st.write('Cash Flows:')
st.write(cash_flows)







      





'''price_var
elif selected_function == "Quantity Variance":
    quantity_var
elif selected_function == "Sales Variance":
    quantity_var

st.sidebar.header('User Input Parameters')
page = st.sidebar.selectbox("Explore Or Predict", ("material price variance", "MQV"))

# Streamlit UI
st.title('CAGR Calculator')



if st.button('Calculate mpv'):
    try:
        mpv = ((actual_price_materaial-standard_price_material) * actual_quantity_material)
        st.success(f'CAGR: {mpv}')
    except ZeroDivisionError:
        st.error("Number of years cannot be zero.")
    except Exception as e:
        st.error(f"An error occurred: {e}")'''
       


'''actual_quantity_materaial = st.number_input('Enter Material Actual Qty:')
standard_quantity_material = st.number_input('Enter Material Standard Qty:')
standard_quantity_material = st.number_input('Enter Material Std Price:')

    price_var
elif selected_function == "Quantity Variance":
    quantity_var
elif selected_function == "Sales Variance":
    quantity_var

st.sidebar.header('User Input Parameters')
page = st.sidebar.selectbox("Explore Or Predict", ("material price variance", "MQV"))

# Streamlit UI
st.title('CAGR Calculator')



if st.button('Calculate mpv'):
    try:
        mpv = ((actual_price_materaial-standard_price_material) * actual_quantity_material)
        st.success(f'CAGR: {mpv}')
    except ZeroDivisionError:
        st.error("Number of years cannot be zero.")
    except Exception as e:
        st.error(f"An error occurred: {e}")'''
