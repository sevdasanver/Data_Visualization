#!/usr/bin/env python
# coding: utf-8

# # Data Visualization 
# 
# 
# ![image-2.png](attachment:image-2.png)
# 
# ## Matplotlib
# 
# Matplotlib is an important library for creating static, animated, and interactive figure visualizations in Python.
# 
# - <code>figsize</code>: Defines the width and height of the figure in inches. The first value in paranthesis is width,and the second one is height.
# - <code>plt.xlabel()</code> : Sets the label for the **x-axis**.
# - <code>plt.ylabel()</code> : Sets the label for the **y-axis**.
# - <code>plt.title()</code> : Specifies title of the visualization.
# - <code>plt.show()</code> : Displays figures. If we do not write this code, the graph will be generated, however, would not be displayed on screen.
# 
# 
# 
# 
# ![image-3.png](attachment:image-3.png)
# 
# ## Seaborn
# 
# Seaborn is a library that uses Matplotlib underneath to plot graphs. 
# It provides a high-level interface for drawing attractive and informative statistical graphics.
# 
# 

# In[1]:


# Import Matplotlib ve Seaborn libraries

import matplotlib.pyplot as plt
import seaborn as sns


# Import pandas portion of the code to tell Python to bring the pandas data analysis library into our current environment.

import pandas as pd


# In[2]:


df = pd.read_csv('credit_card_fixed.csv')


# In[3]:


# Check the number of rows, number of columns of data set

df.shape


# In[4]:


#Access the first n (which is 10) rows of a data frame (df) of series

df.head(n = 10)


# In[5]:


# Check the statistical descriptions out of the data 

df.describe()


# # Grouping Data in Python
# 
# 
# <code>groupby</code> function is used to split the data into groups based on some criteria such as mean, min, max value, standard deviation. It is stated by <code>agg</code> which is an alias for aggregate.
# 
# 
# 

# In[6]:


# Age averages of users based on cities they live

df.groupby('user_city').agg({'user_age':'mean'})


# In[7]:


# Max and min ages based on city names 

df.groupby('user_city').agg({'user_age': 'min'})


# # EXAMPLE - 1
# 
# 
# Find the average age of the credit card users based on their genders.

# In[8]:


df.groupby('user_gender').agg({'user_age': 'mean'})


# # Data Visualization Techniques
# 
# - Data visualization is the process of creating graphical representations of information. 
# - It allows us to gain insight into their vast amounts of data. 
# 
# There are a number of ways to visualize data.
# 
# Here are some important data visualization techniques to know:
# 
# - Bar Chart,
# Pie Chart,
# Scatter Plot,
# Line Chart,
# Histogram,
# Heat Map,
# Box and Whisker Plot,
# Waterfall Chart,
# Area Chart etc.
# 
# ## 1. Bar Chart
# 
# - It presents categorical data with rectangular bars with lengths proportional to the values that they represent.
# 
# - One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.
# 
# 
# 
# ### Average credit card expenses based on cities 
# 
# - Find the average credit card expenses based on cities.

# In[9]:


df.groupby('user_city').agg({'total_amount':'mean'})


# In[10]:


df.groupby('user_city').agg({'total_amount':'mean'}).reset_index()


# In[12]:


#matplotlib

plt.figure(figsize = (12,6))

plt.bar(data = df.groupby('user_city').agg({'total_amount':'mean'}).reset_index(), 
        x = 'user_city',
        height = 'total_amount')
    
plt.show()


# In[13]:


# Creating bar chart in seaborn

plt.figure(figsize = (12,6))
sns.barplot(data = df.groupby('user_city').agg({'total_amount':'mean'}).reset_index(), 
        y ='user_city',
        x ='total_amount')
plt.show()


# In[14]:


# Find total money they spend based on cities
#You can write max or min instead of sum, and see them on bar chart

plt.figure(figsize = (12,6))
sns.barplot(data = df.groupby('user_city').agg({'total_amount':'sum'}).reset_index(), 
        y = 'user_city',
        x = 'total_amount')
plt.show()


# ## Seaborn Styles
# 
# There are multiple options for the background in seaborn such as;
# 
# ### -  sns.set_style('darkgrid')
# ### -  sns.set_style('whitegrid')
# ### -  sns.set_style('dark')
# ### -  sns.set_style('white')

