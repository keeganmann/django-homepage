echo "CREATING DEFAULTDB DIRECTORY"
 sudo mkdir -p /opt/local/var/db/postgresql92/defaultdb
echo "CHANGING OWNERSHIP FOR DEFAULTDB DIRECTORY"
 sudo chown postgres:postgres /opt/local/var/db/postgresql92/defaultdb
echo "INITIALIZING DEFAULTDB"
 sudo su postgres -c '/opt/local/lib/postgresql92/bin/initdb -D
/opt/local/var/db/postgresql92/defaultdb' 
echo "CREATING HOMEPAGEDB IN DEFAULTDB"
 sudo su postgres -c 'createdb homepagedb'
echo "FINISHED"
