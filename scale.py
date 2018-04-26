import urllib.request, json
import numpy as np
import pandas as pd
import time
import os
import matplotlib.pylab as plt
from time import sleep
from sklearn.ensemble import GradientBoostingRegressor
from matplotlib import pyplot
from urllib.parse import urlencode
from matplotlib.style.core import available

def query_number_of_backend_weight(time, window, step):
    params = {'query':'haproxy_backend_weight',
              'start': int(time-window),
              'end' : int(time),
              'step' : step
        }
    
    with urllib.request.urlopen('http://192.168.99.100:9090/api/v1/query_range?' + urlencode(params)) as url:
        data = json.loads(url.read().decode())

    df = pd.DataFrame(columns={'total_wieght_of_server'})
    
    for row in data['data']['result'][0]['values']:
        df.loc[row[0]] = [int(row[1])]
    
    return df.ewm(com=0.5).mean()['total_wieght_of_server'].tolist()[-1]
    
def scale_whit_performance_rule(act, min_available_server, max_available_server, step, max_server ):
    
    servers_weight = np.clip(act, min_available_server, max_server)
    
    while True: 
        act_servers_weight = query_number_of_backend_weight(time.time(), 5, 1)
        print(servers_weight)
        print(act_servers_weight)
        if act_servers_weight < min_available_server:
            servers_weight += step
            os.system("docker service scale executor=" + servers_weight.__str__())
            sleep(5)
        elif act_servers_weight > max_available_server:
            servers_weight -= step
            os.system("docker service scale executor=" + servers_weight.__str__())
            sleep(5)
        sleep(1)

scale_whit_performance_rule(3, 2, 4, 1, 10)
