from cassandra.cluster import Cluster
import random
import string

cluster = Cluster(['10.144.57.203'])
session = cluster.connect('test')
#session.set_keyspace('test')
#session.execute('use test')

#rows = session.execute('select token(name) as tokenid, name, address from users')
#for r in rows:
#    print r.tokenid, r.name, r.address

session.execute(
    """
    INSERT INTO users (name, address)
    VALUES (%s, %s)
    """,
    ("John O'Reilly", "Xi'an")
)

#rows = session.execute('select token(name), name, address from users')
#for r in rows:
#    print r[0], r[1], r[2]

for x in range(0, 10000) :
    s1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    s2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    #print s1, s2
    session.execute(
            """
            INSERT INTO users (name, address)
            VALUES (%s, %s)
            """,
            (s1, s2)
            )
    print x
