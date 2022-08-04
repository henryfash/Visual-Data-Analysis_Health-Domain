
# Exercise 04

import pandas as pd
import numpy as np
import seaborn as sns
sns.set(style="darkgrid")
import matplotlib.pyplot as plt

#Read the excel file
# 4d
df = pd.read_excel("chronic_kidney_disease_numerical.xls")

# 4f
# Boxplot for attribute age
sns.catplot(x="class", y="age", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);

# Boxplot for attribute blood pressure
sns.catplot(x="class", y="blood pressure", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute  specific gravity
sns.catplot(x="class", y="specific gravity", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute  albumin
sns.catplot(x="class", y="albumin", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);

# Boxplot for attribute sugar
sns.catplot(x="class", y="sugar", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);

# Boxplot for attributeblood glucose random
sns.catplot(x="class", y="blood glucose random", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute  blood urea
sns.catplot(x="class",y="blood urea", data=df,kind="box", sharey =False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute serum creatinine
sns.catplot(x="class", y="serum creatinine", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);



# Boxplot for attribute  sodium
sns.catplot(x="class", y="sodium", data=df, kind ="box", sharey=False,
                 order=["ckd", "notckd"]);

# Boxplot for attribute potassium
sns.catplot(x="class", y="potassium", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);



# Boxplot for attribute hemoglobin
sns.catplot(x="class", y="hemoglobin",  data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute packed cell volume
sns.catplot(x="class", y="packed cell volume", data=df,kind= "box", sharey =False,
                 order=["ckd", "notckd"]);

# Boxplot for attribute whilte blood cell
sns.catplot(x="class", y="white blood cell count", data=df, kind="box", sharey=False,
                 order=["ckd", "notckd"]);


# Boxplot for attribute red blood cell count
sns.catplot(x="class", y="red blood cell count",  data=df,kind ="box", sharey=False,
                 order=["ckd", "notckd"]);


# Tranform data from wide to long format 
# Exercise 4e
df = pd.melt(df, id_vars = ["class"])
print (df)