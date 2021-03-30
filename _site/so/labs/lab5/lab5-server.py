import socket
import threading
import time

#from threading import BoundedSemaphore
#count = BoundedSemaphore(2)

def trataCliente(conn, addr):
    #if count.acquire(False):    
    while True:
        data = conn.recv(100)
        print(time.ctime(),addr,'enviou',data)
        if not data:
            #count.release()
            conn.close()
            break 
    #else:
    #    print("Conexões excedidas, tente depois...")
    #    conn.close()

if __name__=="__main__": 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', 9999))
    except:
       print('ERRO no bind')
       sys.exit()

    s.listen()
    print('aguardando conexoes em ', 9999)

    while True:
        conn, addr = s.accept()
        print('recebi uma conexao do cliente ', addr)

        t = threading.Thread( target=trataCliente, args=(conn,addr,))
        t.start()