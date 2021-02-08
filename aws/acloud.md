1. what are the three ways to gain access to s3 cross account?
    1. iam role
    2. bucket policy
    3. acl
2. what is an organization?
    1. a parent entity that is made up of a root account, policies and OUs - should be used for consolidated billing purposes so you pay the least amount
3. what is an organizational unit?
    1. within an organization and a child of the root account, these can contain other accounts and can hold specific policies that apply to those child accounts
4. why would you want everything to bill up to the organization?
    1. by billing up to an organization you pay the least cost per unit because the more you use, the less you pay per unit
5. what needs to be enabled for cross region replication?
    1. versioning on the target bucket
6. does cross region replication replicate objects existing in source when it is turned on
    1. No - only objects moving forward
7. for cross region replication, do the public permissions replicate to the destination?
    1. No - must be made public individually
8. what are multi-part upload and multi-part download?
    1. multi-part upload and multi-part download allow for increased efficiency when uploading and downloading files because small parts can be processed asynchronously. You can also fetch specific ranges of file bytes if there is a failure
9. what is s3 transfer acceleration?
    1. transfer acceleration leverages aws edge locations by allowing users to upload to the closest location and then processing the rest on the backbone of aws, which increases upload speed
10. what does aws data sync allow you to do?
    1. data sync allows you to transfer a large amount files from on-prem to the cloud by using an aws agent
11. true or false: using more prefixes in s3 increase your requests per second?
    1. true because the requests per second limit is set per prefix eg. 1500 requests/sec/prefix
12. define governance and compliance mode for object locks
    1. governance mode allows users WITH SPECIFIC PERMISSIONS to edit/remove object locks before the retention period is up
    2. compliance mode doesn’t allow object lock edit/removal by anyone until the retention period is over
13. what is a delete marker?
    1. a delete marker is a flag that is placed on an object that has versioning turned on when it is “deleted” from s3
    2. to remove this delete marker and restore the last version, just delete the delete marker
14. true or false: you can delete individual versions of an s3 object
    1. true
15. true or false: if I make an object public and then publish a new version, the new one will be public too.
    1. false - each individual version needs to be made public
16. how many facilities can s3 standard sustain the loss of?
    1. 2 (it is replicated to at least 3 facilities)
17. write a sample url for an s3 bucket named docs-bucket in eu-west-1.
    1. https://docs-bucket.s3.amazonaws.com
    2. https://docs-bucket.eu-west-1.amazonaws.com
18. what does the phrase “read after write for puts of new objects and eventual consistency for overwrites and deletes” mean?
    1. you can read the NEW objects immediately after putting them on s3, but there is a potential small lag on put/delete operations of existing objects
19. what are the two cloudfront distribution types and what are they used for?
    1. Web distribution - self explanatory
    2. RTMP - used for media streaming - can’t use signed cookies on these
20. can you invalidate cloudfront cache? Is there a charge?
    1. yes and yes
21. draw a diagram of retrieving a cloudfront signed url/cookies
22. when would you use a cloudfront signed url vs a cookie?
    1. url for single object
    2. cookies for multiple objects
23. how does an s3 signed url differ from a cloudfront signed url?
    1. an s3 signed url is used to access s3 directly and holds the permissions of the user who created the url - while cloudfront signed url is used to access a single s3 object via cloudfront using an oai
24. true or false: num(edge locations) < num(availability zones)
    1. false
25. how does snowball edge differ from snowball?
    1. snowball edge has Compute within the snowball. This allows for Compute to be done “on the edge” like in a semi or airpane
26. what are the three types of gateways with storage gateway?
    1. file gateway
    2. volume gateway
    3. tape gateway
27. what is the difference between data sync and storage gateway?
    1. from my understanding data sync is used to do an initial transfer, with a cutover in sight, while storage gateway is used to give a different access method to s3, whether that be files via nfs, volumes via iscsi
28. what is the difference between stored volumes and cached volumes? (stored keeps all data locally and in s3, while cached only keeps most recent in local)
    1. cached volumes only retains recently received data locally, while stored volumes keeps all data locally
29. what does macie do to battle against the hacker/identity thief?
    1. macie scans s3 for PII
30. what are the four types of ec2 instance pricing?
    1. on demand - pay for what you use at full price
    2. reserved - contract an ec2 for a given duration of time (discounted)
    3. spot - like the stock market of ec2 instances - good for jobs that don’t need to be run right away
    4. dedicated host - good for licensing and/or pii requirements (you get a full physical server)
31. what are the three types of pricing models for reserved instances? (standard, convertible and scheduled)
    1. standard - pay for an ec2 level on a time duration contract at a discount, but can’t change instance type
    2. convertible - like standard, but you can change your instance type
    3. scheduled - reserved during a period of time - like in the morning
32. True or False: You are not charged for a partial hour if AWS terminates your spot instance, BUT you are charged for that partial hour if you terminate it.
    1. true
33. What do you need to ssh into an ec2 instance?
    1. key pair
34. True or False: You cannot encrypt a root volume for EC2.
    1. false
35. What is termination protection on an EC2?
    1. keeps the instance from being deleted, instead stopped
36. security groups are stateful, what does this mean?
    1. if the rule is allowed in it is allowed out
37. True or False: You cannot add a specific deny rule on a security group.
    1. true, everything is denied by default and you add rules to allow
38. What are the five ebs types and corresponding api names?
    1. general purpose - gp2
    2. provisioned iops - io1
    3. throughput optimized st1
    4. cold hdd - sc1
    5. magnetic - standard

