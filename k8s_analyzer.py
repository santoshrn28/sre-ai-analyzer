def detect_k8s(log):
    issues = []

    if "CrashLoopBackOff" in log:
        issues.append("CrashLoop")
    if "OOMKilled" in log:
        issues.append("OOMKilled")

    return issues
