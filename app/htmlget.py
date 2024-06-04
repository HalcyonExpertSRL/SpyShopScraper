import requests

class Request:
    def url (url):
        text = requests.get(url)
        text  = text.text
        return text
