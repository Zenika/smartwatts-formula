from powerapi.cli.generator import PusherGenerator

from .smartwatts_pusher import SmartWattsPusherActor

class SmartwattsPusherGenerator(PusherGenerator):
    def _actor_factory(self, db_config):
        return SmartWattsPusherActor