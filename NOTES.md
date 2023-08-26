> https://www.bootstrap-it.com/troubleshooting

> cd /proc
> ps aux 
> journalctl _PID=pid
> ls -p | grep -v | column
> cpuinfo flags svm  lm bug
> less cpuinfo | grep processor
> https://access.redhat.com/solutions/406773
> free -h

> df
> df -t ext4
> df -i


> iftop
> nethogs


# monitor Solutions for Linux

+ collectd
+ Nagios
+ Munin
+ Nmon
+ cockpit
> sudo apt-get install cockpit -y
> yum install cockpit
> systemctl start cockpit
> systemctl enable --now cockpit.socket


> systemctl status apache2
> systemctl disable apache2  # disable in current session
> systemctl start/stop  apache2  
> yes > /dev/null &
> yes > /dev/null &
> kill pid
> killall yes
> nice and cgroups
> sysstat


# Business Continuity Plan(BcP)

+ Safety
+ Restore Service
+ Restore All Operations
+ Incident Management Protocol
+ Disaster Recovery Plan


> uname -a
> dmidecode 
> dmidecode  -quiet
> dmidecode  -s chassis-type
> dmidecode  -s baseboard-product-name
> dmidecode  -s processor-frequency
> dmidecode  -t bios
> dmidecode  -t slot
> lshw
> lshw -C disk
> lshw -C network
> lshw -short

> apt install memtester
>  memtester 1500 1
> apt install smartmontools
> smartctl -i /dev/sda
> smartctl -A /dev/sda
> smartctl -l selftest /dev/sda
> smartctl -l error /dev/sda
> smartctl -l devstat /dev/sda
> smartctl -t short  /dev/sda

# Controlling Linux Kernels

> vim /etc/default/grub
> vim /boot/grub/grub.cfg

> yum -q kernel
> yum install yum-utils
> package-cleanup --oldkernels --count=2

> apt --purge autoremove

> yum install  kernel kernel-tools kernel-tools-libso

> apt update
> apt upgrade

# Build Packages

+ Debian/APT
+ RPM Package Manager
+ Snaps
+ Appimage

> apt install build-essential tree
> mkdir -p mycodeplace/DEBIAN
> mkdir -p mycodeplace/DEBIAN/usr/bin

> g++ mycode.cc -o mycode
> vim mycodeplace/DEBIAN/control
> cp mycode mycodeplace/DEBIAN/usr/bin/
> dpkg-deb --build mycodeplace

> apt install apache2 
> cp mycodeplace.db /var/www/html

> vim /etc/apt/sources.list

add 

deb [trusted=yes] http://192.168.1.101/debina/ ./

> apt update
> apt install mycodeplace

> yum install rpm-build
> echo '$_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
> mkdir -p ~/rpmbuild/{BUILD, BUILDROOT, RPMS, SOURCES,SPECS,SRPMS}
> mkdir hello-world-1.0
> cd hello-world-1.0
> vim main.c
> make
> sudo make install
> tar zcvf helloworld-1.0.tar.gz hello-world-1.0/
> cp helloworld-1.0.tar.gz  ~/rpmbuild/SOURCES/
> vim helloworld.spec>
> rpm-build -ba helloworld.spec

## snaps

> sudo snap install multipass --classic
> sudo snap install snapcraft --classic

> git clone https://github.com/snapcraft-docs/offlineimap.git
> cd offlineimap
> wget https://snapcraft.io/first-snap/python/snapcraft.yaml
> snapcraft
> sudo snap install --devmode --dangerous *.snap
> snap list
> test-offlineimap-mysnap -h




> hash -r

## flatpak


> sudo apt install flatpak

## appimage


> sudo apt install appstream

> git clone https://github.com/boolean-world/appimage-resources
vim hello-world-appimage/helloworld.desktop

add 

Categories=GNOME;


> wget https://github.com/AppImage/AppImageKit/releases/download/contrnuous/apimagetool-x86_64.AppImage

> chmod -x apimagetool-x86_64.AppImage

> ARCH=x86_64  ./appimagetool-x86_64.AppImage hello-world.appimage/
> ./helloworld-appimage-x86_64.AppImage



 










