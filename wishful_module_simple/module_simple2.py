import logging
import random
import wishful_upis as upis
from wishful_agent.core import wishful_module
from .module_simple import SimpleModule
from random import randint

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz}@tkn.tu-berlin.de"


@wishful_module.build_module
class SimpleModule2(SimpleModule):
    def __init__(self):
        super(SimpleModule2, self).__init__()
        self.log = logging.getLogger('SimpleModule2')
        self.channel = 1
        self.power = 1

    @wishful_module.on_function(upis.radio.set_power)
    def set_power(self, power, iface):
        self.log.debug("SimpleModule2 sets power: {} on device: {} and iface: {}"
                       .format(power, self.device, iface))
        self.power = power
        return {"SET_POWER_OK_value": power}

    @wishful_module.on_function(upis.radio.get_power)
    def get_power(self, iface):
        self.log.debug("SimpleModule2 gets power on device: {}"
                       .format(self.device))
        return self.power

    @wishful_module.on_function(upis.radio.get_noise)
    def get_noise(self):
        self.log.debug("Get Noise".format())
        return random.randint(-120, -30)

    @wishful_module.on_function(upis.radio.get_airtime_utilization)
    def get_airtime_utilization(self):
        self.log.debug("Get Airtime Utilization".format())
        return None

    @wishful_module.on_function(upis.radio.set_mac_access_parameters)
    def setEdcaParameters(self, queueId, queueParams):
        self.log.debug("SimpleModule2 sets EDCA parameters "
                       "for queue: {} on device: {}"
                       .format(queueId, self.device))

        print("Setting EDCA parameters for queue: {}".format(queueId))
        print("AIFS: {}".format(queueParams.getAifs()))
        print("CwMin: {}".format(queueParams.getCwMin()))
        print("CwMax: {}".format(queueParams.getCwMax()))
        print("TxOp: {}".format(queueParams.getTxOp()))
        return 0

