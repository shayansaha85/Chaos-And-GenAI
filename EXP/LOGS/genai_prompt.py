mongo_health_file = open("./LOGS/MONGO_HEALTH.log", "r")
data = mongo_health_file.read().strip()
mongo_health_file.close()

chaosTime_file = open("./LOGS/CHAOS_TIMING.txt", "r")
data_time = chaosTime_file.read().strip()
chaosTime_file.close()

genAIPrompt  = "MONGO LOGS :\n\n" + data + "\n\n\n" + "CHAOS TESTING TIMEFRAME \n\n" + data_time + "\n\n" + "Please provide full insights about the health of mongodb during chaos testing, how it behaved, what are the assumptions, recommendation, root cause analysis"

print(genAIPrompt)