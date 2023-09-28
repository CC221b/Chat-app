# #!/bin/bash

# version=$1

# if [[ -z version ]];then
#     echo "missing parameters"
#     exit 1
# fi

# rooms_dir="$(pwd)/src/rooms"
# users_csv="$(pwd)/src/users.csv"

# docker build -t chatapp:$version .

# docker run  -p 5000:5000 -v "$rooms_dir:/src/rooms" -v "$users_csv:/src/users.csv" chatapp:$version


#!/bin/bash

version=$1

if [[ -z version ]];then
    echo "missing parameters"
    exit 1
fi

#gcloud auth login

gcloud config unset auth/impersonate_service_account

gcloud compute ssh chana-first-instance --project grunitech-mid-project --zone me-west1-a 

gcloud auth configure-docker me-west1-docker.pkg.dev

docker pull me-west1-docker.pkg.dev/grunitech-mid-project/chana-chat-app-images/chatapp:${version}

docker run -p 8080:5000 me-west1-docker.pkg.dev/grunitech-mid-project/chana-chat-app-images/chatapp:${version}



