import subprocess
exc=["java", "-Xms1G", "-Xmx1G", "-jar", 'waterfall.jar', "nogui"]
subprocess.Popen(exc, cwd='servers/proxy/')

server.stdin.write("stop\n".encode("utf-8"))