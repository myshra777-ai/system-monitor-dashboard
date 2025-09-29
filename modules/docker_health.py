import docker

def get_container_health():
    # Connect to Docker via TCP (Windows setup)
    client = docker.DockerClient(base_url='tcp://localhost:2375')
    containers = client.containers.list(all=True)
    health_data = []

    for container in containers:
        status = container.status
        name = container.name

        # Use image tag if available, else fallback to short ID
        image = container.attrs['Config']['Image']

        # Safely extract health status
        health = container.attrs.get('State', {}).get('Health', {}).get('Status', 'N/A')

        health_data.append({
            "Name": name,
            "Image": image,
            "Status": status,
            "Health": health
        })

    return health_data

if __name__ == "__main__":
    print("🔍 Docker Container Health Check\n")
    for info in get_container_health():
        print(f"{info['Name']} ({info['Image']}): Status={info['Status']}, Health={info['Health']}")
