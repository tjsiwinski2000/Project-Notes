0123-2026 
10:30am
decided to go with pythonanywhere for hosting
decided to make separate github repository C:\Users\TJ\source\repos\flask_deploy_2026

 
Here are some tips and insights from Redditors to help you get the most out of PythonAnywhere:
-PythonAnywhere provides an easy way to deploy Flask apps without needing to 
manage Nginx, Gunicorn, or Celery, as it offers its own integrated solutions.

-PythonAnywhere web apps are shut down after a few hours of inactivity. 
To keep your app responsive, consider setting up a scheduled task to ping your site regularly

-Use environment variables to store sensitive information rather than hardcoding credentials 
into your code. PythonAnywhere allows you to set up environment variables securely. 

-Zip and Upload: PythonAnywhere allows you to upload files one by one, 
but you can zip your entire project and upload it to simplify the process. 

"You can do is put your whole project into a zip file, upload that and unzip it on Pythonywhere 
by opening up a Bash console and running unzip ~/foo.zip."


BUT
 For larger applications or those requiring more robust infrastructure, consider other platforms like DigitalOcean or AWS, which offer more flexibility and scalability. "Digital ocean droplets from $4 droplet/month... For a production ready fastapi+jinja2+htmx frontend, database backend, container registry come to $20 a month."
 
  Use the server logs and error logs on PythonAnywhere to debug issues, as direct console output might not always be available. "Probably the most frustrating thing in the move is the debugging - having to go to the error logs / server logs is cumbersome after using pycharm for my local dev."
  
GIT NOTES
Create repo on github.com

from your local computer cmd-line
echo "# flask_deploy_2026" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/tjsiwinski2000/flask_deploy_2026.git
git push -u origin main

-how to find remote origin-
Navigate to your repository on the GitHub website.
Locate the green < > Code button on the main page of your repository. Click on it
e.g. https://github.com/tjsiwinski2000/flask_deploy_2026.git

