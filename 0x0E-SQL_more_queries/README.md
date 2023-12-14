# 0x0E. SQL - More queries
SQL
MySQL

This project contains a set of SQL scripts designed to perform various tasks on a MySQL database. Each script is focused on a specific SQL operation, and the tasks are aimed at practicing and mastering SQL queries.

## Prerequisites

- Ubuntu 20.04 LTS
- MySQL 8.0.25

## Installation

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
sudo apt update
sudo apt install mysql-server
```

## 0. My privileges!
mandatory
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
```bash
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
