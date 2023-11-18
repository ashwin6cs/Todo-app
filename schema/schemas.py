

def document_serial(document, doc_type: str) -> dict:
    common_fields = {
        "id": str(document["_id"])
    }

    if doc_type == "todo":
        specific_fields = {
            "name": document["name"],
            "description": document["description"],
            "complete": document["complete"]
        }
    elif doc_type == "user":
        specific_fields = {
            "user_name": document["user_name"],
            "age": document["age"],
            "email": document["email"],
            "full_name": document["full_name"],
            "is_active": document["is_active"],
        }
    else:
        # Handle other document types if needed
        specific_fields = {}

    return {**common_fields, **specific_fields}

def list_documents_serial(documents, doc_type: str):
    return [document_serial(doc, doc_type) for doc in documents]
