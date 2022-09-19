import pandas as pd
import numpy as np

data = pd.read_csv('randomdata.csv')


# Search function
def search(data, column, search_term):
    # If we are searching by age, we need to use int
    if column == 'Age':
        search_term = int(search_term)

    indexes = data.loc[data[column].isin([search_term])].index
    if indexes.size > 0:
        # Select a value that belongs to this particular data frame
        return data.iloc[indexes]
    else:
        return []

# Funtion to calculate % of male vs females
def gender_distribution(data, column_name):
    
    values = data[column_name].tolist()
    # Storing number of Males and Females 
    distribution = {}
    # Total number of people
    total = 0

    for value in values:
        total += 1
        # If the gender isn't in the disribution, add it and set the total to 1, otherwise add 1 to the existing gender
        if value not in distribution:
            distribution[value] = 1
        else:
            distribution[value] = distribution[value] + 1
    # Each key (gender) divided by the total, multiplied by 100 to get %
    for key in distribution:
        distribution[key] = distribution[key] / total * 100

    df = pd.DataFrame.from_dict(distribution, orient='index')
    df = df.rename(columns = {0:'Percentage'})

    return df



# Function to show salary based on profession
def salary_distribution(data, key_variable, value_variable):
    # Keys set to Profession , values set to salary
    keys = data[key_variable]
    values = data[value_variable]

    info = {}
    # Store values to compute mean
    aux = {}

    for key, value in zip(keys, values):
        if key in info:
            aux[key].append(value)
            # Get mean of specified profession (key)
            info[key][0] = np.around(np.mean(aux[key]), 2)
        # If the profession (key) isn't in info, add it
        else:
            info[key] = [[]]
            aux[key] = []
    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.rename(columns = {0: value_variable})

    return df


