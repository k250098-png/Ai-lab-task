import os

def create_and_store(filename, data):
    with open(filename, 'w') as f:
        for exp in data:
            f.write(f"{exp['id']},{exp['model']},{exp['dataset']},{exp['lr']},{exp['epochs']}\n")

def display_experiments(filename):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())

def search_experiment(filename, exp_id):
    if not os.path.exists(filename): return None
    with open(filename, 'r') as f:
        for line in f:
            if line.split(',')[0] == str(exp_id):
                return line.strip()
    return None

def add_experiment(filename, exp):
    with open(filename, 'a') as f:
        f.write(f"{exp['id']},{exp['model']},{exp['dataset']},{exp['lr']},{exp['epochs']}\n")

def update_experiment(filename, exp_id, new_data):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if line.split(',')[0] == str(exp_id):
                f.write(f"{new_data['id']},{new_data['model']},{new_data['dataset']},{new_data['lr']},{new_data['epochs']}\n")
            else:
                f.write(line)

def remove_experiment(filename, exp_id):
    if not os.path.exists(filename): return
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if line.split(',')[0] != str(exp_id):
                f.write(line)
