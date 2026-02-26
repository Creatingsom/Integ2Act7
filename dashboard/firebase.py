import firebase_admin
from firebase_admin import credentials, firestore
import os
from django.conf import settings

# Get base directory of project
BASE_DIR = settings.BASE_DIR

# Build full absolute path to firebase_key.json
cred_path = os.path.join(BASE_DIR, "firebase_key.json")

cred = credentials.Certificate(cred_path)

# Prevent re-initialization error
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()