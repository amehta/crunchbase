import urllib2
import urllib
import simplejson as json

API_BASE_URL = "http://api.crunchbase.com"
API_VERSION  = "1"
API_URL      = API_BASE_URL + "/v/" + API_VERSION

'''
The crunchbase class
'''
class crunchbase:

  def __init__(self):
      return None

  def __webRequest(self, url):
      response = urllib2.urlopen(url)
      return response.read()

  def getCompanyData(self, company):
      queryUrl = API_URL + "/company/" + company + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def getPersonData(self, firstName, lastName):
      queryUrl = API_URL + "/person/" + firstName + "-" + lastName + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def getFinancialOrgData(self, orgName):
      queryUrl = API_URL + "/financial-organization/" + orgName + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult
  def getProductData(self, product):
      queryUrl = API_URL + "/product/" + product + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def getServiceProviderData(self, name):
      queryUrl = API_URL + "/service-provider/" + name + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def listCompanies(self):
      queryUrl = API_URL + "/companies" + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def listPeople(self):
      queryUrl = API_URL + "/people" + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def listFinancialOrgs(self):
      queryUrl = API_URL + "/financial-organizations" + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def listProducts(self):
      queryUrl = API_URL + "/products" + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult

  def listServiceProviders(self):
      queryUrl = API_URL + "/service-providers" + ".js"
      jsonResult = self.__webRequest(queryUrl)
      queryResult = json.loads(jsonResult)
      return queryResult
