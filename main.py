# libs
from lib_functions import load_config, get_token, store_token


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    token = get_token(load_config())
    store_token(token)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
