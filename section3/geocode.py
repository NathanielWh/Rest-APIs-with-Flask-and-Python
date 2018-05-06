import httplib2
import json
import string

def getGeocodeLocation(inputString):
   google_api_key = "AIzaSyCCv36nUfVGMy0967dHjAP6SBp7UuWdPl4"
   locationString = inputString.replace(" ", "+")
   url = ('https://maps.googleapis.com/maps/api/geocdoe/json?address=%s&key=%s'% (locationString, google_api_key))
   h = httplib2.Http()
   response, content = h.request(url,'GET')
   result = json.loads(content)
   return result


