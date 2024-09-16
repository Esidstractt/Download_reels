import instaloader
import os
from tkinter import filedialog
from tkinter import Tk

# Function to ask for folder location
def ask_for_directory():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()
    
    folder_selected = filedialog.askdirectory(title="Select Folder to Save Reels")
    if folder_selected:
        print(f"Saving reels to: {folder_selected}")
    else:
        print("No folder selected. Exiting...")
        exit()
    return folder_selected

# Function to download reels from a public Instagram account
def download_reels(username, target_folder):
    # Initialize the instaloader instance
    L = instaloader.Instaloader(dirname_pattern=target_folder, download_videos=True)
    
    # Load the public profile
    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: The profile '{username}' does not exist.")
        return
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"Error: The profile '{username}' is private.")
        return

    # Download all available reels
    print(f"Downloading reels from {username}...")
    
    reels_downloaded = 0
    for post in profile.get_posts():
        # Check if the post is a video (Reel)
        if post.is_video:
            print(f"Downloading Reel: {post.shortcode}")
            L.download_post(post, target=target_folder)
            reels_downloaded += 1
    
    if reels_downloaded == 0:
        print("No reels found to download.")
    else:
        print(f"Successfully downloaded {reels_downloaded} reels.")
    
if __name__ == "__main__":
    # Ask user for Instagram username
    username = input("Enter the Instagram username of the public account: ")
    
    # Ask for the directory to save the reels
    target_folder = ask_for_directory()
    
    # Download reels from the given public Instagram account
    download_reels(username, target_folder)
