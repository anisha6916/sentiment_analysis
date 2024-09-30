# sentiment_analysis

### Introduction:
Our project is a machine learning model that identifies the sentiment of user-inputted text as ‘positive’, ‘negative’, or ‘neutral’. We trained this model using a dataset that contains tweets labeled with one of the three sentiments. We decided to train our model using tweets since we wanted to examine whether tweets (which differs in language from regular speech) could produce accurate predictions when used for regular sentences (slightly different than models that currently exist).


### Technical Architecture:
<img width="934" alt="Screen Shot 2023-12-04 at 1 35 09 AM" src="https://github.com/CS222-UIUC-FA23/group-project-team12/assets/116782914/ad7917de-41c9-47ea-9c69-35b213105130">

Our project's backend consists of python and its frontend consists of ReactJS and is tied together using Flask. We built our MultinomialNB model in python using libraries such as scikit-learn (sklearn) and pandas. Using joblib, we were able to extract our model and vectorizer and use it in our Flask setup to build a function that would run the sentiment predictions for inputted sentences. This was our tie to our React App, which consisted of our website design and user interface.

### How to SetUp Sentiment Analysis on Your Machines:
#### Setting up the Virtual Environment:

Run this command in terminal to create the source directory:
```
python3 -m venv venv
```

Run this command to activate the virtual environment (you are going to have to run this everytime you start up your code again):
```
source venv/bin/activate
```

#### Flask installation (run in terminal):
```
pip3 install flask
```
  
#### Necessary Packages to install (run in terminal):
```
pip3 install pandas
pip3 install scikit-learn
pip3 install joblib
pip3 install numpy
```

#### Setting up Frontend(React):
Make sure you have Node.js installed. If you do not, download node.js from https://nodejs.org/en/download/ and follow the installation instructions.
First, move into the client folder.
```
cd client
```

During your initial setup, check to make sure node and npm are properly installed.
```
node -v
npm -v
```

Next, you will set up your node_modules folder. Make sure to check if this folder appears in your client folder after you have run the command.
```
npm install
```

Now, to start the React app, run the following code in terminal within the client folder.
```
npm start
```

These are the steps that we found were needed to run this code on our machines. However, since everyone's machines are different, there may be some further conflicts that you will need to resolve before the code runs smoothly on you machines. We recommend copying and pasting the errors into Google and following further instructions that are recommended to resolve the conflicts.

### Group Members and their roles:
#### Shriya
* Worked on backend (Python)
* Worked on connecting the frontend to the backend (Flask)
#### Anisha
* Worked on backend (Python)
#### Ashwini
* Worked on frontend (React)
* Worked on connecting the frontend to the backend (Flask)
#### Nivedita
* Worked on frontend (React)

#### Everybody
* Worked on resolving issues with pushing our code to Github, running our application on different machines, and writing setup instructions
