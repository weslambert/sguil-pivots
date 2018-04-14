#!/usr/bin/python2.4
#!/usr/bin/python
# Modified from script by Keith Taylor, found here:
# http://informationonsecurity.blogspot.com/2015/10/automating-forensic-artifact-collection.html
import json, urllib2, base64, requests
import requests
import argparse
import sys
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/tmp/hive.conf')

url = parser.get('config', 'url')
apikey = parser.get('config', 'apikey')

sys.stdout = open('/tmp/hive.log', 'w')

parser = argparse.ArgumentParser(description='Post a case to the Hive')
parser.add_argument('-t','--title', help='Title',required=True)
parser.add_argument('-d','--description',help='Description', required=True)
parser.add_argument('-s','--severity',help='Severity', required=True)
args = parser.parse_args()

title = args.title
description = args.description 
severity = args.severity

authheader =  "Bearer " + apikey
headers = {
    "Authorization": authheader,
    "Content-Type": "application/json"
}

data = {
  "title": title,
  "description": description,
  "severity": int(severity)
}

response = requests.post(url + "/api/case",
                          headers=headers, data=json.dumps(data)
			)
print response.content



#import os
#import sys
#import argparse
#sys.stdout = open('/tmp/test.log', 'w')

#parser = argparse.ArgumentParser(description='Post an event to FIR')
#parser.add_argument('-a','--actor', help='Actor',required=False)
#parser.add_argument('-c','--category',help='Category', required=False)
#parser.add_argument('-l','--confidentiality',help='Confidentiality', required=False)
#parser.add_argument('-d','--description', help='Description',required=True)
#parser.add_argument('-t','--detection',help='Detection', required=False)
#parser.add_argument('-p','--plan',help='Plan', required=False)
#parser.add_argument('-s','--severity',help='Severity', required=False)
#parser.add_argument('-j','--subject',help='Subject', required=True)

#args = parser.parse_args()

#actor = args.actor
#category = args.category
#confidentiality = args.confidentiality
#description = args.description
#detection = args.detection
#plan = args.plan
#severity = args.severity
#subject = args.subject

#print actor
#print subject
#print description
