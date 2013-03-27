sudo su postgres -c 'pg_dump -Fc --no-acl --no-owner -h localhost -U postgres dev_django_homepage > /tmp/mydb.dump'
