import nmap
from socket import *
import time

startime = time.time()

# begin = 75
# end = 80

# target = '127.0.0.1'
# scanner = nmap.PortScanner()

# for i in range(begin, end+1):
#     res = scanner.scan(target, str(i))
#     res = res['scan'][target]['tcp'][i]['state']
#     print(f'Port {i} is {res}')
    

#scan without nmap
if __name__=='__main__':
    target = input('Enter the host you want to scan: ')
    hostName = gethostbyname(target)
    if hostName:
        try:
            print('Starting scanning on host: ', hostName)
        except gaierror:
            print('Invalid name or service')

        
    for i in range(1, 7000):
        network = socket(AF_INET, SOCK_STREAM)

        connect = network.connect_ex((hostName, i))
        if (connect == 0):
            print('Port %d: OPEN' % (i,))
        network.close()

print('Time taken: ', time.time() - startime)