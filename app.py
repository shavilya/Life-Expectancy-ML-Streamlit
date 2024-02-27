import streamlit as st
import pandas as pd
import pickle


# Load the pickled model
with open('./artifacts/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the encoded country names. 
with open('./artifacts/country_encoder.pkl' , 'rb') as encoded_file: 
    encoding = pickle.load(encoded_file)


# Function to predict life expectancy
def predict_life_expectancy(Country, Year, Status,adult_mortality,
       infant_deaths,Alcohol,percentage_expenditure,hepatitis_b,
       Measles,bmi,under_five_deaths,Polio,total_expenditure,
       Diphtheria,hivs_or_aids,gdp,Population,
       thinness_one_nineteen_years,thinness_five_nine_years,
       income_composition_of_resources,Schooling):
    
    input_data = pd.DataFrame({
        'Country': [Country],
        'Year': [Year],
        'Status': [Status],
        'adult_mortality': [adult_mortality],
        'infant_deaths': [infant_deaths],
        'Alcohol': [Alcohol],
        'percentage_expenditure': [percentage_expenditure],
        'hepatitis_b': [hepatitis_b],
        'Measles': [Measles],
        'bmi': [bmi],
        'under_five_deaths': [under_five_deaths],
        'Polio': [Polio],
        'total_expenditure': [total_expenditure],
        'Diphtheria': [Diphtheria],
        'hivs_or_aids': [hivs_or_aids],
        'gdp': [gdp],
        'Population': [Population],
        'thinness_one_nineteen_years': [thinness_one_nineteen_years],
        'thinness_five_nine_years': [thinness_five_nine_years],
        'income_composition_of_resources': [income_composition_of_resources],
        'Schooling': [Schooling]
    })

    input_data['Status'] = input_data['Status'].map({'Developed' : 1 , 'Developing' : 0})
    input_data['Country'] = encoding.fit_transform(input_data['Country'])


    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit App
st.title("Life Expectancy Prediction App")

# Input form for user to enter features
Country = st.selectbox("Country", ['Afghanistan',
 'Albania',
 'Algeria',
 'Angola',
 'Antigua and Barbuda',
 'Argentina',
 'Armenia',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas',
 'Bahrain',
 'Bangladesh',
 'Barbados',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bhutan',
 'Bolivia (Plurinational State of)',
 'Bosnia and Herzegovina',
 'Botswana',
 'Brazil',
 'Brunei Darussalam',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 "Côte d'Ivoire",
 'Cabo Verde',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Central African Republic',
 'Chad',
 'Chile',
 'China',
 'Colombia',
 'Comoros',
 'Congo',
 'Cook Islands',
 'Costa Rica',
 'Croatia',
 'Cuba',
 'Cyprus',
 'Czechia',
 "Democratic People's Republic of Korea",
 'Democratic Republic of the Congo',
 'Denmark',
 'Djibouti',
 'Dominica',
 'Dominican Republic',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Ethiopia',
 'Fiji',
 'Finland',
 'France',
 'Gabon',
 'Gambia',
 'Georgia',
 'Germany',
 'Ghana',
 'Greece',
 'Grenada',
 'Guatemala',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hungary',
 'Iceland',
 'India',
 'Indonesia',
 'Iran (Islamic Republic of)',
 'Iraq',
 'Ireland',
 'Israel',
 'Italy',
 'Jamaica',
 'Japan',
 'Jordan',
 'Kazakhstan',
 'Kenya',
 'Kiribati',
 'Kuwait',
 'Kyrgyzstan',
 "Lao People's Democratic Republic",
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Lithuania',
 'Luxembourg',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Maldives',
 'Mali',
 'Malta',
 'Marshall Islands',
 'Mauritania',
 'Mauritius',
 'Mexico',
 'Micronesia (Federated States of)',
 'Monaco',
 'Mongolia',
 'Montenegro',
 'Morocco',
 'Mozambique',
 'Myanmar',
 'Namibia',
 'Nauru',
 'Nepal',
 'Netherlands',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'Niue',
 'Norway',
 'Oman',
 'Pakistan',
 'Palau',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Philippines',
 'Poland',
 'Portugal',
 'Qatar',
 'Republic of Korea',
 'Republic of Moldova',
 'Romania',
 'Russian Federation',
 'Rwanda',
 'Saint Kitts and Nevis',
 'Saint Lucia',
 'Saint Vincent and the Grenadines',
 'Samoa',
 'San Marino',
 'Sao Tome and Principe',
 'Saudi Arabia',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Sierra Leone',
 'Singapore',
 'Slovakia',
 'Slovenia',
 'Solomon Islands',
 'Somalia',
 'South Africa',
 'South Sudan',
 'Spain',
 'Sri Lanka',
 'Sudan',
 'Suriname',
 'Swaziland',
 'Sweden',
 'Switzerland',
 'Syrian Arab Republic',
 'Tajikistan',
 'Thailand',
 'The former Yugoslav republic of Macedonia',
 'Timor-Leste',
 'Togo',
 'Tonga',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Turkmenistan',
 'Tuvalu',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Kingdom of Great Britain and Northern Ireland',
 'United Republic of Tanzania',
 'United States of America',
 'Uruguay',
 'Uzbekistan',
 'Vanuatu',
 'Venezuela (Bolivarian Republic of)',
 'Viet Nam',
 'Yemen',
 'Zambia',
 'Zimbabwe'])  # Add actual country names
Year = st.number_input("Year", min_value=2000, max_value=2015, value=2010)
Status = st.selectbox("Status: (developed : 1 , developing : 0)", ['Developing', 'Developed'])
adult_mortality = st.number_input("Adult Mortality", min_value=1, value=723)
infant_deaths = st.number_input("Infant Deaths", min_value=0, value=1800)
Alcohol = st.number_input("Alcohol", min_value=1, value=18)
percentage_expenditure = st.number_input("Percentage Expenditure", min_value=0, value=19480)
hepatitis_b = st.number_input("Hepatitis B", min_value=1, value=99)
Measles = st.number_input("Measles", min_value=0, value=212183)
bmi = st.number_input("BMI" , min_value = 1 , max_value=89 , value = 42)
under_five_deaths = st.number_input("Under Five Deaths", min_value=0, value=2500)
Polio = st.number_input("Polio", min_value=3, value=99)
total_expenditure = st.number_input("Total Expenditure", min_value=1, value=18)
Diphtheria = st.number_input("Diphtheria", min_value=2, value=100)
hivs_or_aids = st.number_input("HIV/AIDS" , min_value=2 , max_value=51 , value = 2)
gdp = st.number_input("GDP" , min_value = 2 , max_value=119172 , value = 115433)
Population = st.number_input("Population", min_value=34, value=131241556)
thinness_one_nineteen_years = st.number_input("Thinness 1-19 years", min_value=1 , max_value=28, value=5)
thinness_five_nine_years = st.number_input("Thinness 5-9 years", min_value=1 , max_value=29, value=5)
income_composition_of_resources = st.number_input("Income Composition of Resources", min_value=0, value=950)
Schooling = st.number_input("Schooling", min_value=0, value=21)

if st.button("Predict"):
    if Country != "Select Country":
        prediction = predict_life_expectancy(Country, Year, Status,adult_mortality,
       infant_deaths,Alcohol,percentage_expenditure,hepatitis_b,
       Measles,bmi,under_five_deaths,Polio,total_expenditure,
       Diphtheria,hivs_or_aids,gdp,Population,
       thinness_one_nineteen_years,thinness_five_nine_years,
       income_composition_of_resources,Schooling)
        st.success(f"Predicted Life Expectancy: {prediction:.2f}")
    else:
        st.warning("Please select a valid country.")
