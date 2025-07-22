
from app import embedding_model
from utils import plot_2D
import numpy as np
from sklearn.decomposition import PCA
input_1="can you recommend me some ai/ml learning resources"
input_2="can you recommend me a good ai/ml engineering book?"
input_3="what are the secret to being the best tools in music production?"

text_list=[input_1,input_2,input_3]
embeddings=[]

for input_text in text_list:
  emb_aux=embedding_model.get_embeddings([input_text])[0].values
  embeddings.append(emb_aux)
embeddings_array=np.array(embeddings)
print("shape: " +str(embeddings_array.shape)) #this printed (3,768) on my end
#(3,768) means 3 items 768 dimensions... cant really view in 768 dimensions haha

#reduce the 768 dimensions to 2D that i can see, can you see beyond 2D?????? with sklearn.decomposition PCA,principal component analysis
PCA_model=PCA(n_components=2) #number of dimensions to keep set to 2 
PCA_model.fit(embeddings_array)

new_embeddings=PCA_model.transform(embeddings_array)
print("shape: " +str(new_embeddings.shape))

plot_2D(new_embeddings[:,0],new_embeddings[:,1],text_list)