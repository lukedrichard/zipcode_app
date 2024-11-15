import streamlit 
import income_by_zip
import pandas
# Import your other required libraries or modules here
# from your_module import your_function

streamlit.title("My Streamlit App")

# Add interactive elements like text inputs, sliders, etc.
user_input = (streamlit.text_input("Enter a US zipcode:"))

# Your main function or logic that processes user input
#mean, median, location = income_by_zip.analyze(int(user_input))
#streamlit.write(f'The mean income of {location} is ${mean}')
#streamlit.write(f'The median income of {location} is ${median}')

try:
    #run mean and median functions
    if int(user_input) == 0:
        raise ValueError
    mean, median, location = income_by_zip.analyze(int(user_input))
    streamlit.write(f'The mean income of {location} is ${mean}')
    streamlit.write(f'The median income of {location} is ${median}')
except Exception:
    streamlit.write("The zipcode you input is invalid. Please try again.")
