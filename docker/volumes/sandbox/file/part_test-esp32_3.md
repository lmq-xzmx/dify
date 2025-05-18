```json
{
  "segment_01": {
    "text": "A 电源n56 VDDA 电源n57 GND 电源n1. 更多信息，详见下文相应章节，或参考 附录 A – ESP32-S3 管脚总览。n2. 加粗功能为默认启动模式下管脚的默认功能，关于启动模式的更多信息，详见章节 3.1 芯片启动模式控制。n3. 供电管脚一栏，由 VDD_SPI 供电的管脚n• 电源实际来自给 VDD_SPI 供电的内部电源轨，详见章节 2.5.2 电源管理。n4. 供电管脚一栏，由 VDD3P3_CPU  VDD_SPI 供电的管脚n• 供电管脚（VDD3P3_CPU 或 VDD_SPI）由 eFuse 位 EFUSE_PIN_POWER_SELECTION 决定（详见 《ESP32-S3 技术参考手册》n> 章节 eFuse 控制器），可通过 IO_MUX_PAD_POWER_CTRL 位配置，详见 《ESP32-S3 技术参考手册》 > 章节 IO MUX 和nGPIO 交换矩阵。",
    "tags": ["H2 管脚说明","H3 管脚布局","H3 电源管理","VDDA","GND","VDD_SPI","VDD3P3_CPU","EFUSE_PIN_POWER_SELECTION","IO_MUX_PAD_POWER_CTRL","ESP32-S3电源管脚如何配置","VDD_SPI供电机制是什么","如何通过eFuse配置电源管脚"]
  },
  "segment_02": {
    "text": "5. 在 ESP32-S3R8V 芯片中，由于 VDD_SPI 电压已设置为 1.8 V，所以，不同于其他 GPIO，该芯片在 VDD_SPI 电源域中的 GPIO47 和nGPIO48 的工作电压也为 1.8 V。n6. 各管脚的默认驱动电流为n• GPIO17 和 GPIO1810 mAn乐鑫信息科技 16n反馈文档意见nESP32-S3 系列芯片技术规格书 v2.02 管脚n• GPIO19 和 GPIO2040 mAn• 其他管脚20 mA",
    "tags": ["H2 管脚说明","H3 IO管脚功能","ESP32-S3R8V","GPIO47","GPIO48","驱动电流","1.8V工作电压","GPIO17","GPIO18","GPIO19","GPIO20","为什么ESP32-S3R8V的GPIO4748电压不同","如何设置GPIO驱动电流","ESP32-S3各GPIO默认电流是多少"]
  },
  "segment_03": {
    "text": "7. 管脚配置一栏为复位时和复位后预设配置缩写n• IE – 输入使能n• WPU – 内部弱上拉电阻使能n• WPD – 内部弱下拉电阻使能n• USB_PU – USB 上拉电阻使能n– USB 管脚（GPIO19 和 GPIO20）默认开启 USB 功能，此时管脚是否上拉由 USB 上拉决定。USB 上拉由 USB_SERIAL_JTAG_DPnDM_PULLUP 控制，USB 上拉电阻的具体阻值可通过 USB_SERIAL_JTAG_PULLUP_VALUE 位控制，详见 《ESP32-S3 技术参考手册》n> 章节 USB 串口JTAG 控制器。n– USB 管脚关闭 USB 功能时，用作普通 GPIO，默认禁用管脚内部弱上下拉电阻，可通过 IO_MUX_FUN_WPUWPD 配置，n详见 《ESP32-S3 技术参考手册》 > 章节 IO MUX 和 GPIO 交换矩阵。",
    "tags": ["H2 管脚说明","H3 IO管脚功能","IE","WPU","WPD","USB_PU","USB_SERIAL_JTAG_DP","USB_SERIAL_JTAG_PULLUP_VALUE","IO_MUX_FUN_WPU","IO_MUX_FUN_WPD","如何配置USB管脚上拉电阻","USB管脚与GPIO模式怎么切换","ESP32-S3复位时的管脚默认状态"]
  },
  "segment_04": {
    "text": "8. EFUSE_DIS_PAD_JTAG 的值为n• 0 - 弱上拉电阻使能n• 1 - 管脚浮空n部分管脚在芯片上电过程中有毛刺，具体见表 2-2。n表 2-2. 芯片上电过程中的管脚毛刺n管脚名称 毛刺类型1 典型持续时间 (µs)nGPIO1 低电平毛刺 60nGPIO2 低电平毛刺 60nGPIO3 低电平毛刺 60nGPIO4 低电平毛刺 60nGPIO5 低电平毛刺 60nGPIO6 低电平毛刺 60nGPIO7 低电平毛刺 60nGPIO8 低电平毛刺 60nGPIO9 低电平毛刺 60nGPIO10 低电平毛刺 60nGPIO11 低电平毛刺 60nGPIO12 低电平毛刺 60nGPIO13 低电平毛刺 60nGPIO14 低电平毛刺 60nXTAL_32K_P 低电平毛刺 60nXTAL_32K_N 低电平毛刺 60nGPIO17 低电平毛刺 60nGPIO18n低电平毛刺 60n高电平毛刺 60nGPIO19n低电平毛刺 60n高电平毛刺2 60nGPIO20n下拉毛刺 60n高电平毛刺2 60n乐鑫信息科技 17n反馈文档意见nESP32-S3 系列芯片技术规格书 v2.02 管脚n1 低电平毛刺在持续期间维持低电平输出状态；n高电平毛刺在持续期间维持高电平输出状态；n下拉毛刺在持续期间维持内部弱下拉状态；n上拉毛刺在持续期间维持内部弱上拉状态。n关于高低电平和上下拉的相关具体参数，请参考表 5-4 直n流电气特性 (3.3 V, 25 °C)。n2 GPIO19 和 GPIO20 在芯片上电期间会出现两次高电平毛刺，n每次持续时间为 60 µs 左右，两次毛刺及中间的延迟共持续n的时间分别为 3.2 ms 和 2 ms。n乐鑫信息科技 18n反馈文档意见nESP32-S3 系列芯片技术规格书 v2.02 管脚n2.3 IO 管脚n2.3.1 IO MUX 功能nIO MUX 能让一个输入输出管脚连接多个输入输出信号。ESP32-S3 的每个 IO 管脚可在表 2-4 IO MUX 管脚功n能 列出的五个信号（IO MUX 功能，即 F0-F4）中选择，连接任意一个。",
    "tags": ["H2 管脚说明","H3 IO管脚功能","EFUSE_DIS_PAD_JTAG","管脚毛刺","低电平毛刺","高电平毛刺","下拉毛刺","GPIO1","GPIO20","XTAL_32K_P","XTAL_32K_N","如何消除ESP32-S3上电毛刺","管脚毛刺持续时间是多少","哪些GPIO会受上电毛刺影响","IO MUX","F0-F4"]
  }
}
```