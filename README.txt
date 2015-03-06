COMS E6111 Advanced Database Systems (Columbia Computer Science, Prof. Luis Gravano)

Spring 2015 Project 1

Relevance Feedback & Query Expansion

(assignment: http://www.cs.columbia.edu/~gravano/cs6111/proj1.html)

a) Team members:

Meril Dsouza - msd2178

Utkarsha Prakash - up2127

b) List:

README

Demo.py

Weights.py

MyRocchio.py

transcript_musk.txt

transcript_gates.txt

transcript_columbia.txt

c) Run the project by running the Demo.py file as follows:

==============================================================

python Demo.py

==============================================================

You will then be prompted to enter the query and desired precision as follows:

==============================================================

Enter the list of query words :gates
Enter the precision desired (between 0 and 1): .9

==============================================================

You will then be presented with a total of 10 search results from Bing. Each results contains the Title, Description, and URL.
Each result will ask the user if it is relevant or not. 
User inputs 'y' if relevant and 'n' if it is not. An unbiased input from the user is required so as to yield the appropriate results.

The first result will appear as follows:

==============================================================

Title: Gates Corporation
Description: Gates Corporation is Powering Progress™ in the Oil & Gas, Energy, Mining, Marine, Agriculture, Transportation and Automotive Industries.
URL: http://www.gates.com/
Is it relevant? (y/n) :

==============================================================

d) A clear description of the internal design of your project

The project flow is as follows:

First the user is asked to enter a search query along with the precision he desires.
The Bing API then returns the top 10 search results. The title, description, and URL of each result is displayed to the user. The user is then asked if that result is relevant to his search query or not, to which the user must provide his feedback in the form of 'y' or 'n'.
This process continues for the top 10 results from Bing.

Next the precision is calculated based on the user's feedback. If the precision calculated is greater than or equal to the target value, then stop. Else, the users feedback is utilized to generate a new and improved search query which will improve the precision of the results. (Explained in detail in the next section.)
This process continues until we reach at the least the target precision.



e) A detailed description of your query-modification method:

We first calculate the term frequency–inverse document frequency of each term present in the documents. The term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document. We use this value as a weighting factor to help us identify the useful words that can improve our query. The tf-idf value increases proportionally to the number of times a word appears in the document. We perform normalization on these values to finally get the weights of each term in each document.

Query Expansion: For the query expansion we have used Rocchio implementation which can uses reasonable parameters of alpha, beta and gamma. Based of tf-idf and the relevance feedback of the user we modify the weight for the terms in the summary using Rocchio algorithm. We then pick the top 2 weighted terms for addition to the query.
Ordering of terms: For the ordering of terms we are using bi-gram probability for the sentence. We are currently adding just the bi-gram with maximum probability in the right order. Since we are adding 2 additional keywords after every iteration, addition of 1 bi-gram can slowly expand to a sentence with the right order. We have currently considered this approach rather than adding multiple bi-grams.


f) Bing Search Account Key: Amj5zEym/93UZqhYv2TvvO9pgzU1mcewT7NNWAm9JMY

