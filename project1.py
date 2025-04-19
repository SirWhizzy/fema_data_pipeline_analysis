import requests

import pandas as pd

url = 'https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails'

response = requests.get(url)

response_url = response.json()

project_details = response_url['PublicAssistanceFundedProjectsDetails']

df = pd.DataFrame(project_details)

df.to_csv('project1.csv')

