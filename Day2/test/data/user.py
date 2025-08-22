from os import getenv

BASE_URL = getenv("BASE_URL", "https://portal.basebs.net/ucrm/settings")
VALID_USER = {
    "username": getenv("USERNAME", "crmxvtb2.0@basebs.com"),
    "password": getenv("PASSWORD", "12345678x@X"),
}
INVALID_USER = {"username": "wrong@email.com", "password": "wrongpass"}
