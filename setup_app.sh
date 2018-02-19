. ./properties.py
python3 -m venv $VENV
source $VENV/bin/activate
pip install -r requirements.txt

script="
import properties
from django.contrib.auth.models import User;

username = properties.USER_NAME;
password = properties.PASSWORD;
email = properties.MAIL;

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"

python manage.py makemigrations
python manage.py migrate

printf "$script" | python manage.py shell