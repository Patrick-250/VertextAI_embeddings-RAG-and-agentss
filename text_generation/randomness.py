import vertexai
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from vertexai.generative_models import GenerativeModel,GenerationConfig
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

#lets control temperature(randomness and creativity)

temperature=(1)
prompt="""
who is the richest person in africa as of 2025

"""
config = GenerationConfig(temperature=1.0)
response=model.generate_content(
  prompt,generation_config=config
)
print(response.text)

#change the temperature to 0 and see the randomness decrease