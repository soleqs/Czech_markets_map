
import json

with open("/home/ubuntu/supermarkets.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cities = set()
for element in data["elements"]:
    if "tags" in element and "addr:city" in element["tags"]:
        cities.add(element["tags"]["addr:city"])

with open("/home/ubuntu/cities_with_supermarkets.txt", "w", encoding="utf-8") as f:
    for city in sorted(list(cities)):
        f.write(city + "\n")

print("Unique cities with supermarkets saved to cities_with_supermarkets.txt")


