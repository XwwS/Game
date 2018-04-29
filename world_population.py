import json

filename = 'population_data.json'
with open(filename) as f:
	population = load(f)
	print (population)