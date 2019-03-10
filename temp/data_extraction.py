from usda_ndb_client.client import Client

client = Client('2wTHlQ1SsfDETRTvnpSvq4S0HufmdIkRnjPFwAUo')

# get information about a food
data = client.search(q='apple')

ndbno = data.list.item[0].ndbno

#print(data.list.item[0].ndbno)

data1 = client.food_report(ndbno= str(ndbno))

for i in data1.foods[0].food.nutrients:
	print(i.name)
	print(i.value)

