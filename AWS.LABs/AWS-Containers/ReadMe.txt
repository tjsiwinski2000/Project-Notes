01-29-2025 Containers

https://www.youtube.com/watch?v=JF9S3MFDNtI

Notes
- Containers lack OS hence each container is a "slice" of the underlying OS.
- Faster since no OS bootup
- Docker is most popular 
- CMD> docker run hello-world  pulls [https://hub.docker.com/_/hello-world]

Dockerfile->DockerImage->Container [running image]
-built Dockerfile
-docker build -t quote-generator:v1.0 . [grabs content of Dockerfile, builds image]
-docker run quote-generator:v1.0 [launches container]

🌟 **RESOURCES AND LINKS USED IN THIS VIDEO** 🌟
• app.py file (main file of Python app): https://github.com/tinytechnicaltutor...
• Dockerfile used in the video: https://github.com/tinytechnicaltutor...
• Download Docker Desktop: https://docs.docker.com/desktop/
• Details of what can go in a Dockerfile: https://docs.docker.com/get-started/d... 
• Docker Hub: https://hub.docker.com/ 

PS C:\Users\TJ\Documents\AWS-Containers> ls

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         1/29/2025   8:53 PM            900 app.py
-a----         1/29/2025   8:57 PM            422 Dockerfile
[note docker builds not stored as traditional files !]


PS C:\Users\TJ\Documents\AWS-Containers> docker images
REPOSITORY        TAG       IMAGE ID       CREATED              SIZE
quote-generator   v1.0      4c2c6099559e   About a minute ago   181MB   [this is the image we just built! 0129-2025]
hello-world       latest    d715f14f9eca   8 days ago           20.4kB

PS C:\Users\TJ\Documents\AWS-Containers> docker save -o image.tar quote-generator [i want to send a file to my nephew, save image as a tar file]
docker run quote-generator:v1.0 [v.1 tag prevents docker from looking for image in docker on internet]