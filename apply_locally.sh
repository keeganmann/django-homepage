sudo su postgres -c 'pg_restore --verbose --clean --no-acl --no-owner -h localhost -U myuser -d mydb latest.dump'