# In[15]:


sns.set_style('darkgrid')
#sns.set_style('whitegrid')
#sns.set_style('dark')
# sns.set_style('white')

## seaborn

plt.figure(figsize = (12,6))
sns.barplot(data = df.groupby('user_city').agg({'total_amount':'sum'}).reset_index(), 
        y = 'user_city',
        x = 'total_amount')
plt.show()


# # EXAMPLE - 2
# 
# Create a bar chart that shows credit card total amount they spent vs user gender with mathplot and seaborn libraries.
# 

# In[16]:


df.head()


# In[17]:


plt.figure(figsize = (12,6))
sns.barplot(data = df.groupby('user_gender').agg({'total_amount':'mean'}).reset_index(), 
        y='user_gender',
        x='total_amount')
plt.show()


# ## 2. Pie Chart
# 
# - Pie chart is generally used when trying to compare the catagorical data.
# - Pie charts are ideal for giving a quick idea of the proportional distribution of data to the reader.
# - <code>plt.pie</code> is used for creating pie chart, 
# - It is of two main parameters as **x** and **labels**.
# 
# 
# ### Number of Observations of Cities
# 
# - Plot the number of credit card users based on cities.

# In[18]:


df.groupby('user_city').agg({'user_id': 'count'}).reset_index()


# In[19]:


plt.figure(figsize = (14,6))

plt.pie(data = df.groupby('user_city').agg({'user_id': 'count'}).reset_index(),
       x = 'user_id',
       labels = 'user_city')

plt.title('Credit card users based on cities;', size = 12, color = 'green')
plt.show()


# ## Seaborn "Countplot" has the same function as "Pie Chart"!

# In[20]:


# Color Palettes

sns.countplot(data = df,
             y = 'user_city',
            # color ='pink'
             palette = 'Set1')

plt.show()


# # EXAMPLE - 3
# 
# - Show the user numbers with Countplot or Pie Chart based on genders.
# 

# In[21]:


# Color Palettes

sns.countplot(data = df,
             x ='user_gender',
             color = 'green')
plt.title('Number of users based on genders', size = 12)
plt.show()


# ## 3. Scatter Plot
# 
# - If you have two variables that pair well together, plotting them on a scatter diagram is a great way to view their relationship and see if it's a positive or negative correlation. 
# - Even if we cannot understand the reason of the relationship, we can understand if there is a relationship or how strong the it is.
# - <code>plt.scatter</code> is used to create a scatter plot with Matplotlib.
# 
# 
# ![image.png](attachment:image.png)

# In[22]:


plt.scatter(data = df,
           x = 'user_age',
           y = 'total_amount')


plt.title('The relationship between the user age and credit card expenses', size = 14)
plt.xlabel('User age',size = 11)
plt.ylabel('Credit card expenses',size = 11)

plt.show()


# ## 4. Line Chart
# 
# - Line charts are used to represent quantitative data collected over a specific subject and a specific time interval. 
# - Generally we write dates/days on **x-axis** and quantitative data on **y-axis**
# - <code>plt.plot</code> is used to create a scatter plot with Matplotlib.
# 
# 
# 
# ## Show the number of users who received credit cards on the basis of dates with a line chart
# 

# In[23]:


df['card_delivery_date'].value_counts()


# In[24]:


df['card_delivery_date'].dtype


# In[25]:


#Convert it to date format
#type(pd.to_datetime('2022-01-03'))

pd.to_datetime('2022-01-03')


# In[26]:


df['card_delivery_date'] = pd.to_datetime(df['card_delivery_date'])
df


# In[27]:


card_df = df.groupby('card_delivery_date').agg({'user_id':'count'}).reset_index()


# In[28]:


card_df


# In[29]:


plt.figure(figsize = (12,6))

sns.lineplot(data = card_df,
            x = 'card_delivery_date',
            y = 'user_id')

plt.title('The number of user who recevied the credit cards based on dates', size = 12)

plt.show()


# ## 5. Histogram
# 
# - Histogram is used when the data are numerical.
# - They display the shape of the data's frequency distribution, especially when determining whether the output of a process is distributed approximately normally.
# 
# 
# ## Show the distribution of total expenditure with histogram 

# In[30]:


