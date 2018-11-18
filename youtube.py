import urllib.request
import json

GOOGLE_API_KEY = 'AIzaSyDhoNZBc8w_g1GamIK-i0WBZJA6Gr-eDGQ'
URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&maxResults=4&chart=mostPopular&regionCode=US&key=' + GOOGLE_API_KEY

response = urllib.request.urlopen(URL)
json_text = response.read().decode(encoding='utf-8')

refined_list = json.loads(json_text)

def get_results(refined_list:[dict]) -> (list,list,list):
   titles = []
   descriptions = []
   links = []



   for i in refined_list['items']:
       titles.append(i['snippet']['title'])
       descriptions.append(i['snippet']['description'])
       links.append('https://www.youtube.com/watch?v=' + i['id'])

   return titles, descriptions, links

#titles, desc, links = get_results(refined_list)

def results():
	return get_results(refined_lists)