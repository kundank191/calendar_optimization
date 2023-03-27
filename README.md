# add a readme for the project

Nginx Setup
* sudo systemctl enable nginx
* sudo sustemctl restart nginx
* sudo nginx -t
* sudo nginx -s reload

Ufw setup
* sudo ufw status
* sudo ufw enable
* sudo ufw app list
* sudo ffw allow "Nginx HTTP"
* sudo ufw allow 8000
* sudo ufw allow 80,443/tcp
* tail -f /var/log/nginx/error.log

