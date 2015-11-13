---
layout: default
title: "bcbio-nextgen-vm on Windows Azure"
---

###Introduction

A python toolkit providing best-practice pipelines for fully automated high throughput sequencing analysis. You write a high level configuration file specifying your inputs and analysis parameters. This input drives a parallel pipeline that handles distributed execution, idempotent processing restarts and safe transactional steps. The goal is to provide a shared community resource that handles the data processing component of sequencing analysis, providing researchers with more time to focus on the downstream biology.

More information can be found [here](https://bcbio-nextgen.readthedocs.org/en/latest/).

###Table of content

- I. [Environment setup](doc/environment-setup.html)
    - I.1. [Update the system](doc/environment-setup.html#i1-update-the-system)
    - I.2. [Install required packages](doc/environment-setup.html#i2-install-required-packages)
    - I.3. [Install azure client](doc/environment-setup.html#i3-install-azure-client)
    - I.4. [Install miniconda](doc/environment-setup.html#i4-install-miniconda)
    - I.5. [Install additional conda packages](doc/environment-setup.html#i5-install-additional-conda-packages)
- II. [Install bcbio-nextgen-vm](doc/install-bcbio-nextgen-vm.html)
    - II.1. [Add conda channel](doc/install-bcbio-nextgen-vm.html#ii1-add-conda-channel)
    - II.2. [Install bcbio-nextgen-vm package](doc/install-bcbio-nextgen-vm.html#ii2-install-bcbio-nextgen-vm-package)
- III. [Setup Docker](doc/setup-docker.html)
    - III.1. [Install docker](doc/setup-docker.html#install-docker)
    - III.2. [Setup docker groups](doc/setup-docker.html#setup-docker-groups)
    - III.3. [Get bcbio/bcbio docker image](doc/setup-docker.html#get-bcbiobcbio-docker-image)
    - III.4. [Setup the datadir](doc/setup-docker.html#setup-the-datadir)
    - III.5. [Create a new docker image](doc/setup-docker.html#create-a-new-docker-image)
    - III.6. [Create and upload a docker image](doc/setup-docker.html#create-and-upload-a-docker-image)
    - III.7. [Upgrade docker image](doc/setup-docker.html#upgrade-docker-image)
- IV. [Setup azure environment](doc/setup-azure-environment.html)
    - IV.1. [Generate a new management certificate](doc/setup-azure-environment.html#generate-a-new-management-certificate)
    - IV.2. [Uploading managementCert.cer file to Windows Azure](doc/setup-azure-environment.html#uploading-managementcertcer-file-to-windows-azure)
    - IV.3. [Generate the private key](doc/setup-azure-environment.html#generate-the-private-key)
- V. [bcbio cluster on Windows Azure](doc/bcbio-cluster.html)
    - V.1. [Create the elasticluster configuration file](doc/bcbio-cluster.html#create-the-elasticluster-configuration-file)
    - V.2. [Edit the elasticluster configuration file](doc/bcbio-cluster.html#edit-the-elasticluster-configuration-file)
    - V.3. [Set the subscription_id](doc/bcbio-cluster.html#set-the-subscriptionid)

###Troubleshooting

I. [Troubleshooting - Elasticluster](troubleshooting/elasticluster.html)
    -I.1. [The server encountered an internal error](troubleshooting/elasticluster.html#the-server-encountered-an-internal-error)
    -I.2. [bcbio.pickle not found](troubleshooting/elasticluster.html#bcbiopickle-not-found)
    -I.3. [TypeError: expected string or buffer](troubleshooting/elasticluster.html#typeerror-expected-string-or-buffer)
