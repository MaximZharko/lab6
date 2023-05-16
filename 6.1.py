countries = {
    "Russia": "Moscow",
    "USA": "Washington",
    "Kazakhstan": "Nursultan",
    "Belarus": "Minsk",
    "Great Britain": "London"
}

for name in countries:
    print(name + " - " + countries[name])

print(countries["Russia"])

new_countries = dict(sorted(countries.items()))

for name in new_countries:
    print(name + " - " + new_countries[name])