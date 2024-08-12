#!/bin/bash

# Stop all running containers
runningContainers=$(docker ps -q)
if [ -n "$runningContainers" ]; then
    docker stop $runningContainers
fi

# Remove all containers
allContainers=$(docker ps -a -q)
if [ -n "$allContainers" ]; then
    docker rm $allContainers
fi

# Remove all images (forcefully)
allImages=$(docker images -q)
if [ -n "$allImages" ]; then
    docker rmi -f $allImages
fi

# Remove all volumes (optional)
allVolumes=$(docker volume ls -q)
if [ -n "$allVolumes" ]; then
    docker volume rm $allVolumes
fi

# Remove all user-created networks (excluding predefined ones)
allNetworks=$(docker network ls --filter "type=custom" -q)
if [ -n "$allNetworks" ]; then
    docker network rm $allNetworks
fi
