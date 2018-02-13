. ./properies.py
python3 -m venv $VENV
source $VENV/bin/activate
pip install -r requirements.txt

script="
import properies
from django.contrib.auth.models import User;

username = properies.USER_NAME;
password = properies.PASSWORD;
email = properies.MAIL;

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"

python manage.py makemigrations
python manage.py migrate

printf "$script" | python manage.py shell