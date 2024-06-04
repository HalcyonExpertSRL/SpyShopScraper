import requests

class Request:
    def url (self, url):
        text = requests.get(url)
        text  = text.text
        return text

