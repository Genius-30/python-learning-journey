
import json

data_file_name = "youtube.txt"

def load_data():
  try:
    with open(data_file_name, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_data_helper(videos):
  with open(data_file_name, 'w') as file:
   json.dump(videos, file)

def list_all_videos(videos):
  if not videos:
    print("No videos found")
  else:
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
      print(f"{index}. {video['name']} - {video['duration']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
  name = input("Enter video name: ")
  duration = input("Enter video duration: ")
  videos.append({'name': name, 'duration': duration})
  save_data_helper(videos)
  list_all_videos(videos)

def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update: "))
  if 1 <= index <= len(videos):
    name = input("Enter video name: ")
    duration = input("Enter video duration: ")
    videos[index-1] = {'name': name, 'duration': duration}
    save_data_helper(videos)
    list_all_videos(videos)
  else:
    print("Invalid video index selected")

def delete_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to be delete: "))

  if 1 <= index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
    list_all_videos(videos)
  else:
    print("Invalid video index selected")

def main():
  videos = load_data()

  while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice = input("Enter your choice: ")

    match choice:
      case "1":
        list_all_videos(videos)
      case "2":
        add_video(videos)
      case "3":
        update_video(videos)
      case "4":
        delete_video(videos)
      case "5":
        break
      case _:
        print("Invalid Choice")

if __name__ == "__main__":
  main()