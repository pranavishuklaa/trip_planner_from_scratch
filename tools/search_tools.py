import requests
import os
import json

from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")

    def search_internet(query):
        """ Useful to search the internet 
        about a given topic and return relevant results        
        """

        top_result_to_return = 4

        url = "https://serper.dev/search"
        payload = json.dump({"q": query})

        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }

        response = requests.request("POST",url, headers=headers, data=payload)

        if 'organic' not in response.json():
            return " Sorry, I couldn't find anything about that, an error w api key"
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['Link']}",
                        f"Sinppet:{result['snippet']}", '\n..........'
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)