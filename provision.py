import pd

# put a PagerDuty REST API v2 read/write token in token:
token = "YOUR_PD_REST_API_TOKEN"

pd_webhook_name = "sfdc"

# put the list of service IDs you want to add webhooks to in pd_service_ids:
pd_service_ids = [
    "PXXXXXX",
    "PYYYYYY"
]

# put the the Salesforce username of the PD integration user in sfdc_username:
sfdc_username = "martin@pagerduty.com"

# sfdc_rest_resource_url should be the same for everyone
sfdc_rest_resource_url = "pagerduty/webhook"

# Set sfdc_is_sandbox to True if you are using a SFDC sandbox, otherwise False
sfdc_is_sandbox = True

# put the Client ID from your PagerDuty SFDC connected app in sfdc_client_id:
sfdc_client_id = "YOUR_SFDC_CONNECTED_APP_CLIENT_ID"

# put the key that matches your SFDC shared app's certificate in sfdc_shared_key:
sfdc_shared_key = """
-----BEGIN PRIVATE KEY-----
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX==
-----END PRIVATE KEY-----
"""

sfdc_shared_key = " ".join(sfdc_shared_key.splitlines())


for pd_service_id in pd_service_ids:
    body = {
        "webhook":
        {
            "name": pd_webhook_name,
            "type": "webhook",
            "outbound_integration":
            {
                "id": "P2JA7HV",
                "type": "outbound_integration"
            },
            "config":
            {
                "client_id": sfdc_client_id,
                "username": sfdc_username,
                "shared_key": sfdc_shared_key,
                "rest_resource_url": sfdc_rest_resource_url,
                "sandbox": sfdc_is_sandbox
            },
            "webhook_object":
            {
                "id": pd_service_id,
                "type": "service_reference"
            },
        }
    }

    print(f"Adding SFDC webhook for service {pd_service_id}... ", end="", flush=True)
    try:
        r = pd.request(token=token, endpoint="webhooks", method="POST", data=body)
        print(f"added webhook {r['webhook']['id']}.")
    except:
        print(f"failed: {r}")