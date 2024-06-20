#!/bin/bash

# Install AWS CLI
sudo apt-get update &&
sudo apt-get install awscli -y  # Debian/Ubuntu

sudo yum update &&
sudo yum install awscli -y      # CentOS/RedHat

#brew install awscli        -y     # macOS (with Homebrew)

# Install Docker on Ubuntu
sudo apt update &&
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y &&
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - &&
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" &&
sudo apt update &&
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose -y &&
sudo systemctl start docker &&
sudo usermod -aG docker $USER

# Verify Docker installation
docker version
