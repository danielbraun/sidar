from fabric.api import *
from socket import gethostbyname

env.hosts = ['sidar@10.10.10.10']
DESIGN26_HOSTNAME = 'design26.local'

def mount_design26m():
    design26_ip = gethostbyname(DESIGN26_HOSTNAME)
    sudo('mkdir -p /mnt/design26m')
    sudo('if ! mount | grep design26m; then mount.cifs //%s/M$ /mnt/design26m -o user=sidar; fi;' % design26_ip)


def push_ssh_key():
    """Pushes SSH key to remote host, so password won't have to be entered each time"""
    keyfile = '/tmp/%s.pub' % env.user
    run('mkdir -p ~/.ssh && chmod 700 ~/.ssh')
    put('~/.ssh/id_rsa.pub', keyfile)
    run('cat %s >> ~/.ssh/authorized_keys' % keyfile)
    run('rm %s' % keyfile)
