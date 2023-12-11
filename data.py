#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.express as px

# 엑셀 파일 읽기
file = pd.read_excel('c:/analysis/아파트_최종.xlsx')

# '평당 월세' 열의 음수 값 제거
file_cleaned = file[file['평당 월세'] >= 0]

# '계약년월'로 정렬
file_cleaned = file_cleaned.sort_values(by='계약년월')

# 동적 시각화
fig = px.scatter(file_cleaned, x='계약년월', y='평당 월세', color='평당 월세', size='평당 월세', title='평당 월세에 따른 동적 시각화')

# X축 간격 조정
fig.update_layout(xaxis=dict(type='category'))

fig.show()


# In[3]:


import pandas as pd
import plotly.express as px

# 엑셀 파일 읽기
file = pd.read_excel('c:/analysis/연립다세대_최종.xlsx')

# '평당 월세' 열의 음수 값 제거
file_cleaned = file[file['평당 월세'] >= 0]

# '계약년월'로 정렬
file_cleaned = file_cleaned.sort_values(by='계약년월')

# 동적 시각화
fig = px.scatter(file_cleaned, x='계약년월', y='평당 월세', color='평당 월세', size='평당 월세', title='평당 월세에 따른 동적 시각화')

# X축 간격 조정
fig.update_layout(xaxis=dict(type='category'))

fig.show()


# In[4]:


import pandas as pd
import plotly.express as px

# 엑셀 파일 읽기
file = pd.read_excel('c:/analysis/단독다가구_최종.xlsx')

# '평당 월세' 열의 음수 값 제거
file_cleaned = file[file['평당 월세'] >= 0]

# 최대값을 가진 행 제외
max_value_index = file_cleaned['평당 월세'].idxmax()
file_cleaned = file_cleaned.drop(index=max_value_index)

# '계약년월'로 정렬
file_cleaned = file_cleaned.sort_values(by='계약년월')

# 동적 시각화
fig = px.scatter(file_cleaned, x='계약년월', y='평당 월세', color='평당 월세', size='평당 월세', title='평당 월세에 따른 동적 시각화')

# X축 간격 조정
fig.update_layout(xaxis=dict(type='category'))

fig.show()


# In[1]:


get_ipython().system(' pip install gunicorn')


# In[2]:


get_ipython().system(' pip freeze')


# In[ ]:




