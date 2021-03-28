## Storage

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
6. What does incremental mean when talking about EBS snapshots?
    1. Snapshots are increental - meaning after the initial snapshot, only the changs are recorded if new snapshots are made
7. What is the difference between AMI EBS volume backed vs. instance store backed volumes?
    1. Instance store is ephemeral - you cannot "stop" an instance that is backed by instance store and if something goes wrong with the underlying host you will lose all of your data
    2. All instance store volumes have to be added on launch, while EBS volumes can be added whenever
    3. instance store can scale to millions of IOPS where EBS can only go to 64,000 IOPS with provisioned IOPS

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

### S3
1. What are the three ways to gain/restrict access to an S3 bucket?
    1. IAM role
    2. Bucket policy
    3. ACL
2. What needs to be enabled for cross-region replication?
    1. Versioning on both source and destination
3. When cross-region replication is turned on do the existing objects get replicated?
    1. No - only objects moving forward
4. Do public permissions transfer during cross-region replication?
    1. No - each object must be made public
5. What is multi-part upload and download?
    1. Multi-part upload and download assist in moving large objects to and from S3. Multi-part upload allows for individual chunks to be uploaded asynchronously. When using Multi-part download, you can fetch specific chunks using a header in the request.
6. At what file size do you need to use multi-part upload?
    1. 5gb
7. What is transfer acceleration?
    1. Transfer accelertation is used to speed up the uploading of s3 objects by using edge locations. A customer uploads an object to CloudFront and then the object traverses the AWS backbone network to reach its final destination.
8. How does using more prefixes increase your requests per second?
    1. The requests per second limit is set on a prefix. For example, lets say you get 2500 requests per second on the prefix aws/docs. By splitting your data into aws/docs1 and aws/docs2 you can get a total of 5000 requests per second between those two prefixes vs. all data under a single prefix.
9. What is the difference between governance mode and compliance mode for object locks?
    1. Governance mode allows some privelaged users to work around the object lock prior to the fulfillment of the retention period.
    2. Compliance mode keeps the object lock regardless of privelages for the entire retention period.
10. What is a delete marker?
    1. A delete marker is placed on an object with versioning enabled when it is "deleted". The data itself is not actually deleted and the delete marker can be deleted to recover the object.
11. True or False: You can delete individual versions of an S3 object permanently.
    1. True - by deleting an object version that data is permanently gone
12. What is the "public status" of a new uploaded version of an object if the previous version was public?
    1. The new version is not public by default. You need to enable public access manually.
13. How many facilities can S3 standard withstand the loss of?
    1. S3 standard can withstand the loss of 2 facilities because the data is copied to at least 3.
14. What are the two options for an s3 url for a bucket named docs-bucket in us-east-1?
    1. http://docs-bucket.s3.amazonaws.com
    2. http://s3.amazonaws.com/docs-bucket
15. What is the S3 consistency model?
    1. There is strong read-after-write consistency for all DELETES and PUTS of both new and existing objects.
16. What does it mean that updates to a key are atomic?
    1. If you try and concurrently to a PUT and a GET on a key you will either receive the new object or the old object, but never partial data.
17. What is an S3 url?
    1. An S3 url is an endpoint that grants temporary read or write privelages to users. The endpoint permissions are received from the user who creats the url.
18. What does macie do to thwart malicious attackers?
    1. Macie uses machine learning to detect PII in S3 buckets.