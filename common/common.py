

from config.database import user_collection

def check_user_name_existence(user_name):
    user_document = user_collection.find_one({"user_name": user_name})
    return user_document is not None
