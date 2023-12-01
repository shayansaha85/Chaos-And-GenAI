import pymongo
import threading
import time
import subprocess

mongo_host = 'localhost'
mongo_port = 27017

def perform_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.admin
        collection = db.TEST

        client.close()
    except Exception as e:
        print(f"Operation failed: {e}")

def simulate_slow_network():

    subprocess.run(["sudo", "tc", "qdisc", "add", "dev", "eth0", "root", "netem", "delay", "200ms"])

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    subprocess.run(["sudo", "tc", "qdisc", "del", "dev", "eth0", "root", "netem", "delay", "200ms"])

if __name__ == "__main__":
    print("Simulating slow network on MongoDB...")
    try:
        simulate_slow_network()
    except KeyboardInterrupt:
        print("Experiment stopped.")
