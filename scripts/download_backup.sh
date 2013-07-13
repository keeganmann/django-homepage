echo "GENERATING BACKUP ON HEROKU"
heroku pgbackups:capture
echo "DOWNLOADING BACKUP FROM HEROKU"
curl -o latest.dump `heroku pgbackups:url`
echo "FINISHED"
