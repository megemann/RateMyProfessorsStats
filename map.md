# RateMyProfAnalysis
Data Analysis and Summarization of Data from Rate My Professor Reviews 

## Link
https://RMPStats.vercel.app

## Dashboard roadmap:

### Professor Page
(V1)
- Quality rating over time
    (1) Rolling window average
    (2) Overall average regardless of date
- Difficulty rating over time
    (1) Rolling window average
    (2) Overall average regardless of date
- would take again percentage
    (1) time series
    (2) overall percentage
-  attendance mandatory percentage
    (1) overall percentage
- Rating tags distribution
    (1) Overall distribution
- isOnline
    (1) Overall percentage
- isForCredit
    (1) Overall percentage
- Comment
    (1) avg comment length
    (2) something with sentiment analysis
- Filter by class (No analysis, just filter)
- Date span, and heatmap or bargraph of reviews by date

(V2)
- interaction score
    (display score) - Something with thumbs ups and downs, plus # of comments 
- Extractive summary of comments
- Filter by class (with overall class analysis)
- Average grade in class (note - this will be skewed because people reviewing are more likely to review if they did well in the class or did terribly)
- Review volume trends (are they getting more/fewer reviews over time?
- Rating tags distribution
    (1) Make into categories (all options listed on RMP website) then maybe display over time or somehow
- Red flags" analysis (combination of low ratings + specific tags)

(V3)
- Topic summarization
    - Use LDA to get topics
    - Use the comments to get the topics
    - Display the topics and the comments associated with them
- Seasonal patterns in ratings (e.g., Fall vs Spring semester comparisons)
- Best professors for classes
- AI-generated teaching style summary

(V4) - Advanced ML
- Predictive graph of difficulty rating 
- Cluster professors by rating and department (if in top 100 US universities)
- Predict school size, rating, etc from reviews
- Course matching (Top 100 US universities, combine similar courses)
- review authenticity 
- Time series prediction
- Recommendation system (top 100 US universities)



### Overall stats - home page for Top 100 US Universities (w/ disclaimer)

V(1)
- Overall average quality rating
- Overall average difficulty rating
- Overall would take again percentage
- Overall attendance mandatory percentage
- Overall rating tags distribution
- Ratings over time
- Just overall help the people understand the data they are looking at more
- Look at Preprocess & EDA for more ideas

(V2)
- Department-level comparisons across universities
- Gender analysis in ratings (generate by guess of first name)
- Course level distribution (intro vs advanced courses)
- Online vs In-person teaching effectiveness
- University ranking correlation with ratings
- Seasonal trends across universities


(V3)
- Geographic analysis of ratings patterns
- Class size impact on ratings
- Teaching experience correlation with ratings
- Department-specific rating patterns
- Rank universities by overall rating and other things

(V4)
- Predictive graph of difficulty rating 
- Cluster professors by rating and department (if in top 100 US universities)
- Predict school size, rating, etc from reviews
- Course matching (Top 100 US universities, combine similar courses)
- review authenticity 
- Time series prediction
- Recommendation system (top 100 US universities)
    


