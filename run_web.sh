# cd code/
python manage.py makemigrations congress core institute minicourses shirts users
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py createsuperuser
