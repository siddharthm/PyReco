PyReco is a simple recommendation engine written in python 2.7 that 
given a list of people and their ratings corresponding to some items
can return recommendation of items for a person. It can also give items
that are similar to a given item and people that are similar to a given 
person.

It makes use of similarity ratings between the person for whom items 
have to be recommended and some other person to act as a weight for 
the rating of other person to predict the possible rating of that item
for the person. It then takes the weighted sum average over all such
other persons to get the expected rating for a item. This is done for 
all non rated movies of the person and then the expected ratings are 
sorted in descending order and returned as recommendations.

It also has functions for item based collabrative filtering provided
in the file itembased.py

Deployed it on pythonanywhere
    Can see e.g of recommendations for Toby at http://siddharth.pythonanywhere.com/reco/

Update: Added support for retriving data from delicious in deliciousrec.py
although it is slow due to delicious API limitations. You must install
pydelicious first which is a python script providing functions to retrive
data from delicious
