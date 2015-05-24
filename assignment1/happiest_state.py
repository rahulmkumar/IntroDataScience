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
   
    score = 0.00
    for words in twtext:
        if sent_dict.has_key(words) == True:
            score = score + sent_dict[words]

    return score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
   
    sent_dict = sentimentdict(sys.argv[1])
    
    state_score = {}
    states = {
        'Alaska': 'AK',
        'Alabama':'AL',
        'Arkansas':'AR',
        'American Samoa':'AS',
        'Arizona':'AZ',
        'California':'CA',
        'Colorado':'CO',
        'Connecticut':'CT',
        'District of Columbia':'DC',
        'Delaware':'DE',
        'Florida':'FL',
        'Georgia':'GA',
        'Guam':'GU',
        'Hawaii':'HI',
        'Iowa':'IA',
        'Idaho':'ID',
        'Illinois':'IL',
        'Indiana':'IN',
        'Kansas':'KS',
        'Kentucky':'KY',
        'Louisiana':'LA',
        'Massachusetts':'MA',
        'Maryland':'MD',
        'Maine':'ME',
        'Michigan':'MI',
        'Minnesota':'MN',
        'Missouri':'MO',
        'Northern Mariana Islands':'MP',
        'Mississippi':'MS',
        'Montana':'MT',
        'National':'NA',
        'North Carolina':'NC',
        'North Dakota':'ND',
        'Nebraska':'NE',
        'New Hampshire':'NH',
        'New Jersey':'NJ',
        'New Mexico':'NM',
        'Nevada':'NV',
        'New York':'NY',
        'Ohio':'OH',
        'Oklahoma':'OK',
        'Oregon':'OR',
        'Pennsylvania':'PA',
        'Puerto Rico':'PR',
        'Rhode Island':'RI',
        'South Carolina':'SC',
        'South Dakota':'SD',
        'Tennessee':'TN',
        'Texas':'TX',
        'Utah':'UT',
        'Virginia':'VA',
        'Virgin Islands':'VI',
        'Vermont':'VT',
        'Washington':'WA',
        'Wisconsin':'WI',
        'West Virginia':'WV',
        'Wyoming':'WY'
}

     
    for line in tweet_file:
        twdict = json.loads(line)
        if twdict.has_key('place')== True and twdict['place'] <> None:
            twplace = twdict['place']
            if twplace['country'] =='United States' and twplace['place_type']=='admin':# and twplace['name']<>'':
                #print twplace['name']
                #print twdict['text']
                twtext = twdict['text'].split()
                twscore = tweetsent(twtext,sent_dict)
                twstate = states[twplace['name']]
                if state_score.has_key(twstate)==True:
                    state_score[twstate] = (twscore + state_score[twstate])/2
                else: 
                    state_score[twstate] = twscore
    #print state_score.items()
    max =0.00
    max_state = ''
    for state in state_score.keys():
        if max_state == '':
            max_state = state
            max = state_score[state]
            pass
        else:
            if max < state_score[state]:
                max = state_score[state]
                max_state = state

    #print str(max_state),float(max)
    print str(max_state)
                

if __name__ == '__main__':
    main()
