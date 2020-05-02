def validate_file_name(doc, method):
    if doc.is_new():
        if doc.file_url:
            doc.file_name = doc.file_url.split('/')[-1]
