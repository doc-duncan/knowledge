## Application Integration


### SQS
1. What is the maximum time a message can be in SQS?
    1. 14 days

### SWF
1. What is SWF?
    1. Simple Workflow Service is a service that coordinates work between a computer and a human. Amazon uses this in their warehouse to coordinate order processing.

### Kinesis
1. What is the difference between kinesis streams and kinesis firehose?
    1. Kinesis streams has shards that persist your data, while the data in firehose has to be dealt with on the spot.
2. What is kinesis analytics?
    1. Kinesis analytics sits on top of either firehose or streams and analyzes the data in real time and can output it to a persistent storage.