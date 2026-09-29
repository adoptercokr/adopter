import urllib.request
import json

query = """
query getAccommodation($id: String!) {
  accommodation(id: $id) {
    accommodationBookingDetails(size: 20) {
      roomTotal
      resocItems {
        resocId
        resocName
        resocDesc
        cond2Val
        cond3Val
        reprUrl
        subImage
        drtOptionList {
          iconName
          optionName
        }
      }
    }
  }
}
"""

payload = [{
    "operationName": "getAccommodation",
    "variables": {"id": "1716272359"},
    "query": query
}]

req = urllib.request.Request(
    "https://api.place.naver.com/graphql",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)",
        "Referer": "https://m.place.naver.com/accommodation/1716272359/room"
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        with open("tools/rooms_graphql.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Success! Response:")
        print(json.dumps(data, ensure_ascii=False, indent=2)[:600])
except Exception as e:
    print("Error:", e)
