import parameters
import subprocess
import sqlite3

# This script is just a wrapper for the R scripts. They have a lot of parameters that need
# unix timestamps, and it's just easier to generate them in a loop

parameters = parameters.Parameters() # buffalo

# start by making event histograms
# go through each specified event
print()
print()
print("Graphing event Histograms...")
for event in parameters.event_histograms:
	title = parameters.to_title(event)
	database = parameters.database_filename
	process = ["Rscript", "histogram_event.R", event, title, database]
	subprocess.call(process)

print("done")
print()
print()

# we need the database to get names from here on out
connection = sqlite3.connect(parameters.database_filename)
cursor = connection.cursor()
print("Graphing team History...")
for team in parameters.teams_to_review:
	# get the team name
	cursor.execute("select name from Teams where id={}".format(team))
	teamName = cursor.fetchone()[0]
	start_timestamp = parameters.convert_to_timestamp(parameters.review_year_start, parameters.season_line_month, parameters.season_line_day)
	end_timestamp = parameters.convert_to_timestamp(parameters.review_year_end, parameters.season_line_month, parameters.season_line_day)
	# run the whole history graphing script
	process = ["Rscript", "team_history.R", str(team), teamName, str(start_timestamp), str(end_timestamp), database]
	subprocess.call(process)
	# run each year's meet analysis
	for simple_year in range(parameters.review_year_start, parameters.review_year_end):
		start_timestamp = parameters.convert_to_timestamp(simple_year, parameters.season_line_month, parameters.season_line_day)
		end_timestamp = parameters.convert_to_timestamp(simple_year + 1, parameters.season_line_month, parameters.season_line_day)
		title = "{} {}-{} Season".format(teamName, simple_year, simple_year + 1)
		process = ["Rscript", "team_season.R", str(team), title, str(start_timestamp), str(end_timestamp), database]
		subprocess.call(process)

print("done")
print()
print()

print("Graphing Individual Season")
for swimmer in parameters.swimmers_to_review:
	# get the swimmer's name
	cursor.execute("select name from Swimmers where id={}".format(swimmer))
	name = cursor.fetchone()[0]
	for simple_year in range(parameters.review_year_start, parameters.review_year_end):
		# graph each year
		start_timestamp = parameters.convert_to_timestamp(simple_year, parameters.season_line_month, parameters.seasonseason_line_dayLineDay)
		end_timestamp = parameters.convert_to_timestamp(simple_year + 1, parameters.season_line_month, parameters.season_line_day)
		title = "{}'s {}-{} Season".format(name, simple_year, simple_year + 1)
		process = ["Rscript", "individual_season.R", str(swimmer), title, str(start_timestamp), str(end_timestamp), parameters.databaseFileName]
		subprocess.call(process)
