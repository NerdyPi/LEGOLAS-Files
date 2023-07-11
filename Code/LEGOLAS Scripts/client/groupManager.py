import core
import types
import rpyc

from threading import Event, Thread

#import GPy
#import numpy as np
from queue import LifoQueue, Queue


# def predict(X: np.array, Y: np.array, X_grid: np.array):
#         k = GPy.kern.RBF(1)
#         model = GPy.models.GPRegression(X, Y, k)
#         model.optimize('bfgs', max_iters=100)
#     
#         # Predict the mean and covariance of the GP fit over the grid
#         mean, Cov = model.predict(X_grid, full_cov=True)
#         variance = np.diag(Cov)
#         return mean, Cov, variance, model


"""
Wrapper class around a conceptual LEGOLAS unit. Used by the group manager to establish
groups and parallelize tasks
"""
class LegolasUnit:
    def __init__(self, config: str):
        stage, depo_device, pH_device, conn1, conn2, config = core.load_from_config(config)

        # Type annotations used
        self.stage: core.Stage = stage
        self.depo_device: core.DepositionDevice = depo_device
        self.ph_device: core.pHDevice = pH_device
        self.connA: rpyc.classic.ClassicService = conn1
        self.connB: rpyc.ClassicService = conn2
        self.config: core.ConfigurationManager = config

class GroupManager:
    def __init__(self, *config_list: str):
        self.__units = [LegolasUnit(cfg) for cfg in config_list]

        self.__threads = []

        self.taskQueue = LifoQueue()
        self.__results = Queue()

        self.release = Event()

    

    def __digest(self):
        # TODO break condition from digestion

        while not self.release.is_set():
            if not self.__results.empty():
                dataPoint = self.__results.get()
                

    def run(self):
        for unit in self.__units:
            thread = Thread(
                target = self.__dispatch(unit, tasks=self.taskQueue, results=self.__results, releaseTrigger=self.release))
            
            thread.start()
            self.__threads.append(thread)

        self.__digest()



    @staticmethod
    def __dispatch(unit: LegolasUnit, tasks: LifoQueue, results: Queue, releaseTrigger: Event):
        while not releaseTrigger.is_set():
            pass

    """
    This is the primary entry point for asynchronous experiment actions

    Supplied functions must take a single input, of type LegolasUnit
    """
    def executeExperiment(self, func: types.FunctionType):
        for i in self.__units:
            l = lambda: func(i) # Instantiates an anonymous function with internal pointer
                                # Avoids deadlocks for some reason (???)
            
            t = Thread(target=l)
            t.start()
            self.__threads.append(t)
    
    """
    Supplied function takes no input, should handle user scope directly
    """
    def executeAnalysis(self, func: types.FunctionType):
        t = Thread(target=func)
        t.run()