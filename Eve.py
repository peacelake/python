# my_settings = {
#     'MONGO_HOST': 'localhost',
#     'MONGO_PORT': 27017,
#     'MONGO_DBNAME': 'the_db_name',
#     'DOMAIN': {'contacts': {}}
# }
import os
from eve import Eve
from eve.auth import BasicAuth

# app = Eve(settings=my_settings)

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'


class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin' and password == 'secret'


app = Eve(auth=MyBasicAuth)


@app.after_request
def after_request(response):
    response.headers.add('X-Ahmed', 'Je Suis Ahmed.')
    response.headers.add('X-Charlie', 'Je Suis Charlie.')
    return response


if __name__ == '__main__':
    app.run(host=host, port=port)


# $ curl -i http://example.com
# HTTP/1.1 401 UNAUTHORIZED
# Please provide proper credentials.
#
# $ curl -H "Authorization: Basic YWRtaW46c2VjcmV0" -i http://example.com
# HTTP/1.1 200 OK
