import urllib.request
import urllib.parse
import json

APIKey = "20781a32848bcbf28da520ed7e9bccdc"

# Just sends a GET request for information to the given url
def getAPIInfo(url):
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	data = json.loads(response.read().decode())
	return data

# Main driver function that executes all the code on the page
# returns the final suggestions in json format
def getMerchantDict(acc_id):
	purchaseList = getPurchases(acc_id)
	placeList = {}

	for each in purchaseList:
		openMerchant(each, placeList)

	#Runs through Dict first and then list to remove any duplicates
	suggestionsList = []
	for each in placeList.keys():
		suggestionsList.append({'name': each, 'type': placeList[each]})

	return json.dumps(suggestionsList)

# Gets the full list of purchases under an account
def getPurchases(acc_id):
	url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(acc_id, APIKey)
	purchases = getAPIInfo(url)
	purchaseList = []
	for each in purchases:
		if "description" in each.keys():
			if each["description"] in ["food", "bar", "coffee"]:
				purchaseList.append(each)
	return purchaseList

# Looks at a specific merchant ID and confirms that they're a bar, restaurant, or coffee
# place before adding them to the final list of suggestions
def openMerchant(purchase, placeList):
	merchID = purchase['merchant_id']
	url = "http://api.reimaginebanking.com/merchants/{}?key={}".format(merchID, APIKey)
	merchInfo = getAPIInfo(url)
	if merchantCategoryMatch(merchInfo):
		placeList[merchInfo['name']] = merchInfo['category']
	pass

# Helper function that checks that the merchant is a bar, restaurant or coffee place
def merchantCategoryMatch(merchant):
	if merchant['category'] in ['bar', 'food', 'coffee']:
		return True
	else:
		return False
