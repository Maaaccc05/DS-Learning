# What is Machine Learning
    Have you ever wondered how Netflix knows what you want to watch next? or Google Translates works like Magic?
    The secret Behind it all is Machine Learning
    Machine Learning is a way of teaching computers to learn from data - Just like we humans learn from expierences
    Insted of programming every step, we give machines lots of data and let them figure out patterns on their own

    1. Youtube Recommendations -> Learns from your watch history
    2. Spam Detection in Gmail -> Learns Patterns in spam emails
    3. Voice Assistant(Siri, Alexa) -> Learn how you speak
    4. Self-driving cars -> Learn to identify stop signs, pedestrians, and roads
    5. Face Unlock on phones -> Learns to recognize your Face

# Types of ML
    Supervised Learning 
    We train machine based on input nd output cabins from that machine creates pattern nd gives output 

    Unsupervised learning 
    In this we get data buf we don't predict anything 
    We just put data in it in format of input

    Reinforcement Learning 
    This training is like teaching dog it's based on trial nd error if machine gives right ans we will reward else will punish 
    Ex Machine playing flappy game

# EDA - Exploratory Data Analysis 
    We explore data in EDA
    Viewing Data
    * head() shape info, tail
    Summary statistics 
    Mean, median, mode, std, min, max

    Value counts - How many uniques values are there 

    Missing value analysis 
    Visualization 
    Target variable exploration

# Data cleaning 
    1. Removes Duplicates
    2. Fix Data types
    3. Handle inconsistent Categories
    4. Detect and Handle Outliers
    5. Fix Logic or Domain errors

    EDA tells you what's wrong. Data cleaning Fixes it . Cleaning is not glamorous, but it's 80% of the work in real world projects

# Data preprocessing
    To prepare clean data so it can be analyzed or used in a machine learning Model.
    If Data Cleaning is about fixing mistakes,
    Data Preprocessing is about transforming valid data into a usable format.
    1. Encoding categorical variables
    2. Two common methods :
        * Lable Encoding(ordinal)
        * One-Hot Encoding(nominal)
    3. Feature Transformation
    4. Feature Scaling (Normalization and Standardization)
    
    Normalization(Min-Max scaling ):
        Scales values betn 0 and 1
    Standardization(Z-score Scaling ):
        Transforms data to have mean 0 and 1

# Feature Engineering 
    Creating new features or transforming existing ones to expose useful patterns that ML models can learn
    ML models don't know domain logic we have to give them the right signals

    Techniques : 
            * Mathematical combinations
            * Target based flags
            * Binning (when it helps)
            * Time-Based Features(if time exists)

# Feature Selection
    selecting the most useful features and removing the rest 


# What is Regression Algorithm?

    Flow: Start --> Collect Data --> Define Variables --> Split Dataset --> Train Model --> Calculate Coefficents --> Make Predications --> Evaluate Model --> if Model is satisfactory Deploy it --> If not then perform steps from Split Dataset

    Regression is way to predict a number. It helps us find out how one thing change when something else changes
    Regression is about finding pattern and numbers so we can make smart predictions

# How to create best fit line

    y = mx + b -----> m = slope, b = Intercept, x = Data point, y = prediction