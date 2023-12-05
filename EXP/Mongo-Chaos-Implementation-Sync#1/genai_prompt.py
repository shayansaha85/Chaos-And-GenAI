

before_chaos_file = open("MONGO_HEALTH_BEFORE_CHAOS.txt", "r")
before_chaos_data = before_chaos_file.read().strip()
before_chaos_file.close()

during_chaos_file = open("MONGO_HEALTH_DURING_CHAOS.txt", "r")
during_chaos_data = during_chaos_file.read().strip()
during_chaos_file.close()

prompt = f"""
I have performed connection overload Chaos over a MongoDB instance. And collected some metrices

Data collected before Chaos Experiment :\n
===================================================
{before_chaos_data}
\n
\n
Data collected during Chaos Experiment :\n
===================================================
{during_chaos_data}
\n

Please provide your insights on this Chaos experiments.
How MongoDB behaved?
"""

print(prompt)