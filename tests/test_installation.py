"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    'acl',
    'cron-apt',
    'curl',
    'debian-goodies',
    'di',
    'dstat',
    'git',
    'htop',
    'iftop',
    'iotop',
    'molly-guard',
    'mtr',
    'nagios-plugins',
    'nagios-plugins-contrib',
    'rssh',
    'sshfs',
    'sysstat',
    'tree',
    'vim'
])
def test_packages(host, name):
    """
    Tests packages are installed
    """

    assert host.package(name).is_installed
