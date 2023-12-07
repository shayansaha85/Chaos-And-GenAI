import pymongo
import datetime
import time
import json


mongo_host = 'localhost'
mongo_port = 27017


def log_metrics(metrics):
    with open('./LOGS/MONGO_HEALTH.log', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = {"Timestamp": timestamp, "Metrics": metrics}
        log_file.write(json.dumps(log_data) + "\n")

def collect_all_metrics():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        connections = client.admin.command("serverStatus")['connections']
        log_metrics({"Connections": connections})

        network = client.admin.command("serverStatus")['network']
        log_metrics({"Network Traffic": network})

        memory = client.admin.command("serverStatus")['mem']
        log_metrics({"Memory Usage": memory})

        locks = client.admin.command("serverStatus")['locks']
        log_metrics({"Locks": locks})

        opcounters = client.admin.command("serverStatus")['opcounters']
        log_metrics({"Opcounters": opcounters})

        db = client.TEST
        collection_stats = db.command("collStats", "test_collection")
        log_metrics({"Collection Statistics": collection_stats})

        index_usage = db.test_collection.index_information()
        log_metrics({"Index Usage": index_usage})

        client.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print()
    print("Data Collection Started... Press Ctrl + C to stop collecting data")
    print("\n")

    duration = 60
    try:
        while True:
            start_time = time.time()
            collected_data = []
            while time.time() - start_time < duration:
                collect_all_metrics()
                time.sleep(5)
            print("Metrics collection and logging complete for this iteration.")
            time.sleep(30)
    except KeyboardInterrupt:
        print("Process interrupted.")
