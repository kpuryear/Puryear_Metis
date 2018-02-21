## Files included in Project3:

### NoShows.csv
- Original untouched data, downloaded directly from kaggle

### Proj3-Data_cleaning.py:
- Shows my data cleaning process
- Shows my feature engineering
- Returns a cleaned CSV file

### noshowclean_n.csv
- Cleaned CSV file
- Formatted for uploading data to a SQL table

### Proj3-Modeling.py:
- Shows my process for modelling the data
- SQLalchemy engine inplemented
- Stratified Train Test Split with upsampling
- Fit models: KNN, Logistic Regression, Naive Bayes, Decision Tree, Random Forest
- Analyzed ROC Curves and various scoring metrics

### MVP3.pptx:
- A rough presentation of my initial findings 

### Presentation3.pptx
- Complete presentation I gave to wrap up the project and communicate my completed results

### dataviz (folder)
- Folder contains files needed for my interactive D3 visualization:
- Noshow.p (pickled model)
- Awesome.html (webpage rendering html)
- Main.py (flask-assisted python functionality to feed into the html)
