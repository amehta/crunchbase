import urllib2
import urllib
import simplejson as json

API_BASE_URL = "http://api.crunchbase.com"
API_VERSION  = "1"
API_URL      = API_BASE_URL + "/v/" + API_VERSION

class CrunchBase:

    def __init__(self):
        return None

    def __webRequest(self, url):
        response = urllib2.urlopen(url)
        return response.read()

    def getCompanyData(self, company):
        queryUrl = API_URL + "/company/" + company + ".js"
        print queryUrl
        jsonResult = self.__webRequest(queryUrl)
        queryResult = json.loads(jsonResult)
        return queryResult

    def getPersonData(self, firstName, lastName):
        queryUrl = API_URL + "/person/" + firstName + "-" + lastName + ".js"
        print queryUrl
        jsonResult = self.__webRequest(queryUrl)
        queryResult = json.loads(jsonResult)
        return queryResult


