import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
  )
''')

def list_all_videos():
  cursor.execute("SELECT * FROM videos")

  rows = cursor.fetchall()

  print("\n")
  print("-" * 100)
  print("\n")
  
  if len(rows) == 0:
    print("No videos!")
  else:
    for row in rows:
      print(row)
  print("\n")
  print("-" * 100)

def add_video(name, duration):
  cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
  conn.commit()
  list_all_videos()

def update_video(video_id, name, duration):
  cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, video_id))
  conn.commit()
  list_all_videos()

def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()
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

  conn.close()

if __name__ == "__main__":
  main()