## Databases


### Overarching
1. Out of multi-az and read replicas, which is for performance and which is for disaster recovery?
    1. multi-az is for disaster recovery
    2. read replicas are for performance
2. what is the difference between oltp (online transaction processing) and olap (online analytics processing)?
    1. oltp is used for simple targeted queries, which should be used for your website for example
    2. olap is used for complex analytical queries, like a report needed by management
3. What is the difference between db automatic backups and snapshots?
    1. automatic backups occur during a defined window and you can restore a db down to a second in time using the backup and the transaction logs together
    2. snapshots are manual backups done by the user and stored in s3
4. True or False: You can have a read replica in a second region
    1. True
5. What must be enabled for read replica functionality?
    1. automatic backups
6. True or False: You cannot make a read replica multi-az
    1. False
7. What is Database Migration Service (DMS)?
    1. DMS is a tool that helps you migrate from one DB to another, often a good use case for on-prem to cloud. It is essentially an application that runs on an EC2, takes a source and target table config and pulls from the source to populate the destination.


### RDS
1. True or False: You can SSH into an RDS instance
    1. False

### DynamoDB
1. What is the difference between eventual consistent reads and strong consistent reads for dynamo?
    1. It all comes down to the 1 second rule. If your application doesn't need accurate reads of newly put data under a second then eventual consistent reads are acceptable. However, if that put data needs to be read immediately after under 1 second then strong consistent reads are necessary.
2. What are global tables and why do streas need to be on to enable them?
    1. Global tables are DynamoDBs cross region replication mechanism and they leverage dynamo streams, which is a stream of transaction logs performed on the db, to create the replication.
3. What does fine grained access do for dynamodb?
    1. Restricts reads of items to specific attributes. (column level security)
4. What is elasticache?
    1. Offloads common queries and results to a cache for quicker read response
5. How does DynamoDB Accelerator (DAX) decrease read and write time?
    1. DAX is a cache that sits between your application and DynamoDB and by the nature of a cache, decreases the read and write time.
6. How do DynamoDB transactions assist in business logic fulfillment?
    1. They allow for "all-or-nothing" requests, for example, in financial transactions you can't debit an account without crediting another.


### Redshift
1. How many Availability Zones is redshift available in?
    1. 1


### Aurora
1. How many copies of your data does Aurora store?
    1. 2 copies per AZ with a minimum of 3 AZs, so 6 copies
2. True or False: RDS, Redshift and Aurora all have automated backups on by default.
    1. True
3. What would you use Aurora Serverless for?
    1. POCing an idea where you don't know how many requests or what type of requests you are going to be getting
