def getHeader() -> dict:
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'YourCustomUserAgent'
        }
        return header

def getHeaderAuth(token: str) -> dict:
    header = {
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'YourCustomUserAgent'
    }
    return header