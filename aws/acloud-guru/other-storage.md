## Other Storage

### Snowball
1. How does Snowball Edge differ from basic Snowball?
    1. Snowball Edge has compute built into it. Basic Snowball is simply a storage transport/container. Snowball Edge is great if you don't have internet connectivity (in a plane, on a bus...etc.)

### Storage Gateway
1. What are the three types of Storage Gateway?
    1. File Gateway
    2. Volume Gateway
    3. Tape Gateway
2. What is the difference between stored volumes and cached volumes?
    1. Stored volumes keep all of the data locally and asynchronously backup snapshots to S3.
    2. Cached volumes only keep a cache locally and the base data and snapshots live in AWS.

### EBS
1. What are the five ebs types and corresponding api names?
    1. general purpose (ssd) - gp2
    2. provisioned iops (ssd) - io1
    3. throughput optimized (hdd) - st1
    4. cold hdd (hdd) - sc1
    5. magnetic (prev gen hdd) - standard
2. True or False: You cannot encrypt a root volume for EC2.
    1. false
3. What is a snapshot of EBS?
    1. A snapshot is a copy of a volume that represents state at a certain time. EC2 instances can be created from these snapshots then.
4. How would you encrypt a root device volume that has already been created with the "unencrypted" option.
    1. create a snapshot
    2. create a copy of the snapshot that is encrypted
    3. create an ami from the copy to then deploy from
5. True or False: you cannot share encrypted snapshots and make them public.
    1. True, these must be unencrypted

### EFS and FSx
1. How does EFS differ from EBS?
    1. EBS is 1:1 with Ec2 instances while EFS is 1:many
    2. EFS grows dynamically, you don't have to allocate storage on start
2. When using EFS, what do you have to do to enable traffic between EC2 and the file system?
    1. Allow NFS traffic from the EC2 SG to the EFS SG.
3. What is the main difference between EFS and Windows FSx?
    1. EFS is only for unix/linux, while Windows FSx integrates with Windows, AD, Securtity etc.
    2. EFS uses NFS while FSx uses SMB protocol
4. True or False: FSx for for Lustre is only for Windows.
    1. False - it is not exclusive to Windows and is used for high performance throughput
5. True or False: You can modify EBS volumes on the fly, size and type.
    1. True