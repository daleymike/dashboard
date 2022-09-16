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
last_name_options = ['Banner', 'Rogers', 'Maximoff', 'Jordan', 'Bradley Jr', 'Montana', 'Soprano', 'Jones', 'Brown', 'Malone', 'Stockton', 'Capone']
email_domain_options = ['@gmail.com', '@aol.com', '@yahoo.com', '@hotmail.com']

# Using NumPy to Set Age Range / Salary Range and draw random samples from normal distribution
age_distribution = np.random.normal(67, 21, num_rows)
salary_distribution = np.random.normal(120000, 52000, num_rows)

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
        random_first_name = random.chocice(first_name_options_female)

    random_last_name = random.choice(last_name_options)


