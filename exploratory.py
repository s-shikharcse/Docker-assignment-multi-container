
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.model_selection import train_test_split
import pickle


# In[4]:


df = pd.read_csv("Ex03_SystolicBP_Regreesion.csv")


# In[7]:


X = df.iloc()[:, 0:-1]
y = df.iloc()[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 20, random_state = 0)


# In[6]:


pickle_out = open("X_train_file.pkl","wb")
pickle.dump(X_train, pickle_out)
pickle_out.close()

pickle_out = open("X_test_file.pkl","wb")
pickle.dump(X_test, pickle_out)
pickle_out.close()

pickle_out = open("y_train_file.pkl","wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()

pickle_out = open("y_test_file.pkl","wb")
pickle.dump(y_test, pickle_out)
pickle_out.close()

