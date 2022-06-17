# mean-robot
# Setup PI 

## install base packages 
```bash
sudo apt-get install git -y
sudo apt-get install python3 python3-pip uvicorn
pip3 install fastapi rpi.gpio
```
## install gstreamer
```bash
git clone https://github.com/jacksonliam/mjpg-streamer.git

cd mjpg-streamer/
cd mjpg-streamer-experimental/
sudo apt-get install cmake
# sudo apt-get install python-imaging
# sudo apt-get install ibjpeg-dev -y
pip install Pillow

make CMAKE_BUILD_TYPE=Debug
sudo make install

copy livestream.sh to
/etc/init.d/livestream.sh
sudo chmod 755 /etc/init.d/livestream.sh
sudo update-rc.d livestream.sh defaults

# check if working
http://raspy_ip:8080/?action=stream
```


# install adafruit PCA9685 16 
```bash
# sudo apt-get install build-essential python-dev python-smbus i2c-tools python-pip --yes
sudo apt-get install build-essential  i2c-tools --yes
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
#pip install "uvicorn[standart]"
apt-get install uvicorn

```
## start dev 

```bash
# main (file) app(instance of fastAPI class)
uvicorn main:app --reload
```


# robot-service socket api 
```json
{
    "command": "[get,set,method]",
    "path": "path in body object",
    "value": ["int","string","float"]
}

```

# method_queue item 
```json
["path", "method_name", param_1, ..., param_n]
```
# usefull links 
* PCA9685 http://wiki.sunfounder.cc/index.php?title=PCA9685_16_Channel_12_Bit_PWM_Servo_Driver
* PCA9685 connection to Pi https://bluexmas.tistory.com/532#
* Pi 3B Pinout https://www.etechnophiles.com/raspberry-pi-3-gpio-pinout-pin-diagram-and-specs-in-detail-model-b/
* MG90s Servomotor Datasheet https://components101.com/motors/mg90s-metal-gear-servo-motor
* Use pymon for development https://github.com/kevinjosethomas/py-mon