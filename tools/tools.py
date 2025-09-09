import config

import base64

def convert_bas64_to_string(data):
    return str( base64.b64decode(data))

def convert_string_to_list_word(string):
    string = string[2:-1]
    string = string.lower()
    list = string.split(",")
    return list
