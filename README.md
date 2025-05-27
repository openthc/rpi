# OpenTHC Raspberry Pi Toolkit

A collection of documentation, scripts and tools for using Raspberry Pi in cannabis operations. 

## Install

```shell
wget ''
xz -d $IMAGE.xz
dd bs=1M status=progress if=$IMAGE.img of=$DEV
echo ',+' | sfdisk --force -N 2 /dev/mmcblk0
resize2fs /dev/mmcblk0p2
```


## Scale Support

One or more scales can be connected to a RPi via Serial->USB adapters, you may need a high-speed USB hub if more than four scales are used.


## Sensor Support

 * CO2: X
 * CH4 (Methane): 
 * Humidity/Temperature: DHT11, DHT22
 * Lumens:
 * Light Cycle (on/off)
 * Wind Speed
 * Wind Direction
 * Solar?
 * pH (Soil & Liquid)?
 * VPD (Vapor Pressure Deficit)
 * Flood/Moisture Sensor: EK1361, TE215
 * Water Level Sensor?

### Soil Moisture
 
 * https://www.amazon.com/XCSOURCE-Moisture-Automatic-Watering-TE215/dp/B00ZR3B60I/ref=pd_sim_86_13?_encoding=UTF8&pd_rd_i=B00ZR3B60I&pd_rd_r=c3b5e56b-9b65-11e8-800d-291f7dc96a5e&pd_rd_w=8Nsu8&pd_rd_wg=YE39n&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a180fdfb-b54e-4904-85ba-d852197d6c09&pf_rd_r=Y61ESTA6T2N3AX4A6QTB&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=Y61ESTA6T2N3AX4A6QTB
 * https://www.amazon.com/Kuman-Moisture-Compatible-Raspberry-Automatic/dp/B071F4RDHY/ref=pd_sim_86_4?_encoding=UTF8&pd_rd_i=B071F4RDHY&pd_rd_r=520fcfc7-9b65-11e8-8a22-f3d4eee18e06&pd_rd_w=UXO65&pd_rd_wg=AR8oD&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a180fdfb-b54e-4904-85ba-d852197d6c09&pf_rd_r=XP2YX5BB9H3R8MWECG8C&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=XP2YX5BB9H3R8MWECG8C&dpID=51roaVQO3XL&preST=_SY300_QL70_&dpSrc=detail
 * https://www.amazon.com/Gikfun-Moisture-Sensor-arduino-EK1361/dp/B00RK1VYTI/ref=sr_1_1?ie=UTF8&qid=1533771952&sr=8-1&keywords=soil+moisture+sensor
 * https://www.amazon.com/CTYRZCH-Moisture-Sensor-Automatic-Watering/dp/B01ESSMLQU/ref=sr_1_19?ie=UTF8&qid=1533771976&sr=8-19&keywords=soil+moisture+sensor
 * https://www.amazon.com/DFROBOT-Gravity-Capacitive-Corrosion-Resistant/dp/B01GHY0N4K/ref=sr_1_20?ie=UTF8&qid=1533771976&sr=8-20&keywords=soil+moisture+sensor
 * https://www.amazon.com/DFROBOT-Gravity-Capacitive-Corrosion-Resistant/dp/B01GHY0N4K/ref=pd_sim_86_2?_encoding=UTF8&pd_rd_i=B01GHY0N4K&pd_rd_r=520fcfc7-9b65-11e8-8a22-f3d4eee18e06&pd_rd_w=UXO65&pd_rd_wg=AR8oD&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a180fdfb-b54e-4904-85ba-d852197d6c09&pf_rd_r=XP2YX5BB9H3R8MWECG8C&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=XP2YX5BB9H3R8MWECG8C&dpID=41W7vqM6GxL&preST=_SY300_QL70_&dpSrc=detail
 * https://www.amazon.com/WINGONEER-Sensor-Droplet-Detection-Arduino/dp/B06XHDZ3Q4/ref=pd_sim_86_3?_encoding=UTF8&pd_rd_i=B06XHDZ3Q4&pd_rd_r=520fcfc7-9b65-11e8-8a22-f3d4eee18e06&pd_rd_w=UXO65&pd_rd_wg=AR8oD&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a180fdfb-b54e-4904-85ba-d852197d6c09&pf_rd_r=XP2YX5BB9H3R8MWECG8C&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=XP2YX5BB9H3R8MWECG8C
 * https://www.amazon.com/Phantom-YoYo-compatible-Sensitivity-Moisture/dp/B00AFCNR3U/ref=pd_sim_86_50?_encoding=UTF8&pd_rd_i=B00AFCNR3U&pd_rd_r=520fcfc7-9b65-11e8-8a22-f3d4eee18e06&pd_rd_w=UXO65&pd_rd_wg=AR8oD&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a180fdfb-b54e-4904-85ba-d852197d6c09&pf_rd_r=XP2YX5BB9H3R8MWECG8C&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=XP2YX5BB9H3R8MWECG8C
 * https://www.amazon.com/dp/B01N7NA3HP/ref=sxbs_sxwds-stppvp_1?pf_rd_m=ATVPDKIKX0DER&pf_rd_p=6297546923292665688&pd_rd_wg=n1jTP&pf_rd_r=Z9TKR6JWBXESK34WWSZE&pf_rd_s=desktop-sx-bottom-slot&pf_rd_t=301&pd_rd_i=B01N7NA3HP&pd_rd_w=vhI9n&pf_rd_i=soil+moisture+sensor&pd_rd_r=46cb234e-c987-4ef6-8c13-b213336fca55&ie=UTF8&qid=1533771976&sr=1
 * https://www.amazon.com/dp/B00TMD43BS/ref=psdc_3480689011_t4_B00ZR3B60I
 
## Control Support

 * On/Off AC Power
 * On/Off DC Power
 * 


## Hardware 

You'll need misc resistors and capacators and stuff.

 * https://www.amazon.com/dp/B076LH75JQ/ref=sspa_dk_detail_12?psc=1&pd_rd_i=B076LH75JQ&pd_rd_wg=7hA91&pd_rd_r=DT8WEQMJTHSWBH952Y2Y&pd_rd_w=pdYiE
 * https://www.amazon.com/dp/B07BVTFCHP/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B07BVTFCHP&pd_rd_wg=tdERY&pd_rd_r=6K5P8YTEFM594RDCM0V6&pd_rd_w=aaHEC
 * https://www.amazon.com/24Value-Electrolytic-Capacitor-Assortment-0-1uF%EF%BC%8D1000uF/dp/B01MSQOX0Q/ref=pd_bxgy_328_3?_encoding=UTF8&pd_rd_i=B01MSQOX0Q&pd_rd_r=6K5P8YTEFM594RDCM0V6&pd_rd_w=Zmcy1&pd_rd_wg=tdERY&psc=1&refRID=6K5P8YTEFM594RDCM0V6&dpID=51lVgJM9IuL&preST=_SY300_QL70_&dpSrc=detail
