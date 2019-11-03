import json
import urllib
from datetime import datetime

with open('batch_planning_data.json') as json_file:
	data = json.load(json_file)
	cond = None
	if(data):
		print('BEGIN:VCALENDAR')
		print('VERSION:2.0')
		print('CALSCALE:GREGORIAN')
		for p in data['data']:
			if 'start_date' in p:
				datetime_s_str = datetime.strptime(p['start_date'], "%d-%m-%Y")
				if 'end_date' in p:
					datetime_e_str = datetime.strptime(p['end_date'], "%d-%m-%Y")
				print('BEGIN:VEVENT')
				print('DTSTART:' +datetime.strftime(datetime_s_str, "%Y%m%d") + "T000000Z")
				if 'end_date' in p:
					print('DTEND:' +datetime.strftime(datetime_e_str, "%Y%m%d") + "T235959Z")
				print('UID:a4du9v2lvgueruc8mjoepkvjbc@google.com')
				print('ID: ' +p['id'])
				if 'project_url' in p:
					print('DESCRIPTION: Project id ' + p['id'] +'- Name ' +p['text'] +'- Url ' +("https://intranet.hbtn.io" + p['project_url']))
				else:
					print('DESCRIPTION: Project id ' + p['id'] +'- Name ' +p['text'])
				print('LAST-MODIFIED:20070207T065138Z')
				print('LOCATION: https://intranet.hbtn.io')
				print('SEQUENCE:0')
				print('STATUS:CONFIRMED')
				print('SUMMARY: ' +p['text'])
				print('CATEGORIES:http://schemas.google.com/g/2005#event')
				print('END:VEVENT')
