def connect(**opcje):  # argumenty słownikowe
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print(connect_param)


connect(user='home')
connect(user='home', root='/', port='9090')
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'user': 'home', 'root': '/', 'port': '9090'}}

# 11:05
