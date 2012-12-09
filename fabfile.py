from fabric.api import *


env.hosts = ['sidar@10.10.10.10']
DESIGN26_HOSTNAME = 'design26.local'
github_repo = 'https://github.com/dbraun86/sidar.git'
design26m_mount_point = '/mnt/design26m'


def mount_design26m():
    from socket import gethostbyname
    design26_ip = gethostbyname(DESIGN26_HOSTNAME)
    sudo('mkdir -p %s' % design26m_mount_point)
    sudo('if ! mount | grep design26m; then mount.cifs //%s/M$ ' + design26m_mount_point + ' -o user=sidar; fi;' % design26_ip)


def import_sidar_mysql():
    mount_design26m()
    run('mysql -u root < %s' % design26m_mount_point + '/shenkar-php/sidar.sql')


def push_ssh_key():
    """Pushes SSH key to remote host, so password won't have to be entered each time"""
    keyfile = '/tmp/%s.pub' % env.user
    run('mkdir -p ~/.ssh && chmod 700 ~/.ssh')
    put('~/.ssh/id_rsa.pub', keyfile)
    run('cat %s >> ~/.ssh/authorized_keys' % keyfile)
    run('rm %s' % keyfile)


def deploy_design25_from_github():
    mount_design26m()
    local('pip freeze > requirements.txt')
    source = 'source venv/bin/activate && '
    with cd('~/sidar'):
        run('git pull')
        # run('source venv/bin/activate')
        run(source + 'pip install -r requirements.txt')
        run(source + 'python manage.py migrate')
    sudo('service gunicorn restart')
