# Delete the container from the compute engine vm
gcloud compute ssh chana-first-instance --project grunitech-mid-project --zone me-west1-a --command "docker rm -f $(docker ps -a -q)"

# Delete the image from the compute engine vm
gcloud compute ssh chana-first-instance --project grunitech-mid-project --zone me-west1-a --command "docker rmi -f $(docker images -aq)"
