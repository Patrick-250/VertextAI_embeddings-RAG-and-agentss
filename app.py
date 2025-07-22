from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import vertexai
from vertexai.language_models import TextEmbeddingModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


key_path="./vertexai.json"

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

embedding_model=TextEmbeddingModel.from_pretrained("text-embedding-005")


# embedding = embedding_model.get_embeddings(["Patrick"])

#print(embedding)
# vector=embedding[0].values
#print(f"length:{len(vector)}")

#cosine similarity search on different sentences

#start by creating embeddings for different sentences

sentence1_embedding=embedding_model.get_embeddings(["can you recommend me some ai/ml learning resources"])
sentence2_embedding=embedding_model.get_embeddings(["can you recommend me a good ai/ml engineering book?"])
sentence3_embedding=embedding_model.get_embeddings(["what are the secret to being the best tools in music production?"])
#then lets extract individual vectors from embeddings

vector1=[sentence1_embedding[0].values]
vector2=[sentence2_embedding[0].values]
vector3=[sentence3_embedding[0].values]
#print the cosine similarity of specific sentence params
print(cosine_similarity(vector1,vector1)) #should be 1 since the sentences 100% are identical
print(cosine_similarity(vector1,vector2)) #close to one since a book is a resource for learning ai/ml
print(cosine_similarity(vector2,vector3)) #middle similarity
print(cosine_similarity(vector1,vector3)) #middle similarity
print(cosine_similarity(vector3,vector3))#should be 1 since the sentences 100% are identical

#now i can actually vizualize(kinda) the embeddings in 2D space check vizulaize.py

