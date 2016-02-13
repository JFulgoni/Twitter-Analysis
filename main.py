from __future__ import division
import sys
import time
import string
import twitter_manager

__author__ = 'johnfulgoni'

# takes a line from the training set
# and returns the userid, tweetid, tweet, and (date, time)
def process_line(line):
    line = line.strip()
    #print line
    line_list = line.split()
    #print line_list

    # adjust list into different variables
    user_id = line_list.pop(0)
    tweet_id = line_list.pop(0)
    time_id = line_list.pop()
    date_id = line_list.pop()
    date_time = (date_id, time_id)

    tweet = ' '.join(line_list)
    #print user_id, tweet_id, date_time
    #print tweet
    return user_id, tweet_id, tweet, date_time

# takes in the filename
# and returns the appropriate data structures with each set of data
def create_dataset(filename):
    #print filename
    user_id_list = []
    tweet_id_list = []
    tweet_list = []
    date_list = []
    with open(filename) as infile:
        for line in infile:
            #print line
            user_id, tweet_id, tweet, date_time = process_line(line)
            user_id_list.append(user_id)
            tweet_id_list.append(tweet_id)
            tweet_list.append(tweet)
            date_list.append(date_time)
            #break
    infile.close()
    return user_id_list, tweet_id_list, tweet_list, date_list

if __name__ == '__main__':
    # twitter data from:
    # https://archive.org/details/twitter_cikm_2010
    # it's in a zip file in downloads unless you decided to move it
    # will most likely have to preprocess the data in some way

    #filename = 'twitter_cikm_2010/training_set_tweets.txt'
    filename = 'john_training.txt'
    user_id_list, tweet_id_list, tweet_list, date_list = create_dataset(filename)

    # f = open('john_training.txt', 'w')
    # counter = 0
    # with open(filename) as infile:
    #     for line in infile:
    #         f.write(line)
    #         counter = counter + 1
    #         if counter > 1000:
    #             break
    # infile.close()
    # f.close()

    for tweet in tweet_list:
        print tweet

    # currently this function gets an error from the twitter api
    # twitter_manager.get_friends()
    print '\n...Done'