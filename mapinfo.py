from google.appengine.ext import ndb

class Info(ndb.Model):
    title = ndb.StringProperty()
    info = ndb.StringProperty()
    content = ndb.StringProperty()
