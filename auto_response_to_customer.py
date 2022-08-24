import requests
import os

def retrieve_new_ticket_event():
    url = "https://kuberaspeaking.gorgias.com/api/events"
    payload={}
    headers = {
        'Authorization': 'Basic c2FpLnMua2FtYXRAZ21haWwuY29tOmFiNGFhODBhM2E0YTExNGQ1Y2ExNjk5Y2E4Mjg4NzBiYzE1YTdkNGE0YTc3MmJlZGE2NjlmMWQxNDBlMzI1YmI='
    }

    all_events_response = requests.request("GET", url, headers=headers, data=payload).json()

    for i in all_events_response['data']:
        if i['type'] == 'ticket-created':
            print(i['id'])

retrieve_new_ticket_event()