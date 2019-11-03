#!/usr/bin/env python
import json
import urllib
import uuid
from datetime import datetime

today = datetime.today()
with open('batch_planning_data.json') as json_file:
	data = json.load(json_file)
	cond = None
	if(data):
		f = open("holberton.ical", "w+")
		f.write('BEGIN:VCALENDAR\n')
		f.write('PRODID:-//Google Inc//Google Calendar 70.9054//EN\n')
		f.write('VERSION:2.0\n')
		f.write('CALSCALE:GREGORIAN\n')
		f.write('X-WR-CALNAME:Holberton\n')
		f.write('X-WR-TIMEZONE:America/Bogota\n')
		f.write('BEGIN:VTIMEZONE\n')
		f.write('TZID:America/Atikokan\n')
		f.write('X-LIC-LOCATION:America/Atikokan\n')
		f.write('BEGIN:STANDARD\n')
		f.write('TZOFFSETFROM:-0500\n')
		f.write('TZOFFSETTO:-0500\n')
		f.write('TZNAME:EST\n')
		f.write('END:STANDARD\n')
		f.write('END:VTIMEZONE\n')
		for p in data['data']:
			if 'start_date' in p:
				theuid = uuid.uuid1()
				datetime_s_str = datetime.strptime(p['start_date'], "%d-%m-%Y")
				if 'end_date' in p:
					datetime_e_str = datetime.strptime(p['end_date'], "%d-%m-%Y")
				f.write('BEGIN:VEVENT\n')
				f.write('DTSTART:' +datetime.strftime(datetime_s_str, "%Y%m%d") + "T000000Z\n")
				if 'end_date' in p:
					f.write('DTEND:' +datetime.strftime(datetime_e_str, "%Y%m%d") + "T235959Z\n")
				f.write('DTSTAMP:' +datetime.strftime(today, "%Y%m%dT%H%M00Z") +'\n')
				f.write('UID:' +str(theuid) +'@google.com\n')
				f.write('ID: ' +p['id'] +'\n')
				if 'project_url' in p:
					f.write('DESCRIPTION: Project id ' + p['id'] +' Name ' +p['text'] +'\nUrl ' +("https://intranet.hbtn.io" + p['project_url']) +'\n')
				else:
					f.write('DESCRIPTION: Project id ' + p['id'] +' Name ' +p['text'] +'\n')
				f.write('LAST-MODIFIED:' +datetime.strftime(today, "%Y%m%dT%H%M00Z") +'\n')
				f.write('LOCATION: Cali CLO\n')
				f.write('SEQUENCE:0\n')
				f.write('STATUS:CONFIRMED\n')
				f.write('SUMMARY: ' +p['text'] +'\n')
				f.write('CATEGORIES:http://schemas.google.com/g/2005#event\n')
				f.write('END:VEVENT\n')
		f.write('END:VCALENDAR\n')
		f.close()
	else:
		print('ERROR:THE FILE IS EMPTY? - ARE YOU LOGGED IN?')
