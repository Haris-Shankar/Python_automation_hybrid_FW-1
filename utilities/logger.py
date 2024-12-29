import logging
from datetime import datetime
import os

class LogGen:
    #@staticmethod
    # def loggen():
    #     # Get the current timestamp for unique log files
    #     current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    #
    #     # Set up log file path (e.g., in the Logs folder)
    #     log_folder = os.path.join(os.getcwd(), "Logs")
    #     if not os.path.exists(log_folder):
    #         os.makedirs(log_folder)
    #
    #     log_file = os.path.join(log_folder, f"automation_{current_time}.log")
    #     print(f"Log file path: {log_file}")
    #
    #     logging.basicConfig(
    #         filename=log_file,
    #         format='%(asctime)s - %(levelname)s - %(message)s',
    #         level=logging.INFO
    #     )
    #
    #     logger = logging.getLogger()
    #     return logger

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger