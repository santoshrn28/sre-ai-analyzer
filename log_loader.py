import os

def load_logs(folder):
    logs = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".log"):
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    logs.append(f.read())

    return logs
