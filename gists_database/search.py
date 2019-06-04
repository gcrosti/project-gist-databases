from .models import Gist
from datetime import datetime

def search_gists(db_connection, **kwargs):
    l_gists = [Gist(g) for g in db_connection.execute('SELECT * FROM gists')]
    results = []
    if not kwargs:
        return l_gists
    for gist in l_gists:
        for key, value in kwargs.items():
            if type(value) == datetime:
                cleandatetime = getattr(gist,key).replace('T',' ').replace('Z','')
                setattr(gist,key,cleandatetime)
            if getattr(gist,key) == str(value):
                results.append(gist)
    return results
    
