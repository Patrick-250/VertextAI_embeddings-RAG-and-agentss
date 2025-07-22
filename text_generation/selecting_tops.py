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

prompt="""
create the best slogan for online music streaming website/app that features unique experience

"""
top_k = 20
top_p = 0.7
config = GenerationConfig(temperature=0.9, top_p=top_p, top_k=top_k)
response = model.generate_content(prompt, generation_config=config)

print(f"[top_k = {top_k}]")
print(f"[top_p = {top_p}]")
print(response.text)

#top n and top k are really probability controllers,,, in return help randomness etc... research.....