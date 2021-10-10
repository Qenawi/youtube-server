"""
@Docs
"""
import abc


# Description
class AnalyticProtocol:
    # MARK:- Abstract function to return class analytic value
    @abc.abstractmethod
    def calculate_analytic_value(self):
        pass
