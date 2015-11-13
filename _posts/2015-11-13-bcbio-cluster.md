---
layout: page
title: "bcbio cluster on Windows Azure"
category: doc
date: 2015-11-13 12:00:00
---

###Create the elasticluster configuration file

Write Elasticluster configuration file with user information.

```
usage: bcbio_vm.py azure config create [-h] [--econfig ECONFIG]

optional arguments:
  -h, --help         show this help message and exit
  --econfig ECONFIG  Elasticluster bcbio configuration file
```

We will use the default values.

```bash
~ $ bcbio_vm.py azure config create
```

The output for this command.

```
[INFO] Execution of command ECConfig ends with success. (None)
[INFO] The elasticluster config was successfully generated.
```

###Edit the elasticluster configuration file

```bash
~ $ bcbio_vm.py azure config edit
```

```
Number of cluster worker nodes (0 starts a single machine instead of a cluster) [2]: 3    
Machine type for frontend worker node [Small]: 
Machine type for compute nodes [Small]: 
Size of encrypted NFS mounted filesystem, in Gb [200]: 20

[INFO]: Execution of command EditConfig ends with success. (None)
```

In order to check the modification we can run the following command:

```bash
~ $ cat ~/.bcbio/elasticluster/azure.config
```

```ini
[cloud/azure-cloud]
provider = azure
subscription_id = 
certificate = ~/.ssh/managementCert.pem

[login/azure-login]
image_user = ubuntu
image_user_sudo = root
image_sudo = True
user_key_name = az_ec_key
user_key_private = ~/.ssh/managementCert.key
user_key_public = ~/.ssh/managementCert.pem

[setup/ansible]
provider = ansible
frontend_groups = common
compute_groups = clients

[setup/ansible-slurm]
provider = ansible
frontend_groups = slurm_master
compute_groups = slurm_clients
global_var_slurm_selecttype = select/cons_res
global_var_slurm_selecttypeparameters = CR_Core_Memory

[cluster/bcbio]
cloud = azure-cloud
login = azure-login
ssh_to = frontend
ssh_hostkeys_from_console_output = True
security_group = default
setup_provider = ansible-slurm
frontend_nodes = 1
compute_nodes = 3
image_id = b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04-LTS-amd64-server-20140414-en-us-30GB
root_volume_size = 20
flavor = Small
location = East US
wait_timeout = 600
base_name = bcbio
global_var_ansible_ssh_host_key_dsa_public = ''

[cluster/bcbio/frontend]
flavor = Small
encrypted_volume_size = 20
encrypted_volume_type = io1
encrypted_volume_iops = 600
```

###Set the subscription_id

In order to get the `subscription_id` it will require to open a browser and go to the portal: [manage.windowsazure.com](https://manage.windowsazure.com). Once you sign in, select the Settings tab on the far bottom of the left side of the portal, then click on Subscriptions.

![Settings / Subscriptions]({{ site.production_url }}/assets/windows-azure-subscriptions.png){: .center-image }

```bash
~ $ vim ~/.bcbio/elasticluster/azure.config
```

And now edit the following line:

```ini
subscription_id = 
```

with

```ini
# Change the xxx with the value from Windows Azure Portal
subscription_id = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
