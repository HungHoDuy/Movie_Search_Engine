import omdb

def posterPathFind(imdb_id):
    # df['imdb_id'].head()
    keyomdb = "720d0b09"
    #keyomdb = "bda6d3e8"
    omdb.set_default("apikey", keyomdb)
    poster_json = omdb.imdbid(imdb_id)['poster']
    return poster_json
    # print(poster_json)
