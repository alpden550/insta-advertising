# Found contestants from Instagram's post

This script can find contestants for your contest on Instagram.

Three conditions for that:

1. Mention in a real friend in a message

2. Like a post

3. Subscribe on an author

## How to install

You have to have an Instagram account to access.

Create file .env in the root and write in it:

```.env
INST_LOGIN=your Instagram login
INST_PASSWORD=your Instagram password
```

Python3 must be already installed.

Should use virtual env for project isolation.

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

## How to use

Run scripts in terminal with arguments:

link to post

name of post's owner

Example:

```bash
python insta_advertising.py https://www.instagram.com/p/ByIWGMYp5la/ --inst_account beauty_bliss_
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
