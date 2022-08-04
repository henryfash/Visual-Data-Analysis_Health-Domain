#!/usr/bin/env python
# coding: utf-8

# In[367]:


import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set(style="ticks")


# In[368]:


# 2a

df = pd.read_csv("winequality-red.csv", delimiter=";")
df.head()


# In[369]:


# 2b

# Histogram
plt.hist(df["quality"], bins =6,)
plt.xlabel("Quality")
plt.ylabel("Frequency")
plt.show()

# calculating the range
q_max = df["quality"].max()
q_min = df["quality"].min()
 
print("The range is : ", q_max, " and ", q_min)


# In[370]:


# 2c
#bins
bins = np.linspace(min(df["quality"]), max(df["quality"]), 4)

group_names = ['low', 'medium', 'high']

df["quality bin"] = pd.cut(df["quality"], bins, labels=group_names, include_lowest=True )

# Drop the column "quality"
df.drop(["quality"], axis =1, inplace =True)
df.head(15)


# In[371]:


# 2 d
medium_omitted =df[df["quality bin"]=="medium"].index

# drop rows with quality bin value = medium
df.drop(medium_omitted, inplace=True)
df.head()


# In[372]:


# 2e
ax = sns.pairplot(df, hue="quality bin",hue_order =["high", "low"], height = 2.5)


# In[373]:


# 2f
#Alcohol, sulphates, citric acid, volatile acidity,pH


# In[376]:


# 2g

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif, mutual_info_classif

X = df.iloc[:,0:11]
y =df.iloc[:,-1]

f_classif = SelectKBest(score_func=f_classif, k=5)
fit = f_classif.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)

#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Attributes','Score']  #naming the dataframe columns

# Vis as featureScore:
featureScores


# In[377]:


featureScores.nlargest(5,'Score')  #print 5 best features


# In[378]:


# Yes


# In[379]:


df = df[[ "volatile acidity","citric acid","pH","sulphates", "alcohol","quality bin"]]
df.head()


# In[380]:


# 2h
ax = sns.PairGrid(df, hue ="quality bin",hue_order =["high","low"],diag_sharey=False,height = 3)
ax.map_upper(plt.scatter)
ax.map_lower(sns.regplot, scatter = False)
ax.map_diag(sns.kdeplot, legend=False)


# In[382]:


# 2i
# There is a strong Negative correlation between pH and citric acidity

# Yes, sulphates has multimodal distribution

