## Management and Governance


### Organization
1. What is an Organization?
    1. A top level entity that is composed of a root account, OUs and child accounts. The billing for all accounts in an org should be consolidated to get the best price on resources.
2. What is an Organization Unit?
    1. An OU is a child entity to an Organization. Comparisons can be draw from an OU to a company's departments (HR, Finance...). An OU can hold policies that apply to all child acounts in it.

### Cloudwatch and Cloudtrail
1. What is the difference between cloudwatch and cloudtrail?
    1. cloudwatch monitors performance metrics and insight into resources while cloudtrail monitors api calls and interactions with all resources

### SSM Parameter Store
1. What is SSM Parameter Store hierarchy structure?
    1. The hierarchy structure of SSM Parameter Store allows you to organize the logical relationships between parameters and give users access to different levels of the hierarchy for parameter access.
2. What are the main functionality differences between SSM Parameter Store and Secrets Manager?
    1. Automatically rotate secrets
    2. Generate random secrets via API

### Misc.
1. Which is greater, the number of edge locations or the number of availability zones?
    1. The number of edge locations is larger.
2. What are the four services that enable caching in AWS?
    1. DynamoDB Accelerator 
    2. Elasticache
    3. Cloudfront
    4. API Gateway
3. What is the template for an arn?
    1. arn:aws:service:region:account:resource