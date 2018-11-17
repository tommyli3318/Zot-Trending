import json
import praw
import urllib.parse
import urllib.request

api_key = 'AIzaSyAPsz82Vg-RYZ8EQD8QB1Y-45N_IEJDz5o'
base_url = 'https://www.googleapis.com/youtube/v3'

def buildURL(search, maxResults):
	query_parameters = [('key', api_key), ('q', search), ('part', 'snippet'), ('type', 'videos'), ('maxResults', str(maxResults))]
	return base_url + '/search?' + urllib.parse.urlencode(query_parameters)

def getResult(url):
	response = None
	try:
		response = urllib.request.urlopen(url)
		return json.load(response)
	finally:
		if response != None:
			response.close()

def printResults(results):
	for item in results['items']:
		print(item['snippet']['title'], item['snippet']['description'])


if __name__ == '__main__':
	search = input("What do you want to search for? ")
	query_string = buildURL(search, 10)
	result = getResult(query_string)
	printResults(result)
