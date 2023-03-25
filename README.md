# Population Analysis Application

The service that shows countries and population data

## Docker Run

You may run docker image using docker-compose.yml.
To see test results:

1. run:

docker compose up get_data

If you get "success" - the information has been successfully parsed and added to the db"

2. run:

docker compose up print_data

You will see the data printed on your screen. The last 4 lines are the biigest and smallest countries and their population numbers.

