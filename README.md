### Hi there 👋

```
# fix missing amdgpu
sudo apt install git -y
cd ~/Documents && git clone https://kernel.googlesource.com/pub/scm/linux/kernel/git/firmware/linux-firmware.git
sudo cp ~/Documents/linux-firmware/amdgpu/* /lib/firmware/amdgpu && sudo update-initramfs -k all -u -v
# check nvidia version
nvidia-smi
# remove old nvidia
sudo apt autoremove nvidia* --purge
sudo /usr/bin/nvidia-uninstall
sudo /usr/local/cuda-X.Y/bin/cuda-uninstall
# install nvidia
sudo apt install software-properties-common -y
sudo add-apt-repository contrib non-free-firmware
sudo apt update
sudo apt install linux-headers-amd64
sudo apt install nvidia-detect
nvidia-detect
sudo apt install nvidia-driver linux-image-amd64
sudo reboot

sudo ubuntu-drivers list
sudo ubuntu-drivers list --gpgpu
sudo ubuntu-drivers install
sudo ubuntu-drivers install nvidia:535
sudo ubuntu-drivers install --gpgpu
sudo ubuntu-drivers install --gpgpu nvidia:535-server
sudo apt install nvidia-utils-535-server
gsettings set org.gnome.shell.extensions.desktop-icons show-home false
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false
```

<!--
**s3gf4u17/s3gf4u17** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
