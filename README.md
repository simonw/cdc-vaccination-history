# cdc-vaccination-history

A [git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) recording the CDC's [Covid Data Tracker](https://covid.cdc.gov/covid-data-tracker/#vaccinations) numbers on number of vaccinations per state.

Archives the JSON from https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data every time it changes, checking three times an hour.
