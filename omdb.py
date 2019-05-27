import requests_with_caching

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar?q={}&type=movies&limit=5'.format(title.replace(' ', '+'))
    return requests_with_caching.get(url)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
res = get_movies_from_tastedive("Black Panther")
print (res)


import json
import requests_with_caching

def get_movies_from_tastedive(title):
    url = "https://tastedive.com/api/similar"
    params = { 'q' : title, 'type' : 'movies', 'limit' : 5}
    return requests_with_caching.get(url, params = params,  permanent_cache_file="permanent_cache.txt").json()

def extract_movie_titles(json):
    res = json['Similar']['Results']
    return [ x['Name'] for x in res]

def get_related_titles(movies):
    res = []
    for movie in movies:
        titles = extract_movie_titles(get_movies_from_tastedive(movie))
        res.extend(titles)
    return list(set(res))


import requests_with_caching
import json

def get_movie_data(title):
    url = "http://www.omdbapi.com/"
    params = { "t" : title, "r" : "json"}
    resp = requests_with_caching.get(url, params = params)
    return resp.json()
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_rating(result):
    ratings = result['Ratings']
    for rating in ratings:
        print (rating)
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:-1])
    return 0
