#!/usr/bin/env python
# coding: utf-8

# # Chocolate Sales

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv(r"C:\Users\mail2\Downloads\Chocolate Sales.csv")
data


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data.describe(include='all')


# In[7]:


data.shape


# In[8]:


# detecting missing values
data.isnull()


# In[9]:


data.isnull().sum()


# In[10]:


data.duplicated()


# In[11]:


data.duplicated().sum()


# In[12]:


sorted_data = data.sort_values(by='Boxes Shipped', ascending = False)
sorted_data


# In[13]:


sorted_data = data.sort_values(by=['Amount','Boxes Shipped'],ascending=[False,False])
sorted_data


# In[14]:


data['Amount']=data["Amount"].replace('[\$,]', '', regex=True).astype(float)

print(data)



# In[15]:


print(data.columns)


# # Visualisation  Sales Performance
# 

# In[16]:


#Total sales per salesperson


# # Sales by country

# In[17]:


plt.figure(figsize=(14,6))
sns.countplot(x='Country',data=data, palette='rocket')
plt.title('Sales Count by Country', fontsize =15)
plt.xlabel('Country',fontsize=12)
plt.ylabel('Sales Count', fontsize=12)
plt.xticks(rotation=45,ha='right')
plt.show()


# # Sales by product

# In[18]:


plt.figure(figsize=(30,15))
sns.countplot(x='Product', data=data,palette='rocket')
plt.title('Sales by Product', fontsize=14)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Product count',fontsize =12)
plt.xticks(rotation=45,ha='right')
plt.show()


# # Distribution of sales amount

# In[19]:


plt.figure(figsize=(8,6))
sns.histplot(data['Amount'], kde=True, color='green',bins=20)
plt.title('Distribution of Sales Amount',fontsize =14)
plt.xlabel('Sales Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(y=data['Boxes Shipped'], color='green')
plt.title('Box Plot of Boxes Shipped', fontsize=16)
plt.ylabel('Boxes Shipped', fontsize=12)
plt.show()


# # Distribution by sales person 

# In[20]:


plt.figure(figsize=(12,4))
sns.histplot(data['Sales Person'],color='green',bins=20)
plt.title('Sales per person', fontsize=16)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45,ha='right')
plt.show()


# # Best Sales Person 

# In[33]:


#aggregate the total sales by sales person
salesbyperson=data.groupby('Sales Person')['Amount'].sum().reset_index()

# Identify the Best Seller.
bestseller = salesbyperson.loc[salesbyperson['Amount'].idxmax(),'Sales Person']

# Highlight the Best Seller.
colors = ['red' if person == bestseller else 'skyblue' for person in salesbyperson['Sales Person']]

# Plot.
plt.figure(figsize=(12, 6))
sns.barplot(data=salesbyperson, x='Sales Person', y='Amount', palette=colors)
plt.xlabel("Sales Person")
plt.ylabel("Total Sales ($)")
plt.title("Sales by Person")
plt.tight_layout()
plt.xticks(rotation=45, fontsize=8);
plt.show()


# # Sales Over Time

# In[22]:



#convert date column to datetime format
data['Date']=pd.to_datetime(data['Date'],format='%d-%b-%y')
#group by date and calcuate total sales
salestrend=data.groupby('Date')['Amount'].sum().reset_index()
#plot sales trend
plt.figure(figsize=(20,4))
#plt.plot(salestrend['Date'], salestrend['Amount'],color='b')
sns.lineplot(x='Date', y='Amount', data=salestrend, color='steelblue')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:





# # Monthly Sales Distribution 

# In[23]:


#convert date column to datetime format
data['Date']=pd.to_datetime(data['Date'],format='%d-%b-%y')
#group by date and calcuate total sales
salestrend=data.groupby('Date')['Amount'].sum().reset_index()
#plot sales trend
plt.figure(figsize=(20,4))
salestrend = data.groupby(pd.Grouper(key='Date', freq='M'))['Amount'].sum().reset_index()
sns.lineplot(x='Date', y='Amount', data=salestrend, color='steelblue')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:





# # Sales Trend by Country and Product

# In[24]:


plt.figure(figsize=(16, 8))
sns.countplot(x='Country', hue='Product', data=data,palette='Paired')
plt.title('Sales Trends by Country and Product', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Sales Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# # Most Popular Product

# In[38]:


productcounts = data['Product'].value_counts()
productcounts


# In[41]:


#plot
plt.figure(figsize=(12, 6))
sns.barplot(x=productcounts.index, y=product_counts.values, palette='rocket')
plt.title("Most Popular Products by Sales Count", fontsize=16)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Number of Sales", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.show()


# # Popular Product by sales amount

# In[43]:


popularproduct= data.groupby('Product')['Amount'].sum().idxmax()
popularproduct


# In[44]:


#aggregate the product by sales amount
popularproduct=data.groupby('Product')['Amount'].sum().reset_index()

# Identify the Best Seller.
bestseller = popularproduct.loc[popularproduct['Amount'].idxmax(),'Product']

# Highlight the Best Seller.
colors = ['red' if product == bestseller else 'skyblue' for product in popularproduct['Product']]

# Plot.
plt.figure(figsize=(12, 6))
sns.barplot(data=popularproduct, x='Product', y='Amount', palette=colors)
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.title("Popular Product by sales amount")
plt.tight_layout()
plt.xticks(rotation=45, fontsize=8);
plt.show()


# In[ ]:




