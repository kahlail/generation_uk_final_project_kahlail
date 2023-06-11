# Brew-Tea-Full Final Project
![Untitled_Artwork 6](https://user-images.githubusercontent.com/109074529/231804566-2a389d56-46c7-4b31-a678-c8d057143d71.png)
_____________________________________________________________________________________________________________________

# Elevator Pitch!

Our café owners (SuperCafé) want to be able to; <br />
• monitor multiple stores, <br />
• obtain sales data and, <br />
• check the performance of individual products. 

**We offer** a backend system that visually displays sales data and more from multiple data sources. 

The system enables the owner to check live data, such as the number of coffees sold and their most loyal customers **unlike their current manual analysis system** which is time-consuming. 

**With our product**, Super Café can conveniently and securely reorder stock, discover marketing opportunites, and review sales data from the comfort of their own location.

_______________________________________________________________________________________________________________________

# Project Goal

***The solution*** <br />

As a team, our solution was to create an Extract Transform & Load (ETL) pipeline, deployed using Amazon Web Services (AWS). The ETL we designed is able to get value from and load around 100 .csv files of data daily into a relational database. We enabled client-side functionality through interpretation of crucial sales data. We were able to monitor the performance of our ETL pipeline by using CloudWatch and integrate this information as well as sales data with our chosen dashboard tool (Grafana).
<br />

![image](https://github.com/kahlail/generation_uk_final_project_kahlail/assets/109074529/eb0b0aa4-09f2-49eb-9d9d-0d27e3b2bc2d)


In order to achieve this we will work together using agile methodology (scrum). We have created a ways of working document which can be viewed [here](https://github.com/generation-de-lon9/brew-tea-full-final-project/blob/main/documentation/ways_of_working.MD). This document also outlines our group definition of 'done'.

Our primary focus was to deliver the bedrock technical requirements before adding extra functionality which we achieved in five weekly sprints. 


_______________________________________________________________________________________________________________________

# Team Members

[Charlene](https://github.com/ck1ldn) <br />
[Kahlail](https://github.com/kahlail) <br />
[Minhaz](https://github.com/mu601) <br /> 
[Sajjad](https://github.com/spopal) & <br />
[Zain](https://github.com/Zainkhanshin)

_______________________________________________________________________________________________________________________

# Technology Stack
• Python 3.10  <br />
• Postgres  <br />
• AWS Services including S3, Lambda, Redshift, Quicksight and Cloudwatch  <br />
• Grafana
_______________________________________________________________________________________________________________________

# How to run our code locally

We recommend creating a virtual enviroment, where you can download the dependencies from our [requirements.txt](https://github.com/generation-de-lon9/brew-tea-full-final-project/blob/main/src/requirements.txt) file. <br />

1. From the root (brew-tea-full-final-project), move your terminal into the correct folder
```
cd src
```
<br />

2. Creating a virtual environment on Windows
```
py -m venv .venv
```
<br />
&nbsp; &nbsp; &nbsp; Creating a virtual environment on Mac 

```
python3 -m venv .venv
```
<br />
<br />

3. Activate virtual environment on Windows

```
.venv\Scripts\activate
```

&nbsp; &nbsp; &nbsp; Activate virtual environment on Mac
```
source .venv/bin/activate
```
<br />
<br />

4. Installing dependencies
```
pip install -r requirements.txt
```
<br />


