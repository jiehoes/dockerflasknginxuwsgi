# Docker container for Flask, Nginx, and uWSGI, + Letsencrypt's certbot-auto for HTTPS

## Purpose:
Provide Dockerfile and all applicable config and base Flask scripts necessary to start a webpage, with a script to automate HTTPS re-configuration.

## Why do I use it?:
With this container, you can get an HTTP server setup in 2 commands, HTTPS in 4! 
1. <b>Build the image:</b> sudo docker build -t flaskwebpage .
2. <b>Run the container:</b> sudo docker run -d -p 80:80 -p 443:443 --restart=always -t --name flaskwebpage flaskwebpage
3. <b>Connect to the container (optional):</b> function _fu(){ sudo docker exec -i -t flaskwebpage /bin/bash ; };_fu
4. <b>Setup HTTPS (optional):</b> /home/flask/conf/setup-https.py -d [domain_list_csv] -n [certname] -e [email_address]

## More details:
See https://www.mattsvensson.com/nerdings/2017/6/30/docker-flasknginxuwsgi

## Notes/Details:
<ul>
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
</ul>  

  <br>

  <li><b>HTTPS Setup Options (assumes 1 domain per container instance)</b></li>
  <ul>
  <li><b>Do it the easy way!</b> Go into the container and run a command like one of the below examples to automate the setup via a custom script I wrote.  Before running it, yes, you should own the domain and have updated the DNS records.</li>
      - /home/flask/conf/setup-https.py -d test.com -n test.com -e test@test.com
      <br>
      - /home/flask/conf/setup-https.py -d test.com,www.test.com -n test.com -e test@test.com
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


