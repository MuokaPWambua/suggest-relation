users = [{"id": 0,"name": "Hero"}, {"id": 1,"name": "Dunn"}, {"id": 2,"name": "Sue"},{"id": 3,"name": "Chi"},\
    {"id":4,"name": "Thor"}, {"id": 5,"name": "Clive"}, {"id": 6,"name": "Hicks"}, {"id": 7, "name": "Devin"},\
    {"id": 8,"name": "Kate"}, {"id": 9,"name": "Klein"}]

friendships =[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)] 

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")]

# adding a group of friends to each user

for user in users:
    user['friends'] = [] 

#populating the friends list of user using friendships data

for i, j in friendships:
    users[i]['friends'].append(users[j]) #add i as a friend of j
    users[j]['friends'].append(users[i]) #add j as a friend of i


#total number of connections/friends

def number_of_friends(user):
    return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)

print(f'total connections: {total_connections}')

#average connections

average_connections = total_connections/ len(users)

print(f'average connections: {average_connections}')

#find users with a certain interest
def data_scientiest_who_like(interest):
    return[user_id for user_id, user_interest in interests if user_interest == interest]


#print user interested with machine learning
print(f'user interested with machine learning: {data_scientiest_who_like("machine learning")}')


# building an index from interests to users rather than to examine the  whole list of interest for every search
from collections import defaultdict, Counter

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
#from interest to users
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# get common interest
def most_common_interests_with(user):
    return Counter(interested_user_id for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest] if interested_user_id != user["id"])   


#print people you should know from common interest

print(f'people with common interest:{most_common_interests_with(users[0])}')
