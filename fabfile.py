from fabric.api import *

def commit():
    local("git add -p && git commit")

def deploy():
    code_dir = '/home/patsweet/webapps/patsweet/patsweet'
    with cd(code_dir):
        run("git pull")
        run("../apache2/bin/restart")