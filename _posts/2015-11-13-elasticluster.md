---
layout: page
title: "Troubleshooting - Elasticluster"
category: troubleshooting
date: 2015-11-13 12:00:00
---

##Troubleshooting

###The server encountered an internal error

The curent version of elasticluster for Azure doesn't have a friendly error reporting mechanism. If the following errors continue to appear and the attempt number is bigger then 25 is possible to have some misconfigurations in the azure.conf file. 

```
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 1 of 50): async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 2 of 50): async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 3 of 50): async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 4 of 50): async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 5 of 50): async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:async operation failed: The server encountered an internal error. Please retry the request.
ERROR:gc3.elasticluster:error creating vm bcbio_vm0000_bcbio-compute002 (attempt 6 of 50): async operation failed: The server encountered an internal error. Please retry the request.
```

###bcbio.pickle not found
```
! $ bcbio_vm.py azure cluster stop --cluster bcbio
```

```
[DEBUG]: Run elasticluster command: ['elasticluster', '--storage', '/home/alex/.bcbio/elasticluster/storage', '--config', '/home/alex/.bcbio/elasticluster/azure.config', 'stop', 'bcbio']
[ERROR]: gc3.elasticluster:Stopping cluster bcbio: Storage file /home/alex/.bcbio/elasticluster/storage/bcbio.pickle not found

bcbiovm.client.base - [INFO]: Execution of command Stop ends with success. (0)
```

The elasticluster failed to cleanup the environment.

![Elasticluster resources]({{ site.production_url }}/assets/elastic-cluster-resources.png)

In order to cleanup the environment you will need to follow this steps:

####Delete all the bcbio_vm\*\*\* virtual machines**

![Delete bcbio virtual machine]({{ site.production_url }}/assets/azure-delete-vm-1.png)

![Delete bcbio virtual machine]({{ site.production_url }}/assets/azure-delete-vm-1.png)

####Delete the Storage Account

![Delete the Storage Account]({{ site.production_url }}/assets/delete-storage-account.png)

####Delete the Cloud Service

![Delete the Cloud Service]({{ site.production_url }}/assets/delete-cloud-service.png)

####Delete the Virtual Network

![Delete the Virtual Network]({{ site.production_url }}/assets/delete-virtual-network.png)

###TypeError: expected string or buffer

```
INFO:gc3.elasticluster:_start_node: node has been started
INFO:gc3.elasticluster:_start_node: node has been started
INFO:gc3.elasticluster:_start_node: node has been started
Traceback (most recent call last):
  File "/home/alex/miniconda/envs/_test/bin/bcbio_vm.py", line 4, in <module>
    __import__('pkg_resources').run_script('bcbio-nextgen-vm==0.1.0a0', 'bcbio_vm.py')
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/setuptools-18.4-py2.7.egg/pkg_resources/__init__.py", line 735, in run_script
    
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/setuptools-18.4-py2.7.egg/pkg_resources/__init__.py", line 1659, in run_script
    
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/bcbio_nextgen_vm-0.1.0a0-py2.7.egg/EGG-INFO/scripts/bcbio_vm.py", line 89, in <module>
    
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/bcbio_nextgen_vm-0.1.0a0-py2.7.egg/EGG-INFO/scripts/bcbio_vm.py", line 85, in main
    
  File "build/bdist.linux-x86_64/egg/bcbiovm/client/base.py", line 70, in run
  File "build/bdist.linux-x86_64/egg/bcbiovm/client/base.py", line 335, in work
  File "build/bdist.linux-x86_64/egg/bcbiovm/client/base.py", line 70, in run
  File "build/bdist.linux-x86_64/egg/bcbiovm/client/commands/provider/cluster.py", line 185, in work
  File "build/bdist.linux-x86_64/egg/bcbiovm/provider/base.py", line 153, in start
  File "build/bdist.linux-x86_64/egg/bcbiovm/common/cluster.py", line 161, in start
  File "build/bdist.linux-x86_64/egg/bcbiovm/common/cluster.py", line 144, in execute
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/main.py", line 181, in main
    app.run()
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/cli/app.py", line 245, in run
    return self.post_run(returned)
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/cli/app.py", line 241, in run
    returned = self.main(*args)
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/main.py", line 169, in main
    return self.params.func()
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/subcommands.py", line 71, in __call__
    return self.execute()
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/subcommands.py", line 190, in execute
    cluster.start(min_nodes=min_nodes)
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/cluster.py", line 415, in start
    keys, node.instance_id, node.ips)
  File "/home/alex/miniconda/envs/_test/lib/python2.7/site-packages/elasticluster/cluster.py", line 649, in _get_ssh_key_from_console_output
    r'\1', console_output, flags=re.DOTALL).strip()
  File "/home/alex/miniconda/envs/_test/lib/python2.7/re.py", line 155, in sub
    return _compile(pattern, flags).sub(repl, string, count)
TypeError: expected string or buffer
```

Information related to keys from [Elasticluster for Azure documentation](https://github.com/chapmanb/elasticluster/blob/bcbio/README-AZURE.rst):

6\. You'll need a keypair to access the virtual machines during provisioning, and later via ssh. For now, you should create a private key file that matches your management cert, like this:

```bash
~ $ openssl rsa -in managementCert.pem -out managementCert.key
```

SSH is picky about ownership/permissions on key files. Make sure that yours look like this:

```
~ $  ls -l ~/.ssh
[...]
-rw------- 1 my_user_name my_user_name  797 May  3 18:00 managementCert.cer
```
Use these commands if needed on the .pem, .cer, and .key files:

```bash
# replace 'my_user_name' with your username - you knew that
~ $ sudo chown my_user_name:my_user_name ~/.ssh/managementCert.pem
~ $ sudo chmod 600 ~/.ssh/managementCert.pem
# make sure you do this to all 3 files!
```

(**Note**:  access to a specific virtual machine using a keypair that is not also an Azure management keypair doesn't work at present, but is an open work item.)


**Step1** Replace `~/.ssh` with `/home/user/.ssh`

```
[cloud/azure-cloud]
provider = azure
subscription_id = [secret]
certificate = /home/alex/.ssh/managementCert.pem

[login/azure-login]
image_user = ubuntu
image_user_sudo = root
image_sudo = True
user_key_name = az_ec_key
user_key_private = /home/alex/.ssh/managementCert.key
user_key_public = /home/alex/.ssh/managementCert.pem

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

**Step2** Check keys permissions in `/home/user/.ssh`

```
~ $ ls -la
```

```
total 116
drwx------  3 alex alex  4096 Nov  7 13:55 .
drwx------ 87 alex alex 20480 Nov 13 15:45 ..
-rw-r--r--  1 alex alex  1522 Nov  7 10:49 config
drwx------  2 alex alex  4096 Apr  6  2015 keys
-rw-------  1 alex alex 11574 Nov 12 22:22 known_hosts
-rw-------  1 alex alex 11352 Nov  7 10:51 known_hosts.old
-rw-------  1 alex alex   989 Oct 26 15:00 managementCert.cer
-rw-------  1 alex alex  1675 Oct 26 15:39 managementCert.key
-rw-------  1 alex alex  3099 Oct 26 15:00 managementCert.pem
```

**Step3** Update keys permissions

```
~ $ chmod 600 managementCert.cer
~ $ chmod 600 managementCert.key
~ $ chmod 600 managementCert.pem
```

**Note**: For the current issue doesn't exist a fix yet.