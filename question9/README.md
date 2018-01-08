# Solution

## 1. `Overview`
>The Twitter API V1.1 requires Oauth, which would require backend code to be run from a server served to a fully qualified domain name. Neither of these things were provided to me and would otherwise cost me money. So instead, I decided to fulfill the desired functionality by means of writing a javascript web-scraper. This does use a proxy CORS url, so it is not intended for commercial use.

1. After entering a twitter handle, the app, calls "whateverorigin" + the twitter url we want(Whateverorigin.com is a CORS bypass service).
2. Regex through the source code for the tweet contents
3. Regex through the source code for the date contents
4. Then it returns the html skeleton we need to the webpage with ```.html```
5. Finally it calls the ```countwords()``` function which gets the content of an online word dictionary to do list comprehension on to calculate each tweet's word count(This takes a few seconds to complete for each tweet.)

## 2. `Build/Compile/Run`
As this is an .html file, any web browser will be able to display [question9.html](../question9/) and [question10.html](../question10/)

Enter any twitter handle you like, and it will retreive the last 5 tweets, the date and time they were tweeted, and the english dictionary word count.

## 3. `Output`
Different twitter handles may be entered. The results will be printed in 5 divs with the tweet number(in royalblue), the date and time below(in black), and the word count(in grey, to the right). 

It may take a few seconds for the word count to load on each tweet as it is looking through almost 500k words.
