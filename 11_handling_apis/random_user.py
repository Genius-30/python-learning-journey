import requests

def fetch_random_user():
  url = "https://randomur.me/api/"
  res = requests.get(url)
  data  = res.json()

  if "results" in data and len(data['results']) != 0:
    user_data = data["results"]
    username = user_data[0]['login']['username']
    country = user_data[0]['location']['country']
    return username, country
  else:
    raise requests.exceptions.RequestException("Failed to fetch user data")

def main():
  try:
    username, country = fetch_random_user()
    print(f"Username: {username} \nCountry: {country}")
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
  main()