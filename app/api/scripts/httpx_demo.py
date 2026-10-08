import httpx


def fetch_example() -> dict:
    response = httpx.get("https://httpbin.org/get", timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(fetch_example())
