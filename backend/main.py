from flask import request, jsonify
from config import app, db
from models import Contact

#Get Context with crud

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()







if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)