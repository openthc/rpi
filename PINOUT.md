# Pinout Diagram

                            J8
                           .___.
                  +3V3   1 |X X|  2  +5V >> OT-RAIL-RED
          (SDA)  GPIO2   3 |O X|  4  +5V
         (SCL1)  GPIO3   5 |O _|  6  _
    (GPIO_GLCK)  GPIO4   7 |O O|  8  GPIO14 (TXD0)
                     _   9 |_.O| 10  GPIO15 (RXD0)
    (LED-RGB R) GPIO17  11 |X O| 12  GPIO18 (GPIO_GEN1)
    (LED-RGB G) GPIO27  13 |X _| 14  _
    (LED-RGB B) GPIO22  15 |X O| 16  GPIO23 (GPIO_GEN4)
                  +3V3  17 |X O| 18  GPIO24 (GPIO_GEN5)
     (SPI_MOSI) GPIO10  19 |O._| 20  _
     (SPI_MOSO)  GPIO9  21 |O O| 22  GPIO25 (GPIO_GEN6)
     (SPI_SCLK) GPIO11  23 |O O| 24  GPIO8  (SPI_C0_N)
                     _  25 |_ O| 26  GPIO7  (SPI_C1_N)
        (EEPROM) ID_SD  27 |O O| 28  ID_SC Reserved for ID EEPROM
                 GPIO5  29 |O._| 30  _
                 GPIO6  31 |O O| 32  GPIO12
                GPIO13  33 |O _| 34  _
                GPIO19  35 |O O| 36  GPIO16
                GPIO26  37 |O O| 38  GPIO20
                     _  39 |_ O| 40  GPIO21
                           '---'



## See Also

 * https://pinout.xyz/
 * https://github.com/tvierb/raspberry-ascii

