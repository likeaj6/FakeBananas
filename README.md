# Fake Bananas
Fake news detection made simple and scalable for real people. 

> **Note:**
> - This project is ***a work in progress*** for HackMIT. We'll be done soon.
> - If you would like to contribute please reach out to one of us through GitHub! You're more then welcome.
> - If you experience any problems, please create an Issue.

## Working information

1. Only file to be run is `pipeline.py` in root director. 
2. All discrete portions of code are contained in respective directories.


## How this works

Our fake news detection is based on the concept of ***stance detection***.  Fake news is tough to identify. Many 'facts' are are highly complex and difficult to check, or exist on a 'continum of truth' or are compound sentences with fact and fiction overlapping.  The best way to attack this problem is not through fact checking, but by comparing how reputible sources feel about a claim.

1. Users input a claim like *"The afganistan war was bad for the world"*
2. Our program will search the thousands of global and local news sources for their 'stance' on that topic.  
3. We run sources through our Reputability Algorithm. If lots of reputible sources all agree with your claim, then it's probably ture!
3. Then we cite our sources so our users can click through and read more about that topic!



### News Sources
@Henry

### Determining Reputation
@Josh

### Stance Detection
@Kastan


### Frontend backend info?
@Jason

## Other (worse) methods
##### 1. Fact checking
Some teams try to granularly check the truth of each fact in an article. This is interesting, and may ultimately be a part of some future fake news detection system, but today this method is not fesible. The truth of facts exists on a continum and relies heavily on the neuance of individual words and their connotations. The neuances of human language are difficult to parse into true/false dichtomies.

1. Human language is neuanced. Determining a single statement as true or false 
2. No databases of what's true or false
3. Many facts in a single article exsiting on all sides of the truth spectrum -- is that article true or false?  

##### 2. 'Fake News Style' Detection
Some teams try to train machine learning models on sets of 'fake' articles and sets of 'real' articles.  This method is terrible because fake news can appear in well written articles and vice versa!  Style is not equal to content and we care about finding true content.
