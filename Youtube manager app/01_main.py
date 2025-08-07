
# This manager app is a simplest app that store your favorite youtube videos with their duration(time)


#code:

import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except:
        return []
    
    
def save_data_helper(videos):    
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)
        
        
        
def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}")
        
        

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time :")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    
    
def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update: "))
    if 1<= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print('Invalid index selected')
    
    
    
def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of video you want to delete: "))
    if 1<= index <= len(videos):
        del  videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def main():
    videos = load_data()
    while(True):
        print("\n Youtube Manager | Choose an option ")
        print("1. List all videos  ")
        print("2. Add a youtube video  ")
        print("3. Update a youtube video details  ")
        print("4. Delete a youtube video details  ")
        print("5. Exit the app  ")
        choice = input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()