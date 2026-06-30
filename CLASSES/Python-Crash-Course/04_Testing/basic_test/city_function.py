#1218-2025 CrashCourse p217 ex 11-1

def city_country_string(city,country,population=""):
    """build string City,Country title case"""
    temp=f"{city.title()},{country.title()} {str(population)}" 
    return temp

