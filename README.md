# vsphere-nsx-lab-deploy
Ansible playbook to automate deployment of vCenter, nested ESXi hosts

#### Table of Contents

1. [Description](#description)
1. [Setup - The basics of getting started with nsxt](#setup)
    * [Dependencies](#Dependencies)
    * [Edit answersfile.yml](#Edit answersfile.yml)
1. [Usage](#usage)
1. [Limitations)
1. [Development](#development)

## Description

This repository will be used to hold an Ansible Playbook to deploy and configure vCenter and nested ESXi VMs 

## Setup

### Dependencies

apt-get install sshpass python-pip git
pip install vim
pip install pyvmomi
git clone https://github.com/yasensim/vsphere-nsx-lab-deploy.git

Place the ESXi and VCSA ISOs in /root/ISOs


### Edit answersfile.yml

Edit answersfile.yml according to your infrastructure!

## Usage

ansible-playbook *.yml


## Limitations
Ansible => 2.2 is required
ESXi version 6.0 and above is supported
VCSA version 6.0U2 and above is supported

## Development

VMware internal

