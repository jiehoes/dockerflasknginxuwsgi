# Flask+Nginx+uwsgi Docker Container

<b>Purpose:</b> Provide Dockerfile and all applicable config and base Flask scripts necessary to start a webpage

<b>Instructions to build and run the container</b>:

sudo docker build -t flaskwebpage .

sudo docker run -d -p 80:80 -p 443:443 --restart=always -t --name flaskwebpage flaskwebpage
