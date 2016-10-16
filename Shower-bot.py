#! /usr/bin/env python3

# reddit bot to pull /r/showerthought top 20 and add them to a fortune file

import praw, os, subprocess

r = praw.Reddit(user_agent=("Showerthoughts-fortunes by /u/bbcjk v 0.0.1"))
os.chdir('/usr/share/games/fortunes')

# read hot 20 entries in /r/showerthoughts
subreddit = r.get_subreddit("Showerthoughts")

# check for duplicate entries and add new posts to file.
for submission in subreddit.get_hot(limit = 20):
    with open('golden-st.txt', 'r+') as st:
        if submission.title in st.read():
            continue

        else:
            st.write(submission.title + '\n' + '%' + '\n')

# convert to fortunes format
subprocess.call(['strfile', '-c', '%', 'golden-st.txt', 'golden-st.dat'])
