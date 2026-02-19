# app/modules/gallery/repositories.py

from app.infrastructure.supabase_client import get_supabase_client

# name your bucket supabasse
bucket_id = "gallery"

def upload_photo(file_binary, filename, content_type):
    
    # upload file to supabase storage
    supabase = get_supabase_client()
    
    try:
        # upload file to supabase storage
        res = supabase.storage.from_(bucket_id).upload(
            path=filename,
            file=file_binary,
            file_options={"content-type": content_type}
        )
        return res
    except Exception as e:
        print(f"Error Upload: {e}")
        raise e

def get_all_photos():
    
    # take list all file on supabase storagr
    supabase = get_supabase_client()
    # list all file on supabase storage
    files = supabase.storage.from_(bucket_id).list()
    
    # url public for <img src="">
    photo_url = []
    for f in files:
        if f['name'] != '.emptyFolderPlaceholder': # skip file system
            public_url = supabase.storage.from_(bucket_id).get_public_url(f['name'])
            photo_url.append({
                'name': f['name'],
                'url': public_url
            })
            
    return photo_url