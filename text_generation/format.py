import vertexai
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from vertexai.generative_models import GenerativeModel
key_path="../vertexai.json"

Credentials=Credentials.from_service_account_file(

  key_path,
  scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

if Credentials.expired:
  Credentials.refresh(Request())

PROJECT_ID="vertex-ai-466717"
REGION="us-central1"


#start of vertex ai initialization

vertexai.init(project=PROJECT_ID,location=REGION,credentials=Credentials)

model = GenerativeModel("gemini-2.0-flash-001")

prompt="""
Patrick Ty is a 26-year-old teacher living in Texas. He has 1 child and loves tech. His email is can'tgive@gmail.com.


Create a simple table with two columns: Field and Value showing the key details.

Also provide the same information as a JSON object.

Only provide the table and the JSON, no other explanation.

"""
response=model.generate_content(prompt)
print(response.text)