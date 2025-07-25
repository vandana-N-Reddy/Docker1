import docker
import os
import time
client = docker.from_env()
print("Pulling the Docker image...")
client.images.pull('hello-world')
print("Running the container...")
container = client.containers.run('hello-world', detach=True)
time.sleep(2)
print("Fetching container logs...")
logs = container.logs().decode('utf-8')
print("Container Output:\n", logs)
container.remove()
print("Container removed.")
