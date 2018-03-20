from logger import logger


class file_logger(logger):

    """
       Constructor
       """

    def __init__(self, log_level):
        self.__log_level__ = log_level

    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """

    def log(self, log_level, message):
        my_file = open("my_file.txt", 'a')

        if (log_level <= self.__log_level__):
            my_file.write(str(log_level) + ": " + message + "\n")

            my_file.close()

        return
