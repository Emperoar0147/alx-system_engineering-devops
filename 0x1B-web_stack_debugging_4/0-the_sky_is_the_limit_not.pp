# This Puppet manifest configures Nginx to handle higher load and reduce failed requests.
exec { 'fix--for-nginx':
  command => '/usr/sbin/nginx -s reload',
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['fix--for-nginx'],
}
