# PYTHON DJANGO #
```python
# MAKE WEB PAGE DJANGO->define URL / writing views / writing templates
python manage.py shell #Django Shell
python manage.py runserver #Django Launch Site
python manage.py runserver 192.168.86.21:8000 #Viewable to other devices on LAN
django-admin startproject p_project #New Project
#0406-2026
# 1. Clone the repository
git clone https://github.com/pythonanywhere/example-django-project-unpinned-django.git .

# 2. Setup your environment
mkvirtualenv my-env --python=/usr/bin/python3.10
pip install django

# 3. Prepare the database
python manage.py migrate
```
# PYTHON DJANGO-PART2 #
```python
#views.py================
# NOTE: must import login_requiredV
from django.contrib.auth.decorators import login_required
....
@login_required
def add_shop(request):
    """ Add a new coffeeshop. """
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ShopForm()
    else:
        # POST data submitted; process data
        # -- note: request.FILES required for IMAGE upload
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            new_shop = form.save(commit=False)
            new_shop.owner = request.user
            new_shop.save()
            return redirect('cafe_it_2026:shops')
```
```html 
 <!-- enctype=... needed for IMAGE upload -->
 <form action = "{% url 'cafe_it_2026:add_shop' %}" method = 'post' enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_div }}
    <button name = "submit">Add Shop</button>
 </form>
```
# PYTHON DJANGO-PART3 #
```python
cafe_it_2026/views.py
@login_required
def edit_shop(request,shop_id):
    """ Edit existing shop. """
    shop_to_edit = CoffeeShops.objects.get(id = shop_id)
    print (f"id = {shop_to_edit.id}")
    if request.method != 'POST' : 
        # Initial request; pre-fill with current information
        form = ShopForm(instance = shop_to_edit)
    else:
        form = ShopForm(instance = shop_to_edit, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe_it_2026:shops')
    
    # create the context dictionary and pass it to the template
    context = {'name': shop_to_edit.name, 'address' : shop_to_edit.address, 'description' : shop_to_edit.description, 'id':shop_to_edit.id, 'form':form}
    return render(request,'cafe_it_2026/edit_shop.html', context)

```
```html 
cafe_it_2026/edit_shop.html
<!--0413-2026 id is simply id as that is how the context dictionary shows -->
<form action = "{% url 'cafe_it_2026:edit_shop' id %}" method="post" 
    enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_div }}
    <button name ="submit">Save changes</button>
</form>
```

## PYTHON DJANGO PART4
```python
# shell to check update to GB 0414-2026
 from guest_book.models import Guest_Book
 gb = Guest_Book.objects.filter(date_added__gte='2026-04-10')
for g in gb:
    print(g.name, g.message, g.date_added, g.client, g.approved)
```
# PYTHON CLASSES #
```python
class Restaurant:
    """Crash Course page 162"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
   
    def describe_restaurant(self):
        print(f"The {self.name} restaurant proudly serves {self.cuisine} food.")
   
    def open_restaurant(self):
        print(f"The {self.name} restaurant is now open.")
       
restaurant = Restaurant("Minnies", "Korean")
print(restaurant.name)
print(restaurant.cuisine)
```

# Virtual Environments #
- Ctrl+Shift+P 
- 1)select create virtual environment 
- 2)select interpreter
- 3)confirm by opening new terminal (.venv)
- OR...
```python
python -m venv ll_env
source ll_env\Scripts\Activate #Note for powershell
deactivate #Stops the venv
```

