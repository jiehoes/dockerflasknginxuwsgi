# Docker container for Flask, Nginx, and uWSGI, including Letsencrypt's certbot-auto for HTTPS

<b>Purpose:</b> Provide Dockerfile and all applicable config and base Flask scripts necessary to start a webpage

<b>Why do I use it?:</b> See https://www.mattsvensson.com/nerdings/2017/6/30/docker-flasknginxuwsgi

<b>Notes/Details:</b>
<ul>
  <li><b>Build and run the container</b></li>
  <ul>
    <li>Clone this repo and go to into the "docker-flask-nginx-uwsgi" folder (where the Dockerfile is)</li>
    <li>Build: sudo docker build -t flaskwebpage .</li>
    <li>Run: sudo docker run -d -p 80:80 -p 443:443 --restart=always -t --name flaskwebpage flaskwebpage</li>
  </ul>
  
  <br>
  
  <li><b>Folder/File Sctructure</b></li>
  <ul>
    <li>All of the files+folders in this repo will be, by default, put into /home/flask.  If you modify this you need to update the files in /home/flask/conf as well</li>
    <li>The /home/flask/app folder will contain the Flask app.  As long as the wsgi.py file uses "app" not "application," you can swap in and out any flask app that you want (so long as you have the necessary libraries installed)</li>
  </ul>
  
  <br>
  
  <li><b>Services/Notes</b></li>
  <ul>
    <li>This script uses linux's Supervisor to monitor and control uWSGI and nginx.</li>
    <li>Port 443 is left on the run command in case you want to use it.  If you never will, you can remove "-p 443:443"</li>
    <li>If you want to get shell on the container, run: function _fu(){ sudo docker exec -i -t flaskwebpage /bin/bash ; };_fu</li>
</ul>  

  <br>

  <li><b>HTTPS</b></li>
  <ul>
    <li>certbot is installed, by default, with the Dockerfile.  To get certs from letsencrypt, in the container, run the following command, using authentication option 2 (Place files in a webroot directory):  /home/flask/certbot-auto certonly -d [domain] -w /home/flask/app</li>
    <li>Once the certs are installed, adjust /home/flask/conf/nginx.conf to use HTTPS, replacing YOURDOMAIN with your actual domain.</li>
    <li>Test and restart Nginx</li>
  </ul>  
  
  <br>
  
  <li><b>Credits</b></li>
  <ul>
    <li>Credit to Thatcher Peskens (https://github.com/atupal/dockerfile.flask-uwsgi-nginx), who this code was forked from.</li>
  </ul>  

</ul>


