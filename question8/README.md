# Solution

## 1. `Overview`
>This problem took me some time. After reviewing the graphic provided, I initially thought that I would need to take the amount of data points in the file, square root it, and then use that value to create an actual grid full of all the data points. However I realized this was not necessary and developed the solution provided.

1. The json file is opened and passed to each function
2. ```findmostfrequentword()``` Iterates through the json object for each item in 'words' array. It returns the max number of occurenced words
3.```findmostfrequentwordyesterday()``` First runs through the conditional to determine yesterday's date. It then iterates through the json object for each item in 'words' array. It returns the max number of occurenced words for that particular date(yesterday)
3.```findtrendingword()``` Essentially this needs to calculate the max number of occurences for both today and yesterday, and compare the two for the same word and the highest difference in todays occurences compared to yesterdays'. Code comments provide more detailed info.

## 2. `Build/Compile/Run`
(Depending on your enviromental path variables)To build/compile this solution, with python installed, simply navigate to question8/ directory and run...

    $  python question8.py

or

    $ python3 question8.py

You may use my mongodbexample.json file(You will have to change the dates on the documents for it to work correctly) or create your own in the same json structure. I chose the example to be in JSON as a baseline for a relational database example.

## 3. `Output`
The output will be answer the questions posed in the question8 prompt in the same order they were asked. The output should look like this...

```
The most frequent word found in the documents is: bar
The most frequent word found in the documents with yesterday's date is: baz
The trending word is: qux
```
