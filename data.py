#part 2-3
import requests as api

parameters = {
  "amount": 10,
  "type":"boolean",
  #part 9
  "category:": 18
}

response = api.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
