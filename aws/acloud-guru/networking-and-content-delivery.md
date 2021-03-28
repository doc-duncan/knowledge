## Networking and Content Delivery


### CloudFront
1. What are the two types of CloudFront distributions and what are they used for?
    1. Web - used for basic web content
    2. RTMP - used for streaming
2. What is invalidating the CloudFront cache and is it free?
    1. Invalidating the cache pushes new changes to the CloudFront cache. There is a small fee for invalidating.
3. When would you use a CloudFront cookie vs. a signed url.
    1. A cookie should be used for accessing multiple objects.
    2. A signed url should be used for a single object.
4. What can't you use with an RTMP distribution?
    1. cookies
5. Draw a diagram showing the retrieval of a CloudFront signed url or cookie.
    ![cloudfront-url-cookies](/aws/acloud-guru/img/cloudfront-url-cookies.jpg)

### Route 53
1. What is simple routing in route 53?
    1. This is where you have an A record pointing to multiple IP Addresses and Route53 simply returns the list in random order.
2. What does weighted routing in route 53 do?
    1. Allows you to assign weights to multiple A records that use the weights to determine frequency of routing to the designated IPv4 addresses.
3. What is latency based routing?
    1. Allows you to route traffic along the lowest latency path.

### VPC
1. What is the difference between ENI, ENA, VF and EFA?
    1. ENI is elastic networking interface, which is essentially a virtual network card - giving you addresses
    2. ENA is elastic networking adapter and allows for enhanced throuput in contrast to the ENI, supports up to 100 gbps
    3. 82599 Virtual Function is also enhanced networking like ENA, but only supports up to 10gbps (this is used for older instance types and usually you should choose ENA over this).
    4. EFA is elastic fabric adapter and is used to increase throughput for HPC and machine learning. It also includes OS-bypass where workloads can bypass the OS kernel and speak directly to the EFA device, therefore decreasing latancy.
2. True or False: **Custom** NACLs deny everything by default
    1. True
3. How many NACLs can a subnet be associated with?
    1. One
4. How many subnets can a NACL be associated with?
    1. Many
5. What resources are created by default when you create a custom VPC?
    1. NACL
    2. SG
    3. Route Table
6. True or False: You can have up to 3 internet gateways associated with a VPC.
    1. False, only one
7. How many AZs can a subnet span?
    1. Only one
8. Which rule has the highest precedence in a NACL.
    1. The lowest
9. What does a VPC endpoint allow you to do?
    1. A VPC endpoint is a private connection to AWS services within a VPC. You do not have to leave the AWS network to reach services like S3, Dynamo and more.
10. True or False: Data transfer using private IPs over the AWS backbone network in the same AZ is free.
    1. True

### Load Balancers
1. What is the minimum number of subnets that an ELB must reside in?
    1. Two
2. What are the three types of load balancers and what layer does each operate at?
    1. Application Load Balancer - layer 7
    2. Network Load Balancer - layer 4
    3. Classic Load Balancer - layer 7
3. What is the X-Forwarded-For header used for in relation to ELBs?
    1. Forwards the clients IP to the instance that was load balanced to (without the X-Forwarded-For header the instance would receive the IP of the load balancer)
4. What is cross zone load balancing?
    1. Cross zone load balancing is where a load balancer can route traffic to targets across availability zones.

### Global Accelerator
1. Whats is Global Accelerator?
    1. Global Accelerator is a service that allows users to traverse the AWS backbone network to reach specific endpoints. Users enter the network via edge locations and then are quickly routed to target endpoint groups.
2. True or False: You get a dedicated IPv4 address on an ELB.
    1. False


### Connectivity
1. What should you use if you want to connect your VPC to tens, hundreds or even thousands of customer VPCs?
    1. VPC PrivateLink
2. What is Transit Gateway?
    1. Transit Gateway is a way of simplifying your network architecture. It is a hub and spoke model that allows transitive peering of multipe VPCs. You connect to the transit gateway and therefore can connect to everything peered with it.
3. What is VPN CloudHub?
    1. VPN CloudHub is a service that is also a hub and spoke model, but allows you to easily join multiple VPNs using a virtual private gateway as the single point for connection.

### WAF
22. What is a WAF?
    1. A WAF is a layer 7 firewall that therefore operates at the application layer. It can act on query params, ip addresses, country origin, request headers, sql injection code, and xss scripting code
23. Can you block a specific IP using a WAF?
    1. Yes

