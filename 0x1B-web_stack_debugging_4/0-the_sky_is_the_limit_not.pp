# Sky is the limit, let's bring that limit higher
exec {'/etc/default/nginx':
command  => 'sed -i "s/15/500/g" /etc/default/nginx; sudo service nginx restart',
provider => shell,
}
