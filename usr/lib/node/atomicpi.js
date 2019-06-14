
const sig = (chip, chipIndex, globalIndex) => ({
  chip: `gpiochip${chip}`,
  chip_idx: chipIndex,
  global_idx: globalIndex
})

const signals = {
  // External GPIO
  ISH_GPIO_0: sig(3, 21, 335),
  ISH_GPIO_1: sig(3, 18, 332),
  ISH_GPIO_2: sig(3, 24, 338),
  ISH_GPIO_3: sig(3, 15, 329),
  ISH_GPIO_4: sig(3, 22, 336),
  ISH_GPIO_7: sig(3, 16, 330),
  // Volume Up Pin
  GPIO_DFX_2: sig(1, 7, 348),
  // Volume Down Pin
  GPIO_DFX_4: sig(1, 5, 346),
  // Internal Signals
  I2C2_3P3_SDA: sig(0, 62, 476),
  I2C2_3P3_SCL: sig(0, 66, 480),
  AU_MIC_SEL: sig(1, 0, 341),
  XMOS_RESET: sig(1, 8, 349),
  BN_INT: sig(1, 17, 358),
  BN_RESET: sig(1, 25, 366)
}

// 26-pin connector descriptions
const atomicpi = {
  index_of: {
    ISH_GPIO_0: 24,
    ISH_GPIO_1: 25,
    ISH_GPIO_2: 26,
    ISH_GPIO_3: 18,
    ISH_GPIO_4: 19,
    ISH_GPIO_7: 20
  }
}

// Enchilada Breakout Board
const enchilada = {
  index_of: {
    ISH_GPIO_0: 9,
    ISH_GPIO_1: 10,
    ISH_GPIO_2: 11,
    ISH_GPIO_3: 3,
    ISH_GPIO_4: 4,
    ISH_GPIO_7: 5
  },
  leds: {
    green: 'ISH_GPIO_1',
    yellow: 'ISH_GPIO_2'
  }
}

// Physical Connector Descriptions
const connectors = {
  atomicpi,
  enchilada
}

Object.assign(module.exports, {
  /* Kernel-visible signals */
  signals,
  connectors
})
