---
layout: page
title: "Install bcbio-nextgen-vm"
category: doc
date: 2015-11-06 12:00:00
---

###II.1. Add conda channel

There are two versions of *bcbio-nextgen-vm* available, the stable (on **bcbio** channel) one and the develop one (on **bcbio-dev** channel). 

For bcbio-nextgen-vm stable version we will add only the **bcbio** channel.

```
~ $ conda config --add channels bcbio
```

And for the development version we will need the both channels.

```
~ $ conda config --add channels bcbio
~ $ conda config --add channels bcbio-dev
```

###II.2. Install bcbio-nextgen-vm package

```
~ $ conda install --yes bcbio-nextgen-vm
```