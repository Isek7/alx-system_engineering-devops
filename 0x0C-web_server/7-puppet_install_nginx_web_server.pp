# Installing Nginx package
package { 'nginx':
  ensure => installed,
}

# Adding the rewrite line to the Nginx configuration
file_line { 'install':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/Isek7 permanent;',
}

# Creating the index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensuring Nginx service is running and requires the Nginx package
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
