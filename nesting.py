capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}



travel_log = [
    {"country":"France" ,
    "cities_visited" : ["Paris","Little","Dijon"], 
    "total_visits" :12},
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)



add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)