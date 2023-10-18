import omdb


def posterPathFind(imdb_id):
    # df['imdb_id'].head()
    keyomdb = "bda6d3e8"
    omdb.set_default("apikey", keyomdb)
    poster_json = omdb.imdbid(imdb_id)['poster']
    # print(poster_json)
    return poster_json
