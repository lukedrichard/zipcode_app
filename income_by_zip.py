import pandas as pd
import requests
from io import StringIO

# implement a function that calculates the mean income for a ZIP area
def mean_income(zip_dict) -> int:
    
    #make a list of bracket means
    
    brack_mean = [((u+l)/2)*a for u,l,a in zip(zip_dict['upper_brack'], zip_dict['lower_brack'], zip_dict['amount'])]
    mean = round(sum(brack_mean)/sum(zip_dict['amount']))
    
    return mean

def median_income(zip_dict) -> int:
    
    #get the total filings
    total = sum(zip_dict['amount'])
    #find median filing number
    med_return = round(total/2)

    #iterate until finding the correct bracket, then use the information to calculate the mean and break
    median = 0
    cum_total = 0

    for u,l,a in zip(zip_dict['upper_brack'], zip_dict['lower_brack'], zip_dict['amount']):
        cum_total += a
        if med_return <= cum_total:
            #calculate relative position of med_return within the bracket
            #note this counts back from the cumulative total
            rel_pos = cum_total - med_return
            #find the total income range within the bracket
            size = u - l
            #find the size of each income segment based on number of filings in the bracket
            seg_size = size/a
            #subtract back the segments until reaching the median income
            median = round(u - (rel_pos * seg_size))

            break
    
    return median

def analyze(zipcode_int):
    #irs_df = pd.read_csv('20zpallagi.csv')
    # URL of the large file in GitHub (raw)
    file_url = "https://github.com/lukedrichard/zipcode_app/blob/main/20zpallagi.csv"

    # Download the file
    response = requests.get(file_url)

    # Assuming it's a CSV, load it into pandas DataFrame
    data = StringIO(response.text)  # Convert the text to a file-like object
    irs_df = pd.read_csv(data)



    location_df = pd.read_csv('zipcodes.us.csv')

    zip_dict = {'lower_brack':[1, 25000, 50000, 75000, 100000, 200000],
            'upper_brack':[24999, 49999, 74999, 99999, 199999, 10000000],}
    
    num_returns = irs_df[irs_df['zipcode'] == zipcode_int]['N1']
    zip_dict.update({'amount': num_returns})

    city= location_df[location_df['zipcode'] == zipcode_int]['place'].iloc[0]
    state = location_df[location_df['zipcode'] == zipcode_int]['state'].iloc[0]
    location = city + ', ' + state

    mean = mean_income(zip_dict)
    median = median_income(zip_dict)

    return mean, median, location
