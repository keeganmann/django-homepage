echo "APPLYING latest.dump TO LOCAL DATABASE homepagedb"
sudo su postgres -c 'pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d homepagedb latest.dump'
echo "FINISHED"
