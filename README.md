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

apt-get install sshpass python-pip git <br/>
pip install vim <br/>
pip install pyvmomi <br/>
git clone https://github.com/yasensim/vsphere-nsx-lab-deploy.git <br/>

Place the ESXi and VCSA ISOs in /root/ISOs <br/>


### Edit answersfile.yml

Edit answersfile.yml according to your infrastructure!

## Usage

ansible-playbook *.yml


## Limitations
Ansible => 2.2 is required <br/>
ESXi version 6.0 and above is supported <br/>
VCSA version 6.0U2 and above is supported <br/>

## Development

VMware internal

