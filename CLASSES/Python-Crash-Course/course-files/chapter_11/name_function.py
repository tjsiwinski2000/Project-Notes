def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
        #full_name = f"{first} {last}" #contrived fail 1218-2025
    else:
        full_name = f"{first} {last}"
    return full_name.title()