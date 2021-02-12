# libs
import requests


# defs
def load_config(file_name="api_config.txt") -> dict:
    config_file = open(file_name, mode="r")
    config_data = config_file.readlines()
    config_file.close()
    config = {}
    for line in config_data:
        marker = line.find("=")
        key = line[0:marker]
        value = line[(marker+1):].rstrip("\n")
        config.update({key: value})
    return config


def get_token(config: dict) -> dict:
    url = config["api_url"]
    headers = {"Ocp-Apim-Subscription-Key": config["api_key"]}
    data = {
        "grant_type": config["grant_type"],
        "username": config["username"],
        "password": config["password"]
    }
    try:
        token_post = requests.post(url, headers=headers, data=data)
    except requests.exceptions.Timeout:
        output = {"error": "timeout"}
    except requests.exceptions.InvalidHeader:
        output = {"error": "invalid_header"}
    except requests.exceptions.InvalidURL:
        output = {"error": "invalid_url"}
    except:
        output = {"error": "other"}
    else:
        if token_post.status_code == 200:
            received = token_post.json()
            if "access_token" in received.keys():
                output = {"access_token": received["access_token"]}
            else:
                output = {"error": "corrupted_data"}
        else:
            output = {"error": "status_code_" + str(token_post.status_code)}
    return output


def store_token(token: dict, file_name="api_token.txt"):
    token_file = open(file_name, mode="w")
    if "access_token" in token.keys():
        token_file.writelines(token["access_token"])
        output = "Token storing OK."
    else:
        output = "Token storing failed."
    token_file.close()
    return output


def