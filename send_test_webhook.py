import sys
import json
import requests

WEBHOOK_URL = os.environ.get("MAKE_WEBHOOK_URL", "https://hook.eu1.make.com/YOUR_MAKE_WEBHOOK_URL_HERE")

TEST_CASES = {
    "1": {
        "client_name": "Sarah Jenkins",
        "client_email": "sarah@melbourneretail.com.au",
        "inquiry_text": "Hi team, we currently run a brick-and-mortar clothing boutique in South Yarra and need to build a modern online store. We want customers to be able to browse catalog items, pay with Stripe or Afterpay, and track inventory. We don't have our brand guidelines or high-res logo ready yet because our designer is finalizing them next week. Hoping to launch before Christmas."
    },
    "2": {
        "client_name": "David Ross",
        "client_email": "david@rossconsulting.com.au",
        "inquiry_text": "Good morning. We need a 7-page corporate B2B website on WordPress. We have our brand guidelines, vector logos, and finalized copy ready in Google Drive. We need a booking calendar integration (Calendly) and HubSpot form sync for lead generation. Our budget is around $8k AUD and we need delivery by November 30."
    }
}

def send(case_num="1"):
    payload = TEST_CASES.get(str(case_num), TEST_CASES["1"])
    print(f"Firing Test Case {case_num} ({payload['client_name']}) to Make...")
    try:
        res = requests.post(WEBHOOK_URL, json=payload, timeout=35)
        print(f"Status Code: {res.status_code}")
        print(f"Response: {res.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    case = sys.argv[1] if len(sys.argv) > 1 else "1"
    send(case)
