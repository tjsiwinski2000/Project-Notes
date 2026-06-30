#0407-2026 clever way to avoid overwhelming the API 
#          with abundance concurrent requests

#=======================                    
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

#=======================
from django.core.cache import cache

def my_view(request):
    # 1. Manually ask the cache: "Do you have this?"
    data = cache.get('weather_report')

    # 2. Django only goes to the API if 'data' is empty (None)
    if data is None:
        # This code ONLY runs if the cache is empty
        response = requests.get(url, params=parameters)
        data = response.json()
        
        # 3. Put it in the cache so the NEXT load finds it
        cache.set('weather_report', data, 900)

    return render(request, 'weather.html', {'data': data})