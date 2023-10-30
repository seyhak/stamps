# STAMPS APP
is an app for managing client cards with loyality stamps. Basic assumptions:

### Company client
* company-client is able to see how many cards user-clients used within his company range
* company-client is able to create card-types with (exp. date and maximum number of stamps)
* company-client is able to send to user-clients cards with free stamps
* company-client is able to increment amount of collected stamps on a card

### User Client
* user-client is able to subscribe to company and receive loyality card
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
- get all card types for company user with GET `/api/card_types/`
- get card type by id  GET `/api/card_types/<id>`
- create card type POST `/api/card_types/`
```
{
    "name": name,
    "maximum_stamps": max_stamps,
    "company": user_company.id,
}
```
- delete card type by id DELETE `/api/card_types/<id>`
- edit card type by id PATCH `/api/card_types/<id>`
```
{
    "name": changed_name,
    "maximum_stamps": changed_max_stamps,
}
```
### CARDS
- create card POST `/api/card/`
```
{
    "card_types": id,
}
```
- delete card `/api/card/<id>`
- increment card's stamps POST `/api/card/<id>/increment`
- get all card for company user with GET `/api/card/`
- get card by id GET `/api/card/<id>`
