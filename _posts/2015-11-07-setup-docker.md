---
layout: page
title: "Setup Docker"
category: doc
date: 2015-11-07 12:00:00
---

**Note**: this steps are not required if you intend to use one of the supported cloud providers.

###Install docker

Docker Engine is supported on Linux, Cloud, Windows, and OS X. Installation instructions are available for the following:

- On Linux
    - [Arch Linux](https://docs.docker.com/engine/installation/archlinux/)
    - [CentOS](https://docs.docker.com/engine/installation/centos/)
    - [CRUX Linux](https://docs.docker.com/engine/installation/cruxlinux/)
    - [Debian](https://docs.docker.com/engine/installation/debian/)
    - [Fedora](https://docs.docker.com/engine/installation/fedora/)
    - [FrugalWare](https://docs.docker.com/engine/installation/frugalware/)
    - [Gentoo](https://docs.docker.com/engine/installation/gentoolinux/)
    - [Oracle Linux](https://docs.docker.com/engine/installation/oracle/)
    - [Red Hat Enterprise Linux](https://docs.docker.com/engine/installation/rhel/)
    - [openSUSE and SUSE Linux Enterprise](https://docs.docker.com/engine/installation/SUSE/)
    - [Ubuntu](https://docs.docker.com/engine/installation/ubuntulinux/)
- On OSX and Windows
    - [Mac OS X](https://docs.docker.com/engine/installation/mac/)
    - [Windows](https://docs.docker.com/engine/installation/windows/)

**Note**: If your linux distribution is not listed above, don’t give up yet. To try out Docker on a distribution that is not listed above, go here: [Installation from binaries](https://docs.docker.com/engine/installation/binaries/).

###Setup docker groups

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

###Get bcbio/bcbio docker image

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

###Create a new docker image

```
~ $ bcbio_vm.py -v azure devel dockerbuild \
    --buildingtype full \
    --rundir /tmp/bcbio-nextgen \
    --no-upload
```

```
< PLAY [Create the bcbio_vm docker image locally] >
 -------------------------------------------------

 _________________
< GATHERING FACTS >
 -----------------
<127.0.0.1> REMOTE_MODULE setup
ok: [127.0.0.1]

 ________________________________________________________
< TASK: bcbio_vm_build | Clone bcbio-nextgen from GitHub >
 --------------------------------------------------------
<127.0.0.1> REMOTE_MODULE git version=master
                          dest=/tmp/bcbio-nextgen 
                          repo=https://github.com/chapmanb/bcbio-nextgen.git
changed: [127.0.0.1]

 ______________________________________________
/ TASK: bcbio_vm_build | set_fact              \
\ image_name=chapmanb/bcbio-nextgen-devel-work /
 ----------------------------------------------
ok: [127.0.0.1]

 _________________________________________
/ TASK: bcbio_vm_build | set_fact         \
\ image_name=chapmanb/bcbio-nextgen-devel /
 -----------------------------------------
skipping: [127.0.0.1]

 ____________________________________________________
/ TASK: bcbio_vm_build | Update code in bcbio docker \
\ container                                          /
 ----------------------------------------------------
skipping: [127.0.0.1]

 __________________________________________________________
< TASK: bcbio_vm_build | Build full bcbio docker container >
 ----------------------------------------------------------
<127.0.0.1> REMOTE_MODULE async_status jid=432667395995.21107
changed: [127.0.0.1]
<job 432667395995.21107> finished on 127.0.0.1

 __________________________________________
/ TASK: bcbio_vm_build | command tail -100 \
\ {{bcbio_dir}}/build.log                  /
 ------------------------------------------
<127.0.0.1> REMOTE_MODULE command tail -100 /tmp/bcbio-nextgen/build.log
changed: [127.0.0.1]

 _____________________________________
/ TASK: bcbio_vm_build | debug        \
\ var=bcbio_docker_debug.stdout_lines /
 -------------------------------------
ok: [127.0.0.1] => {
    "var": {
        "bcbio_docker_debug.stdout_lines": [
            "Sending build context to Docker daemon 557.1 kB",
            "Sending build context to Docker daemon 1.114 MB",
            "Sending build context to Docker daemon 1.671 MB",
            "Sending build context to Docker daemon 2.228 MB",
            "Sending build context to Docker daemon 2.785 MB",
            "Sending build context to Docker daemon 3.342 MB",
            "Sending build context to Docker daemon 3.899 MB",
            "Sending build context to Docker daemon 4.456 MB",
            "Sending build context to Docker daemon 5.014 MB",
            "Sending build context to Docker daemon 5.571 MB",
            "Sending build context to Docker daemon 6.128 MB",
            "Sending build context to Docker daemon 6.685 MB",
            "Sending build context to Docker daemon 7.242 MB",
            "Sending build context to Docker daemon 7.799 MB",
            "Sending build context to Docker daemon 8.356 MB",
            "Sending build context to Docker daemon 8.913 MB",
            "Sending build context to Docker daemon  9.47 MB",
            "Sending build context to Docker daemon 10.03 MB",
            "Sending build context to Docker daemon 10.58 MB",
            "Sending build context to Docker daemon 11.14 MB",
            "Sending build context to Docker daemon  11.7 MB",
            "Sending build context to Docker daemon 12.26 MB",
            "Sending build context to Docker daemon 12.81 MB",
            "Sending build context to Docker daemon 13.37 MB",
            "Sending build context to Docker daemon 13.93 MB",
            "Sending build context to Docker daemon 14.48 MB",
            "Sending build context to Docker daemon 15.04 MB",
            "Sending build context to Docker daemon  15.6 MB",
            "Sending build context to Docker daemon 16.15 MB",
            "Sending build context to Docker daemon 16.71 MB",
            "Sending build context to Docker daemon 17.27 MB",
            "Sending build context to Docker daemon 17.83 MB",
            "Sending build context to Docker daemon 18.38 MB",
            "Sending build context to Docker daemon 18.94 MB",
            "Sending build context to Docker daemon  19.5 MB",
            "Sending build context to Docker daemon 20.05 MB",
            "Sending build context to Docker daemon 20.61 MB",
            "Sending build context to Docker daemon 21.17 MB",
            "Sending build context to Docker daemon 21.73 MB",
            "Sending build context to Docker daemon 22.28 MB",
            "Sending build context to Docker daemon 22.84 MB",
            "Sending build context to Docker daemon  23.4 MB",
            "Sending build context to Docker daemon 23.95 MB",
            "Sending build context to Docker daemon 24.48 MB",
            "Sending build context to Docker daemon 25.01 MB",
            "Sending build context to Docker daemon 25.53 MB",
            "Sending build context to Docker daemon 26.06 MB",
            "Sending build context to Docker daemon  26.6 MB",
            "Sending build context to Docker daemon 27.13 MB",
            "Sending build context to Docker daemon 27.69 MB",
            "Sending build context to Docker daemon 28.25 MB",
            "Sending build context to Docker daemon  28.8 MB",
            "Sending build context to Docker daemon 29.36 MB",
            "Sending build context to Docker daemon 29.92 MB",
            "Sending build context to Docker daemon 30.47 MB",
            "Sending build context to Docker daemon 31.03 MB",
            "Sending build context to Docker daemon 31.59 MB",
            "Sending build context to Docker daemon 32.15 MB",
            "Sending build context to Docker daemon  32.7 MB",
            "Sending build context to Docker daemon 33.26 MB",
            "Sending build context to Docker daemon 33.82 MB",
            "Sending build context to Docker daemon 34.37 MB",
            "Sending build context to Docker daemon 34.93 MB",
            "Sending build context to Docker daemon 35.49 MB",
            "Sending build context to Docker daemon 36.04 MB",
            "Sending build context to Docker daemon  36.6 MB",
            "Sending build context to Docker daemon 37.16 MB",
            "Sending build context to Docker daemon 37.72 MB",
            "Sending build context to Docker daemon 38.27 MB",
            "Sending build context to Docker daemon 38.83 MB",
            "Sending build context to Docker daemon 39.39 MB",
            "Sending build context to Docker daemon 39.94 MB",
            "Sending build context to Docker daemon  40.5 MB",
            "Sending build context to Docker daemon 41.06 MB",
            "Sending build context to Docker daemon 41.62 MB",
            "Sending build context to Docker daemon 42.17 MB",
            "Sending build context to Docker daemon 42.73 MB",
            "Sending build context to Docker daemon 43.29 MB",
            "Sending build context to Docker daemon 43.84 MB",
            "Sending build context to Docker daemon  44.4 MB",
            "Sending build context to Docker daemon 44.96 MB",
            "Sending build context to Docker daemon 45.51 MB",
            "Sending build context to Docker daemon 46.07 MB",
            "Sending build context to Docker daemon 46.63 MB",
            "Sending build context to Docker daemon 46.93 MB",
            "Sending build context to Docker daemon 46.93 MB",
            "",
            "Step 1 : FROM stackbrew/ubuntu:14.04",
            " ---> 1d073211c498",
            "Step 2 : MAINTAINER Brad Chapman \"https://github.com/chapmanb\"",
            " ---> Using cache",
            " ---> 78f8b74a3cfc",
            "Step 3 : RUN apt-get update && apt-get install -y build-essential zlib1g-dev wget curl python-setuptools git &&     apt-get install -y openjdk-7-jdk openjdk-7-jre ruby libncurses5-dev libcurl4-openssl-dev libbz2-dev     unzip pigz bsdmainutils &&     mkdir -p /tmp/fuse-hack && cd /tmp/fuse-hack &&     apt-get install libfuse2 &&     apt-get download fuse &&     dpkg-deb -x fuse_* . &&     dpkg-deb -e fuse_* &&     rm fuse_*.deb &&     echo -en '#!/bin/bash\\nexit 0\\n' > DEBIAN/postinst &&     dpkg-deb -b . /fuse.deb &&     dpkg -i /fuse.deb &&     rm -rf /tmp/fuse-hack &&     mkdir -p /tmp/bcbio-nextgen-install && cd /tmp/bcbio-nextgen-install &&     wget --no-check-certificate       https://raw.github.com/chapmanb/bcbio-nextgen/master/scripts/bcbio_nextgen_install.py &&     python bcbio_nextgen_install.py /usr/local/share/bcbio-nextgen       --nodata -u development &&     git config --global url.https://github.com/.insteadOf git://github.com/ &&     /usr/local/share/bcbio-nextgen/anaconda/bin/bcbio_nextgen.py upgrade --sudo --tooldir=/usr/local --tools &&     /usr/local/share/bcbio-nextgen/anaconda/bin/bcbio_nextgen.py upgrade --isolate -u development --tools --toolplus data  &&     echo 'export PATH=/usr/local/bin:$PATH' >> /etc/profile.d/bcbio.sh &&     wget --no-check-certificate -O createsetuser       https://raw.github.com/chapmanb/bcbio-nextgen-vm/master/scripts/createsetuser &&     chmod a+x createsetuser && mv createsetuser /sbin &&     apt-get clean &&     rm -rf /var/lib/apt/lists/* /var/tmp/* &&     /usr/local/share/bcbio-nextgen/anaconda/bin/conda remove --yes qt &&     /usr/local/share/bcbio-nextgen/anaconda/bin/conda clean --yes --tarballs &&     rm -rf /usr/local/share/bcbio-nextgen/anaconda/pkgs/qt* &&     rm -rf $(brew --cache) &&     rm -rf /usr/local/.git &&     rm -rf /.cpanm &&     rm -rf /tmp/bcbio-nextgen-install &&     mkdir -p /mnt/biodata &&     mkdir -p /tmp/bcbio-nextgen &&     mv /usr/local/share/bcbio-nextgen/galaxy/bcbio_system.yaml /usr/local/share/bcbio-nextgen/config &&     rmdir /usr/local/share/bcbio-nextgen/galaxy &&     ln -s /mnt/biodata/galaxy /usr/local/share/bcbio-nextgen/galaxy &&     ln -s /mnt/biodata/gemini_data /usr/local/share/bcbio-nextgen/gemini_data &&     ln -s /mnt/biodata/genomes /usr/local/share/bcbio-nextgen/genomes &&     ln -s /mnt/biodata/liftOver /usr/local/share/bcbio-nextgen/liftOver &&     chmod a+rwx /usr/local/share/bcbio-nextgen &&     chmod a+rwx /usr/local/share/bcbio-nextgen/config &&     chmod a+rwx /usr/local/share/bcbio-nextgen/config/*.yaml &&     chmod a+rwx /usr/local/share/bcbio-nextgen/gemini-config.yaml &&     find /usr/local -perm /u+x -execdir chmod a+x {} \\; &&     find /usr/local -perm /u+w -execdir chmod a+w {} \\;",
            " ---> Using cache",
            " ---> 77a2d9ee7d3f",
            "Successfully built 77a2d9ee7d3f"
        ]
    }
}

_______________________
/ TASK: bcbio_vm_build | Create gzipped bcbio docker \
\ container                                          /
 ----------------------------------------------------
<127.0.0.1> REMOTE_MODULE command
    chdir=/tmp/bcbio-nextgen
    creates=bcbio-nextgen-docker-image.gz
    DID=$(docker run -d chapmanb/bcbio-nextgen-devel-work /bin/bash)
    docker export $DID | gzip -c > bcbio-nextgen-docker-image.gz
    #USE_SHELL
changed: [127.0.0.1]
```

###Create and upload a docker image

In order to create a new docker image and upload it to the default storage account we will use the following command:

```
bcbio_vm.py azure devel dockerbuild \
    --buildtype full \
    --rundir /tmp/bcbio-nextgen \
    --container bcbio-nextegen
```

The output for the above command will look like:

```
[DEBUG]: Creating docker image: /tmp/bcbio-nextgen/bcbio-nextgen-docker-image.gz
[DEBUG]: Setup the environment before playbook run.
[DEBUG]: Trying to run '/home/alex/miniconda/envs/_test/share/bcbio-vm/ansible/bcbio_vm_docker_local.yml' ansible playbook.
[DEBUG]: Playbook started playing: Create the bcbio_vm docker image locally
[DEBUG]: Playbook is setting up.
[DEBUG]: Playbook starting task 'bcbio_vm_build | Clone bcbio-nextgen from GitHub':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | set_fact image_name=chapmanb/bcbio-nextgen-devel-work':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | set_fact image_name=chapmanb/bcbio-nextgen-devel':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | Update code in bcbio docker container':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | Build full bcbio docker container':False
[DEBUG]: Playbook starting task u'bcbio_vm_build | command tail -100 {{bcbio_dir}}/build.log':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | debug var=bcbio_docker_debug.stdout_lines':False
[DEBUG]: Playbook starting task 'bcbio_vm_build | Create gzipped bcbio docker container':False
[DEBUG]: Cleanup the environment after playbook run.
[DEBUG]: Playbook response: ([], {})
[INFO]: Uploading docker image /tmp/bcbio-nextgen/bcbio-nextgen-docker-image.gz ...
[INFO]: The docker image was successfully uploaded ! Image URL: https://bcbio.blob.core.windows.net/bcbio-nextegen/bcbio-nextgen-docker-image.gz 
```

![Upload docker image]({{ site.production_url }}/assets/upload-docker-image.png)

**Note**: In order to upload the image to a specific storage account the following arguments can be used:

```
  -c CONTAINER, --container CONTAINER
                        The container name where to upload the gzipped docker
                        image to
  -s STORAGE_ACCOUNT, --storage-account STORAGE_ACCOUNT
                        The storage account name. All access to Azure Storage
                        is done through a storage account.
  -k ACCESS_KEY, --access-key ACCESS_KEY
                        The key required to access the storage account.
```

###Upgrade docker image

bcbio-nextgen-vm enables easy updates of the wrapper code, tools and data.

To update the wrapper code:

```
~ $ git clone https://github.com/champmanb/bcbio-nextgen /tmp/bcbio-nextgen
~ $ cd /tmp/bcbio-nexgen
~ $ bcbio_vm.py upgrade --wrapper --image bcbio/bcbio
```

```
[DEBUG]: The sample_config was not provided.
[INFO]: bcbio-nextgen-vm updated with latest wrapper scripts
[INFO]: Execution of command Upgrade ends with success. (None)
```

To update tools, with a download of the latest docker image:
```
~ $ bcbio_vm.py upgrade --tools --image bcbio/bcbio
```

```
[DEBUG]: The sample_config was not provided.
[INFO]: Retrieving bcbio-nextgen docker image with code and tools
    [DEBUG]: bcbio-nextgen: Running in docker container: bb0fa025fb47b22ecfb617d34acd4d7b4ae7e6e4eaf18a18ca2ea988c237ac39
    [DEBUG]: bcbio-nextgen-commands: docker attach --no-stdin bb0fa025fb47b22ecfb617d34acd4d7b4ae7e6e4eaf18a18ca2ea988c237ac39
    [DEBUG]: bcbio-nextgen-stdout: Upgrade completed successfully.
[WARNING]: Stopping docker container
[INFO]: bcbio-nextgen-vm updated with latest bcbio-nextgen code and third party tools
[INFO]: Execution of command Upgrade ends with success. (None)
```

To update the associated data files:

```
~ $ bcbio_vm.py upgrade --data --image bcbio/bcbio --genomes GRCh37
```

```
[DEBUG]: The sample_config was not provided.

DEBUG: bcbio-nextgen: Running in docker container: c3b1385c2c0bee74296d1f83d4a07e652c72225c2b9c0d27b0d15bf88d95351e
DEBUG: bcbio-nextgen-commands: docker attach --no-stdin c3b1385c2c0bee74296d1f83d4a07e652c72225c2b9c0d27b0d15bf88d95351e
Cloning into 'cloudbiolinux'...
INFO: <cloudbio.flavor.Flavor instance at 0x7fbbb9cf74d0>
INFO: This is a ngs_pipeline_minimal flavor
INFO: Reading default fabricrc.txt
DBG [config.py]: Using config file /home/alex/tmpbcbio-install/cloudbiolinux/cloudbio/../config/fabricrc.txt
INFO: Distribution __auto__
INFO: Get local environment
INFO: Ubuntu setup
DBG [distribution.py]: Debian-shared setup
DBG [distribution.py]: Source=trusty
DBG [distribution.py]: NixPkgs: Ignored
INFO: Now, testing connection to host...
INFO: Connection to host appears to work!
DBG [utils.py]: Expand paths
INFO: List of genomes to get (from the config file at '{'install_liftover': False, 'genome_indexes': ['rtg'], 'genomes': [{'rnaseq': True, 'name': 'Human (GRCh37)', 'dbsnp': True, 'validation': ['giab-NA12878', 'dream-syn3', 'dream-syn4'], 'annotations': ['battenberg', 'GA4GH_problem_regions', 'MIG', 'prioritize'], 'dbkey': 'GRCh37'}], 'install_uniref': False}'): Human (GRCh37)

--2015-11-12 15:12:02--  https://s3.amazonaws.com/biodata/annotation/GRCh37-rnaseq-2014-07-14.tar.xz

Resolving s3.amazonaws.com (s3.amazonaws.com)... 54.231.98.179
Connecting to s3.amazonaws.com (s3.amazonaws.com)|54.231.98.179|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 544869372 (520M) [binary/octet-stream]
Saving to: 'GRCh37-rnaseq-2014-07-14.tar.xz'

     0K .......... .......... .......... .......... ..........  0% 82.9K 1h46m
    50K .......... .......... .......... .......... ..........  0%  122K 89m46s
   100K .......... .......... .......... .......... ..........  0%  335K 68m40s
   150K .......... .......... .......... .......... ..........  0%  191K 63m6s
   200K .......... .......... .......... .......... ..........  0%  244K 57m44s
   250K .......... .......... .......... .......... ..........  0%  243K 54m12s
   300K .......... .......... .......... .......... ..........  0%  245K 51m37s
   350K .......... .......... .......... .......... ..........  0%  244K 49m42s

...

```

```
DEBUG: bcbio-nextgen-stdout: Upgrade completed successfully.
[WARNING]: Stopping docker container
[INFO]: bcbio-nextgen-vm updated with latest biological data
[INFO]: Execution of command Upgrade ends with success. (None)

```

