def validate_query(query):
    """
    Validate user query.
    """
    if not query or len(query.strip()) == 0:
        return False
    return True