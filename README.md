# Physician Rules
## Design
### Django
I chose django as my web framework because my main concern was development time. Django is faster than it's counter part, ruby-on-rails, however Django is less scalable than Node.js and express, PHP and laravel, or Java and Spring. Scalability was sacrificed for development time.
### PostgreSQL
I chose postgresql as my database because django works great with relational databases and postgres is one of the fastest and most support RDB there is. A noSQL document database would have been just as useful, as the rules are stored in JSON format and there is not actually any relations between database entries. But again, RDB's work out of the box with django and development time was a priority.
### Venmo Business Rules Engine
I chose venmo's Business Rules engine as it met all of the requirements of this project and was well documented. The rules engine pulls rules from JSON and the UI pulls parameters from the backend. The UI also supports loading existing rules for editing and updating. Again speed was sacrificed for development time, the rules engine is not run asynchronously so as rules get more complex and plentiful the loadspeed after clicking "Run rules" will slow down. Since rules can be run in the background, runtime is not actually an issue here.
## Usage
* Clicking submit a new entry on the main page will allow you to submit a new Physician entry. The values you enter are validated serverside to avoid sql injections and invalid parameters.
* Clicking view existing entries will allow you to view all existing Physicians. Clicking on an existing Physician will bring you to a page that shows all of the original parameters entered, and the output of the rules engine. If the rules have changed since the last time you ran the rules engine, you can press the large "Run rules" button to update the output in the database.
* Clicking edit rules engine will allow you to either create a new rule or edit and existing one. After setting the names and conditions of the rule, click generate rule data, followed by SUBMIT and the rule will be created. 

## Setup
1. Setup and activate a virtual environment for python
    ```
    python3 -m venv env
    source env/bin/activate
    ```
1. Install required modules
    ```
    pip install -r requirements.txt
    ```
1. Place your secret key as an environment variable
    ```
    export SECRET_KEY=donttellanyoneok
    ```
1. Run development server
    ```
    python manage.py runserver
    ```
