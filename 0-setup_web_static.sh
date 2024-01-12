#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R 1000:1000 /data/

sudo sed -i "/server_name _;/a location /hbnb_static {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
