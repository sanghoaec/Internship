#!/usr/bin/env python
# coding: utf-8

# 1. Write a python program to display all the header tags from wikipedia.org.

# In[256]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests.')


# In[7]:


from bs4 import BeautifulSoup
import requests


# In[258]:


page=requests.get('https://www.wikipedia.org')


# In[259]:


page


# In[260]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[ ]:


# 2.Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
and make data frame


# In[12]:


import pandas as pd
import requests
from bs4  import BeautifulSoup


# In[124]:


url="https://www.imdb.com/chart/top"


# In[ ]:


# response=requests.get(url)


# In[126]:


response


# In[129]:


soup=BeautifulSoup(response.content,'html.parser')


# In[11]:


soup


# In[700]:


movies_name=BeautifulSoup(requests.get("https://www.imdb.com/chart/top").content,"html.parser")


# In[701]:


movies_name=[ i.text.split('\n')[2] for i in movies_name.find_all('td',class_="titleColumn")]


# In[702]:


movies_name


# In[704]:


movies_ratings=BeautifulSoup(requests.get("https://www.imdb.com/chart/top").content,"html.parser")


# In[705]:


movies_ratings=[i.text.split('\n')[1]  for i in movies_ratings.find_all('td',class_="ratingColumn imdbRating")]


# In[ ]:





# In[706]:


movies_ratings


# In[707]:


data=pd.DataFrame()


# In[708]:


data['movies_name']=movies_name


# In[709]:


data['movies_ratings']=movies_ratings


# In[710]:


data.head()


# 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[741]:


topmovies_name=BeautifulSoup(requests.get("https://www.imdb.com/india/top-rated-indian-movies/").content,"html.parser")


# In[742]:


topmovies_name=[i.text.split('\n')[2]  for  i in topmovies_name.find_all('td',class_="titleColumn")]


# In[743]:


topmovies_name


# In[744]:


topmovies_ratings=BeautifulSoup(requests.get("https://www.imdb.com/india/top-rated-indian-movies/").content,"html.parser")


# In[745]:


topmovies_ratings=[i.text.split('\n')[1] for i in topmovies_ratings.find_all('td',class_="ratingColumn imdbRating")]


# In[746]:


topmovies_ratings


# In[747]:


year=BeautifulSoup(requests.get("https://www.imdb.com/india/top-rated-indian-movies/").content,"html.parser")


# In[748]:


year=[i.text  for i in year.find_all('span',class_="secondaryInfo")]


# In[749]:


year


# In[750]:


data=pd.DataFrame()


# In[751]:


data['movies_name']=topmovies_name


# In[754]:


data['year']=year


# In[755]:


data['rating']=topmovies_ratings


# In[784]:


data.head(10)


# 
# 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
# from https://presidentofindia.nic.in/former-presidents.htm

# In[290]:



president_soup=BeautifulSoup(requests.get("https://presidentofindia.nic.in/former-presidents.htm").content,"html.parser")


name=[i.text.split('\n')[1] for i in president_soup.find_all('div',class_="presidentListing")]


# In[291]:


name


# In[531]:


office=president_soup.find_all('p')


# In[532]:


office


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating

# In[565]:


team_soup=BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").content,"html.parser")


# In[566]:


team_soup=[i.text  for i in team_soup.find_all('span',class_="u-hide-phablet")]


# In[567]:


team_soup


# In[611]:


rating=BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").content,"html.parser")


# In[612]:


rating=[i.text  for i in rating.find_all('td', class_="table-body__cell u-text-right rating")]


# In[614]:


rating


# In[618]:


points =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").content,"html.parser")


# In[619]:


points=[i.text  for i in points.find_all('td', class_="table-body__cell u-center-text")]


# In[620]:


points


# In[ ]:





# Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[761]:


batsman =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi?at=2022-01-01").content,"html.parser")


# In[762]:


batsman=[i.text.split('\n')[1]   for i in batsman.find_all('td', class_="table-body__cell name")]


# In[763]:


batsman


# In[770]:


team =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi?at=2022-01-01").content,"html.parser")


# In[771]:


team=[i.text.split('\n')[0]   for i in team.find_all('span', class_="table-body__logo-text")]


# In[772]:


team


