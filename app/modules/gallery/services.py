# app/modules/gallery/services.py

from . import repositories # repositories.py
from werkzeug.utils import secure_filename
import uuid # name file
import os # extension file
import io # for buffer
from PIL import Image # pillow

# Kita izinkan input JPG/PNG/GIF, tapi outputnya nanti selalu WEBP
ALLOW_EXT = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allow_file(filename):
    # check extension file
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOW_EXT

def process_upload(file_obj):
    # validasi file
    if not file_obj or file_obj.filename == '':
        raise ValueError("Tidak ada file yang dipilih")

    if not allow_file(file_obj.filename):
        raise ValueError("Format file tidak didukung (Gunakan JPG, PNG, atau GIF)")

    try:
        # open img use pillow package
        img = Image.open(file_obj)
        
        # konvert | use io package
        buffer = io.BytesIO()
        
        # save img to buffer format webp
        img.save(buffer, format="WEBP", quality=80, optimize=True)
        
        # reset buffer
        buffer.seek(0)
        
        # data for supabase | webp
        content_file = buffer.read() # read data(buffer)
        content_type = "image/webp" # webp
        
        # create new name file
        original_name = secure_filename(file_obj.filename)
        # change extensi to .webp
        without_ext = original_name.rsplit('.', 1)[0]
        unique_filename = f"{uuid.uuid4().hex}_{without_ext}.webp"

        # upload photo
        return repositories.upload_photo(content_file, unique_filename, content_type)
        
    except Exception as e:
        print(f"error konversi gambar: {e}")
        raise ValueError("gagal proses gambar")

def get_photos():
    return repositories.get_all_photos()