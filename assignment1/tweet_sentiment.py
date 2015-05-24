import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def sentimentdict(f):    
    afinnfile = open(f)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
    #print scores.items() # Print every (term, score) pair in the dictionary
def tweetsent(twtext,sent_dict):
   
    score = 0
    for words in twtext:
        if sent_dict.has_key(words) == True:
            score = score + sent_dict[words]

    return score

    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    score = 0
    twtext = []
    twcount = 0
    sentiment_score = []
    

    
    sent_dict = sentimentdict(sys.argv[1])
    #print tweet_file.readlines()
    for line in tweet_file:
        #print json.loads(line).keys()[0]
        twdict = json.loads(line)
        #tweetdictsent(twdict,sent_dict)
        if twdict.has_key('text')== True:
            twcount = twcount + 1
            twtext = twdict['text'].split()
            score = tweetsent(twtext,sent_dict)
            sentiment_score.append(score)
            print score
            

    #print twcount   
    #print len(sentiment_score)
if __name__ == '__main__':
    main()
