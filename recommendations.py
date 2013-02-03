from math import sqrt

# A function to calculate similarity between person1 and person2 using eucledian metric
def sim_distance(pref,person1,person2):
	si={}
	for item in pref[person1]:
		if item in pref[person2]:
			si[item]=1
	n=len(si)
	if n==0:
		return 0
	sum_of_squares=sum([pow(pref[person1][item]-pref[person2][item],2) for item in si if si[item] ] )
	return 1/(1+sum_of_squares)

# A function to calculate the pearson distance between p1 and p2 using Pearson metric
def sim_pearson(pref,p1,p2):
	si={}
	for item in pref[p1]:
		if item in pref[p2]:
			si[item]=1
	if len(si)==0:
		return 0
	n=len(si)
	sum1=sum([pref[p1][it] for it in si ])
 	sum2=sum([pref[p2][it] for it in si ])

	sum1sq=sum([ pow(pref[p1][it],2) for it in si ])
	sum2sq=sum([ pow(pref[p2][it],2) for it in si ])

	psum=sum([ pref[p1][it]*pref[p2][it] for it in si ])
	num = psum-(sum1*sum2/n)
	den = sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
	if den==0: return 0
	return num/den	

# A function to return the top n best matches for a given person 
# The function optionally takes a similarity function as parameter
def topMatches(pref,person,n=5,similarity=sim_pearson):
	scores = [ (similarity(pref,person,other),other) for other in pref if other!=person ]
	scores.sort()
	scores.reverse()
	return scores[0:n]

# A function to return the recommendations of movies for a person 
# by using a weighted average of every other user's rating
def getRecommendations(pref,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in pref:
		if other==person:
			continue
		sim=similarity(pref,person,other)
		if sim<=0:
			continue
		for item in pref[other]:
			if item not in pref[person] or pref[person][item]==0:
				totals.setdefault(item,0)
				totals[item]+=(pref[other][item] * sim)
				simSums.setdefault(item,0)
				simSums[item]+=sim
	rankings=[(total/simSums[item],item) for item,total in totals.iteritems()]
	rankings.sort()
	rankings.reverse()
	return rankings

# A function that transforms the mapping from a,b-c to b,a-c
def transform(mat):
	result={}
	for person in mat:
		for item in mat[person]:
			result.setdefault(item,{})
			result[item][person]=mat[person][item]
	return result
	

# A dictionary of movie critics and their ratings of a small
# set of movies

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# print "Top 5 movies recommended for Toby using Pearson metric and euclidian metric"
# print getRecommendations(critics,'Toby')
# print getRecommendations(critics,'Toby',sim_distance)
# print "Top 5 movies similar to Superman Returns using Pearson and euclidian metric "
# movies=transform(critics)
# print topMatches(movies,'Superman Returns',5)
# print topMatches(movies,'Superman Returns',5,sim_distance)
