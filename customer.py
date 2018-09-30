import requests

USERS_URL = 'http://api/customers/'


def get_customer(user_id):
    """Get specific user"""
    response = requests.get(USERS_URL+user_id)
    if response.ok:
        return response
    else:
        return None