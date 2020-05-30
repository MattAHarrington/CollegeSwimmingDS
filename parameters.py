import datetime

class Parameters:

	# explanations of these parameters can be found in the README

	# Global Parameters. If you change these, delete the database and re-run main.py
	databaseFileName = "./collegeswimming.db"
	seasonLineMonth = 9
	seasonLineDay = 15

	# main.py parameters
	eventsToPull = ["5200Y"]
	gendersToPull = ["F"]
	ptn = 477
	hrv = 134
	yle = 376
	brn = 17
	col = 283
	pen = 416
	cor = 258
	drt = 272
	teamsToPull = [ptn, hrv, yle, brn, col, pen, cor, drt]
	yearStart = 2018
	yearEnd = 2019

	# analysis parameters
	eventHistograms = ["F5200Y"]
	teamsToReview = [114]
	swimmersToReview = [347491]
	reviewYearStart = 2016
	reviewYearEnd = 2017


	def convertToTimestamp(self, year, month, day):
		'converts a given month day and year into a timestamp. Why is this so hard?'
		return (datetime.datetime(int(year), int(month), int(day)) - datetime.datetime(1970,1,1)).total_seconds()


	def toTitle(self,eventString):
		'converts an event string into a human readable title'
		gender = eventString[0]
		stroke = eventString[1]
		distance = eventString[2:-1]
		genderMap = {"M":"Men", "F":"Women"}
		strokeMap = {"1":"Freestyle", "2":"Backstroke", "3":"Breaststroke", "4":"Butterfly", "5":"IM"}
		return "{}'s {} Yard {}".format(genderMap[gender], distance, strokeMap[stroke])
