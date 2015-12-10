from cassandra.cluster import Cluster
import random
import string

cluster = Cluster(['10.144.57.203'])
session = cluster.connect('test')
session.default_timeout = 180 # in seconds

#session.set_keyspace('test')
#session.execute('use test')

#rows = session.execute('select count(*) as count from users')
#for r in rows:
#    print r[0]

users = ['usera', 'userb', 'userc', 'userd', 'usere']
games = ['game1', 'game2', 'game3']
years = [2011, 2012, 2013, 2014, 2015]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(0, 100000) :
    user = random.choice(users)
    game = random.choice(games)
    year = random.choice(years)
    month = random.choice(months)
    day = random.choice(days)
    score = random.choice(scores)

    session.execute(
            """
            INSERT INTO scores (user, game, year, month, day, score)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (user, game, year, month, day, score)
            )
    print x
