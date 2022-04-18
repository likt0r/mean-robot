# mean-robot
# Setup PI 

## install base packages 
```bash
sudo apt-get install git -y
```
## install gstreamer
```bash
git clone https://github.com/jacksonliam/mjpg-streamer.git

cd mjpg-streamer/
cd mjpg-streamer-experimental/
sudo apt-get install cmake
# sudo apt-get install python-imaging
sudo apt-get install python-pil
sudo apt-get install libjpeg-dev
make CMAKE_BUILD_TYPE=Debug
sudo make install

copy livestream.sh to
/etc/init.d/livestream.sh
sudo chmod 755 /etc/init.d/livestream.sh
sudo update-rc.d livestream.sh defaults<>
```


# install adafruit PCA9685 16 
```bash
sudo apt-get install build-essential python-dev python-smbus i2c-tools python-pip --yes

# activate i2c in interfacing options
sudo raspi-config
# detect adafruit
i2cdetect -y 1
#      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00:          -- -- -- -- -- -- -- -- -- -- -- -- --
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 70: 70 -- -- -- -- -- -- --

sudo pip install Adafruit-PCA9685
```

# clone mean robot repository

## install robot-api
```bash
pip install fastapi
pip install "uvicorn[standar]"

```
## start dev 

```bash
# api (file) app(instance of fastAPI class)
uvicorn api:app --reload
```