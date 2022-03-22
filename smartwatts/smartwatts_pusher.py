from powerapi.pusher import PusherActor
from powerapi.report import BadInputData
from powerapi.exception import PowerAPIExceptionWithMessage, PowerAPIException

from thespian.actors import ActorAddress

from .report import FormulaReport

class SmartWattsPusherActor(PusherActor):
    def receiveMsg_FormulaReport(self, message: FormulaReport, _: ActorAddress):
        self.log_debug('received message ' + str(message))
        try:
            self.database.save(message)
            self.log_debug(str(message) + 'saved to database')
        except BadInputData as exn:
            log_line = 'BadinputData exception raised for report' + str(exn.input_data)
            log_line += ' with message : ' + exn.msg
            self.log_warning(log_line)
        except PowerAPIExceptionWithMessage as exn:
            log_line = 'exception ' + str(exn) + 'was raised while trying to save ' + str(message)
            log_line += 'with message : ' + str(exn.msg)
            self.log_warning(log_line)
        except PowerAPIException as exn:
            self.log_warning('exception ' + str(exn) + 'was raised while trying to save ' + str(message))