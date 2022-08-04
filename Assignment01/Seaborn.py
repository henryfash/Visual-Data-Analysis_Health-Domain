import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
# Question 1
sns.relplot(x="time", y="day", data=tips);
plt.show()
# Question 2 + 3
sns.relplot(x="total_bill", y="tip", style="sex", data=tips);
plt.show()
print("done")