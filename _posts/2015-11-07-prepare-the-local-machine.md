---
layout: page
title: "Prepare the local machine"
category: doc
date: 2015-11-07 12:00:00
order: 3
---

###Setup the `datadir`

Create the `datadir`:

```bash
~ $ mkdir -p ~/install/bcbio-vm/data
~ $ cd ~/install/bcbio-vm/data
~ $ ln -s /usr/local/share/bcbio_nextgen/genomes
~ $ ln -s /usr/local/share/gemini/data gemini_data
```  

Create the `datadir` using bcbiovm client application: 

```bash
~ $ bcbiovm.py azure prepare datadir --path ~/install/bcbio-vm/data
```

Update the default value for `datadir`:

```bash
~ $ bcbio_vm.py --datadir=~/install/bcbio-vm/data saveconfig
```

The output:

```
[DEBUG]: Updating `datadir` value with `/home/alex/install/bcbio-vm/data`
[INFO]:  Writing the config file to `/home/alex/.config/bcbio-nextgen/bcbio-docker-config.yaml`.
[INFO]:  Execution of command `SaveConfig` ends with success. (None)
```

###Setup docker (if is required)

Docker Engine is supported on Linux, Cloud, Windows, and OS X. Installation instructions are available [here](https://docs.docker.com/engine/installation/).
**Note:** in order to complete this step it will need **root** permissions.

Setup a docker group to provide the ability to run Docker without being root. Some installations, like Debian/Ubuntu packages do this automatically. You'll also want to add the trusted user who will be managing and testing docker images to this group:

```bash
~ $ sudo groupadd docker
~ $ sudo service docker restart
~ $ sudo gpasswd -a ${USERNAME} docker
~ $ newgrp docker
```

Ensure the driver script is setgid to the docker group. This allows users to run bcbio-nextgen without needing to be in the docker group or have root access. To avoid security issues, bcbio_vm.py sanitizes input arguments and runs the internal docker process as the calling user using a small wrapper script so it will only have permissions available to that user:

```bash
~ $ sudo chgrp docker /usr/local/bin/bcbio_vm.py
~ $ sudo chmod g+s /usr/local/bin/bcbio_vm.py
``` 

Install the current bcbio docker image into your local repository by hand with:

```bash
~ $ docker pull bcbio/bcbio
```

```
Using default tag: latest
latest: Pulling from bcbio/bcbio
78f8b74a3cfc: Pull complete 
77a2d9ee7d3f: Pull complete 
Digest: sha256:8e4a8372c2846607e4c32c33b08035340b7c2a2e54463ec06ac698ce5af27595
Status: Downloaded newer image for bcbio/bcbio:latest
```

The installer does this automatically, but this is useful if you want to work with the bcbio-nextgen docker image independently from the wrapper.
