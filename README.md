# Covid19 Dashboard
Tutorial to create a simple Covid19 dashboard using Python and Dash. Deploy the dashboard in Heroku.

In the command prompt navigate to the folder where this python file is saved in your local system and execute it. The output dashboard will be displayed in the default Dash url http://127.0.0.1:8050/. In the browser open this url, and voila your dashboard is displayed.

To deploy this dashboard in Heroku you have to first create a account in Heroku and GitHub. Heroku is a cloud platform as a service supporting several programming languages. You can build and deploy applications easily on the Heroku platform. Get all the information about working with Heroku at https://devcenter.heroku.com/. 

Open command prompt, navigate to your project folder location, and type the following commands:

heroku login (login to your heroku account)
heroku create "app name" (provide a name for your app, which will be used during deployment)
Create Procfile by typing the following command:

echo web: run this thing >Procfile
Procfile is a mechanism for declaring what commands are run by your application's dynos on the Heroku platform. Learn more about Procfile at https://devcenter.heroku.com/articles/procfile

Open the Procfile created from the above command and enter the following line:

web: gunicorn 'your python file name':server (Enter the file name without the file extension)
Create the Requirements file using the following command:

pip freeze > requirements.txt
The requirements.txt file is used for specifying what python packages are required to run the project you are deploying. It is located in the root directory of your project.

Enter the follwing commands to initialize git and push your code file to Heroku:

git init
git add .
git commit -am "first commit"
heroku git:remote -a yourappname
git push heroku master
heroku ps:scale web=1
heroku open
That's it! Your dashboard is now deployed to Heroku with a custom URL like https://covid2020global.herokuapp.com/

