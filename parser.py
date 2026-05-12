import re

def find_issues(log):
    patterns = {
        "OOM": r"out of memory",
        "Disk Full": r"No space left",
        "Crash": r"segfault|core dumped",
        "Timeout": r"timeout"
    }

    issues = []
    for k, v in patterns.items():
        if re.search(v, log, re.IGNORECASE):
            issues.append(k)

    return issues
