
import subprocess, time, os

# Klasa Zarząðzająca pojedyńczym serwerem, np. na początek proxy.

class ServerManager():
    exc=["java", "-Xms1G", "-Xmx1G", "-jar", "waterfall.jar", "nogui"]
    # Uruvhomienie maszyny za pomocą subprocess.Popen
    server=subprocess.Popen(exc,
                            cwd='./servers/proxy/',
                  stdin=subprocess.PIPE
                  )

    #wyl
    #time.sleep(30) #
    #server.__exit__()

    id=os.name
    a=True
    while a:
        inp=input('Input: {id}_>')
        if inp=='ext()':
            a=False
        else:
            try:
                server.stdin.write("{inp}\n".encode("utf-8"))
                server.stdin.flush()
                server.stdout.read
            except:
                print('err')
        

