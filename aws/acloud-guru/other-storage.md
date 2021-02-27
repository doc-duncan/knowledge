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