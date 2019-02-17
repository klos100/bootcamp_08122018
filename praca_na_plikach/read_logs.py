import sys
from collections import defaultdict
f_name = None

if len(sys.argv) > 1:
    f_name = sys.argv[1]

def prepare_line(napis):
    login, akcja, czas = line.strip().split(";")
    return login, akcja, czas

def my_key(item):
    return int(item[0].split("-")[-1])

if f_name:
    dict_users_in = {}
    dict_users_total = defaultdict(int)
    with open(f_name) as f:
        for line in f:
            login, action, time = prepare_line(line)
            if action == 'LOGIN':
                dict_users_in[login] = time
            elif action == 'LOGOUT':
                session_time = int(time) - int(dict_users_in[login])
                dict_users_total[login] += session_time

    for login, time in sorted(dict_users_total.items(), key = my_key): #key = lambda x: x[1],reverse=True):
        print(f"{login}: {time}")




