# OnlyFans Scraper
![License](https://img.shields.io/badge/license-MIT-black.svg?style=flat)

# Description
A CLI tool that lets you download media, manage likes, and perform various actions on creators content from OnlyFans.

# Features
- **Download Media**

- **Like & Unlike Posts**

- **Metadata Management (automatically store post details like title, description, date, tags, and author)**.

- **Custom File Organization**.

- **Queue & Retry System (handle multiple tasks with automatic retries for failed downloads)**.

- **Filters & Selection**

# Requirements
- Python 3.10+
- Windows/Linux/Mac OS
- Full requirements are provided in requirements.txt

# Setup
You can easily setup the program by launching `setup.py` file. It will create `auth.json` file, you will need to fill it with the following data:
``
{
    "auth": {
        "username": " ",
        "cookie": " ",
        "user_agent": "",
        "x-bc": ""
    }
}
```
To obtain this data, follow steps on the image below:
