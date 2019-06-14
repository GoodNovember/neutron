__all__ = ["signals", "atomicpi", "enchilada"]

class _data(dict):
  def __getattr__(self, name):
    return self[name]

# Kernel-visible signals
signals = _data(
  #  External GPIO
    ISH_GPIO_0    = _data(chip='gpiochip3', chip_idx=21, global_idx=335),
    ISH_GPIO_1    = _data(chip='gpiochip3', chip_idx=18, global_idx=332),
    ISH_GPIO_2    = _data(chip='gpiochip3', chip_idx=24, global_idx=338),
    ISH_GPIO_3    = _data(chip='gpiochip3', chip_idx=15, global_idx=329),
    ISH_GPIO_4    = _data(chip='gpiochip3', chip_idx=22, global_idx=336),
    ISH_GPIO_5    = _data(chip='gpiochip3', chip_idx=16, global_idx=330),
  # Volume up pin
    GPIO_DFX_2    = _data(chip='gpiochip1', chip_idx=7, global_idx=348),
  # Volume down pin
    GPIO_DFX_4    = _data(chip='gpiochip1', chip_idx=5, global_idx=346),
  # Internal signals
    I2C2_3P3_SDA  = _data(chip='gpiochip0', chip_idx=62, global_idx=476),
    I2C2_3P3_SCL  = _data(chip='gpiochip0', chip_idx=66, global_idx=480),
    AU_MIC_SEL    = _data(chip='gpiochip1', chip_idx=0,  global_idx=341),
    XMOS_RESET    = _data(chip='gpiochip1', chip_idx=8,  global_idx=349),
    BN_INT        = _data(chip='gpiochip1', chip_idx=17, global_idx=358),
    BN_RESET      = _data(chip='gpiochip1', chip_idx=25, global_idx=366)
)

# Physical connector descriptions
connectors = _data(
  # 26 pin connector interface
  atomicpi = _data(
    index_of = _data(
      ISH_GPIO_0 = 24,
      ISH_GPIO_1 = 25,
      ISH_GPIO_2 = 26,
      ISH_GPIO_3 = 18,
      ISH_GPIO_4 = 19,
      ISH_GPIO_7 = 20
    )
  ),
  enchilada = _data(
    index_of = _data(
      ISH_GPIO_0 = 9,
      ISH_GPIO_1 = 10,
      ISH_GPIO_2 = 11,
      ISH_GPIO_3 = 3,
      ISH_GPIO_4 = 4,
      ISH_GPIO_7 = 5
    ),
    leds = _data(
      green = "ISH_GPIO_1",
      yellow = "ISH_GPIO_2"
    )
  )
)