# cdc-vaccination-history

A [git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) recording the CDC's [Covid Data Tracker](https://covid.cdc.gov/covid-data-tracker/#vaccinations) numbers on number of vaccinations per state.

Archives the JSON from https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data every time it changes, checking three times an hour.

Watch [Git scraping, the five minute lightning talk](https://simonwillison.net/2021/Mar/5/git-scraping/) to see me live-code the creation of this repository.

## Should you trust these numbers?

I honestly don't know. These are not coming from a documented API - I found it using the Firefox developer tools network pane. I don't know how the CDC are sourcing these. I don't know if they themselves consider them to be accurate.

All I know is that these are the numbers they are displaying on their own site - so you should treat this repository as tracking "numbers that were displayed on the CDC's website" as opposed to assuming it represents the full truth on the ground.