plt.figure(figsize = (12,6))
sns.histplot(data = df,
            x = 'total_amount')

plt.show()


# # EXAMPLE - 4
# 
# Show age distribution with histogram.

# In[31]:


plt.figure(figsize = (8,5))
sns.histplot(data = df, x = 'user_age')

plt.show()


# # Plotly
# 
# - Plotly is a sophisticated data visualization library that is suited for creating elaborate plots efficiently. 
# - It is an open source tool, and has 40 different visualization package.
# - It has 2 main parameters as **data** and **layout**.
# - **Data** is the part where we specify the visualization type and data.
# - **Layout** is the part where we specify the graph features such as titles, color, size, theme etc.
# 
# 

# In[ ]:


get_ipython().system('pip install plotly')


# In[33]:


import plotly.graph_objs as go

from plotly.offline import iplot


# In[34]:


# Total spending amaounts based on the cities where users live 

bar_df = df.groupby('user_city').agg({'total_amount' : 'sum'}).reset_index()


# In[35]:


bar = go.Bar(x = bar_df['user_city'],
      y = bar_df['total_amount'])

fig = go.Figure(data = bar)

iplot(fig)


# In[36]:


scatter = go.Scatter(x = df['user_age'],
          y = df['total_amount'],
                   mode ='markers')

fig = go.Figure(data = scatter)
iplot(fig)


# In[37]:


scatter = go.Scatter(x = df['user_age'],
          y = df['total_amount'],
                   mode = 'markers',
                   marker = dict(size = 8,
                               color = 'blue',
                               opacity = 0.65)
                    )

layout = go.Layout(title = dict(text = 'The relationship between user age and total expenditure'),
                   xaxis = dict(title = 'Age'),
                   yaxis = dict(title = 'How much they spent'))

fig = go.Figure(data = scatter, layout = layout)

iplot(fig)


# ### Relationship of Age-Total Expenditure Based on Genders 

# In[38]:


male = df.loc[df['user_gender'] == 'Male']
female = df.loc[df['user_gender'] == 'Female']


male_scatter = go.Scatter(x = male['user_age'],
                        y = male['total_amount'],
                        mode = 'markers',
                        name = 'Male')

female_scatter = go.Scatter(x = female['user_age'],
                        y = female['total_amount'],
                        mode ='markers',
                        name ='Feale')

gender_layout = go.Layout(title = dict(text = 'Age-Total Expenditure Relationship Based on Genders'),
                         xaxis = dict(title ='Age'),
                         yaxis = dict(title = 'Total Expenditure'),
                         template = 'plotly_dark')                          
                         
fig = go.Figure (data = [male_scatter, female_scatter], layout = gender_layout)
                         
iplot(fig)
                         


# # FINAL PROJECT

# In[39]:


from plotly.subplots import make_subplots


# In[40]:


def city_analysis():
    
    city = str(input('Enter a city: '))
    
    if city not in df['user_city'].unique():
        
        print('The city you enter is not on our list.. Sorry :(')
        
    else:
    
        city_data = df.loc[df['user_city'] == city]
        
        bar_df = city_data.groupby('user_gender').agg({'total_amount': 'mean'}).reset_index()
        
        fig = make_subplots(rows = 1,
                            cols = 2,
                            subplot_titles = ['Average consumption based on gender',
                                              'Age & Consumption Relationship'])
        
        fig.add_trace(go.Bar(x = bar_df['user_gender'],
                             y = bar_df['total_amount'],
                             showlegend = False),
                      
                      row = 1, col = 1)
        
        fig.add_trace(go.Scatter(x = city_data['total_amount'],
                                y = city_data['user_age'],
                                showlegend = False,
                                mode = 'markers'),
                     
                     row = 1, col = 2)
        
        fig.update_layout(title = dict(text = city + ' Credit Card Consumption Analysis ',
                                      x = 0.5),
                         xaxis = dict(title = 'Gender'),
                         yaxis = dict(title = 'Total Expenditure'),
                         xaxis2 = dict(title = 'Total Expenditure'),
                         yaxis2 = dict(title = 'Age'),
                         template = 'plotly_dark')
        
        iplot(fig)


# In[41]:


city_analysis()


# In[43]:


city_analysis()


# In[44]:


city_analysis()


# In[ ]:




