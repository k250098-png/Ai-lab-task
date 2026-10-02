import json
import os

def analyze_models(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        data = json.load(f)
    
    if not data: return
    highest_acc = max(data, key=lambda x: x['accuracy'])
    highest_f1 = max(data, key=lambda x: x['f1'])
    print(f"Highest Accuracy Model: {highest_acc['name']} ({highest_acc['accuracy']})")
    print(f"Highest F1-Score Model: {highest_f1['name']} ({highest_f1['f1']})")

def add_model_result(filename, model_data):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
    data.append(model_data)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def update_model_result(filename, model_name, new_metrics):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        data = json.load(f)
    for m in data:
        if m["name"] == model_name:
            m.update(new_metrics)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def remove_model_result(filename, model_name):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        data = json.load(f)
    data = [m for m in data if m["name"] != model_name]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
