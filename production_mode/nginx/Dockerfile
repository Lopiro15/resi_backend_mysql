FROM daocloud.io/nginx

#Delete the original configuration file, create static resource folder and SSL certificate save folder
RUN rm /etc/nginx/conf.d/default.conf \
&& mkdir -p /usr/share/nginx/html/static

#Add profile
ADD ./nginx.conf /etc/nginx/conf.d/