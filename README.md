# STAMPS APP
is an app for managing client cards with loyality stamps. Basic assumptions:
* company-client is able to see how many cards user-clients used within his company range
* company-client is able to create card-types with (exp. date and maximum number of stamps)
* company-client is able to send to user-clients cards with free stamps 
* user-client is able to see and remove his loyality cards

## CREATE SUPERUSER ##
```
1. get inside container
2. python manage.py createsuperuser
3. (optional) user: seyhak, password: admin
```
## RUN ALL ##
```
docker-compose up
```

## MANUAL TESTING
```
1) REUSE_DB=1 python app/manage.py test api.tests.test_endpoints.TestGetMyCards.test_get_my_cards -v=2
2) python app/manage.py test --verbosity=2
```
## MANUAL TESTING
Go to `admin/`


## API

### CARD TYPES
- get all cards for company with <id> `get/`
