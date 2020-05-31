import datetime

class Parameters:

	# explanations of these parameters can be found in the README

	# Global Parameters. If you change these, delete the database and re-run main.py
	database_filename = "./collegeswimming.db"
	season_line_month = 9
	season_line_day = 15

	# main.py parameters
	events_to_pull = ["150Y", "1100Y", "4200Y", "5200Y"]
	genders_to_pull = ["M"]
	ptn = 477
	hrv = 134
	yle = 376
	brn = 17
	col = 283
	pen = 416
	cor = 258
	drt = 272
	teams_to_pull = [ptn, hrv, yle, brn, col, pen, cor, drt]
	year_start = 2018
	year_end = 2019

	# analysis parameters
	event_histograms = ["M150Y", "M1100Y", "M4200Y", "M5200Y"] 
	teams_to_review = teams_to_pull
	swimmers_to_review = [242825]
	review_year_start = year_start
	review_year_end = year_end


	def convert_to_timestamp(self, year, month, day):
		'converts a given month day and year into a timestamp. Why is this so hard?'
		return (datetime.datetime(int(year), int(month), int(day)) - datetime.datetime(1970,1,1)).total_seconds()


	def to_title(self,event_string):
		'converts an event string into a human readable title'
		gender = event_string[0]
		stroke = event_string[1]
		distance = event_string[2:-1]
		gender_map = {"M":"Men", "F":"Women"}
		stroke_map = {"1":"Freestyle", "2":"Backstroke", "3":"Breaststroke", "4":"Butterfly", "5":"IM"}
		return "{}'s {} Yard {}".format(gender_map[gender], distance, stroke_map[stroke])
