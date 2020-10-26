
from youtube_search import YoutubeSearch

import webbrowser

# returns a json string

########################################

keyword = str(input("What do you want to play? "))

results = YoutubeSearch(keyword, max_results=10).to_dict()

result = results[0]["url_suffix"]

url = "https://youtube.com" + result

controller = webbrowser.get()

controller.open(url)

print(url)

# returns a dictionary
