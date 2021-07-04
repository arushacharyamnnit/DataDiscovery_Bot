# DataDiscovery_Bot
The main aim of the project is to develop a bot which can cater to the user’s ad-hoc queries regarding the metadata information related to job, catalog and glossary items. The Bot has been integrated with slack where it can cater to the user’s queries.

Install the following in your system before proceeding:
- VS Code
- Python 
- MySQL Installer
- Elastic Search
- Kibana
- Ngrok
- Slack

Set-Up:

Create a Virtual Enivronment by running following commands
- pip install virtualenv
- virutalenv env
Now enable the virtual environment by
- .\env\Scripts\activate.ps1

All the configurations and execution part should be done after enabling the virtual environment

Now install all the dependencies from requirements.txt file

Traning the NER models:
- For training the models, first you create the train_data.spacy but here those are already created and present in data1,data_ocidw and data_gloss folders for job, catalog and glossary respectively. 
- If you want to create your own config file instead of using the provided config file, go to https://spacy.io/usage/training and copy the default
base_config file by checking on ner in components section and accuracy in optimize section and paste in base_config.cfg
- Run this command to create/overwrite the config.cfg file
 - python -m spacy init fill-config base_config.cfg config.cfg
- In config file, under train and dev, provide the path of train_data.spacy file depending on which model you want to train
-To train your model, run the following command
 - python -m spacy train config.cfg --output ./output 
- The above command will create a folder with name 'output' and later it can be loaded in the server to use it


Setting up Slack worksapce and Configuration of bot on api.slack.com :

- Register yourself on slack (if not having an account)
- Create a new workspace in it
- Go to api.slack.com->your apps and then select 'create new app' and then enter your app name and choose the workspace in which you want to add it
- Got to OAuth & Permissions section->scopes and add the following scopes to bot:
 app_mentions:read, channels:history, chat:write, commands,  im:history, im:read, im:write
- Go to Basic information section, copy the Slack Token and then go to  OAuth & Permissions section, click on 'install app to workspace' and paste the slack token there and reinstall app to workspace
- Copy Slack token and Signing secret from Basic Information section and then in VS code, under Server directory create a .env file and add the variables and paste the corresponding values of Slack token and Signing secret:
 - SLACK_TOKEN='your unique slack token'
 - SIGNING_SECRET='your unique signing secret'



Database Configuration:

- Start the Elasticsearch and kibana at your localhost servers by going to their respective bin folders and opening the terminal and running follwing commands
- elasticsearch.bat     # on elastic search cmd
- kibana.bat            # on kibana cmd

- In Database->ElasticSearch, run all the python files to upload the data to elasticsearch

- Open you Mysql workbench, and make a new mysql connection
- Create a schema in it and then create the the tables following ddl.txt file
- You can change the user , password and database name in mysql.connector.connect in Databse->MySQL according to your connection name, password and schema name respectively



Running and Execution guide:

Start the Elasticsearch and kibana at your localhost servers
- elasticsearch.bat     # on elastic search cmd
- kibana.bat            # on kibana cmd

Start the ngrok server 
- ngrok http 5000
- Copy the the url and go to api.slack.com->your apps and click on your app name
- Under the Events Subscriptions section, paste the url and add /slack/events to it and save the changes
- Under Interactivity and Shortcuts section, paste the url in Interactivity space and save the changes
- Under Slash Commands section, paste the url in all the endpoints created and save the changes

- Enable virtual environment on VS code and run the app.py file
- python .\app.py

Open your personal workspace where your app is integerated and you can chat with bot as a DM or in the channel.







