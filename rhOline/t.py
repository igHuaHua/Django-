# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',8080))
# sk.listen()
# sk.setblocking(False)
# conn_list = []
# del_list = []
# while True:
#     try:
#         conn, addr = sk.accept()
#         conn_list.append(conn)
#     except BlockingIOError:
#         for conn in conn_list:
#             try:
#                 ret = conn.recv(1024)
#                 if ret == b'':
#                     conn_list.append(conn)
#                     continue
#                 print(ret)
#                 conn.send(b'yes')
#             except BlockingIOError:
#                 pass
#         for i in del_list:
#             i.close()
#             conn_list.remove(i)
#         del_list.clear()


import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
sk.setblocking(False)
ret_list = [sk,]

while True:
    r_lst,w_list,x_list = select.select(ret_list,[],[])
    for ready in r_lst:
        if ready == sk:
            conn,addr = sk.accept()
            ret_list.append(conn)
        else:
            try:
                msg = ready.recv(1024)
                print(msg)
                if not msg:
                    ready.close()
                    r_lst.remove(ready)
                    continue
            except ConnectionResetError:
                ready.close()
                ready.remove(ready)

