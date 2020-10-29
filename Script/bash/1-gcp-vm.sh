#!/usr/bin/bash

if ! command -v gcloud &> /dev/null
then
    echo "'gcloud' command does not exists"
    echo "Installing gcloud within the system"
    system_name=`cat /etc/os-release | grep -Ei 'ID=\"[a-zA-Z]+\"' | sed -E 's/ID=\"([a-zA-Z]+)\"/\1/'`
    if [ "$system_name" == "ubuntu" ] || [ "$system_name" == "debian" ]
    then
        echo "Installing the gcloud for debian/ubuntu based system"
        echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

        sudo apt-get update
        sudo apt-get install apt-transport-https ca-certificates gnupg -y
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
        sudo apt-get update && sudo apt-get install google-cloud-sdk -y

    else
        sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

       sudo yum install google-cloud-sdk -y

    fi

else

    echo "Create a Basic gcloud VM Instance ................"
    echo "===================================================="
    echo

    gcloud compute instances create test-gcp-instance --image-family=centos-7 --image-project=centos-cloud --zone=us-central1-a


    echo "===================================================="
    echo "===================================================="
    echo "Complex compute instance......"

fi