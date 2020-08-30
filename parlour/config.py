import json

config = {}
with open('.settings.json', 'r') as f:
    config = json.load(f)
