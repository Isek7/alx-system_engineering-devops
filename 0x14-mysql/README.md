# `MySQL Master-Slave Replication`

- MySQL replication is a process that enables data from one MySQL database server (the master) to be copied automatically to one or more MySQL database servers (the slaves).
- It is usually used to spread read access on multiple servers for scalability, although it can also be used for other purposes such as for failover, or analyzing data on the slave in order not to overload the master.

![](https://bs-uploads.toptal.io/blackfish-uploads/components/blog_post_page/content/cover_image_file/cover_image/1279580/retina_1708x683_staging.toptal.net_mysql_mysql-master-slave-replication-tutorial-c4941d5e44de507b5850d42c138eddc0.png)















Futhermore,this project involved learning how to configure database servers in a
primary-replica model. I configured the two servers provided to me by
ALX in a MySQL primary-replica setup with a dummy database, and wrote
a Bash script to automate generation of database backups.

## Tasks :page_with_curl:

* [4-mysql_configuration_primary](./4-mysql_configuration_primary): The MySQL
`my.conf` configuration file used to set up my first server as a primary database
server on the database `tyrell_corp`.

* [4-mysql_configuration_replica](./4-mysql_configuration_replica): The MySQL
`my.conf` configuration file used to set up my second server as the replica
database server on the database `tyrell_corp`.

* [5-mysql_backup](./5-mysql_backup): Bash script that generates a compressed
`tar.gz` archive from a MySQL dump.
  * Usage: `./5-mysql_backup <MySQL root password>`
  * Generates a dump containing all MySQL databases on the root server.
  * Names the resulting tar archive in the format `day-month-year.tar.gz`.
