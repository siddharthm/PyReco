from recommendations import getRecommendations,critics,topMatches,sim_distance,transform

def buildSimilarityDict(pref,similarity=sim_distance):
	result={}
	prefs=transform(pref)
	for item in prefs:
		scores=topMatches(prefs,item,5,similarity)
		result[item]=scores
	return result

def itemBasedReco(prefs,simDict,user):
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
	return rankings

simDict=buildSimilarityDict(critics)
# print itemBasedReco(critics,simDict,'Toby')	
		
