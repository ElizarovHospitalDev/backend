#!/bin/bash

DIRECTORY=/opt/backend/;

cd $DIRECTORY;

docker pull ghcr.io/ElizarovHospitalDev/backend:$CI_COMMIT_SHORT_SHA;

if [[ $? = 0 ]]
    then
      docker compose down;
      docker compose up -d;
    else
      echo "Failed to pull Docker images"
      exit 1
fi