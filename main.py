# libs
from lib_functions import load_config, get_token, store_token, load_token
from lib_functions import list_tenants


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#    token = get_token(load_config())
#    store_token(token)
#    print(load_token())
    print(list_tenants(load_config(), load_token()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
