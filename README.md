### YouTube API Sentiment Analysis Introduction
This is a python project that makes up the first part of the Sentiment Analysis.
The dislike button was recently removed from YouTube, which was met with much opposition online. This news was broken to the world in the video ["Update to YouTube's Dislike Count"](https://www.youtube.com/watch?v=kxOuG8jMIgI), by YouTube Creators, which has reached over 3.6 million views as of August 2022.
Although the change was initially met with hostility, the video does state very real issues the change looks to tackle. After letting this solution settle for several months, this project aims to understand if overall sentiment has changed and if the solution is being embraced by the community.
### Usage
Simply download the file and replace the video key with a video of your choice. You do need to sign up for credentials and an API key on the YouTube API website, and make a .env file with the key inside the file for the calls to work.
### Notes
- A small condition was included in the while loop in line 26 to limit calls to the API. On its own, the loop will continue to call the API until there is no new page of comments. Especially for big videos with lots of reviews like the video mentioned above, the unrestricted loop would make too many calls and exceed the daily quota of the API. If this condition is not needed, simply remove the counter and the condition.
- The comments are fetched in order of most recent. This was to ensure that the opinions found in the comments would be a proper reflection of current times.
