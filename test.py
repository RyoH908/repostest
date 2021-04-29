# Databricks notebook source
import sys
import os
import example

# COMMAND ----------

import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e']
)

# COMMAND ----------

df.head(5)

# COMMAND ----------

display(df)

# COMMAND ----------

profile = ProfileReport(df, title='Pandas Profiling Report')

# COMMAND ----------

example.add(2,3)

# COMMAND ----------

example.multi(2,2.9)

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore/tables/titanic/")

# COMMAND ----------


