#   Qenawi created BaseModel.py at 4/29/21, 10:35 PM
#   BaseModel.py @Docs
#

# Description
import abc


class BaseModelProtocol:
    # MARK:- Abstract function to return class analytic value
    # MARK:- get_hashmap get hash map of the object
    @abc.abstractmethod
    def get_hashmap(self):
        pass
