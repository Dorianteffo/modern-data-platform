## Prerequisites

Before pushing the code, we need to create two schema in the RDS database : 
* test 
* app 


The python code will run every 5 hours and load 500 new rows to the tables.

Run `make generate-data`in the EC2 instance