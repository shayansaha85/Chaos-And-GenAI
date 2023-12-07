echo "=== READING LOG FILES ==="
timeout 5
start python ./Mongo-Exp/genai_prompt_generator.py
timeout 5
echo "=== READING LOG FILES COMPLETED ==="

timeout 5
echo "=== FEED CHAOS DATA ==="
timeout 5
start python ./Mongo-Exp/genAI_interaction_api.py