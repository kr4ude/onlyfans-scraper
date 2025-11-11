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
You can easily set up the program by running the `setup.py` file.
It will create an `auth.json` file, which you need to fill in with the following data:
```
{
    "auth": {
        "username": " ",
        "cookie": " ",
        "user_agent": "",
        "x-bc": ""
    }
}
```
To obtain this information, log in to your OnlyFans account, press F12, and locate the cookie, x-bc header,
<img width="1320" height="669" alt="pre22212341ww" src="https://github.com/user-attachments/assets/2c0a43fa-bd50-43a6-9479-b2a04165b015" />
You can also obtain this data by using cookie helper tools.

This is what the auth file should typically look like:
```
{
    "auth": {
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-bc": "jncx05ryygvsu6e2q44e830l49stj1ab16e9xpal",
        "auth_id": "123456",
        "sess": "1pfa4tyad154lwyztvbjfdcnlk",
        "auth_uid_": "123245"
    }
}
```

# Usage
After setup, type
```
of-scraper
```
to start using the scraper

**Below is a command list for CLI provided to simplify usage of the script:**

### 🔐 login

Starts an authentication prompt and stores credentials locally.

Usage:
```
of-scraper login
```
### Init

Creates the initial folder structure for your media library.

Usage:

```
of-scraper init
```

### Download

Downloads media (videos, images, audio) for the selected creator(s).
Supports advanced filtering by type, date range, and tags.

Usage:
```
of-scraper download --creator username
```

Filter Examples:
```
of-scraper download --creator username --type video
of-scraper download --creator username --date-after 2024-01-01 --date-before 2025-01-01
of-scraper download --creator username --tag premium
```
### 🔍 Search

Searches through creators or posts using filters such as keywords, type, or date range.

Usage:
```
of-scraper search --creator username --query "holiday"
```

Filter Examples:
```
of-scraper search --type image --date-after 2023-06-01
of-scraper search --tag behindthescenes
of-scraper search --liked true
```
### 📤 Export
Exports metadata and media indexes to a structured format (JSON, CSV, YAML).

Usage:
```
of-scraper export --format json --output ./exports/
```

###  Status

Displays current library information — number of media files, space used, errors, etc.

Usage:
```
of-scraper status
```

###  Cleanup

Removes temporary, duplicate, or incomplete media files.

Usage:
```
of-scraper cleanup --duplicates
```

### Rename

Renames media files according to a given pattern.

Usage:
```
of-scraper rename --pattern "{creator}_{date}_{id}"
```

### Interactive

Launches an interactive mode that uses prompts for all settings and actions.

Usage:
```
of-scraper interactive
```
and follow the on-screen prompts to select creators, media types, and filters.

###  Like

Marks a post as liked.

Usage:
```
of-scraper like --post-id 12345
```
###  Unlike

Removes a like from a post.

Usage:
```
of-scraper unlike --post-id 12345
```
### Sync

Synchronizes your local media and metadata with the latest updates from creators.

Usage:
```
of-scraper sync
```

### ⚙️ Config

Displays or edits configuration settings from the command line.

Usage:
```
of-scraper config --edit
```


