import socket, time
from dcrcp import send_method

DCSERVER = '10.10.10.241'
DCSERVER_PORT = 5001
    

def main(dc_ip, dc_port):
    sock = socket.create_connection((dc_ip, dc_port))

    # login
    print 'Login as "Operator"'
    result = send_method(sock, 'login', {'username': 'Logger', 'api_version': "1.0"})
    print result

    # get outputs
    print "\n\nGet all outputs"
    outputs = send_method(sock, 'get_outputs')
    print outputs

    # select output 1 for control
    print "\n\nSelect output 1"
    result = send_method(sock, 'select_outputs', {"selection_mask": 1})
    print result

    ## Return output 1 to live
    print "\n\nPush selected output to live"
    send_method(sock, 'goto_live_capture')


    count = 1
    
    print "\n\nCreate mark %d" % count
    send_method(sock, 'create_mark', {'name':'Logger.mark%d'%count})
    time.sleep(1)
    count+=1

    print "\n\nCreate mark %d" % count
    send_method(sock, 'create_mark', {'name':'Logger.mark%d'%count})
    time.sleep(1)
    count+=1

    print "\n\nCreate mark %d" % count
    send_method(sock, 'create_mark', {'name':'Logger.mark%d'%count})
    time.sleep(1)
    count+=1

    print "\n\nCreate mark %d" % count
    send_method(sock, 'create_mark', {'name':'Logger.mark%d'%count})
    time.sleep(1)
    count+=1


if __name__ == '__main__':
    import os
    DCSERVER = os.getenv('DCSERVER', DCSERVER)
    DCSERVER_PORT = os.getenv('DCSERVER_PORT', DCSERVER_PORT)
    main(DCSERVER, DCSERVER_PORT)

