from recommendations import getRecommendations,critics,topMatches,sim_distance,transform

# Builds a dictionary of all items mapped to their top 5
# similar items returns mapping of form (item,(score,item2))

def buildSimilarityDict(pref,similarity=sim_distance):
	result={}
	prefs=transform(pref)
	for item in prefs:
		scores=topMatches(prefs,item,5,similarity)
		result[item]=scores
	return result

# Returns a list top n recommendations for a given user
# based on item based collabrative filtering

def itemBasedReco(prefs,simDict,user,n=5):
	scores={}
	totalSim={}
	for item in prefs[user]:
		for sim,item2 in simDict[item]:
			if item2 in prefs[user]: continue
			scores.setdefault(item2,0)
			scores[item2]+=sim*prefs[user][item]
			totalSim.setdefault(item2,0)
			totalSim[item2]+=sim
	rankings=[(scores[item]/totalSim[item],item) for item in scores]
	rankings.sort()
	rankings.reverse()
	return rankings[0:n]

simDict=buildSimilarityDict(critics)
# print itemBasedReco(critics,simDict,'Toby')	
		
