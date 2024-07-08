# Database Setup Instructions

## Prerequisites
Before downloading, ensure you have the following installed on your devices:
- [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [SQL](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

## Step 1: Download Necessary Files
Download all the necessary files, including the `admin_information.sql` file.

## Step 2: Update Database Connection
In the `database.py` file, connect it to your MySQL Workbench by updating the connection information as shown below:

![Database Connection](img/img.png)

MAKE SURE TO CHANGE THE NECESSARY DETAILS SUCH AS THE HOST!!!!

## Step 3: Create Tables in MySQL Workbench
Here are the table settings for your MySQL Workbench:

### Admin Table
![Admin Table](img/img_1.png)

### Player Table
![Player Table](img/img_2.png)
![Player Table](img/img_3.png)

### Role Table
![Role Table](img/img_4.png)

### Team Table
![Team Table](img/img_5.png)
![Team Table](img/img_6.png)

### Coach Table
![Coach Table](img/img_7.png)

### Player Performance Table
![Player Performance Table](img/img_8.png)
![Player Performance Table](img/img_9.png)

## Step 4: Insert Values in the Database
When inserting values into the database, follow this order:
1. Role
2. Coach
3. Team
4. Player
5. Player Performance

## Step 5: Enjoy Testing!
Feel free to give feedback and suggestions!

---
