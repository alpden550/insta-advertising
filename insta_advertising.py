import os
import re
import argparse
from dotenv import load_dotenv
from instabot import Bot


def get_post_id(url):
    return bot.get_media_id_from_link(url)


def get_all_comments_for_post(post_id):
    return [(comment['user_id'],
             comment['user']['username'],
             comment['text']) for comment in bot.get_media_comments_all(post_id)]


def find_names(text):
    # resgular expression was taken https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
    pattern = re.compile(
        r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)')
    result = pattern.findall(text)
    return result


def is_any_user_exist(users):
    return any(bot.get_user_id_from_username(user) for user in users)


def create_parser():
    parser = argparse.ArgumentParser(description='Get contestants from instagram post')
    parser.add_argument('inst_post', help='Post from which you need to get contestants')
    parser.add_argument('-i', '--inst_account', help="Instagram's author")
    return parser.parse_args()


def get_contestants(post_url, author):
    post_id = get_post_id(post_url)
    all_comments = get_all_comments_for_post(post_id)
    filter_comments = []
    likers = bot.get_media_likers(post_id)
    followers = bot.get_user_followers(author)

    for comment in all_comments:
        inst_id, inst_author, inst_text = comment
        users_in_text = find_names(inst_text)
        if (users_in_text and is_any_user_exist(users_in_text) and
                str(inst_id) in likers and str(inst_id)) in followers:
            filter_comments.append(inst_author)

    return set(filter_comments)


if __name__ == "__main__":
    args = create_parser()
    load_dotenv()
    bot = Bot()
    bot.login(username=os.getenv('INST_LOGIN'), password=os.getenv('INST_PASSWORD'))

    print("We're counting contestants, please, wait. It can take some time...")
    contestants = get_contestants(args.inst_post, args.inst_account)
    print(contestants)
