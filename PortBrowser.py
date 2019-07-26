import os
import re
import sys

urls = []


def generate_urls(gnmap_file):
    with open(gnmap_file) as ports:
        data = ports.read()

        get_line = re.findall(r'.*Ports.*', data)

        for line in get_line:
            ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            open_ports = re.findall(r'\d{1,5}\/open', line)

            for ip in ips:
                for port in open_ports:
                    port = port.strip('/open')
                    url = ip + ':' + port
                    urls.append(url)
        create_file()


def create_file():
    f = open("urls.txt", "w+")
    for url in urls:
        f.write(url + '\r\n')
    f.close()
    run_eyewitness()


def run_eyewitness():
    os.system('python /opt/EyeWitness/EyeWitness.py -f urls.txt --web -d PortBrowser_screenshots')
    os.system('rm urls.txt')


if len(sys.argv) == 2:
    gnmap_file = sys.argv[1]
    generate_urls(gnmap_file)
else:
    print("Usage: python3 main.py file_name.gnmap")
    