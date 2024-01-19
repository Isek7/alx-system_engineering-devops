# install puppet-lint using Puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1', # or the version compatible with Flask 2.1.0
  provider => 'pip3',
}
