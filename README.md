###Introduction

A python toolkit providing best-practice pipelines for fully automated high throughput sequencing analysis. You write a high level configuration file specifying your inputs and analysis parameters. This input drives a parallel pipeline that handles distributed execution, idempotent processing restarts and safe transactional steps. The goal is to provide a shared community resource that handles the data processing component of sequencing analysis, providing researchers with more time to focus on the downstream biology.

More information can be found [here](https://bcbio-nextgen.readthedocs.org/en/latest/).

###Table of content

- I. [Environment setup](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html)
    - I.1. [Update the system](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html#i1-update-the-system)
    - I.2. [Install required packages](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html#i2-install-required-packages)
    - I.3. [Install azure client](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html#i3-install-azure-client)
    - I.4. [Install miniconda](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html#i4-install-miniconda)
    - I.5. [Install additional conda packages](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/environment-setup.html#i5-install-additional-conda-packages)
- II. [Install bcbio-nextgen-vm](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/install-bcbio-nextgen-vm.html)
    - II.1. [Add conda channel](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/install-bcbio-nextgen-vm.html#ii1-add-conda-channel)
    - II.2. [Install bcbio-nextgen-vm package](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/install-bcbio-nextgen-vm.html#ii2-install-bcbio-nextgen-vm-package)
- III. [Prepare the local machine](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/prepare-the-local-machine.html)
    - III.1. [Setup the datadir](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/prepare-the-local-machine.html#iii1-setup-the-datadir)
    - III.2. [Setup docker (if is required)](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/prepare-the-local-machine.html#iii2-setup-docker-if-is-required)
- IV. [Setup azure environment](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/setup-azure-environment.html)
    - IV.1. [Generate a new management certificate](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/setup-azure-environment.html#generate-a-new-management-certificate)
    - IV.2. [Uploading managementCert.cer file to Windows Azure](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/setup-azure-environment.html#uploading-managementcertcer-file-to-windows-azure)
    - IV.3. [Generate the private key](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/setup-azure-environment.html#generate-the-private-key)
    - IV.4. [Create the elasticluster configuration file](https://alexandrucoman.github.io/docs-azure-bcbiovm/doc/setup-azure-environment.html#create-the-elasticluster-configuration-file)
