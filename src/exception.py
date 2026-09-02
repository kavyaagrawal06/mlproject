#This is a custom exception handling module commonly used in ML projects. It helps you get a detailed error message showing which Python file and which line caused the error.

import sys #sys is a built-in Python module that lets your program interact with the Python interpreter and the system.
#sys is mainly used for sys.exc_info().
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    """sys.exc_info() returns three values:   
        (type of exception, exception object, traceback)
          You don't need the first two values here, so _ is used:
            therefore :exc_tb
                contains the traceback information. """
    
    file_name=exc_tb.tb_frame.f_code.co_filename #This extracts the Python file where the error occurred.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception): #You are creating your own exception class.It inherits from Python's built-in: exception
                                       #This allows you to use: raise CustomException(...)
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self): #The __str__() method is specifically responsible for returning the message when we print the exception.
        return self.error_message   
    
    
"""Main parts:
1.error_message_detail()
Gets information about the error
Finds:
File name where error occurred
Line number
Actual error message

2.CustomException
Creates a custom error class using Python's built-in Exception.
Calls error_message_detail() to create a detailed error.

3.__str__()
Returns the detailed error message when we print the exception.    """


        