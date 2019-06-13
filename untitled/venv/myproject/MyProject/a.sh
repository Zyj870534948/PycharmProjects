#!/bin/sh
export PATH=$PATH:/home/nao/.local/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/bin/X11:/usr/local/bin:/opt/aldebaran/bin
pname="MyProject"
dirproject="/data/home/nao/nplus/"
dirdownload="/data/home/nao/nplus/download/"
dirbackups="/data/home/nao/nplus/backups/"
value="/*"
v1="*"
dirname=$dirbackups$pname

dirpy="/data/home/nao/nplus/filepy/"
dirlog="/data/home/nao/nplus/filepy/"
supy="updatesuccess.py"
fapy="updatefailed.py"

dateTime="`date +%Y-%m-%d,%H:%m`"
echo "*******************$dateTime******************" >> "$dirlog dlog.log"

echo "pname:"$pname >> "$dirlog dlog.log"
echo "dirproject"$dirproject >> "$dirlog dlog.log"
echo "dirdownload"$dirdownload >> "$dirlog dlog.log"
echo "dirbackups"$dirdownload >> "$dirlog dlog.log"
echo "dirname:"$dirname >> "$dirlog dlog.log"


mainPid=`ps aux |grep menuControl.py |grep -v "grep" |awk '{print $2}'`


backupfun(){
    `cp -ri $dirproject$pname$value $dirbackups$pname`
    if [ $? -ne 0 ];then
        echo "copy failed" >> "$dirlog dlog.log"
    else
        echo "copy success" >> "$dirlog dlog.log"
        #`rm -rf /home/lin/nplus/tornado_new/*`
        `rm -rf $dirproject$pname$value`
        if [ $? -ne 0 ];then
            echo "delete failed" >> "$dirlog dlog.log"
        else
            echo "delete success" >> "$dirlog dlog.log"
            if [ ! -d $dirdownload$pname ];then
                echo "dirdownload not exit" >> "$dirlog dlog.log"
                recoverdir1
                updatefailed
                echo "*****************************************************" >> "$dirlog dlog.log"  
            else
                echo "dirdownload exit" >> "$dirlog dlog.log"
                `cp -rp $dirdownload$pname$value $dirproject$pname`
                if [ $? -ne 0 ];then
                    echo "update failed" >> "$dirlog dlog.log"
                    recoverdir
                    updatefailed
                    echo "*****************************************************" >> "$dirlog dlog.log" 
                else
                    echo "update success" >> "$dirlog dlog.log"
                    deletdownlad
                    deletebackups
                    updatesuccess
                    echo "*****************************************************" >> "$dirlog dlog.log" 
                fi
                
            fi
        fi
    fi
}

deletdownlad(){
    #`rm -rf /home/lin/nplus/download/*`
    `rm -rf $dirdownload$v1`
    if [ $? -ne 0 ];then
        echo "delete download failed" >> "$dirlog dlog.log"
    else
        echo "delete download success" >> "$dirlog dlog.log"
    fi
}
deletebackups(){
    #`rm -rf /home/lin/nplus/backups/*`
    `rm -rf $dirbackups$v1`
    if [ $? -ne 0 ];then
        echo "delete backups failed" >> "$dirlog dlog.log"
    else
        echo "delete download success" >> "$dirlog dlog.log"
    fi
}

recoverdir(){
    `cp -rp $dirbackups$pname$value $dirproject$pname`
    if [ $? -ne 0 ];then
        echo "recover  failed" >> "$dirlog dlog.log"
    else
        echo "recover  success" >> "$dirlog dlog.log"
    fi
}
recoverdir1(){
    `cp -rp $dirbackups$pname$value $dirproject$pname`
    if [ $? -ne 0 ];then
        echo "recover  failed" >> "$dirlog dlog.log"
    else
        echo "recover  success" >> "$dirlog dlog.log"
        deletebackups
    fi
}
updatesuccess(){
    `chmod a+x $dirpy$supy`
    python $dirpy$supy

}
updatefailed(){
    `chmod a+x $dirpy$fapy`
    python $dirpy$fapy
}




kill $mainPid
if [ $? -ne 0 ];then
    echo "kill $mainPid failed" >> "$dirlog dlog.log"
else 
    echo "kill $mainPid success" >> "$dirlog dlog.log"
    if [ ! -d $dirname ];then
        `mkdir -p $dirname`
        if [ $? -ne 0 ];then
            echo "create $dirname failed" >> "$dirlog dlog.log"
        else
            echo "create $dirname success" >> "$dirlog dlog.log"
            backupfun    
        fi    
    else 
        echo "dir exist"
        `rm -rf $dirbackups$pname$value`
        if [ $? -ne 0 ];then
            echo "delete dir failed" >> "$dirlog dlog.log"
        else 
            echo "delete dir success" >> "$dirlog dlog.log"
            backupfun
        fi
    fi
fi

