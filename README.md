# Docker container for Flask, Nginx, and uWSGI, + Letsencrypt's certbot-auto for HTTPS (and a custom script to automate re-configuration)

<b>Purpose:</b> Provide Dockerfile and all applicable config and base Flask scripts necessary to start a webpage, with a script to automate HTTPS re-configuration.

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

  <li><b>HTTPS Setup Options</b></li>
  <ul>
  <li><b>Do it the easy way</b> and run a command like one of the below to automate the setup via a custom script!</li>
      - /home/ubuntu/docker-flask/conf/setup-https.py -d test.com -n test.com -e test@test.com
      <br>
      - /home/ubuntu/docker-flask/conf/setup-https.py -d test.com,www.test.com -n test.com -e test@test.com
      <br>
    <li>Do it the hard way: 
    - Run "/home/flask/certbot-auto certonly -d [domain] -w /home/flask/app" 
    <br>
    - Adjust /home/flask/conf/nginx-http.conf to use HTTPS or modify /home/flask/conf/nginx-https.conf, remove /etc/nginx/sites-enabled/nginx-http.conf, re-link ntinx-https.conf to /etc/nginx/sites-enabled 
    <br>
    - Test and restart nginx</li>
  </ul>  
  
  <br>
  
  <li><b>Credits</b></li>
  <ul>
    <li>Credit to Thatcher Peskens (https://github.com/atupal/dockerfile.flask-uwsgi-nginx), who this code was forked from.</li>
  </ul>  

</ul>


