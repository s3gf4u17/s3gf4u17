sudo apt-get update && sudo apt-get upgrade -y

sudo apt install virtualbox -y
sudo apt-get install linux-headers-`uname -r`
sudo dpkg-reconfigure virtualbox-dkms
sudo modprobe vboxdrv