
# coding: utf-8

# In[13]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle


# In[14]:


pickle_in = open("exploratory/X_train_file.pkl","rb")
X_train = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("exploratory/X_test_file.pkl","rb")
X_test = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("exploratory/y_train_file.pkl","rb")
y_train = pickle.load(pickle_in)
pickle_in.close()

pickle_in = open("exploratory/y_test_file.pkl","rb")
y_test = pickle.load(pickle_in)
pickle_in.close()


# In[33]:


linreg = LinearRegression()

X_train.drop(X_train.columns[[2, 3, 4]], axis=1)
X_test.drop(X_train.columns[[2, 3, 4]], axis=1)

model_2 = linreg.fit(X_train, y_train)
predict_values_2 = model_1.predict(X_test)
model_2_score = r2_score(y_test, predict_values_1)


# In[34]:


pickle_out = open("model_2_score_file.pkl", "wb")
pickle.dump(model_2_score, pickle_out)
pickle_out.close()

