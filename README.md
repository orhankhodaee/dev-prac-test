# Python Web Service DevOps Task

This project contains a simple Python web service, containerized with Docker and monitored by Prometheus.

## 1. Setup and Run
1.  Clone this repository.
2.  Ensure you have Docker and Docker Compose installed.
3.  Run the service stack:
    ```bash
    docker-compose up --build
    ```
4.  The service will be available at `http://localhost:5000`.
5.  Prometheus UI is at `http://localhost:9090`.

## 2. CI/CD Pipeline Trigger
The GitLab CI/CD pipeline (`.gitlab-ci.yml`) is triggered on every `git push` to the repository. The pipeline has three stages:
* **build**: Builds the Docker image.
* **test**: Runs placeholder tests.
* **deploy**: Runs placeholder deployment scripts.

## 3. Failure-Recovery Demonstration
[cite_start]The web service container is configured with a restart policy of `always`. To test its auto-restart capability:
1.  Get the container ID: `docker ps`
2.  Run `docker exec -it <container_name> bash ` and run  `apt update && apt install procps -y` then `exit`
3.  Manually kill the container: `docker ecex <container_id> kill -9 1`
4.  Observe Docker automatically restarting the container by running `docker ps` again.

## 4.Apply simple iptables rules 
1. Run commands in host `sudo iptables -A INPUT -p tcp -s YOUR_IP_ADDRESS --dport 5000 -j ACCEPT  && sudo iptables -A INPUT -p tcp --dport 5000 -j DROP ` 
