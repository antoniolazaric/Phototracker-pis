# Phototracker-pis

My project will enable an advertising agency to more easily track photographers. It will allow them to create their ads with the photographer's first name and last name, level of experience, equipment, phone, and email. They will be able to create, view, update, and delete photographer information.

## Features

-Add a new photographer
-See all pgotographers
-Edit photographer
-Delete photographer

## Running the Backend

Application is run by docker

#### Creating a docker image

```sh
cd Phototracker-pis
docker build -t phototracker -f ./Dockerfile .
```

#### Running the docker image

```sh
docker run -p 5000:5000 phototracker
```
