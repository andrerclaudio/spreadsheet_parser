# Build-in modules
import logging
import time
from datetime import timedelta
from threading import ThreadError, Thread

# Added modules
from pytictoc import TicToc
import pandas as pd

# Project modules

# Print in file
# logging.basicConfig(filename='logs.log',
#                     filemode='w',
#                     level=logging.INFO,
#                     format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
#                     datefmt='%d/%b/%Y - %H:%M:%S')

# Print in software terminal
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
                    datefmt='%d/%b/%Y - %H:%M:%S')

logger = logging.getLogger(__name__)


class ElapsedTime(object):
    """
    Measure the elapsed time between Tic and Toc
    """
    def __init__(self):
        self.t = TicToc()
        self.t.tic()

    def elapsed(self):
        _elapsed = self.t.tocvalue()
        d = timedelta(seconds=_elapsed)
        logger.info('< {} >'.format(d))


class ThreadingProcessQueue(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval):
        """
        Constructor
        """
        self.interval = interval

        thread = Thread(target=run, args=(self.interval,), name='Thread_name')
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution


def run(interval):
    """ Method that runs forever """
    while True:
        try:
            time.sleep(interval)

        except ThreadError as e:
            logger.exception('{}'.format(e))

        finally:
            pass


def application():
    """" All application has its initialization from here """
    logger.info('Main application is running!')

    df = pd.read_csv(r'~/Desktop/data.csv')
    steps = build_groups(df)

    return


def build_groups(df):
    """

    """
    group_number = df['Group Number'].tolist()
    action = df['Action'].tolist()
    feature = df['Feature'].tolist()
    target = df['Target'].tolist()

    big_group = []
    small_group = []

    index = 0
    previous_group = group_number[index]

    for group in group_number:
        row = [action[index], feature[index], target[index]]

        if group == previous_group:
            small_group.append(row)
        else:
            big_group.append(small_group.copy())
            small_group.clear()
            small_group.append(row)

        index += 1

    big_group.append(small_group.copy())

    return big_group
