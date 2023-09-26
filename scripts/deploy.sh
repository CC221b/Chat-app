#!/bin/bash

version=$1
commit_hash=$2


if [[ -z $version && -z $commit_hash ]]; then
    echo "missing parameters"
    exit 1
fi


# Check if the image exists
if docker image inspect chatapp:$version > /dev/null 2>&1; then
    # Image exists, ask the user if they want to rebuild it
    echo "Image chatapp:$version already exists."
    echo "Do you want to rebuild it? (y/n)"
    read -n 1 rebuild
    echo


    if [[ "$rebuild" == "y" ]]; then
        # Delete the existing image
        docker rmi chatapp:$version
        # Rebuild the image
        docker build -t chatapp:$version .
    else
        # Use the existing image
        echo "Using existing image chatapp:$version."
    fi
else
    # Image does not exist, build it
    docker build -t chatapp:$version .
fi


# Ask the user if they want to tag and push the image to the Git repository
echo "Do you want to tag and push the image to the Git repository? (y/n)"
read -n 1 tag_and_push
echo


if [[ "$tag_and_push" == "y" ]]; then
    # Tag and push the image to the Git repository
    git tag $version $commit_hash
    git push origin $version
fi


# Ask the user if they want to push the image to the Artifact Registry repository
echo "Do you want to push the image to the Artifact Registry repository? (y/n)"
read -n 1 push_to_artifact_registry
echo


if [[ "$push_to_artifact_registry" == "y" ]]; then
    # Push the image to the Artifact Registry repository
    # Use service account impersonation to authenticate to the Artifact Registry
    gcloud auth activate-service-account artifact-admin-sa --key-file artifact-admin-sa.json
    gcloud artifacts repositories list
    gcloud artifacts repositories add-tag chana-chat-app-images chatapp:$version
fi
