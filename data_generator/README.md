## Prerequisites

To connect to the database, you can use DBEAVER, and the RDS is in the private subnets, you will need to specify the SSH Tunnel (EC2 instance in a public subnet in the same VPC)
Before pushing the code, we need to create this schema in the database: 
* app 


The python code will run every 2 hours and load 100 new rows to the tables.
