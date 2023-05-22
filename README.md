# Violin players pose estimation

## PaperS analysis

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
* head inclination
* left wrist roundness
* left wrist movement
* right wrist movement
* left elbow movement
* right elbow movement
* sitting straight
* analyze if the face muscles are moving (if the person is smiling -> noise is not good)

TODO: define some formulas to track the described movements