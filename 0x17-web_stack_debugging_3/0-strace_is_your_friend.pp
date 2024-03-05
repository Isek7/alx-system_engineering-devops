# A puppet manuscript to replace a line in a file on a server
# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin:/usr/bin:/bin',
}
