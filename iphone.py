class iPhone:
    def __init__(self,version):
        self.version = version
        self.battery = 100

    def play_game(self):
        self.battery = int(self.battery - self.battery * .2)
        
    def send_text(self):
        self.battery = int(self.battery - .01)

    def watch_video(self):
        self.battery = int(self.battery - self.battery*.1)

    def take_picture(self):
        self.battery = self.battery - 1

    def recharge(self,amount_recharge):
        self.battery = self.battery+amount_recharge

        if self.battery > 100:
            self.battery = 100
