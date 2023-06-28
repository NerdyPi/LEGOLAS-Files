#!/bin/bash

cd $HOME
#install buildhat if its not there
buildhat=$(pip3 list | grep buildhat)
if [[ ! -n "$buildhat"]]
then
#    pip3 install buildhat==VERSION
else
    echo buildhat found
fi

#install rpyc if its not there
rpyc=$(pip3 list | grep rpyc)
if [[ ! -n $rpyc ]]
then
#    pip3 install rpyc
else
    echo rpyc found
fi

#git clone rpyc classic if its not there
rpyc_classic=$(ls $HOME/git | grep rpyc)
if [[ ! -n "$rpyc_classic" ]]
then
#    cd $HOME
#    mkdir git
#    cd git
#    git clone LINK
#    cd $HOME
else
    echo git folder found
fi

#check where the classic rpyc server is downloaded

#write the auto_server if it doesn't exist
#CHECK if I should use rpyc or rpyc-master
auto_server=$(ls | grep auto_rpyc_server.sh)
if [[ ! -n "$auto_server" ]]
then
#    "#!/bin/bash\n" >> auto_rpyc_server.sh
#    #PATH_TO_RPYC_SERVER
else
    echo auto_server found
fi


#write the reset_server if it doesn't exit/update to current
#reset_server=

#Write to chrontab if necessary
crontab_write=$(cat /tmp/crontab | grep '@reboot sh /home/pi/auto_rpyc_server.sh')
if [[ ! -n "$crontab_write"]]
then
#    "@reboot sh /home/pi/auto_rpyc_server.sh" >> CHONTAB_PATH
else
    echo crontab has boot for rpyc server
fi

#Write the notor script if necesary
pyPack_dir=$(pip3 show buildhat | awk '/Location/ {print $2}')
cd $(echo pyPack_dir | tr -d '\r')
build_not=$(ls buildnot.py)
if [[ ! -n "$build_not" ]]
then
#    "from buildhat import motor\n\n" >> buildnot.py
#   "class notor(motor):\n" >> buildnot.py
#    "     def __del__:\n" >> buildnot.py
#    "          ALL THE THINGS" >> buildnot.py
else
    echo buildnot has been made
fi