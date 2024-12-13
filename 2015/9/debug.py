import itertools

# input = '''London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141'''

def parse_input():
	with open("2015\\9\\input.txt", "r") as file:
		input = file.read()

	return [row for row in input.splitlines()]

def get_cities_distances(cities):
	city_distances = dict()

	for city in cities:
		route, distance = city.split(' = ')
		city1, city2 = route.split(' to ')
		distance = int(distance)

		city_distances[f"{city1} to {city2}"] = distance
		city_distances[f"{city2} to {city1}"] = distance

	return city_distances

def get_cities(cities):
	city_list = set()

	for city in cities:
		city1, city2 = city.split(" = ")[0].split(' to ')
		city_list.add(city1)
		city_list.add(city2)

	return list(city_list)

def get_path(city_list, city_distance):
	min_distance = float('inf')
	max_distance = 0
	min_path = []
	max_path = []

	for path in itertools.permutations(city_list, len(city_list)):
		distance = 0

		for i in range(len(path) - 1):
			city1 = path[i]
			city2 = path[i + 1]

			distance += city_distance[f"{city1} to {city2}"]

		if distance < min_distance:
			min_path = path
			min_distance = distance

		elif distance > max_distance:
			max_path = path
			max_distance = distance

	return min_distance, max_distance, min_path, max_path

CITIES = parse_input()
CITY_DISTANCES = get_cities_distances(CITIES)
CITY_LIST = get_cities(CITIES)

MIN_DISTANCE, MAX_DISTANCE, MIN_PATH, MAX_PATH = get_path(CITY_LIST, CITY_DISTANCES)

print(MIN_DISTANCE, MIN_PATH)
print(MAX_DISTANCE, MAX_PATH)