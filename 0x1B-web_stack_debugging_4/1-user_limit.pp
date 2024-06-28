# This Puppet manifest increases the open file limit for the holberton user.
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton soft nofile 4096" /etc/security/limits.conf',
}

exec { 'apply-sysctl-changes':
  command => 'sysctl -p',
  refreshonly => true,
  subscribe => Exec['change-os-configuration-for-holberton-user'],
}
