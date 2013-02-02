PyReco is a simple recommendation engine written in python 2.7 that 
given a list of people and their ratings corresponding to some movies
can return recommendation of movies for a person. It can also give movies
that are similar to a given movie and people that are similar to a given 
person.
	It makes use of similarity ratings between the person for whom
movie has to be recommended and some other person to act as a weight for 
the rating of other person to predict the possible rating of that movie
for the person. It then takes the weighted sum average over all such
other persons to get the expected rating for a movie. This is done for 
all non rated movies and then the expected ratings are sorted in descending
order and returned as recommendations.
