#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a python program to display all the header tags from wikipedia.org.


# In[4]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests.')


# In[5]:


from bs4 import BeautifulSoup
import requests


# In[6]:


page=requests.get('https://www.wikipedia.org')


# In[7]:


page


# In[14]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame

# In[15]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[ ]:





# 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
# from https://presidentofindia.nic.in/former-presidents.htm

# In[23]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests.')


# In[56]:


from bs4 import BeautifulSoup
import requests


# In[80]:



president_soup=BeautifulSoup(requests.get("https://presidentofindia.nic.in/former-presidents.htm").content,"html.parser")


name=[i.text.split('\n')[1] for i in president_soup.find_all('div',class_="presidentListing")]


# In[81]:


name


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating

# In[ ]:





# In[62]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[66]:


country_soup=BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").content,"html.parser")


# In[ ]:





# In[67]:


countryname=[i.text  for i in country_soup.find_all('span',class_="u-hide-phablet")]


# In[68]:


countryname


# In[74]:


matches_soup=BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").content,"html.parser")


# In[75]:


matches=[i.text  for i in matches_soup.find_all('td',class_="ranking-block_banner--matches")]


# In[76]:


matches


# In[77]:


points=[i.text  for i in points_soup.find_all('td',class_="ranking-block_banner--points")]


# In[78]:


i in soup.find_all('td',class_="table-body__cell u-center-text"):


# In[79]:


match.append(i.text)


# In[ ]:





# In[ ]:




