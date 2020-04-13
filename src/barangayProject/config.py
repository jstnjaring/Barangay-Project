import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth


if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('./service_account.json')
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://django-firebase-testing.firebaseio.com'
    })

ref = db.reference()
