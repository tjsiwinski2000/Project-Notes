from city_function import city_country_string

def test_city_country():
    """does Seoul,Korea work"""
    formatted_string = city_country_string('seoul','korea')
    assert formatted_string == 'Seoul,Korea '

def test_city_country_population():
    """does Seoul,Korea work"""
    formatted_string = city_country_string('seoul','korea', '9,300,000')
    assert formatted_string == 'Seoul,Korea 9,300,000'