---
last-updated: 2026-10-22
applies-to: SOA-C03 exam guide v1.1
---

# Domain 1 (part 2): Performance Optimization (Task 1.3)

This note covers **Task 1.3 - Implement performance optimization strategies for compute, storage, and database resources**. It is part of Domain 1, "Monitoring, Logging, Analysis, Remediation, and Performance Optimization" (**22%** of scored content). Tasks 1.1 and 1.2 are in [01 - Monitoring, Logging, Analysis, and Remediation](./01-monitoring-logging.md).

> **Scope note.** SOA-C02 had a separate cost and performance domain. SOA-C03 does not. Performance is Task 1.3 here, and **network cost** is Task 5.1.4 in [05 - Networking and Content Delivery](./05-networking.md#514-optimize-the-cost-of-network-architectures). The exam guide lists **analyzing costs and TCO** and **managing billing and invoicing** as out of scope, so Cost Explorer reports, Reserved Instance and Savings Plans purchase maths, and billing consoles are no longer study targets. What stays in scope is choosing the configuration that meets the performance need at sensible cost, for example moving `gp2` volumes to `gp3`, or using an S3 Lifecycle rule.

Performance questions follow a pattern: a metric shows a bottleneck, and you must pick the change that removes it with the least disruption. So for each resource type, learn **which metric reveals the bottleneck** and **which knob fixes it**.

---

## 1.3.1 Optimize compute resources and remediate performance problems

### Find the bottleneck first

Before resizing anything, confirm which resource is saturated. For EC2 that means `CPUUtilization` (standard), memory and disk (CloudWatch agent, see [note 01](./01-monitoring-logging.md#112-configure-and-manage-the-cloudwatch-agent-ec2-ecs-eks)), network (`NetworkIn`/`NetworkOut`, packets per second), and EBS metrics (1.3.2). A CPU-bound web tier and a memory-bound Java tier need different instance families, and a disk-bound database needs a different volume, not more vCPUs.

### AWS Compute Optimizer

**AWS Compute Optimizer** analyzes historical utilization metrics and recommends better-fitting configurations for **EC2 instances, Auto Scaling groups, EBS volumes, Lambda functions, ECS services on Fargate** and some other resource types. Each recommendation is classed as over-provisioned, under-provisioned or optimized, with a performance risk rating. By default it looks only at CloudWatch metrics it can see, so **memory** is only considered if the CloudWatch agent publishes it. Enabling **enhanced infrastructure metrics** extends the look-back period so monthly patterns are captured. It is an opt-in service and can be enabled for a whole organization.

### Use tags to find and act on resources

The exam guide mentions **resource tags** in this task for a practical reason: you optimize fleets, not single instances. Tags let you group resources in CloudWatch dashboards and Resource Groups, target Systems Manager Run Command and Automation at "every instance tagged `Tier=web`", filter Compute Optimizer findings by application, and drive Auto Scaling or scheduled start and stop of non-production instances by tag.

### Burstable instances (T family)

T instances earn **CPU credits** while below their baseline and spend them above it. Watch `CPUCreditBalance` and `CPUSurplusCreditBalance`. A T instance in **standard** mode that runs out of credits is throttled to its baseline, which looks like a mysterious slowdown hours into a busy period. Fixes: switch to **unlimited** mode (pay for surplus credits), or move to a fixed-performance family (M, C, R) if the load is sustained.

### Lambda performance

Lambda memory runs from 128 MB to 10,240 MB, and **CPU is allocated in proportion to memory**, so raising memory often makes a CPU-bound function both faster and cheaper per invocation. `Duration` close to the configured timeout means the function is starved or waiting on a slow dependency. **Provisioned concurrency** keeps execution environments initialized to remove cold-start latency for latency-sensitive functions; **reserved concurrency** caps (and guarantees) concurrency for one function so it neither starves others nor overwhelms a downstream database. `Throttles` mean you hit a concurrency limit.

### Containers

For ECS and EKS, look at Container Insights for CPU and memory per task or pod versus their reservations and limits. A task that is killed with exit code 137 has hit its memory limit. Right-sizing task definitions and using **service auto scaling** (Domain 2) is the remediation.

**[📖 What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)** - supported resources and findings
**[📖 Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)** - CPU credits, standard and unlimited modes
**[📖 Configuring Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)** - memory and CPU relationship
**[📖 Configuring provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)** - removing cold starts

---

## 1.3.2 Analyze EBS performance metrics and optimize volume types

### Volume types at a glance

| Type | Media | Performance model | Typical use |
|---|---|---|---|
| **gp3** | SSD | 3,000 IOPS and 125 MiB/s baseline included; provision more IOPS (up to 80,000) and throughput (up to 2,000 MiB/s) independently of size | Default for most workloads, boot volumes |
| **gp2** | SSD | IOPS scale with size (3 IOPS per GiB) and small volumes burst using a credit bucket | Legacy; migrate to gp3 |
| **io2 Block Express** | SSD | Provisioned IOPS, up to 256,000 IOPS, sub-millisecond latency | Latency-sensitive, I/O-intensive databases |
| **st1** | HDD | Throughput-optimized, burst on throughput | Big sequential reads: logs, data warehouses, streaming |
| **sc1** | HDD | Lowest cost, cold | Infrequently accessed sequential data |

HDD types cannot be boot volumes. The key performance-and-cost lesson is **gp2 to gp3**: gp3 costs less per GiB, does not use burst credits, and lets you buy IOPS without buying capacity you do not need. The change is made online with **Elastic Volumes** (modify type, size, IOPS or throughput without detaching), though there is a cooldown before you can modify the same volume again.

### Metrics that reveal the problem

- **`VolumeQueueLength`** - I/O requests waiting. A queue that stays high while latency rises means the volume (or instance) cannot keep up with demand.
- **`VolumeReadOps`/`VolumeWriteOps`** and **`VolumeReadBytes`/`VolumeWriteBytes`** - divide by the period to get IOPS and throughput, then compare to the volume's provisioned limits.
- **`BurstBalance`** (gp2, st1, sc1) - falling to zero explains a sudden drop in performance on a gp2 volume.
- **`VolumeIdleTime`** and the average latency metrics (total read/write time divided by operations).
- **Instance-level limits** - every instance type has its own maximum EBS bandwidth and IOPS. Smaller instances report `EBSIOBalance%` and `EBSByteBalance%` for burst. If the volume is under its limit but the instance is at its EBS limit, the fix is a larger or EBS-optimized instance, not a faster volume.

### Other EBS performance facts

- **Snapshots and initialization.** A volume created from a snapshot loads blocks from S3 lazily, so the first read of each block is slow. To avoid that, either read every block once (with `fio` or `dd`) before production use, or enable **Fast Snapshot Restore** on the snapshot in the target AZ so volumes are fully initialized at creation.
- **RAID 0** across several volumes adds their IOPS and throughput together, at the cost of losing everything if one volume fails. RAID 5 and 6 are not recommended on EBS.
- **EBS-optimized** instances (default on current generations) give EBS dedicated bandwidth.

**[📖 Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)** - comparison of all types
**[📖 General Purpose SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)** - gp3 limits and gp2 to gp3 migration
**[📖 Amazon EBS metrics in CloudWatch](https://docs.aws.amazon.com/ebs/latest/userguide/using_cloudwatch_ebs.html)** - volume metrics
**[📖 Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-initialize.html)** - first-read latency and Fast Snapshot Restore

---

## 1.3.3 Implement S3 performance strategies

**Request rates.** S3 scales automatically and supports at least 3,500 `PUT`/`COPY`/`POST`/`DELETE` and 5,500 `GET`/`HEAD` requests per second **per partitioned prefix**. Spreading objects across more prefixes raises total throughput. A burst of `503 Slow Down` errors means a prefix is being hit harder than S3 has scaled for yet; spread keys and retry with exponential backoff.

**Multipart upload.** Splits an object into parts that upload in parallel and can be retried individually. AWS recommends it for objects over 100 MB, and it is **required** above 5 GB (a single `PUT` is limited to 5 GB). The AWS CLI `s3 cp` and the SDK transfer managers use it automatically. Incomplete uploads leave billable parts behind, so add a Lifecycle rule to **abort incomplete multipart uploads** after a few days. For downloads, **byte-range fetches** pull parts of an object in parallel.

**S3 Transfer Acceleration.** Uploads go to the nearest CloudFront edge location and then travel over the AWS backbone to the bucket's Region. It helps when clients are geographically far from the bucket and upload large objects over the public internet. You enable it per bucket and use the `bucketname.s3-accelerate.amazonaws.com` endpoint. The bucket name must be DNS-compliant and must not contain periods. AWS provides a speed comparison tool to check whether it helps for a given location.

**AWS DataSync.** A managed online transfer service for moving large datasets between on-premises storage (NFS, SMB, HDFS, object storage), other clouds, and AWS storage (S3, EFS, FSx). It handles parallelism, encryption in transit, scheduling, bandwidth throttling and **data integrity verification**. Choose DataSync over scripts when the question says "recurring", "large", "verify" or "with minimal operational overhead". On-premises sources need a DataSync **agent** deployed near the data.

**S3 Lifecycle policies.** Rules on a bucket, prefix or tag that **transition** objects to cheaper storage classes (Standard-IA, One Zone-IA, Glacier tiers) after a number of days and **expire** current or noncurrent versions. They are also how you keep versioned buckets from growing forever. **S3 Intelligent-Tiering** moves objects between access tiers automatically when access patterns are unknown.

**[📖 Best practices design patterns: optimizing S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html)** - request rates and parallelization
**[📖 Uploading and copying objects using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)** - limits and behavior
**[📖 Configuring S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)** - requirements and endpoints
**[📖 What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)** - agents, locations, tasks
**[📖 Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)** - transitions and expiration

---

## 1.3.4 Evaluate and select shared storage, and optimize it

### Choosing a shared file system

| Need | Choose |
|---|---|
| Linux clients, NFS, elastic capacity, many instances or containers across AZs | **Amazon EFS** |
| Windows clients, SMB, Active Directory integration, NTFS permissions | **FSx for Windows File Server** |
| HPC or ML training needing very high throughput, optionally linked to an S3 bucket | **FSx for Lustre** |
| Multi-protocol (NFS and SMB, plus iSCSI) with NetApp features such as SnapMirror | **FSx for NetApp ONTAP** |
| ZFS features such as snapshots and clones, NFS | **FSx for OpenZFS** |
| File access to data that lives in an S3 bucket, without copying it | **Amazon S3 Files** |

### Amazon EFS and its lifecycle policies

EFS is a Regional, elastic NFS file system (One Zone file systems also exist for lower cost). Two settings decide performance:

- **Throughput mode** - **Elastic** (scales automatically with the workload and you pay for what you use; recommended for spiky or unknown patterns), **Provisioned** (you set throughput independent of storage size) or **Bursting** (throughput scales with the amount stored and uses burst credits). On a Bursting file system, a falling `BurstCreditBalance` explains slowdowns; switch to Elastic or Provisioned.
- **Performance mode** - **General Purpose** (lowest latency, recommended for almost everything) or **Max I/O** (legacy option for highly parallel workloads, with higher latency; not available with Elastic throughput or One Zone). Watch `PercentIOLimit` on General Purpose file systems.

**EFS lifecycle management** moves files that have not been accessed for a set number of days from **EFS Standard** to **EFS Infrequent Access (IA)** and then to **EFS Archive**, and can move them back to Standard on first access. This is the "optimize shared storage" answer when most files go cold after a few weeks.

### Amazon S3 Files

**S3 Files** (in scope from guide v1.1) is a shared file system linked to an S3 bucket or a prefix in it. It is built using Amazon EFS and gives compute resources (**EC2, Lambda, EKS and ECS**) file system access to S3 data, with full file system semantics, **without the data leaving S3**. Actively used file data and metadata are loaded onto a low-latency **high-performance storage** layer on demand; writes go there first and are synchronized back to the bucket, and changes made in the bucket are synchronized to the file system. Small files (below a configurable threshold, 128 KiB by default) are imported for low-latency reads, while large reads stream directly from S3. Data not read within a configurable window (1 to 365 days, default 30) expires from the high-performance layer; the authoritative copy always stays in S3. Compute connects through **mount targets** created in each Availability Zone of the chosen VPC.

Choose S3 Files when the data already lives in S3 and file-based tools or agents need to work on it; choose EFS when you want a general-purpose NFS file system whose data is not tied to a bucket; choose FSx for Lustre for the highest-throughput HPC scratch or S3-linked processing.

**[📖 Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)** - throughput and performance modes
**[📖 Managing EFS storage lifecycle](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)** - IA and Archive transitions
**[📖 Amazon FSx](https://aws.amazon.com/fsx/)** - the four FSx file systems
**[📖 Working with Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html)** - how S3 Files works

---

## 1.3.5 Monitor RDS metrics and modify configurations

### What to watch

Standard RDS CloudWatch metrics include `CPUUtilization`, `FreeableMemory`, `SwapUsage`, `FreeStorageSpace`, `DatabaseConnections`, `ReadIOPS`/`WriteIOPS`, `ReadLatency`/`WriteLatency`, `DiskQueueDepth` and, for replicas, `ReplicaLag`. Alarm on low `FreeStorageSpace` (or turn on **storage autoscaling**), rising `ReplicaLag`, and `DatabaseConnections` approaching the engine's connection limit.

**Enhanced Monitoring** adds operating-system metrics (per-process CPU and memory, file system, swap) from an agent on the DB host, at intervals as short as one second, delivered to CloudWatch Logs. Use it when you need to know what is happening on the host rather than inside the database engine.

### Performance Insights and CloudWatch Database Insights

**Performance Insights** shows **database load** (average active sessions) broken down by **wait events, SQL statements, hosts and users**, so you can see that, for example, one query waiting on I/O is the cause of a CPU spike. AWS now delivers this capability as **Amazon CloudWatch Database Insights**, which consolidates database metrics, logs and the Performance Insights load analysis into CloudWatch, with a Standard and an Advanced mode. Expect exam questions to say either name.

**Proactive recommendations** are generated when metric values cross automatically determined thresholds, before they turn into an outage, for example sustained high load or a configuration likely to cause problems, each with a suggested action. RDS shows them on the Recommendations page of the console.

### Configuration changes that fix common problems

- **Too many connections, especially from Lambda** - put **RDS Proxy** in front of the database. It pools and shares connections, reduces failover time by holding client connections while the writer changes, and can enforce IAM authentication with credentials stored in Secrets Manager.
- **Read-heavy load** - add **read replicas** and point read traffic at them (or the Aurora reader endpoint).
- **CPU or memory bound** - change the **DB instance class** (a short outage on Single-AZ; on Multi-AZ the standby is modified first, then a failover).
- **Engine parameters** - change a custom **DB parameter group**. **Dynamic** parameters apply immediately; **static** parameters need a reboot, and the instance shows `pending-reboot` until then. You cannot edit the default parameter group.
- **Storage** - increase allocated storage or IOPS, or move to a faster storage type.

**[📖 Monitoring metrics in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)** - CloudWatch, Enhanced Monitoring, Database Insights
**[📖 Overview of Database Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.html)** - database load and pricing
**[📖 Recommendations from Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)** - proactive recommendations
**[📖 Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)** - connection pooling and failover
**[📖 Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)** - static and dynamic parameters

---

## 1.3.6 Implement, monitor and optimize EC2 instances, storage and networking

### Placement groups

| Strategy | What it does | Use it for |
|---|---|---|
| **Cluster** | Packs instances close together in one AZ for low latency and high per-flow throughput | HPC, tightly coupled jobs |
| **Spread** | Places each instance on distinct hardware; at most seven running instances per AZ per group | A small number of critical instances that must not share a failure |
| **Partition** | Divides instances into partitions that do not share racks; up to seven partitions per AZ | Large distributed systems such as HDFS, Cassandra, Kafka |

An `InsufficientInstanceCapacity` error when adding to a cluster placement group means AWS cannot find room on the same hardware. The usual fix is to stop and start all instances in the group (so they are placed together again) or launch all needed instances in one request, using the same instance type.

### Networking performance

- **Enhanced networking** with the **Elastic Network Adapter (ENA)** gives higher bandwidth, higher packets per second and lower latency; it is supported on current generation instances. The **Elastic Fabric Adapter (EFA)** adds OS-bypass for HPC and ML workloads that use MPI or NCCL.
- Network bandwidth scales with instance size; the "up to" figures are burst limits. Sustained traffic needs an instance with that baseline.
- **Jumbo frames** (MTU 9001) work inside a VPC, but traffic over an internet gateway, and across most VPN and inter-Region paths, is limited to 1500 bytes. Mismatched MTU shows up as connections that open but stall on large transfers.

### Storage attached to instances

**Instance store** volumes are physically attached NVMe or SSD disks with very high IOPS, but their data is lost when the instance stops, hibernates or terminates. Use them for caches, buffers and scratch data. Use EBS (1.3.2) for anything that must persist. Pick EBS-optimized instances with enough EBS bandwidth for the volumes attached.

**[📖 Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)** - cluster, spread and partition rules
**[📖 Enhanced networking on EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)** - ENA and EFA
**[📖 Network MTU for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html)** - jumbo frames
**[📖 Instance store temporary block storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)** - lifecycle of instance store data

---

## Key takeaways

1. **Measure first.** Pick the fix that matches the saturated resource: CPU, memory, disk queue, network or connections.
2. **Compute Optimizer** recommends right-sizing for EC2, ASGs, EBS, Lambda and Fargate; memory needs the CloudWatch agent.
3. **gp3 over gp2**: lower cost, no burst credits, IOPS and throughput set independently. Change it online with Elastic Volumes.
4. **Check the instance's EBS limit** before blaming the volume.
5. **S3**: multipart over 100 MB (required over 5 GB), Transfer Acceleration for long-distance uploads, DataSync for large or recurring transfers, Lifecycle rules for tiering and cleanup.
6. **EFS**: Elastic throughput for unknown patterns; lifecycle to IA and Archive for cold files. **S3 Files** for file access to data in S3.
7. **RDS**: Performance Insights (now CloudWatch Database Insights) for wait events and top SQL; RDS Proxy for connection storms; static parameters need a reboot.
8. **Placement groups**: cluster for latency, spread for isolation of a few critical instances, partition for big distributed systems.
9. **Billing, TCO and cost analysis are out of scope**; network cost (5.1.4) is in scope and lives in note 05.

## Key terms

- **AWS Compute Optimizer** - recommends right-sized EC2, Auto Scaling, EBS, Lambda and Fargate configurations from utilization history
- **CPU credits** - what T-family burstable instances earn below baseline and spend above it; standard mode throttles at zero balance
- **gp3** - General Purpose SSD with 3,000 IOPS and 125 MiB/s baseline, where IOPS and throughput are provisioned independently of size
- **VolumeQueueLength** - EBS metric of I/O requests waiting; persistently high values signal the volume cannot keep up
- **Elastic Volumes** - modify an EBS volume's type, size, IOPS or throughput while it stays attached and in use
- **Fast Snapshot Restore** - makes volumes created from a snapshot fully initialized at creation, removing first-read latency
- **Multipart upload** - parallel, retryable upload of an object in parts; recommended over 100 MB and required over 5 GB
- **S3 Transfer Acceleration** - routes uploads through CloudFront edge locations and the AWS backbone to a distant bucket
- **AWS DataSync** - managed online transfer service with scheduling, encryption and integrity verification between storage systems
- **EFS lifecycle management** - moves files not accessed for a set number of days from Standard to Infrequent Access and then Archive
- **Amazon S3 Files** - shared file system linked to an S3 bucket that gives EC2, Lambda, EKS and ECS file access without moving data out of S3
- **Performance Insights** - RDS database load analysis by wait events, SQL, hosts and users; now delivered as CloudWatch Database Insights
- **RDS Proxy** - managed connection pool in front of RDS or Aurora that absorbs connection storms and speeds failover
- **Cluster placement group** - packs instances close together in one AZ for low latency and high network throughput
- **Spread placement group** - places each instance on distinct hardware, at most seven running instances per AZ per group

## Vendor documentation

**[📖 SOA-C03 Domain 1 in the exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03-domain1.html)** - official task statements for 1.3
**[📖 AWS Well-Architected Performance Efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)** - selection and monitoring principles
**[📖 Amazon EC2 instance types](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)** - families and limits
