from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = "mongodb+srv://geniusporwal01:ZqgpislpTZByzUyF@cluster0.tumlw.mongodb.net/"

client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
db = client['python_practice']
videos_collection = db['videos']

def list_all_videos():
  videos = list(videos_collection.find())

  print("\n")
  print("-" * 100)
  print("\n")
  
  if len(videos) == 0:
    print("No videos!")
  else:
    for video in videos:
      print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")

  print("\n")
  print("-" * 100)

def add_video(name, duration):
  videos_collection.insert_one({"name": name, "duration": duration})
  list_all_videos()

def update_video(video_id, name, duration):
  videos_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "duration": duration}})
  list_all_videos()

def delete_video(video_id):
  videos_collection.delete_one({"_id": ObjectId(video_id)})
  list_all_videos()

def main():
  while True:
    print("\nYoutube Manager With SQlite | Choose an option")
    print("1. List all videos")
    print("2. Add a video")
    print("3. Update a video details")
    print("4. Delete a video")
    print("5. Exit the app")
    choice = input("Enter your choice: ")

    if choice == "1":
      list_all_videos()

    elif choice == "2":
      name = input("Enter the video name: ")
      duration = input("Enter the video duration: ")
      add_video(name, duration)

    elif choice == "3":
      video_id = input("Enter the video ID to update: ")
      name = input("Enter the video name: ")
      duration = input("Enter the video duration: ")
      update_video(video_id, name, duration)

    elif choice == "4":
      video_id = input("Enter the video ID to update: ")
      delete_video(video_id)

    elif choice == '5':
      break

    else:
      print("Invalid Choice")

if __name__ == "__main__":
  main()