## Analytics

### EMR
1. What are the three types of EMR nodes and their purposes?
    1. master node - orchestrates other nodes and holds logs
    2. core node - performs tasks and does write to HDFS (Hadoop File System)
    3. task node - performs tasks but does not write to HDFS (Hadoop File System)

### Kinesis
1. What is the difference between kinesis streams and kinesis firehose?
    1. Kinesis streams has shards that persist your data, while the data in firehose has to be dealt with on the spot.
2. What is kinesis analytics?
    1. Kinesis analytics sits on top of either firehose or streams and analyzes the data in real time and can output it to a persistent storage.