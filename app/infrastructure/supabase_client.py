from supabase import create_client, Client
import os

# use connection pooling
_supabase_client: Client = None

def get_supabase_client() -> Client:
    global _supabase_client

    if _supabase_client is None:

        # take credentials frm environment
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        
        
        if not url or not key:
            raise ValueError("ERROR: Your SUPABASE_URL or SUPABASE_KEY 'NOT FOUND' in file .env!")
            
        # create connection
        _supabase_client = create_client(url, key)
        print("Success, connect to Supabase")

    return _supabase_client