
echo "=== STARTED CHAOS EXPERIMENT ==="
start python ./Mongo-Exp/inject_chaos.py 60
timeout 180
echo "=== CHAOS TESTING STOPPED ==="