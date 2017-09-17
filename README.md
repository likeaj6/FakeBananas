# Fake Bananas
Fake news detection made simple and scalable for real people. 

![alt](https://user-images.githubusercontent.com/13607221/30521745-822c4900-9b92-11e7-9fcf-d8ec6ad4a186.png)

## Getting Started 
I would strongly recommend a `conda` environment in order to easily install our older version of TensorFlow. We used `TensorFlow 0.12.1` for backwards compatibility with previous work in the field.
Newer versions of TensorFlow may work, but certainly not 'out of the box'.

```bash
# download and install anaconda
# python 3.5 is required for this version of TensorFlow
conda create --name FakeBananas python=3.5
NumPy==1.11.3
scikit-learn==0.18.1
TensorFlow==0.12.1
# note: older versions of TF (like 0.10) require less modification to use than newer ones
Pandas
eventregistry
watson_developer_cloud # IBM api signup required
py-ms-cognitive # microsoft 

```

## How this works

Our fake news detection is based on the concept of ***stance detection***.  Fake news is tough to identify. Many 'facts' are highly complex and difficult to check, or exist on a 'continuum of truth' or are compound sentences with fact and fiction overlapping.  The best way to attack this problem is not through fact checking, but by comparing how reputable sources feel about a claim.

1. Users input a claim like *"The Afghanistan war was bad for the world"*
2. Our program will search the thousands of global and local news sources for their 'stance' on that topic.  
3. We run sources through our Reputability Algorithm. If lots of reputable sources all agree with your claim, then it's probably true!
3. Then we cite our sources so our users can click through and read more about that topic!



### News Sources
After combing through numerous newspaper and natural language processing APIs, I discovered that the best way to find related articles is by searching for keywords. The challenge was implementing a natural language processing algorithm that extracted the most relevant keywords that were searchable, and to extract just the right number of keywords. Many algorithms were simply summarizers, and would return well over 50 keywords, which would be too many to search with. On top of that, many algorithms were resource exhaustive and would sometimes take up to a minute to parse a given text.

In the end, I implemented both Microsoft’s Azure and IBM’s Watson to process, parse, and extract keywords given the URL to a news article or a claim. I passed the extracted keywords to Event Registry’s incredible database of almost 200 million articles to find as many related articles as possible.  

With more time, I would love to implement Event Registry’s data visualization capabilities which include generating tag clouds and graphs showing top news publishers given a topic.
-@Henry

### Determining Reputation
Using a large set of default sources with hard coded reputability, our database of sources continues to become more accurate with each web scraping by adding new sources and articles. To ensure this makes our algorithm better, the weights of each source are adjusted according to how much each new article agrees or disagrees with sources determined to be reputable. In the future, we would love to implement deep learning to further advance this ‘learning’ aspect of our reputability, but the current system more than supplies a proof of concept.
-@Josh

### Stance Detection

To determine if a claim is true or false, we go out and see where sources which are known to be reputable stand on that issue.  We do this by leaning on established machine learning principles used for 'stance detection.'  So we:

1. Ask the user to input a claim (which holds a 'stance') on a topic.  A claim might be "ISIS has developed the technology to fire missiles at the International Space Station." 
2. We search databases, and scrape web pages, to find other articles on that issue.
3. Then run our 'stance detection' machine learning algorithm to determine if reputable sources generally agree or generally disagree with that claim.  *If many reputable sources all agree with a claim, then it's probably true!*
 
Our stance detection is run by [Google's Tensorflow](https://www.tensorflow.org/) and our model is built off of the work of the fantastic people at University College London's (UCL) [Machine Reading group](http://mr.cs.ucl.ac.uk/).  -@Kastan
 
### Frontend/backend info
Our backend is written on a Flask python server which connects to our front-end written in JavaScript. 

## Other (worse) methods
##### 1. 'Fake News Style' Detection
Some teams try to train machine learning models on sets of 'fake' articles and sets of 'real' articles.  This method is terrible because fake news can appear in well written articles and vice versa!  Style is not equal to content and we care about finding true content.
##### 2. Fact checking
Some teams try to granularly check the truth of each fact in an article. This is interesting, and may ultimately be a part of some future fake news detection system, but today this method is not feasible. The truth of facts exists on a continuum and relies heavily on the nuance of individual words and their connotations. The nuances of human language are difficult to parse into true/false dichotomies.

1. Human language is nuanced. Determining a single statement as true or false 
2. No databases of what's true or false
3. Many facts in a single article existing on all sides of the truth spectrum -- is that article true or false?  

## Team Members
- [Kastan Day](https://github.com/KastanDay)
- [Josh Frier](https://github.com/jfreier1)
- [Henry Han](https://github.com/hanksterhan)
- [Jason Jin](https://github.com/likeaj6)


### Acknowledgements
[The Fake News Challenge](fakenewschallenge.com) provided great inspiration for our project and guiding principles for tackling the task.


The University of College London's short paper on the topic:
```latex
@article{riedel2017fnc,
    author = {Benjamin Riedel and Isabelle Augenstein and George Spithourakis and Sebastian Riedel},
    title = {A simple but tough-to-beat baseline for the {F}ake {N}ews {C}hallenge stance detection task},
    journal = {CoRR},
    volume = {abs/1707.03264},
    year = {2017},
    url = {http://arxiv.org/abs/1707.03264}
}
```
