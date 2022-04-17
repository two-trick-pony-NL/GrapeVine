from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Post, User, Comment, Like
from . import db

payments = Blueprint("payments", __name__)

#Here we created an endpoint that catches a callback from Zapier
#If a payment comes in on the Frankly bankaccount it triggers a script at Zapier that calls this endpoint. 
#We can now add logic that checks if the payment ID is something we expected. 

@payments.route("/incoming_payment/<paymentID>", methods=['GET', 'POST'])
def incoming_payment(paymentID):
    user = User.query.filter_by(id=paymentID).first()
    usernumber = str(user)
    print("We got paid: $$$$$$$  " +usernumber + " has paid his bill")
    user.haspaid =  1
    db.session.commit()
    return('', 204)
