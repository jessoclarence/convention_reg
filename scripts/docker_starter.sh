sh -c /opt/ohmyzsh.sh
cp /opt/.zshrc /home/ntcuser/

cd /srv/src/convreg/
python manage.py migrate
touch /srv/logs/access.log
touch /srv/logs/gunicorn.log

tail -n 0 -f /srv/logs/*.log &

echo "Starting Gunicorn"
exec gunicorn convreg.wsgi:application \
		 --name ntcregapp \
		 --bind 0.0.0.0:8000 \
		 --workers 3 \
		 --log-level=info \
		 --log-file=/srv/logs/gunicorn.log \
		 --access-logfile=/srv/logs/access.log \
		 "$@"
