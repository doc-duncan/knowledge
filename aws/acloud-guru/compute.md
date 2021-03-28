## Compute


### EC2/EBS
1. what are the four types of ec2 instance pricing?
    1. on demand - pay for what you use at full price
    2. reserved - contract an ec2 for a given duration of time (discounted)
    3. spot - like the stock market of ec2 instances - good for jobs that don’t need to be run right away
    4. dedicated host - good for licensing and/or pii requirements because you get a full physical server
2. what are the three types of pricing models for reserved instances?
    1. standard - pay for an ec2 level on a time duration contract at a discount, but can’t change instance type
    2. convertible - like standard, but you can change your instance type
    3. scheduled - reserved during a period of time - like in the morning
3. True or False: You are not charged for a partial hour if AWS terminates your spot instance, BUT you are charged for that partial hour if you terminate it.
    1. true
4. What do you need to ssh into an ec2 instance?
    1. key pair
5. What is termination protection on an EC2?
    1. keeps the instance from being deleted, instead it is stopped
6. True or False: An EC2 instance and its volume are always in the same availability zone.
    1. true
7. How would you move an EC2 and volume to another AZ?
    1. Create a snapshot and then deploy from that to the new AZ
8. True or False: Any instance coming from an encrypted image must also be encrypted by default.
    1. True, since the base is encrypted the instance must be as well
9. What is the difference between one-time and persistent spot instances?
    1. one time spot instances will deploy and then terminate when the price exceeds your limit and will not deploy again
    2. persistent spot instances will redeploy after termination when the price falls within your limits again
10. What are spot blocks and spot fleets?
    1. spot blocks put a block on terminating spot instances when the price exceeds your maximum
    2. spot fleets are groups of spot instances and optional on-demand instances
11. How is Ec2 hibernation mode related to RAM and why is it beneficial?
    1. Ec2 hibernation puts the memory in ram into ebs when it "hibernates" this lends itself to quick boot times
12. What does this command do when run from an ec2 instance? curl http://169.254.169.254/meta-data/local-ipv4
    1. fetches the instance's private ipv4 address
13. What is the difference between clustered, spread and partitioned placement groups?
    1. clustered placement group puts the instances very close together from a hardware viewpoint. This leads to low latency.
    2. spread placement groups puts individual instances on individual server racks that are not dependent on the same power/networking. This allows for critical apps to be more resilient.
    3. partitioned placement groups are similar to both spread and clustered. This strategy creates groupings of instances on individual racks. This is good for critical clustered applications.
14. True or False: Spread and partition placement groups cannot span across multiple AZs, but clustered groups can.
    1. False - reverse it
15. True or False: You directly connect a role to an EC2 instance
    1. False - you attach an instance profile (this is done under the covers in the console)