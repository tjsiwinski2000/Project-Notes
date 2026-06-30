from  pizza import make_pizza
        
make_pizza(12,"mushrooms" , "sausage", "monkeymeat")

def configure_user_settings(theme: str, language: str, **user_info) -> dict:
    """
    Configures basic settings and captures any extra settings 
    into the user_info dictionary via **kwargs.
    """
    settings = {
        "theme": theme,
        "language": language
    }
    
    # Merge the captured **kwargs into the settings dictionary
    settings.update(user_info)
    
    return settings

# user_profile = configure_user_settings('dark-theme','korean', 
# location='San Antonio', field='python programming')
# print(user_profile)
# print(type(user_profile))