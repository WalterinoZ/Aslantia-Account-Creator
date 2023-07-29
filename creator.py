import requests
import random
import string
import threading

totalProxi = 0
useProxi = False

for proxi in open("proxi.txt"):
    totalProxi += 1

print(f"Total Proxy you have {totalProxi}")

def randomPayload():
    def random_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(length))

    return {
        'kawaidinda': 'bapr' + random_string(4),
        'username': 'baperan' + random_string(5),
        'email': 'gmkokbaper' + random_string(5) + '@localhost.root',
        'DiscordName': 'lumibaper#' + str(random.randint(1000, 9999)),
        'LoliMoncrottUhaHH': 'IoriYagami',
        'password': 'gmbaper' + random_string(4) + '#' + random_string(4)
    }

def makeRequest(proxies):
    try:
        getAgent = str(open("agent.txt", "r").readlines()[random.randint(0, 999)]).replace("\n", "")
        headers = {
            'User-Agent': getAgent,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest"
        }
        payload = randomPayload()

        if proxies is None:
            r = requests.post('http://aslantia.lost-saga.my.id/fungsional/DRejisterSlurrr.php', headers=headers, data=payload, timeout=10)
        else:
            r = requests.post('http://aslantia.lost-saga.my.id/fungsional/DRejisterSlurrr.php', headers=headers, data=payload, timeout=10, proxies=proxies)

        if "Berhasil Mendaftarkan Akun. Silahkan Login..." in r.text:
            print("Account registration successful. Please log in.")
            f = open("results.txt","a+")
            f.write(f"\n{payload}")

    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)

# Create threads
threads = []
for _ in range(totalProxi):
    proxies = None

    if totalProxi >= 1:
        getPrxy = str(open("proxi.txt", "r").readlines()[random.randint(0, totalProxi - 1)]).replace("\n", "")

        try:
            checkPrxy = str(getPrxy).split("http://")[1]
        except:
            oldPrxy = str(getPrxy)
            getPrxy = f"http://{oldPrxy}"

        proxies = {"http": str(getPrxy), "https": str(getPrxy)}

    # Create a thread for each request
    thread = threading.Thread(target=makeRequest, args=(proxies,))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
