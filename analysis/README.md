***In this direcotry I will be performing my analysis on my data set on credit card default rates***
# I hope to answer my research question regarding whether there are correlations between credit card default and people 
*Milestone 1 Analysis*
# I imported my data into my analysis file, and got a first look at all the variables and rows
*Milestone 2 Analysis*
# I started to explore my data and mess around with: 
`.info()`

`.describe()`

`.mean()`
## I also started wrangling my data by renaming columns that did not makesense to me, such as PAY_0 to PAY_1, and shortened some of the column names as they long and cumbersome when coding

### I then created my first method chain, it was fairly simple once I got the hang of it and then converted it into a function so it is more versatile and then created my first python module! 

### I also did my first round of analysis on my two research questions, and was able to draw some initial conclusions. 
 
 1.Starting with question 1:What is the distribution of the credit card in this dataset and is there any correlation between the limit balance and default rate?
### Summary of findings: 
- Based on the above, there are 81 different limit balances given in the dataset. The limit of 50,000 has the highest number of clients with 3365 individuals with that limit. Most defaults are for credit limits 0-100,000. The larger default number is for the amounts of 50,000, 20,000, and 30,000.
### Insight: 
- I'm intrigued by how the rate of default is highest at the credit limits of 50,000, 20,000, and 30,000. My initial thoughts were that higher default would be correlated to lower limit balances as riskier clients would normally have lower limits. It could be my initial thoughts are wrong.
### Conclusion:
- After my above analysis and visualizations, the range of balance limit is from 1000 to 1000000. In regards to correlations between default and limit balances, the limit balances between 20,000 to 50,000 seem to have higher default rates.
2.Are there any conclusions that can be drawn about different types of people defaulting on their credit cards?
### Summary of findings:
- Sex: Interestingly enough, in my EDA I said that it seemed as though women had a higher default rate and said that it may be due to their being more females in the data. But now that I have plotted gender and default alone, it seems that men have a higher default, which is interesting as there are fewer of them overall. 
- Age: The barplot is a bit busy in this format, I may draft a new one with age ranges over 5 years such as 20-25, etc.. to not have so many X variables. But looking at the barplot above, there is still some interesting insight. For the most part default rate is fairly steady from 20% to 40% but there are a few instances at 73 where the default is a lot higher, this may be due to one or a few data points thought so no real conclusion can be drawn yet of whether this is a true value or simply an outlier. 
- Marriage: Looking at the three variables, single and married are fairly close between 20% and 25% rates of default. The other category is interesting, in my EDA the visualization I used wasn't very insightful on default for those in this category but now I can see that even though overall there are fewer data points the rate of default is high. 
- Education: This visualization is interesting as well. The highest rate of default is category 3 which is high school education, yet the number of data points for high school is a lot less than 1 or 2 which corresponds to post-secondary schooling. This also differs from my EDA analysis. 
### Insight:
- One thing I've noticed by using this sort of visualization is that I can't see the number of data points that correspond to each X variable, so although it may seem that one variable has a higher default rate, this may be due to several factors such as more/fewer data available for such range. 
- But still, this does give me some insight into what better visualizations should include and helps guide me to a better way to find a more concrete answer to my research question.

### Conslusion:
- At this point, my initial conclusions are: (***These may change as I change my visualization/ create new ones***)
- Sex: Men may have a higher rate of default.
- Age: Default based on age seems to be fairly consistent, besides a few outliers at later ages. 
- Marriage: The other category seems to have a higher rate of default this may be due to the surrounding circumstances that get someone classified as "other".
- Education: It seems that higher education might correlate with less defaulting.

