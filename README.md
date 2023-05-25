# Violin players pose estimation

## Links to Colab Notebooks
### Experiment: Distinguish between I, S, C
Vlad: https://colab.research.google.com/drive/1HW-VPXOxJYWOASW_ykiMYC_BkHefwB55?usp=sharing
Tanya: https://colab.research.google.com/drive/1XfzwqvEy8uZXX_l2Us3reG9Acvu3UkKc?usp=sharing

## Paper analysis

### Tanya's notes 
Most important info for https://link.springer.com/article/10.1007/s12559-020-09768-8:
* problem can be transformed to binary classification -> challenge: extract features
* Suggestion for binary class problem: Random Forest + eval: confusion matrix & accuracy
* Create features:
  1) Sample time series of different features: left
head inclination, left wrist roundness, (idea: elbow movements). 
  Fixed-width sliding windows of 10 s is applied. Fixed-width sliding windows
have 50% of overlap in time. In order to analyze clear data and avoid
noise due to the initial and final moments of recording,
only timestamps where a piece of music is played are
chosen.
  2) Create feature vector from each extracted time series. The values of the vector are presented in the table 2.
  3) Apply model

## Ideas summary
For every movement consider not just angle, 
but also the change in the position in comparison with the previous point.
For every time series data, the features can be extracted: mean, var, max, min (see table 2 in https://link.springer.com/article/10.1007/s12559-020-09768-8)
Following movements can be analyzed:
Angles: 
* head inclination (12-0-11)
* left wrist roundness (15-19-17)
* right elbow movement (11-13-15) **MOST IMPORTANT**
* right shoulder (23-11-13)
* player should sit straight: the two hips need to be on a straight line (24-23-25)
* fingers' positions (13-15-17)
* the same for the left side as for right
* analyze if the face muscles are moving (8-10-9 and 7-9-10) (if the person is smiling -> noise is not good)

Relative position:
* right elbow **MOST IMPORTANT**
* right wrist
* hips
* knees
* shoulders
* position of nose (to define if the head is holded stanble)
* relative distance from noise/month/eyes - create metric to define if the person laughing

# Interesting papers:
https://towardsdatascience.com/feature-engineering-on-time-series-data-transforming-signal-data-of-a-smartphone-accelerometer-for-72cbe34b8a60