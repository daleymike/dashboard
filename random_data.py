import pandas as pd
import random
import numpy as np
import datetime

# Set Amount of Randomized Data Points
num_rows = 2000
filename = 'randomdata.csv'

# Set Options for Randomized Data
gender_options = ['Male', 'Female']
state_options = ['Alabama', 'California', 'Florida', 'New Jersey', 'Maine', 'Idaho', 'Hawaii', 'Georgia', 'Texas']
profession_options = ['Teacher', 'Software Developer', 'Super Hero', 'Chef', 'Police Officer', 'Business Analyst', 'Accountant', 'Construction Worker', 'Professional Athlete', 'Doctor', 'Personal Trainer', 'Insurance Rep', 'Bank Teller']
first_name_options_male = ['Mike', 'Richie', 'Deven', 'Casey', 'Bruce', 'Steve', 'Jason', 'James', 'Wally', 'Pablo']
first_name_options_female = ['Steph', 'Tara', 'Corey', 'Alyssa', 'Wanda', 'Jane', 'Natasha', 'Carol', 'Diana']
last_name_options = ['Banner', 'Rogers', 'Maximoff', 'Jordan', 'Ragnarsson', 'Montana', 'Soprano', 'Jones', 'Brown', 'Malone', 'Stockton', 'Capone']
email_domain_options = ['@gmail.com', '@aol.com', '@yahoo.com', '@hotmail.com']

data = []

# Assign Random Row Data, Store in Data List
for i in range(num_rows):
    random_gender = random.choice(gender_options)
    random_state = random.choice(state_options)
    random_profession = random.choice(profession_options)
    
    # Using Male vs Female Names
    if random_gender == 'Male':
        random_first_name = random.choice(first_name_options_male)
    else:
        random_first_name = random.choice(first_name_options_female)

    random_last_name = random.choice(last_name_options)
    random_name = random_first_name + ' ' + random_last_name
    random_email = random_first_name[0].lower() + random_last_name.lower() + random.choice(email_domain_options)
    random_age = random.randint(21, 67)
    random_salary = random.randint(52000, 120000)

    row = [random_name, random_email, random_age, random_gender, random_state, random_profession, random_salary]

    # Store each row in data list
    data.append(row)

df = pd.DataFrame(data, columns=['Name', 'Email', 'Age', 'Gender', 'State', 'Profession', 'Salary'])
print(df)
df.to_csv(filename, index=False)


