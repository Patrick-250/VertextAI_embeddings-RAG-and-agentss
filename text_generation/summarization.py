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

transcript= """
{
  "conversation_id": "conv_20250722_001",
  "timestamp": "2025-07-22T18:10:00Z",
  "participants": {
    "customer": {
      "id": "cust_001",
      "name": "Chris"
    },
    "agent": {
      "id": "agent_001",
      "name": "Angel"
    }
  },
  "messages": [
    {
      "sender": "customer",
      "timestamp": "2025-07-22T18:01:12Z",
      "message": "Hi, I need help tracking my package. It's been a week since I ordered."
    },
    {
      "sender": "agent",
      "timestamp": "2025-07-22T18:01:40Z",
      "message": "Hi Chris! I'd be happy to help. Can you share your order number with me?"
    },
    {
      "sender": "customer",
      "timestamp": "2025-07-22T18:02:03Z",
      "message": "Yes, it’s #ORD789123."
    },
    {
      "sender": "agent",
      "timestamp": "2025-07-22T18:02:30Z",
      "message": "Thanks! I see your package is currently in transit and should be delivered by tomorrow."
    },
    {
      "sender": "customer",
      "timestamp": "2025-07-22T18:02:55Z",
      "message": "Great, thanks for the update!"
    },
    {
      "sender": "agent",
      "timestamp": "2025-07-22T18:03:10Z",
      "message": "You're welcome, Chris! Let me know if you need help with anything else."
    }
  ]
}
"""

prompt=f"""
Given the following transcript of a customer support chat:{transcript}
1.Determine the overall sentiment of the conversation, was the customer happy?
2.Extract the list of resolution provided by the agent 
3.how long did the chat last?, was there too much latency?
"""
top_k = 20
top_p = 0.7
max_token=200
config = GenerationConfig(temperature=0.9, top_p=top_p, top_k=top_k, max_output_tokens=max_token) #fewer tokens to control my spending

response=model.generate_content(prompt,generation_config=config)
print(response.text)