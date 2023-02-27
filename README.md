1. What is Docker and how does it differ from a virtual machine? [1]
   - It shares the OS with the host machine. 
2. How does Docker ensure that containers are isolated from each other and the host
   system? [2]
    - It uses networks and namespaces to isolate the containers from each other and the host system.
3. What is the purpose of a Dockerfile? [2]
    - Describes how to build a docker image.
4. What is the purpose of a requirements.txt file? [2]
    - Describes the dependencies of a python project.
5. How can you mount a host directory as a volume in a container? [2]
    - ```bash
      docker run -v /path/to/host/dir:/path/to/container/dir
      ```
6. What is the difference between a docker image and a docker container? [2]
    - A container is a running instance of an image. The image describes how to build the container.
7. What command can be used to create an image from a Dockerfile? [2]
    - ```bash
      docker build -t <image_name> .
      ```
8. What command will start a docker container? [2]
    - ```bash
      docker run <image_name>
      ```
9. What command will stop a docker container? [2]
    - ```bash
      docker stop <container_name>
      ```
10. What command will remove a docker container? Image? [5]
    - ```bash
      docker rm <container_name> # Container
      ```
    - ```bash
      docker rmi <image_name> # Image
      ```
11. What command will list all running docker containers? all containers? [5]
    - ```bash
      docker ps # Running containers
      ```
    - ```bash
      docker ps -a # All containers
      ```
12. What command will list all docker images? [1]
    - ```bash
      docker images -a 
      ```
13. What command do you use to deploy docker containers using the information in the
    dockercompose.yml file? [2]
    - ```bash
      docker-compose -f dockercompose.yml up 
      ```
    - if the file is named docker-compose.yml, you can omit the -f flag with the explict name.
14. How can you specify in the docker-compose.yml file that you want docker containers
    to use the hosts' network? [5]
    - ```yaml
      networks:
        default:
          external:
            name: host
      ```
15. How can you specify in the docker-compose.yml file where the Dockerfile for a
    particular container is found? [5]
    - ```yaml
        services:
            <service_name>:
              build:
                context: /path/to/context
                dockerfile: /path/to/dockerfile # Relative to context
      ```