# coding: utf-8
import pandas as pd
df = pd.read_csv('survey_results_public.csv')
df.head()
df.shape
df['Age'].value_counts()
df['Age'].value_counts(normalize=True)
get_ipython().run_line_magic('matplotlib', 'inline')
df['Age'].value_counts().plot(kind='pie', figsize=(15,7))
df['Age'].value_counts().plot(kind='bar',figsize=(15,7))
whoseRussian = df[df['Country'] == 'Russian Federation']
whoseRussian.head()
whoseRussian.shape
whoseRussian['Age'].value_counts()
