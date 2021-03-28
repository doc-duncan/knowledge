## Security, Identity and Compliance


### Security Groups
1. security groups are stateful, what does this mean?
    1. If traffic is allowed in then the reply traffic is allowed back out, and vice versa.
2. True or False: You cannot add a specific deny rule on a security group.
    1. True, everything is denied by default and you add rules to allow

### AD
1. What are the three MS AD services provided and what do they do?
    1. Microsoft Managed AD - Full AD in AWS with high availability and trust capability
    2. Simple AD - small scale, no trust AD
    3. AD connector - hook into on-prem AD using supported AWS services

### IAM
1. What does a permissions boundary do?
    1. sets a cap on permissions regardless of the policy. For example if there is an IAM user that has admin access, you can set a permissions boundary on that user that scopes it down to S3 star for example.

### Resource Access Manager
1. True or False: You can use AWS Resource Access Manager to share EC2 instances cross account.
    1. True

### CoudHSM
1. What is CloudHSM?
    1. A single tenant, dedicated hardware, multi-AZ security module that has industry-standard APIs to store keys.

### Cognito
1. What is the difference between a cognito user pool and identity pool?
    1. The user pool is used to hold user login information and data. The identity pool deals with the actual granting of aws permissions.