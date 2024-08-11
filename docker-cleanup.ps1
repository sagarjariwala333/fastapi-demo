# Stop all running containers
$runningContainers = docker ps -q
if ($runningContainers) {
    docker stop $runningContainers
}

# Remove all containers
$allContainers = docker ps -a -q
if ($allContainers) {
    docker rm $allContainers
}

# Remove all images (forcefully)
$allImages = docker images -q
if ($allImages) {
    docker rmi -f $allImages
}

# Remove all volumes (optional)
$allVolumes = docker volume ls -q
if ($allVolumes) {
    docker volume rm $allVolumes
}

# Remove all user-created networks (excluding predefined ones)
$allNetworks = docker network ls --filter "type=custom" -q
if ($allNetworks) {
    docker network rm $allNetworks
}
