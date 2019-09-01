# 9DaysOfAPIs

## About
As a SysAdmin who uses Python for automating/simplifying certain tasks, I've always wanted to do more.
I by no means claim to be a developer, but enjoy it as a hobby and a way to advance my career.
This little project is a way for me to get used making API calls with Python. All of the topics
of the APIs are things that I think are interesting or funny.

This project started out at 30 days of APIs, and then 21. However, it was easier to find 9 interesting APIs
than 30.

While all of the projects will use argparse for certain variables, keep in mind that it is probably safer to 
set an environment variable with your API keys.

## Activities
### Day 1 - NASA Astronomy Photos
nasa-apod.py

Simple CLI app that takes a NASA API key and grabs the APOD for today, or the specified date, and downloads it to the current directory.

Arguments:

[optional] `--api-key` The api.nasa.gov API key to use. Defaults to DEMO_KEY.

[optional] `--date` The date to grab the photo from. Defaults to today.

### Day 2 - NASA Near Earth Asteroids (NEO)
nasa-asteroids.py

Returns a list of Near Earth Objects on a given date range and notes if they are considered potentially hazardous.

Arguments:

<REQUIRED>`api_key` The API key to use.

<REQUIRED>`start_date` The start date that the asteroid will be near Earth. example: 2019-07-23

<REQUIRED>`end_date` The end date that the asteriod will be near Earth. example: 2019-07-30

### Day 3 - Open Weather Maps (OMW)
omw-weather.py

Obtains weather forecast for a given city using a given API key from openweathermap.org

Arguments:

<REQUIRED> `api_key` Your OWM API key.

<REQUIRED> `zip_code` The zipcode you wish to query about.

### Day 4 - Taco Fancy
taco-recipe.py 

Gives you a random taco recipe!

Arguments:

NONE!

### Day 5 - REST Countries
countries-basicinfo.py

Gives the capital and language(s) of a given country.

<REQUIRED> `country` The full name of the country.

### Day 6 - FOAAS
foaas-foff.py

Returns a random message from FOAAS that only requires input in the from field.

Arguments:

[OPTIONAL] `--signed` Who are you?

## Lessons Learned
- MVP (minimum viable product) is easy and provides a way for quick feedback.
- If you have to look up documentation or Google something, it's best to know the 'lingo' to know what to look for.
- I should be writing tests (possibly do 9 days of tests as a companion to this project?).
- Don't always rely on a demo key.
- f strings are useful, but ugly.
- Not all JSON output is meant to be printed as plain text.
- There's more than one way to skin a cat. 
- I should probably script the API endpoint to scrape possibilities instead of hardcoding them.
