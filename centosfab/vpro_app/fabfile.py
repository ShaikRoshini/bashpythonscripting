#env.hosts='127.0.0.1'
#env.user='vagrant'
#env.password='vagrant'
from fabric.api import *
def if_condition():
    if  sudo("uname -a | awk '{print $4}' | cut -b 5-10") == "Ubuntu":
        print "this is ubuntu"
        ubuntu()
    else:
        print "this is centos"
        centos()


def centos():
    ciserver()
    appserver()
    db_server()
    lb()
    rabbitmq()
    memcache()

def ubuntu():
    ciserver_u()
    appserver_u()
    db_server_u()
    lb_u()
    rabbitmq_u()
    memcache_u()

#####################################################   VPROFILE FOR CENTOS    ###########################################################

def ciserver():
     sudo("yum update -y")
     sudo("yum install epel-release -y")
     sudo("yum install  java-1.8.0-openjdk -y")
     sudo("yum  install git -y")
     sudo("yum update -y")
     with cd("/root"):
          sudo("git clone -b vp-memcached-rabbitmq https://github.com/wkhanvisualpathit/VProfile.git")
          sudo("yum install maven -y")
     with cd("/root/VProfile"):
          sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
          sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
          sudo("sed -i 's/localhost:3306/db.com:3306/' src/main/resources/application.properties")
          sudo("sed -i 's/address=127.0.0.1/address='rmq.com'/' src/main/resources/application.properties")
          sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache.com'/' src/main/resources/application.properties")
          sudo("mvn clean install")

def appserver():
     sudo("yum update -y")
     sudo("yum install epel-release -y")
     sudo("yum install java -y")
     sudo("yum install wget -y")
     with cd("/root"):
          sudo("wget http://redrockdigimark.com/apachemirror/tomcat/tomcat-8/v8.5.32/bin/apache-tomcat-8.5.32.tar.gz")
          sudo("mv apache-tomcat-8.5.32.tar.gz /opt/apache-tomcat-8.5.32.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.32.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.32/webapps/ROOT")
          sudo("cp  /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.32/webapps/ROOT.war")
          sudo("/opt/apache-tomcat-8.5.32/bin/startup.sh")

def db_server():
     sudo("yum update -y  ")
     sudo("yum install epel-release -y")
     sudo("yum install mysql-server -y")
     sudo("service mysqld start")
     sudo("sed -i 's/127.0.0.1/0.0.0.0/' /etc/my.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\"  --password='';")
     sudo("mysql -u root --password='' accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='';")
     sudo("service mysqld restart")


def lb():
     sudo("yum install epel-release -y")
     sudo("yum install nginx -y")
     sudo("cat /root/vproapp  > /etc/nginx/conf.d/vproapp.conf")
     sudo("service nginx restart")


def rabbitmq():
     sudo("yum update")
     sudo("yum install wget -y")
     sudo("yum install epel-release -y")
     sudo("echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list")
     sudo("wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
     sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
     sudo("yum install rabbitmq-server -y")
     sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
     sudo("rabbitmqctl add_user test test")
     sudo("rabbitmqctl set_user_tags test administrator")

def memcache():
     sudo("yum install memcached -y")
     sudo("memcached -p 11111 -U 11111 -u memcache -d")



#############################################    VPROFILE FOR UBUNTU     ######################################################


def ciserver_u():
     sudo("apt update -y")
     #sudo("add-apt-repository ppa:openjdk-r/ppa -y")
     #sudo("apt-get update")
     sudo("apt-get install openjdk-8-jdk -y")
     sudo("apt-get  install git -y")
     with cd("/"):
         sudo("git clone -b vp-memcached-rabbitmq https://github.com/wkhanvisualpathit/VProfile.git")
         sudo("apt-get install maven -y")
     with cd("/VProfile"):
         sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
         sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
         sudo("sed -i 's/localhost:3306/db.com:3306/' src/main/resources/application.properties")
         sudo("sed -i 's/address=127.0.0.1/address='rmq.com'/' src/main/resources/application.properties")
         sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache.com'/' src/main/resources/application.properties")
         sudo("mvn clean install")

def appserver_u():
     sudo("apt-get update -y")
     sudo("apt-get install openjdk-8-jdk -y")
     sudo("apt-get install wget -y")
     with cd("/"):
          sudo("wget http://www-us.apache.org/dist/tomcat/tomcat-8/v8.5.32/bin/apache-tomcat-8.5.32.tar.gz")
          sudo("mv apache-tomcat-8.5.32.tar.gz /opt/apache-tomcat-8.5.32.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.32.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.32/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.32/webapps/ROOT.war")
          sudo("/opt/apache-tomcat-8.5.32/bin/startup.sh")

def db_server_u():
     sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'")
     sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'")
     sudo("apt-get update")
     sudo("apt-get install mysql-server -y")
     sudo("sed -i 's/127.0.0.1/0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf")
     sudo("mysql -u root -e \"create database accounts\" --password='root';")
     sudo("mysql -u root -e  \"grant all privileges on *.* TO 'root'@'app.com' identified by 'root'\"  --password='root';")
     sudo("mysql -u root --password='root' accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='root';")
     sudo("service mysql restart")

def lb_u():
     sudo("apt-get install nginx -y")
     sudo("cp /root/vproapp /etc/nginx/sites-available/vproapp")
     sudo("rm -rf /etc/nginx/sites-enabled/default")
     sudo("ln -s /etc/nginx/sites-available/vproapp /etc/nginx/sites-enabled/vproapp")
     sudo("sudo service nginx restart")

def rabbitmq_u():
     sudo("echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list")
     sudo("wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
     sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
     sudo("apt-get install rabbitmq-server -y")
     sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
     sudo("rabbitmqctl add_user test test")
     sudo("rabbitmqctl set_user_tags test administrator")

def memcache_u():
     sudo("apt-get install memcached -y")
     sudo("memcached -p 11111 -U 11111 -u memcache -d")

