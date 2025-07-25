import os
from dotenv import load_dotenv
import requests

# loading env variable
load_dotenv()

# collecting user input on the job and location
criteria = input('what jo are you looking for: ')
country = input("select country ( us , ca , ae ): ")

# the endpoint url
endpoint_url = 'https://jsearch.p.rapidapi.com/search'

# api_key
# use your api key
api_key = os.getenv('RAPIDAPI_JSEARCH_KEY')

# the type of method using to collect data
method = 'GET'

# headers containing the api key and host
headers = {
    'x-rapidapi-key' : api_key,
    'x-rapidapi-host' : 'jsearch.p.rapidapi.com'
}

# parameters to specify the data needed
parameters = {
    'query' : criteria,
    'country' : country,
    'num_pages' : '1',
    'date_posted' : 'all'
}

# initialising request to the server
response = requests.request(method, endpoint_url , params=parameters , headers=headers)

# converting the response from the server into a JSON format
data = response.json()


# using the while loop to loop through the response json to collect 5 available job
print(f"--- Showing Job Result For ' {criteria} ' location ' {country} ' ---\n")
for job in data['data']:
    print(f"Job Title : {job['job_title']}\n")
    print(f"---------------------------------------------------------------")
    print(f"Company Name / Employer Name : {job['employer_name']}\n")
    print(f"---------------------------------------------------------------")
    print(f"Job Location : {job['job_location']}\n")
    print(f"---------------------------------------------------------------")
    print(f"Job Employment Type : {job['job_employment_type']}\n")
    print(f"---------------------------------------------------------------")
    print(f"Job Description : {job['job_description']}\n")
    print(f"---------------------------------------------------------------")
    print(f"Job Apply Link : {job['job_apply_link']} \n")
    print(f"---------------------------------------------------------------")