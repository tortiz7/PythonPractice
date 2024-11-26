# Return the ones that are running

processes = {
    "nginx": "running",
    "mysql": "stopped",
    "redis": "running",
    "mongodb": "stopped",
    "apache2": "running",
    "docker": "running",
    "kubelet": "stopped",
    "postgresql": "running",
    "elasticSearch": "running",
    "filebeat": "stopped",
    "logstash": "running",
    "grafana": "running",
    "prometheus": "stopped",
    "vault": "running",
    "jenkins": "stopped"
}

def running_process(processes):
    for key, value in processes.items():
        if value == "running":
            processes = print(f"{key}: {value}")
    return processes

running_process(processes)
