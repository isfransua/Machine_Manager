
from subprocess import Popen, PIPE, STDOUT

# Klasa Zarząðzająca pojedyńczym serwerem, np. na początek proxy.

class ServerManager():

    # Uruvhomienie maszyny za pomocą subprocess.Popen
    server=Popen('java -Xms1G -Xmx1G -jar "waterfall.jar"',
                  cwd='./Server/Proxy/'
                  )

    #wylaczsieblagam bo mi zlaguje znowu procaa

    server.stdin.write("stop\n".encode("utf-8"))

