import twilio
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
import os


twilio_client = twilio.rest.TwilioRestClient(
    "AC8785a0ab24a08edcf4e7427c3ee42dd3",
    "fb838481285047827014f94fd493a6d4"
)

app.config['SQLALCHEMY_DATABSE_URI'] = os.environ['DATABASE_URL']
database = SQLAlchemy(app)