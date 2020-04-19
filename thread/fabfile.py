from fabric.api import run,env

#env.hosts=['192.168.161.100','192.168.161.101']

#env.roledefs={"web":["192.168.161.100","127.0.0.1"],"db":["192.168.161.101"]}
env.roledefs["web"]=["192.168.161.100","127.0.0.1"]
env.roledefs["db"]=["192.168.161.101"]

env.usr="root"
env.password="coco0769"

def host_type():
    run('whoami;uname -s')
