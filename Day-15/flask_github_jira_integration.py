from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__) # Creating a flask application instance

@app.route("/createJira", method=['POST'])
def createJira():
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org


    API_TOKEN="ENTER YOUR API TOKEN HERE"

    url = "https://sachingavade5912.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("sachingavade5912@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "First Bub Issue created via GitHub",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "AWS"
        },
        "issuetype": {
        "id": "10047" # 10047 is for Bug
        },
        "summary": "Main order flow broken",
        "timetracking": {
        "originalEstimate": "10",
        "remainingEstimate": "5"
        }
    },
    "update": {}
    } )

    github_payload = request.json # Reading incoming GitHub webhook
    comment_body = github_payload["comment"]["body"]
    if comment_body == "/jira":
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    else:
        return "Enter a valid comment to create a Jira issue, accepted comment is /jira"
    
app.run('0.0.0.0')