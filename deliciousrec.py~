from pydelicious import get_popular,get_userposts,get_urlposts
import time
# A function to return the list of users who have posted a
# popular link containing a given tag. Top 'count' URLs 
# are considered for this purpose
def initializeUserDict(tag,count=5):
	user_dict={}
	for p1 in get_popular(tag=tag)[0:count]:
		for p2 in get_urlposts(p1['url']):
			user=p2['user']
			user_dict[user]={}
	return user_dict



def fillItems(user_dict):
	all_items={}
	for user in user_dict:		
		posts={}
		for i in range(3,6):
			try: 
				posts=get_userposts(user)
				break
			except:
				print "Failed for user "+ user + " Retrying..."
				time.sleep(4)
				posts=1
		if posts != {}:
			for post in posts:
				url=post['url']
				user_dict[user][url]=1.0
				all_items[url]=1
	for user in user_dict:
		for url in all_items:
			if url not in user_dict[user]:
				user_dict[user][url]=1.0

users=initializeUserDict('coding')
print users
fillItems(users)
for user in users:
	print users[user]
				

			
		
