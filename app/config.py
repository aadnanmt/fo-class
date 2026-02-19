# app/config.py

import os
from dotenv import load_dotenv # your .env.example

# load fil file .env to memory
load_dotenv()

class Config:
    # pick SECRET_KEY from .env
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_default_key')
    
    # pick setting Supabase
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

    # Folder for upload photo
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/uploads')