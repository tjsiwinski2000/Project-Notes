#Crash Course p11 exercise 06-11
cities_dict ={
    "San Diego": {
        "country" : "USA",
        "population" : "1.4 million",
        "fact" : "Balboa Park is amazing."
    },
    "Seoul": {
        "country" : "South Korea",
        "population" : "9.6 million",
        "fact" : "Mom's hometown."
    },
    "Chicago":{
        "country" : "USA",
        "population" : "2.7 million",
        "fact": "Art Institue is awesome"
    }
}

for city in cities_dict:
    print(f"Name: {city}")
    for key, value in cities_dict.get(city).items():
       print(f"\t{key}:{value}")