# In[773]:


rating =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi?at=2022-01-01").content,"html.parser")


# In[776]:


rating=[i.text.split('\n')[0]   for i in rating.find_all('td', class_="table-body__cell u-text-right rating")]


# In[777]:


rating


# In[778]:


data=pd.DataFrame()


# In[779]:


data['batsman']=batsman


# In[780]:


data['team']=team


# In[781]:


data['rating']=rating


# In[783]:


data.head(10)


#  Top 10 ODI Batsmen along with the records of their team and rating.rating =BeautifulSoup(requests.get("https://www.icc-rating =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling").content,"html.parser")cricket.com/rankings/mens/player-rankings/odi/bowling").content,"html.parser")

# In[44]:


name =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling").content,"html.parser")


# In[45]:


name= [i.text for i in name.find_all('td', class_="table-body__cell rankings-table__name name")]


# In[46]:


name


# In[41]:


team =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling").content,"html.parser")


# In[29]:


team=[ i.text for i in team.find_all('span', class_="table-body__logo-text")]


# In[30]:


team


# In[31]:


bolwerrating =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling").content,"html.parser")


# In[32]:


bolwerrating=[i.text  for i in bolwerrating.find_all('td', class_="table-body__cell rating")]


# In[33]:


bolwerrating


# In[34]:


data=pd.DataFrame()


# In[35]:


data['bolwerrating']=bolwerrating


# In[36]:


data['team']=team


# In[47]:


data['name']=name


# In[48]:


data.head(10)


# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[219]:


team =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/womens/overview").content,"html.parser")


# In[220]:


team=[i.text  for i in team.find_all('td', class_="table-body__cell u-text-left nationality-logo")]


# In[221]:


team


# In[222]:


women_bating =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/womens/overview").content,"html.parser")


# In[223]:


women_bating=[i.text  for i in women_bating.find_all('td', class_="table-body__cell name")]


# In[225]:


women_bating


# In[227]:


women_allrounder =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/womens/overview").content,"html.parser")


# In[228]:


women_allrounder=[i.text  for i in women_allrounder.find_all('td', class_="table-body__cell name")]


# In[229]:


women_allrounder


# In[232]:


rating =BeautifulSoup(requests.get("https://www.icc-cricket.com/rankings/womens/overview").content,"html.parser")


# In[234]:


rating=[i.text  for i in rating.find_all('div', class_="rankings-block__banner--rating")]


# In[235]:


rating


# 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link

# In[123]:


link =BeautifulSoup(requests.get("https://www.cnbc.com/world/?region=world").content,"html.parser")



# In[124]:




link=[ i.text for i in link.find_all('div', class_="RiverHeadline-headline RiverHeadline-hasThumbnail")]


# In[125]:


link


# In[ ]:





# In[138]:


latestnews =BeautifulSoup(requests.get("https://www.cnbc.com/world/?region=world").content,"html.parser")


# In[139]:


latestnews=[ i.text for i in latestnews.find_all('div', class_="LatestNews-headlineWrapper")]


# In[140]:


latestnews


# 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :
# i) Paper Title 
# ii) Authors
# iii) Published Date 
# iv) Paper URL

# In[144]:


download =BeautifulSoup(requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles").content,"html.parser")


# In[142]:



download=[ i.text for i in download.find_all('h1', class_="sc-1qrq3sd-0 sc-orwwe2-4 iUciVs fuwoaH")]


# In[143]:


download


# In[269]:


title=[]

for i in BeautifulSoup.find_all("a",class_="sc-5smygv-0 fIXTHm"):

    title.append(i.get_text())


# In[ ]:





# In[ ]:





# In[ ]:





# 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[245]:


resturentname =BeautifulSoup(requests.get("https://www.dineout.co.in").content,"html.parser")


# In[246]:



resturentname=[ i.text for i in resturentname.find_all('div', class_="_1JdPN PGkDX")]


# In[248]:


resturentname


# In[266]:


rating=BeautifulSoup(requests.get("https://www.dineout.co.in").content,"html.parser")


# In[267]:



rating=[ i.text for i in rating.find_all('div', class_="kGUdK _1oTbl")]


# In[268]:


rating


# In[258]:





# In[259]:




