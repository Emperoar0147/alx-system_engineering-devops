# This Puppet manifest increases the file descriptor limit for the holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 1024\nholberton hard nofile 2048" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton" /etc/security/limits.conf',
}

# Reload the PAM limits to apply changes
exec { 'reload-pam-limits':
  command => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => Exec['change-os-configuration-for-holberton-user'],
}
