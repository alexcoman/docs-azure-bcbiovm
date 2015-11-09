---
layout: page
title: "Setup Windows Azure environment"
category: doc
date: 2015-11-09 12:00:00
---

###Generate a new management certificate

```
usage: bcbio_vm.py azure prepare management-cert [-h] [-c COUNTRY] [-st STATE]
                                                 [-o ORGANIZATION] [-cn CNAME]
                                                 [-e EMAIL] [-f]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNTRY, --country COUNTRY
                        Country Name (2 letter code)
  -st STATE, --state STATE
                        State or Province Name (full name)
  -o ORGANIZATION, --organization ORGANIZATION
                        Organization Name (eg, company)
  -cn CNAME, --cname CNAME
                        Common Name (e.g. server FQDN or YOUR name)
  -e EMAIL, --email EMAIL
                        Email Address
  -f, --force           Overwrite the management certificate if already exits.


```

For example if we want to generate a management certificate for **Alexandru Coman** from **Iași, Romania** which works at **Cloudbase Solutions** the command line will look as follows:
 
```bash
~ $ bcbio_vm.py azure prepare management-cert \
    --country RO \
    --state Iasi \
    --organization "Cloudbase Solutions" \
    --cname "Alexandru Coman" \
    --email "acoman@cloudbasesolutions.com"
```

The output for this command:
```
[INFO] Execution of command ManagementCertificate ends with success. (None)
[INFO] The management certificate was successfully generated.
```

###Uploading managementCert.cer file to Windows Azure

Once you have the **managementCert.cer** file which contains the public key, you need to upload it to the Windows Azure Management Portal. Open a browser and go to the portal: [manage.windowsazure.com](https://manage.windowsazure.com). Once you sign in, select the Settings tab on the far bottom of the left side of the portal, then click on Management Certificates.

![Settings / Management Certificates]({{ site.url }}/assets/upload-management-cer-1.png)

On the Management Certificates page, you can select the Upload action from the command bar at the bottom of the screen. It will prompt you for the .cer file you created which contains the public key for the certificate. Click on the little folder icon and locate the .cer file you created. If you have more than one subscription you may also see a drop-down with your subscriptions listed. If so, select the subscription you want to relate the certificate to. Finally, click the check mark to complete the upload.

![Management Certificates / Upload]({{ site.url }}/assets/upload-management-cer-2.png)

Within a few seconds the upload will complete and you will see the certificate in your list. If you wish to relate the same certificate to multiple subscriptions just repeat the steps above for each subscription. Note that relating the same certificate to multiple subscriptions is convenient, but somewhat like using the same password for multiple accounts. If someone gets a hold of the private portion of the certificate they would have access to all of the subscriptions.

![Management Certificates]({{ site.url }}/assets/upload-management-cer-3.png)

###Generate the private key

Create a private key file that matches your management certificate.

```
usage: bcbio_vm.py azure prepare pkey [-h] [--cert CERT] [-f]

optional arguments:
  -h, --help   show this help message and exit
  --cert CERT  The management certificate name. [default: managementCert.pem]
  -f, --force  Overwrite the management certificate if already exits.
```

We will use the default values.

```bash
~ $ bcbio_vm.py azure prepare pkey
```

The output for this command:

```
[INFO] Execution of command PrivateKey ends with success. (None)
[INFO] The private key was successfully generated.
```

###Create the elasticluster configuration file

Write Elasticluster configuration file with user information.

```
usage: bcbio_vm.py azure prepare ec-config [-h] [--econfig ECONFIG]

optional arguments:
  -h, --help         show this help message and exit
  --econfig ECONFIG  Elasticluster bcbio configuration file
```

We will use the default values.

```
~ $ bcbio_vm.py azure prepare ec-config
```

The output for this command.
```
[INFO] Execution of command ECConfig ends with success. (None)
[INFO] The elasticluster config was successfully generated.
```
