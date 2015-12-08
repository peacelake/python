from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('mykeyspace')
session.set_keyspace('mykeyspace')
session.execute('use mykeyspace')

rows = session.execute('select token(name) as tokenid, name, address from users')
for r in rows:
    print r.tokenid, r.name, r.address

session.execute(
    """
    INSERT INTO users (name, address)
    VALUES (%s, %s)
    """,
    ("John O'Reilly", "Xi'an")
)

rows = session.execute('select token(name), name, address from users')
for r in rows:
    print r[0], r[1], r[2]
