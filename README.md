# Django REST Test
Simple Django REST app to investigate [Django Ninja](https://django-ninja.rest-framework.com/).

-------------

## Execute
### Install locally
Assuming that you created a Postgres database with the necessary settings.
```bash
pip install -r ./requirements/local.txt
python manage.py migrate
python manage.py loaddata fixture_1.json fixture_2.json
python manage.py runserver
```

### Docker
```bash
docker-compose -f docker-compose-dev.yaml up --build
```

> The app will run in **http://localhost:7171**

-------------
## Login
With the app already running, login with one of these users:
```
username: user1 ; password: Secret1234!
username: user2 ; password: Secret1234!
```
-------------
## API Docs
Navigate to `/api/v1/docs`.

-------------
## Brief explanation of project

[Brief explanation of project.](./DOCS.md) (spanish)