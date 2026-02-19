# app/modules/messages/repositories.py

from app.infrastructure.supabase_client import get_supabase_client

def add_message(content: str):
    # send data to supabase
    supabase = get_supabase_client()
    
    # still use it now, insert() and execute() 
    try:
        data = supabase.table("messages").insert({"content": content}).execute()
        return data
    except Exception as e:
        # for error handling
        raise e

def get_all_messages():
    # select all message "*" table supabase
    supabase = get_supabase_client()
    
    # select("*")
    response = supabase.table("messages").select("*").order("created_at", desc=True).execute()
    return response.data