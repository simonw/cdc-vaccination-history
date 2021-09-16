import sqlite_utils
import csv

# Outputs everything in the SQLite database into a condensed CSV files, 
# similar in format to the [New York Times COVID-19 data](https://github.com/nytimes/covid-19-data).

# Note that this must be run after build_database.py.

def create_csv(name, cols):
    cursor = db.execute("select " + ','.join(cols) + " from " + name); 
    rows = cursor.fetchall()
    csvWriter = csv.writer(open(name + ".csv", "w"))
    csvWriter.writerow(cols) 
    for row in rows:
        csvWriter.writerow(row)

if __name__ == "__main__":
    db = sqlite_utils.Database("cdc.db")

    # Create condensed CSV for daily_reports
    cols = ["Date", "Location", "ShortName", "LongName", "Census2019", "Administered_Dose2", "Series_Complete_18Plus", "Series_Complete_Pop_Pct"]
    create_csv("daily_reports", cols) 
    
    # Create condensed CSV for daily_reports_counties
    cols = ["Date", "FIPS", "StateName", "StateAbbr", "County", "Series_Complete_18PlusPop_Pct", "Series_Complete_Pop_Pct"]
    create_csv("daily_reports_counties", cols)

