def countTweets(tweet_list):
    count_dict = dict()
    for tweet in tweet_list:  # counting tweets for all user
        if tweet.split()[0] not in count_dict:
            count_dict[tweet.split()[0]] = 1
        else:
            count_dict[tweet.split()[0]] += 1
    max_count = max(count_dict.values())  # getting maximum number of tweets
    max_tweets = [[i, count_dict[i]]  # generating a list of all user with maximum number of tweets
                  for i in count_dict if count_dict[i] == max_count]
    # returning the sorted list of all user with maximum number of tweets
    return sorted(max_tweets)


if __name__ == "__main__":
    T = int(input())  # Number of test case
    for i in range(T):
        N = int(input())  # Number of tweets
        tweet_list = list()
        for j in range(N):  # Tweet inputs
            tweet = input()
            tweet_list.append(tweet)
        results = countTweets(tweet_list)  # Checking maximum number of tweets
        for result in results:
            print(*result)  # result
