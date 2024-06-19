# This Puppet manifest fixes file permissions for the WordPress directory

exec { 'fix-wordpress-permissions':
  command => 'chown -R www-data:www-data /var/www/html/wordpress && chmod -R 755 /var/www/html/wordpress',
  path    => ['/bin', '/usr/bin'],
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => Exec['fix-wordpress-permissions'],
}
