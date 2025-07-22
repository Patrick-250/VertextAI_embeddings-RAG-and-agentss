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

# response = model.generate_content("Hi, what is photosynthesis.")
# print(response.text)

prompt="""
 I want you to help me choose the best way to lose weight as an obese 45 old male.

 Question:"what is the best way to lose weight"

 options:
 1.regular diet especially salads,drink much water and exercise regularly
 2.Drink wine and grape related drinks
 3.drink plenty of alcohol


please select one of the options and explain why is it the best

"""
response=model.generate_content(prompt)
print(response.text)