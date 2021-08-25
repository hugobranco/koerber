import sys
import traceback


class BaseExceptionHandler(Exception):

    def __init__(self, error_msg: str, class_name=None, def_name=None, app_dependency=None):
        self._error_message = ''

        self.__build_error_message(class_name=class_name, def_name=def_name, error_message=error_msg)

        if(app_dependency):
            app_dependency.execution_error(error_message=self.error_message)



    @property
    def error_message(self) -> str:
        return self._error_message



    @error_message.setter
    def error_message(self, new_error_message: str):
        self._error_message = new_error_message if new_error_message else ''



    def __build_error_message(self, class_name, def_name, error_message: str):
        """
            build error message and set to error_message instance attribute

            :param class_name:
                class name where the exception occurred
            :param def_name:
                function name where the exception occurred
            :param error_message:
                exception message
        """
        if(not class_name and not def_name):
            # Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()

            # Extract unformatter stack traces as tuples
            trace_back = traceback.extract_tb(ex_traceback)

            # Format stacktrace
            self.error_message = f"File : {trace_back[0][0]}\n" \
                                 f"Line Number : {trace_back[0][1]}\n" \
                                 f"Func.Name : {trace_back[0][2]}()\n" \
                                 f"Exception type : {ex_type.__name__} \n" \
                                 f"Exception Message : {error_message}\n"
        else:
            self.error_message = f"Class Name: {class_name}() \n" \
                                 f"Function Name: {def_name}() \n" \
                                 f"Exception Message: {error_message}"
