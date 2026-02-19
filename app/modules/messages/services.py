# app/modules/messages/services.py

from . import repositories

# list bad word
BAD_WORD = ["bodoh", "jelek", "anjing", "kasar", "tolol", "stupid", "idiot", "goblok", "bangsat", "bajingan", "brengsek", "sialan", "anj", "babi", "kontol", "memek", "perek", "pepek", "jembut", "jancok", "kampret", "gila", "sarap", "bangsad","pantek", "panteq"]

def process_new_message(raw_content: str):
    
    # validation empety message
    if not raw_content or not raw_content.strip():
        raise ValueError("Pesan tidak boleh kosong!")

    # max character
    if len(raw_content) > 280:
        raise ValueError("Pesan terlalu panjang (maks 280 karakter).")

    # change BAD_WORD to **
    clean_content = raw_content
    for word in BAD_WORD:
        # replace bad word with ****
        clean_content = clean_content.replace(word, "*" * len(word))

    # save message to db supabase
    return repositories.add_message(clean_content)

def get_messages_list():
    # get all medsages from db supabase
    return repositories.get_all_messages()