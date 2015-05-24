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

def main():
    tweet_file = open(sys.argv[1])
    #lines(sent_file)
    #lines(tweet_file)
    
    hashtags = {}
    
    sentiment_score = []
    score = 0
    twtext = []
    twcount = 0
    nzcount = 0
    nzscore = 0
    avgscore = 0.00
    
    freqdict = {}
    
    for line in tweet_file:

        twdict = json.loads(line)
        if twdict.has_key('entities')== True:
            if len(twdict['entities']['hashtags']) > 0:
                for hash_idx in range(0,len(twdict['entities']['hashtags'])):
                    hashtag= twdict['entities']['hashtags'][hash_idx]['text']
                    encoded_tag = hashtag.encode('utf-8')
                    #print encoded_tag
                    #print hashtag
                    if freqdict.has_key(hashtag) == True:
                        freqdict[encoded_tag] = freqdict[encoded_tag] + 1
                    else:
                        freqdict[encoded_tag] = 1
                    #print encoded_tag,freqdict[encoded_tag]
    #sorteddict = freqdict.sorted(freqdict, key=freqdict.get, reverse = True)
    #print sorteddict
    count = 0
    for freq in sorted(freqdict, key=freqdict.get, reverse = True):
        print freq, freqdict[freq]
        count += 1
        if count > 9:
            break
     
            
if __name__ == '__main__':
    main()

'''        
        if twdict.has_key('text')== True:
            twcount = twcount + 1
            #print twdict['text']
            twtext = twdict['text'].split()
            #print "First Word:", twtext[0]
            for words in twtext:
                if freqdict.has_key(words) == True:
                    freqdict[words] = freqdict[words] + 1
                elif freqdict.has_key(words) == False:
                    freqdict[words] = 1
                    

    for item in freqdict:
        print item, freqdict[item]


    #print twcount   
    #print len(sentiment_score)
'''

