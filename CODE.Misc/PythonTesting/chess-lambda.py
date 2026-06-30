import requests

def query_chess_api(fen: str) -> dict:
    """
    Sends a POST request to https://chess-api.com/v1 with a FEN position.

    Parameters:
        fen (str): The FEN string representing the chess position.

    Returns:
        dict: The JSON response from the API.
    """
    url = "https://chess-api.com/v1"
    payload = {
        "fen":  fen
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage:
#fen_example = "r1bqkbnr/pppppppp/n7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 2 2"
#result = query_chess_api(fen_example)

def lambda_handler(event, context):
    position = "8/1P1R4/n1r2B2/3Pp3/1k4P1/6K1/Bppr1P2/2q5 w - - 0 1"
    report = query_chess_api(position)
    
    return {
        'statusCode': 200,
        'body': json.dumps(report)
    } 