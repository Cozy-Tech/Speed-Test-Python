import speedtest

net = speedtest.Speedtest()


print("Fetching Servers...")
servers = net.get_servers() # Gerefrane list server ha
print("Selecting Best Server...")
best_server = net.get_best_server() # Gereftane behtarin server
print(f"Found Best Server From => {best_server['name']}")
print("--------------------")
print("Starting Download...")
download = net.download()
print("Starting Upload...")
upload = net.upload()
ping = net.results.ping
print("--------------------")

print(f"Your Download Speed Is => {download / 1024 / 1024:.2f} Mb")
print(f"Your Upload Speed Is => {upload / 1024 / 1024:.2f} Mb")
print(f"Your Ping is => {ping} ms")

result = net.results.share()
result_dict = net.results.dict()

print(result_dict)