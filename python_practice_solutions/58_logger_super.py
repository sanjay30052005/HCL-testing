
class Logger:
    def log(self,msg):
        print("Log:",msg)

class FileLogger(Logger):
    def log(self,msg):
        super().log(msg)
        print("Saved to file")

FileLogger().log("Test")
