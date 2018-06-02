
# coding: utf-8

# In[39]:


import pickle
from datetime import datetime


# In[40]:


pickle_in = open("model_1_score_file.pkl", "rb")
model_1_score = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("model_2_score_file.pkl", "rb")
model_2_score = pickle.load(pickle_in)
pickle_in.close()


# In[41]:


datestring = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
file = open('dataOn_'+datestring+'.txt', "w")

if model_1_score > model_2_score:
   file.write("model_1 is better \n")
   file.write("model_1 score is \n")
   #file.write(model_1_score)
elif model_1_score < model_2_score:
    file.write("model_2 is better \n")
    file.write("model_2 score is \n")
    #file.write(model_2_score)
else:
    file.write("Both model have equal accuracy")

file.close()

