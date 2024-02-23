hadoop jar '/home/hdoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar' -files /home/hdoop/210968016_BDA/Week2/textmapperW2.py#textmapperW2.py,/home/hdoop/210968016_BDA/Week2/textreducerW2.py#textreducerW2.py -mapper 'python3 textmapperW2.py' -reducer 'python3 textreducerW2.py' -input  /210968016_BDA/input.txt -output /210968016_BDA/output
* cat input.txt |python3 mapper.py 
* cat input.txt |python3 mapper.py|sort|python3 reducer.py 
* hadoop jar '/home/hdoop/hadoop/share/hadoop/tools/lib/hadoop
streaming-3.3.6.jar' -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py 
input /bda1/input.txt -output /bda1/oup1
* hdfs dfs -cat /bda1/oup1/part-00000
* hdfs dfs -get /bda/output/part-00000 /home/hdoop
* Cat part-0000

* all commands should run in master

**batch mode

-->Pig -x local myfile.Pig


input, outputs files should be  in master

-->Pig -x mapreduce myfile.pig

 here input output files are in hdfs

 pig file should be in master

**interactive Mode (grunt)

-->Pig -x local  (local)


-->pig (hdfs)


file path same as batch mode

Hdfs Basic File Operations:
1.File Upload:
hadoop fs -put <localsource> <hdfsdestination>
hdfs dfs -put <localsource> <hdfsdestination>

2.File Download:
hadoop fs -get <hdfssource> <localdestination>
hdfs dfs -get <hdfssource> <localdestination>

3.File Listing:
hadoop fs -ls <hdfslocation>
hdfs dfs -ls <hdfslocation>

4.File Deletion:
hadoop fs -rm <hdfsfile>
hdfs dfs -rm <hdfsfile>

5.File Moving/Renaming:
hadoop fs -mv <hdfsoldpath> <hdfsnewpath>
hdfs dfs -mv <hdfsoldpath> <hdfsnewpath>

6.File Copying:
hadoop fs -cp <hdfsfile> <hdfsdestination>
hdfs dfs -cp <hdfsfile> <hdfsdestination>
Advanced File Operations:

7.Changing File Permissions:
hadoop fs -chmod <permissions> <hdfsfile>
hdfs dfs -chmod <permissions> <hdfsfile>


8.Changing File Ownership:
hadoop fs -chown <owner:group> <hdfsfile>
hdfs dfs -chown <owner:group> <hdfsfile>

9.File Block Size Alteration:
hadoop fs -Ddfs.block.size=<blocksize> -put <localsource> <hdfsdestination>
hdfs dfs -Ddfs.block.size=<blocksize> -put <localsource> <hdfsdestination>

10.Appending to Files (Hadoop 3.x and above):
hdfs dfs -appendToFile <localsource> <hdfsfile>
hdfs dfs -appendToFile <localsource> <hdfsfile>

11.Checksum Calculation:
hadoop fs -checksum <hdfsfile>
hdfs dfs -checksum <hdfsfile>

12.File Concatenation:
hadoop fs -concat <src1> <src2> <dst>
hdfs dfs -concat <src1> <src2> <dst>


Extended File Operations:
File Compression/Decompression:
hadoop fs -gzip <hdfsfile>
hadoop fs -gunzip <hdfsfile>

File Checksum Comparison:
hadoop fs -compareChecksum <hdfsfile1> <hdfsfile2>
hadoop fs -diff <hdfsfile1> <hdfsfile2>


File Content Summary:
hadoop fs -du -s -h <hdfslocation>
hadoop fs -count -q -h <hdfslocation>

File Block Location Information:
hadoop fsck <hdfsfile> -files -blocks -locations

File Replication Factor Modification:
hadoop fs -setrep -R <replicationfactor> <hdfslocation>
hadoop fs -setrep -w <replicationfactor> <hdfslocation>

File Snapshot Creation and Management:
hadoop fs -createSnapshot <hdfslocation> <snapshotname>
hadoop fs -deleteSnapshot <hdfslocation> <snapshotname>
hadoop fs -renameSnapshot <hdfslocation> <oldsnapshotname> <newsnapshotname>


File Encryption/Decryption (when encryption is enabled):
hadoop key create <keyname>
hadoop fs -encrypt -keyName <keyname> <hdfsfile>
hadoop fs -decrypt <hdfsfile>


B)	Interacting with HDFS using command line interface to understand the basic working structure of Hadoop cluster.
List contents of a directory: 
Change current working directory: 
View the current working directory:
File Operations:
Copy files/directories from local file system to HDFS:
Copy files/directories from HDFS to local file system:
Remove files/directories from HDFS:
Rename files/directories in HDFS:

3. File System Information:
Get file information such as replication, block size, owner, etc.:
Check disk usage of files/directories:
Check integrity of the file system:

Admin Operations:
Change replication factor of a file: 
View and modify HDFS quotas:
Check cluster health and status:

Additional File Operations:
1. Appending to Files (Hadoop 3.x and above):
•	Append content to a file in HDFS:
hdfs dfs -appendToFile <local-source> <hdfs-destination> 
2. Concatenating Files:
•	Concatenate multiple files into a single file in HDFS:
hdfs dfs -getmerge <hdfs-source> <local-destination> 
3. File Content Summary:
•	Get a summary of directory sizes and their contents:
hdfs dfs -du [-h] <path> 
4. File Block Manipulation:
•	Get information about blocks in a file:
hdfs fsck <hdfs-file> -files -blocks -locations 
•	Force an immediate block replication of a file:
hdfs dfs -setrep -R <replication-factor> <hdfs-file> 
5. File Checksum Operations:
•	Calculate checksum of a file in HDFS:
hdfs dfs -checksum <hdfs-file> 
•	Compare checksums of two files:
hdfs dfs -compareChecksum <hdfs-file1> <hdfs-file2> 
6. File Encryption/Decryption (when encryption is enabled):
•	Create a new key for encryption:
hdfs crypto -createZone -keyName <key-name> -path <path> 
•	Encrypt a file:
hdfs crypto -encrypt -keyName <key-name> <hdfs-file> 
•	Decrypt a file:
hdfs crypto -decrypt <hdfs-file>




