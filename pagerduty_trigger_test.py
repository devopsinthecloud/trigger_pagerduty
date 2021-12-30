#!/usr/bin/env python

import requests
import json

# Update to match your API key
API_KEY = 'YOUR API KEY'
SERVICE_ID = 'https://YOUR_DOMAIN'
FROM = 'YOUR EMAIL'

def trigger_incident():
    """Triggers an incident via the V2 REST API using sample data."""

    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'From': FROM
    }

    payload = {
        "incident": {
            "type": "incident",
            "title": "The server is on fire.",
            "service": {
                "id": SERVICE_ID,
                "type": "service_reference"
            },
            "incident_key": "baf7cf21b1da41b4b0221008339ff3571",
            "body": {
                "type": "incident_body",
                "details": "A disk is getting full on this machine. You should investigate what is causing the disk to fill, and ensure that there is an automated process in place for ensuring data is rotated (eg. logs should have logrotate around them). If data is expected to stay on this disk forever, you should start planning to scale up to a larger disk."
            }
          }
        }

    r = requests.post(url, headers=headers, data=json.dumps(payload))

    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    trigger_incident()