---
# PYTHON SNIPPETS #
```python
s = "tj siwinski"
print(s.title()) #Tj Siwinski
print(s.upper()) #TJ SIWINSKI
print(s.lower()) #tj siwinski
print(s[::-1]) #iksniwis jt
print(''.join(sorted(s))) #iiijknsstw
#DICTIONARY
fruits = {"apple":2, "pear" : 1, "pineaple" : 3, "peach" : 1 , "zebra" : 0 }
print(max(fruits,key=fruits.get)) # fruit with highest value e.g. pineapple 3
print(max(fruits)) # fruit with "highest" name  e.g. zebra 
#SETTING VALUES 
a,b,c = 1,2,3
bignum = 1_000_000
print(bignum) #1000000
#LISTS
tj = ['knicks', 'mets']
kn = tj
kn.append('tigers')
print(tj) #['knicks', 'mets', 'tigers'] same location in mem.
kn = tj[:]
kn.append('diamond.backs')
print(tj) #['knicks', 'mets', 'tigers'] kn separate list
print(kn) #['knicks', 'mets', 'tigers', 'diamond.backs'] 
print(tj[-1]) #tigers, last item
print(kn[-3]) #mets, 3d last item
#FOR LOOPS
>>> fruits = ["apple", "banana", "cherry"]
>>> for fruit in fruits:
...          print(fruit)
...
apple
banana
cherry
>>> for char in "python":
...     print(char)
...
p
y
t
h
o
n
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
---
# PYTHON FLASK RUN COMMANDS #
```python
flask run --host 0.0.0.0
. . snip..
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.86.24:5000
Any device📱 on LAN can access flask app URL: http://192.168.86.24:5000
```

---
# PYTHON APP CONTEXT AKA PYTHON SHELL #
```python
(gci env:FLASK_APP).Value #should be hello.py or flask_app.py
flask shell
from hello import db
db.create_all() #db specified in app.config is created
db.session.commit()
users = User.query.all() #query user table
#0303-2026 START  
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Role': Role}
#0303-2026 END 
# add to hello.py don't have to import each time
```
```python 
#03052026-START-CAFE-IT
$env:FLASK_APP = 'flask_app.py' #windows
export FLASK_APP=flask_app.py #pythonanywhere shell
flask shell
from flask_app import get_user_data_db 
get_user_data_db() #actually run it
#03052026-END
```
---
# PYTHON EXCEPTION HANDLING #
```python 
try:
   age = int(input("How old are you?"))
except ValueError:
   print("You have typed in an invalid number. Please try again with a numerical response.")
   age = int(input("How old are you?"))

my_dict = {"batman": "Bruce Wayne"}
try:
    print(my_dict["flash"])
except KeyError as error_message:
    print(f"The key {error_message} does not exists.")
   ```
---
# PYTHON FILE I/O #
```python
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close() #must close explicitly
-
with open("my_file.txt") as file:
   contents = file.read()
   print(contents)
-
with  open("new_file.txt", mode = "w") as file:
   file.write("New text.") #DNE create, otherwise open
-
with  open("C:\\Users\\TJ\\Desktop\\my_file.txt", mode = "w") as file:
   file.write("New text 1245pm") #absolute path from root
-
with  open("..\\..\\my_file.txt", mode = "w") as file:
   file.write("New text 1255pm") #relative path 2 levels ⬆️

```

---
# PYTHON FLASK COOKIES #
```python
@app.route('/')
def index():
    response = make_response('<h1>this document carries a cookie</h1>')
    response.set_cookie('answer', '88')
    return response

@app.route('/cookie')
def print_cookie():
    cookie =  request.cookies.get('answer')
    return '<h1> Found cookie {}!</h1>'.format(cookie)
```
--- 
# PYTHON ENVIRONMENT SETUP #
| Syntax | Description |
| ----------- | ----------- |
| Install the required packages |  python -m pip install -r requirements.txt |
| CAPTURE CURRENT LIBRARY | pip freeze > requirements.txt | 
| SHOW VERSION (specfic package) | pip show sqlalchemy |



---
# PYTHONANYWERE SPECIFIC #
| Syntax | Description |
| ----------- | ----------- |
| Refresh  pythonanywere|touch /var/www/tjsiwinski2000_pythonanywhere_com_wsgi.py|
| Clone GIT | git clone git@github.com:tjsiwinski2000/flask_login_2026.git |
| Update pythonanywere | git pull |
---
# GIT COMMANDS#
1. create git repository on github.com
2. cmd prompt:
- echo "# flask_login_2026" >> README.md
- git init
- git add . create .gitignore : pycache/ 
- which makes updating easier. 
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/tjsiwinski2000/flask_login_2026.git
- git push -u origin main

**bold text**

*italic*
This text is ***really important***.
# Heading#

```python
s = "Python syntax highlighting"
print s
```
---

 	| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text | 

---
# CODIUM SHORTCUTS #
- save file as HTML
- Type " ! " and enter HTML skeleton comes up
---
# JSON TIPS #
```python
with open("review_data.json") as f1:
    my_dict = json.load(f1)
#must be double quotes
my_dict["www.jw.org"] = {"email": "tjsiwinski_2000@yahoo.com", "password": "+foo-nba"}
print(f'Updated data {my_dict}')

# json dump (data, file) if you reverse wipes out the file
with open(file="review_data.json",mode='w') as f2:
    json.dump(data,f2)
with open("review_data.json") as f1:
    my_dict = json.load(f1)
```