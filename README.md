# Log Analysis Project
*A Udacity Full Stack Nanodegree Degree project*
## Technologies used

1.  PostgreSQL
2.  Python code with DB-API
3.  Linux-based virtual machine (VM) Vagrant

## Requirements
- Python  (https://www.python.org)
- Psycopg2 v2.7.5  (http://initd.org/psycopg/download/)
- PostgreSQL v9.5.14  (https://www.postgresql.org/download/)
- Vagrant v2.2.0  (https://www.vagrantup.com/downloads.html) 
- VirtualBox v5.1.38  (https://www.vagrantup.com/downloads.html)

## Instructions
1. Create empty folder that will be project main folder for example (Logs-Analysis) here will be your python file.
2. Download "Vagrantfile" (https://goo.gl/wLBxDA) and place it inside recently created folder.
3. Run "vagrant up" command inside folder using any CLI (cmd,pwoershell,bash, git bash ...etc) and wait till it finish.
4. Download datafile "newsdata.sql" (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
5. Unzip "newsdata.zip" and copy "newsdata.sql" to our project folder.
6. Now the project folder should be something like this

	    \--- <Folder name>
	    |   newsdata.sql
	    |   Vagrantfile
	    |   log.py
	    |   
	    \---.vagrant
	        +---machines
	        |   \---default
	        |       \---virtualbox
	        |               action_provision
	        |               action_set_name
	        |               box_meta
	        |               creator_uid
	        |               id
	        |               index_uuid
	        |               private_key
	        |               synced_folders
	        |               vagrant_cwd
	        |               
	        \---rgloader
	                loader.rb

7. Run `vagrant ssh` inside project folder.
8. cd to vagrant using command `cd /vagrant`. 
9. Fill database from "newsdata.sql" file using this command `psql -d news -f newsdata.sql`.
10. Now VM machine and database with data is ready.

The database includes three tables:
-   Authors table
-   Articles table
-   Log table

To execute the program, run  `python log.py`  from the command line.

## Author

-   **Yasir Albardawil**  -  _Initial work_  -  [yasir-albardawil](https://github.com/yasir-albardawil)

## License

This project is licensed under the MIT License - see the  [LICENSE](https://github.com/yasir-albardawil/log-analysis-project/blob/master/LICENSE)  file for details
