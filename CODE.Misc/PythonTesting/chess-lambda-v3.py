import json
import urllib.request

def lambda_handler(event, context):
    url = "https://chess-api.com/v1"
    payload = {
        "fen": "8/1P1R4/n1r2B2/3Pp3/1k4P1/6K1/Bppr1P2/2q5 w - - 0 1"
    }

    data = json.dumps(payload).encode("utf-8")

    headers = {
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read()
            return {
                "statusCode": response.getcode(),
                "body": json.loads(response_data.decode("utf-8"))
            }
    except urllib.error.HTTPError as e:
        return {
            "statusCode": e.code,
            "body": e.reason
        }
    except urllib.error.URLError as e:
        return {
            "statusCode": 500,
            "body": str(e.reason)
        }