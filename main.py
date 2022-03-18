# libs
from lib_functions import load_config, get_token, store_token, load_token
from lib_functions import list_tenants, list_plants
from lib_functions import list_view_nodes, list_vn_items
from lib_functions import list_data_points, fetch_data_point, fetch_dp_analytics
import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #token = get_token(load_config())
    #store_token(token)
    #print(list_tenants(load_config(), load_token()))
    #print(list_plants(load_config(), load_token()))
    #print(list_view_nodes(load_config(), load_token()))
    #print(list_vn_items(load_config(), load_token(), "T5e6c396d-3186-4d94-832f-24533a61b2fd"))
    #print(list_vn_items(load_config(), load_token(), "T61278430-4e7b-4e87-8fb5-3e04b4bd8957"))
    #print(list_vn_items(load_config(), load_token(), "P97acd4b5-4847-4b39-b946-0b940f69aeeb"))
    #print(list_vn_items(load_config(), load_token(), "V97acd4b5-4847-4b39-b946-0b940f69aeeb;DPPage1"))
    #print(list_data_points(load_config(), load_token()))
    #print(fetch_data_point(load_config(), load_token(), "P97acd4b5-4847-4b39-b946-0b940f69aeeb;1!N3ASTFPMBPPTYAN"))
    #print(fetch_dp_analytics(load_config(), load_token(), "P97acd4b5-4847-4b39-b946-0b940f69aeeb;1!N3ASTFPMBPPTYAN"))
    end = datetime.datetime.now()
    step_ms = 30 * 24 * 3600000
    for i in range(0, 12):
        end_ms = int(1000 * end.timestamp()) - i * step_ms
        start_ms = end_ms - step_ms
        #print("from ", start_ms, " to ", end_ms)
        print(datetime.datetime.strftime(datetime.datetime.fromtimestamp(start_ms/1000.0), "%d.%m.%Y"), end= " ... ")
        print(datetime.datetime.strftime(datetime.datetime.fromtimestamp(end_ms/1000.0), "%d.%m.%Y"), end= " ... ")
        data = fetch_dp_analytics(load_config(), load_token(), start_ms, end_ms, "P97acd4b5-4847-4b39-b946-0b940f69aeeb;1!6WHH6047V7FDVT")
        print(data["totalCount"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
