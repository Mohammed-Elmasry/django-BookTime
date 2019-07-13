class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


    def warn(self, warning=""):
        print(bcolors.FAIL + warning + bcolors.ENDC)

    def info(self, message=""):
        print(self.warning + str(message) + self.ENDC)