# BasicPythonChatBot
A simple command line python chat bot without using any AI or any complicated machine learning. 

Things we might need to do:
- split the input message into words. 
    - the split message should not have any special symobls, as it might hamper with our response logic. 
- distinguish message intent. (intent -> what the sentence is trying to say.) To do that we might need: 
    - for this we might need a way to calculate the probability of the i/p message being message from our records. 
        - to calculte the probabilty we might match the i/p with possible inputs from our records and find **how many words among them matched?**. 
            - for example: user i/p = `how you doing?` matches with `how are you doing?` by 2 words.
    - But this is **not enough to distinguish the intent.** To understand this let's take an example: lets say i/p = `how you doing`, and we have in our poissible input records, `r[0]=what are you doing?` and `r[1]=how are you?`. Here, both records 0 and 1 match the i/p by 2 words. But they mean different things. We must have a way to distinguish between same match score responses. 
    - To combat this problem, we need a way to assign a particular list of required words that must occur in the i/p, for it to match. 
- to return a response, we have to store all the possible response in some file. 
- to return the best response, we can score every response, store it in a list and choose the best.  

## Requirement:
    - yaml
    - pyowm
    - newsapi

## Files needed to run the program:
- config.yml file (in directory containing main)

config.yml must have the following 2 key value pairs
```
weather_api_key: <YOUR-PYOWM-API-KEY>
news_api_key: <YOUR-NESAPI-API-KEY>
```


## Input/Output examples
### Greetings
```
user: hello
Bot: Hello!


user: hey
Bot: Hello!


user: hi 
Bot: Hello!
```
### Temperature
```
user: what is the current temperature?
Bot: Temperature right now is: 50
```

### News
```

user: can you give me some latest news?
Bot: Latest headlines:
--------------------------------------------------------
Judge assigned to Trump case previously said ‘the country is watching to see what the consequences are’ for January 6 - CNN
Stock market today: Live updates - CNBC
Trump indicted over efforts to overturn his 2020 presidential election loss - The Associated Press
Prepare to flick off your incandescent bulbs for good under new US rules that kicked in this week - The Associated Press   
2023 MLB trade deadline grades: Marks for all 30 teams as Angels and Rangers receive and 'A', Yankees fail - CBS Sports    
Jamaica heads to Women’s World Cup knockout stage for first time, as Brazil crashes out of tournament - CNN
DJI's Osmo Action 4 camera comes with a larger sensor and a higher price | Engadget - Engadget
Hosting Ars, part three: CI/CD, or how I learned to stop worrying and love DevOps - Ars Technica
The Galaxy Z Flip 5's cover screen software beats Motorola's in every way but one - The Verge
Behind Ukraine's Deadly Drones: Putin's Invasion and Biden's Limits - The Wall Street Journal
Writers union and Hollywood will resume talks, aiming to end the strike - CNN
Pope Francis urges Europe to work for peace as he lands in Portugal for World Youth Day - The Associated Press
Beyonce honors dancer O'Shae Sibley after stabbing death investigated as hate crime - CBS News
CVS Health turns in better-than-expected 2Q even as pharmacy pricing, increased care use hurt - Yahoo Finance
The 7 things you need to know for Wednesday, August 2 - The Washington Post
Mega Millions next drawing: At $1.25B, jackpot fourth-largest ever - USA TODAY
Why are leprosy cases surging in US state of Florida? - Al Jazeera English
Elon Musk's X/Twitter is letting paying users hide their blue ticks - Mashable
Zendaya pays tribute to Euphoria co-star Angus Cloud - BBC
Rex Heuerma
```

### Day
```
user: what is today?
Bot: Monday


user: what day is today?
Bot: Monday


user: day
Bot: Monday
```
