# python-data-1

docker --version

# list out all the images available on host system
docker images
docker images -a

docker pull <image>

docker rmi <image_name:tag>


docker run <image>
docker run <image> "command"

-- docker run python python -c 'python("Hello")'

-- docker run --rm -v .:/app python python --version

-- docker run --rm -v .:/app python:3.9.20-alpine3.19  python --version


Volumes

docker run -v .:/app python python /app/main.py

docker run -v .:/otherdir python python /otherdir/main.py

Delete the container once it finishes its job
docker run --rm -v .:/pqrs python ls .

# list out all the containers (Running)
docker ps

docker ps -a

docker rm <container_name/container_id>. # only for stopped containers

docker rm -f <container_name/container_id>

docker container prune

docker container prune -f


Create a container that runs continously and does not finish immediately

Container is a machine, and its running

docker exec 3e3fe0693ca8 python -c "print('other command')"

docker exec -it 3e3fe0693ca8  bash