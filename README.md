Below is a `README.md` file for the Instagram Reels downloader program. It contains all the essential information a user would need to understand, install, and run the program.

---

# Instagram Reels Downloader

This is a Python program that downloads all available reels from a public Instagram account and saves them to a user-specified folder on the local machine in video format (e.g., `.mp4`).

## Features

- **Download Reels**: Downloads all available reels (video posts) from a public Instagram profile.
- **Custom Save Location**: Asks the user to select a folder on their local machine to save the downloaded reels.
- **Error Handling**: Notifies the user if the Instagram profile doesn't exist or is private.
- **File Format**: Reels are downloaded in `.mp4` format for easy viewing.

## Requirements

Before running the program, ensure that you have the following installed:

1. **Python 3.x**
2. **Pip package manager**

### Python Libraries:

- **instaloader**: Used for scraping and downloading Instagram reels.
- **tkinter**: Used for creating a folder dialog window to let the user choose a save directory.

You can install the required libraries by running:

```bash
pip install instaloader
```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/instagram-reels-downloader.git
   cd instagram-reels-downloader
   ```

2. **Install dependencies**:
   Run the following command to install the necessary libraries:
   ```bash
   pip install instaloader
   ```

3. **Run the script**:
   Run the Python script to start downloading reels:
   ```bash
   python download_reels.py
   ```

4. **Follow the prompts**:
   - Enter the username of the public Instagram account whose reels you want to download.
   - Choose the folder where the reels will be saved.

5. The reels will be saved as `.mp4` files in the folder you selected.

## Example Usage

```bash
Enter the Instagram username of the public account: travel_inspo
Saving reels to: /Users/username/Downloads/Reels
Downloading reels from travel_inspo...
Successfully downloaded 5 reels.
```

## Error Handling

- **Profile Not Found**: If the Instagram profile does not exist or is misspelled, the program will notify the user and exit.
- **Private Profile**: If the profile is private, the program will notify the user and exit without attempting to download.
- **No Reels Available**: If the profile has no reels, the program will inform the user that there are no videos to download.

## Limitations

- The program only works with **public Instagram accounts**.
- For **private accounts**, you need to authenticate using Instagram credentials (this feature is not implemented in the current version).
- Instagram might limit the number of requests in a short time frame. If you encounter issues, try downloading again after some time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you have suggestions or improvements for this program, feel free to open a pull request or submit an issue on GitHub.

---

### Additional Notes:
- Update the GitHub URL (`https://github.com/your-username/instagram-reels-downloader.git`) with your actual GitHub repository link before publishing. 
