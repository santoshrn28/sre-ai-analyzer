from datetime import datetime

def parse_ts(line):
    try:
        return datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
    except:
        return None
