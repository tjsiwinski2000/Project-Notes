from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })
# HTTP GET - Read Record
@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    #START clever solution from instructor
    # This uses a List Comprehension but you could also split it into 3 lines.
    # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    # per student comments:
    # def to_dict(self):
    # This is a dictionary comprehension function created inside the Cafe class definition.
    # It will be used to turn rows into a dictionary before sending it to jsonify.
    #         return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    # END clever solution from instructor

    #0120-2026 my solution, this actually works
    cafe_dict={}
    for item in all_cafes:
        cafe_dict[item.name] ={
        "id": item.id,
        "map_url": item.map_url,
        "img_url": item.img_url,
        "location": item.location,
        "seats": item.seats,
        "has_toilet": item.has_toilet,
        "has_wifi": item.has_wifi,
        "has_sockets": item.has_sockets,
        "can_take_calls": item.can_take_calls,
        "coffee_price": item.coffee_price
        }
    return cafe_dict

@app.route("/search")
def get_cafe_at_location():
    location = request.args.get('loc')
    print(f"Passed location = {location}")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = result.scalars().all()
    if all_cafes:
        cafe_dict = {}
        for item in all_cafes:
            cafe_dict[item.name] = {
                "id": item.id,
                "map_url": item.map_url,
                "img_url": item.img_url,
                "location": item.location,
                "seats": item.seats,
                "has_toilet": item.has_toilet,
                "has_wifi": item.has_wifi,
                "has_sockets": item.has_sockets,
                "can_take_calls": item.can_take_calls,
                "coffee_price": item.coffee_price
            }
        return cafe_dict
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    name = request.args.get('name')
    location = request.args.get('loc')
    map = request.args.get('map')
    img = request.args.get('map')
    seats= request.args.get('seats')
    toilet =  request.args.get('toilet')
    toilet_bool = (toilet == "true")
    wifi = request.args.get('wifi')
    wifi_bool = (wifi == "true")
    socket = request.args.get('socket')
    socket_bool = (socket == "true")
    calls = request.args.get('calls')
    calls_bool = (calls == "true")
    price = request.args.get('coffee_price')
    new_cafe= Cafe(name = name,
                   location = location,
                   map_url=map,
                   img_url=img,
                   seats = seats,
                   has_toilet = toilet_bool,
                   has_wifi = wifi_bool,
                   has_sockets = socket_bool,
                   can_take_calls = calls_bool,
                   coffee_price = price
                   )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price_reported = request.args.get('new_price')
    temp = f"cafe_id:{cafe_id}\nreported new price:{new_price_reported}"
    print(temp)
    try:
        #cafe = db.get(Cafe,int(cafe_id))
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        #db.get is deprecated? so instructor provided solution ❌ cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price_reported
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    print(f"About to delete cafe id: {cafe_id}")
    api_proviced = request.args.get('api-key')
    if api_proviced != "TopSecretAPIKey":
        return jsonify(response = {"error": "Sorry, that's not allowed. Make sure you have the correct api_key."})
    else:
        try:
            cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            if cafe:
                # delete record code here
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success": f"Successfully deleted cafe number: {cafe_id}"}), 200
            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
