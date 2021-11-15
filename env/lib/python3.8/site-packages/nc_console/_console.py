from ._logger import logger, ilogger
from getpass import getpass
import typing as t
import click as c

default_input = input

#default colour configuration for the output stream
_op_box_colour:str = "white"
_op_msg_colour:str = "bright_yellow"
_op_type_info_colour:str = "bright_blue"
_op_type_success_colour:str = "bright_green"
_op_type_error_colour:str = "bright_red"
_op_type_warning_colour:str = "bright_magenta"

#default colour configuration for input stream
_ip_box_colour = "white"
_ip_msg_colour = "bright_yellow"
_ip_base_colour = "bright_blue"
_ip_type_colour = "bright_blue"

def setLogConfig(box_colour:t.Optional[str] = None,
        msg_colour:t.Optional[str] = None,
        type_info_colour:t.Optional[str] = None,
        type_success_colour:t.Optional[str] = None,
        type_error_colour:t.Optional[str] = None,
        type_warning_colour:t.Optional[str] = None
        ) -> None:
        """
        Please use this function if you want to customize default 
        available colour to print different logs.

        Customize the log color by providing value to this function.
        
        :param box_colour:
            add colour for the open and close boxes. 
            It's take the all the colour available for click.style

        :param msg_colour:
            add colour for the message body.
            It's take the all the colour available for click.style

        :param type_info_colour:
            add colour for the type info.
            It's take the all the colour available for click.style

        :param type_success_colour:
            add colour for the type success.
            It's take the all the colour available for click.style

        :param type_error_colour:
            add colour for the type error.
            It's take the all the colour available for click.style

        :param type_warning_colour:
            add colour for the type warning.
            It's take the all the colour available for click.style

        example::

            from nc_colsole import Console
            Console.setLogConfig(msg_colour="bright_cyan")
        """
        if box_colour is not None:
            global _op_box_colour
            _op_box_colour = box_colour

        if msg_colour is not None:
            global _op_msg_colour
            _op_msg_colour = msg_colour

        if type_info_colour is not None:
            global _op_type_info_colour
            _op_type_info_colour = type_info_colour

        if type_success_colour is not None:
            global _op_type_success_colour
            _op_type_success_colour = type_success_colour

        if type_error_colour is not None:
            global _op_type_error_colour
            _op_type_error_colour = type_error_colour

        if type_warning_colour is not None:
            global _op_type_warning_colour
            _op_type_warning_colour = type_warning_colour


def setInputConfig(box_colour:t.Optional[str] = None,
                msg_colour:t.Optional[str] = None,
                base_colour:t.Optional[str] = None,
                type_colour:t.Optional[str] = None
                ) -> None:
    """
    Please use this function if you want to customize default 
    available colour for input system.

    Customize the input log color by providing value to this function.

    :param box_colour:
            add colour for the open and close boxes. 
            It's take the all the colour available for click.style

    :param msg_colour:
        add colour for the message body.
        It's take the all the colour available for click.style

    :param base_colour:
        add colour for the base INPUT data.
        It's take the all the colour available for click.style

    :param type_colour:
        add colour for the input type.
        It's take the all the colour available for click.style   

    example::

        from nc_console import Console
        Console.setInputConfig(msg_colour="green") 

    """
    if box_colour is not None:
        global _ip_box_colour
        _ip_box_colour = box_colour

    if msg_colour is not None:
        global _ip_msg_colour
        _ip_msg_colour = msg_colour

    if base_colour is not None:
        global _ip_base_colour
        _ip_base_colour = base_colour

    if type_colour is not None:
        global _ip_type_colour
        _ip_type_colour = type_colour



class log:

    _logger_class = logger

    @classmethod
    def _clogger(cls, 
            type:str, 
            message_:str,
            open_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
            log_type_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
            close_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
            message_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None 
            ) -> None:

            _logger:t.Type["logger"] = cls._logger_class(_op_box_colour,
                                                 _op_msg_colour, 
                                                 _op_type_info_colour, 
                                                 _op_type_success_colour, 
                                                 _op_type_error_colour, 
                                                 _op_type_warning_colour
                                                 )
            
            if open_box_options is not None:
                ob_msg_ins = _logger._open_box(**open_box_options)
            else:
                ob_msg_ins = _logger._open_box()

            if log_type_options is not None:
                clbm_msg_ins = _logger._create_log_type_msg(type, **log_type_options)
            else:
                clbm_msg_ins = _logger._create_log_type_msg(type)

            if close_box_options is not None:
                cb_msg_ins = _logger._close_box(**close_box_options)
            else:
                cb_msg_ins = _logger._close_box()

            if message_options is not None:
                m_msg_ins = _logger._message(message_, **message_options)
            else:
                m_msg_ins = _logger._message(message_)

            c.echo(ob_msg_ins+clbm_msg_ins+cb_msg_ins+m_msg_ins)

    @classmethod
    def Success(cls, 
                message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                log_type_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                message_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None
                ) -> None:
        """
        Log the success message at terminal.

        :param message:
            the default message to be logged in the terminal.

        :param open_box_options:
            provide a dictionary to customize the look of open box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param log_type_options:
            provide a dictionary to customize the look of base type message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param close_box_options:
            provide a dictionary to customize the look of close box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param message_options:
            provide a dictionary to customize the look of the message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        example::

            Console.log.Success("image added successfully.")
        """
        if "\n" in message:
            message_line_list:list = message.split("\n")
            
            for _message in message_line_list: 
                 cls._clogger("success", _message,
                        open_box_options,
                        log_type_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("success", message,
                open_box_options,
                log_type_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Error(cls, message:str=None,
                open_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                log_type_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                message_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None
                ) -> None:
        """
        Log the error message at terminal.

        :param message:
            the default message to be logged in the terminal.

        :param open_box_options:
            provide a dictionary to customize the look of open box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param log_type_options:
            provide a dictionary to customize the look of base type message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param close_box_options:
            provide a dictionary to customize the look of close box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param message_options:
            provide a dictionary to customize the look of the message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        example::

            Console.log.Error("Failed to add image.")
        """
        if "\n" in message:
            message_line_list:list = message.split("\n")
            
            for _message in message_line_list: 
                 cls._clogger("error", _message,
                        open_box_options,
                        log_type_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("error", message,
                open_box_options,
                log_type_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Info(cls, message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                log_type_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                message_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None
                ) -> None:
        """
        Log the info message at terminal.

        :param message:
            the default message to be logged in the terminal.

        :param open_box_options:
            provide a dictionary to customize the look of open box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param log_type_options:
            provide a dictionary to customize the look of base type message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param close_box_options:
            provide a dictionary to customize the look of close box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param message_options:
            provide a dictionary to customize the look of the message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        example::

            Console.log.Info("Image upload process started.")
        """
        if "\n" in message:
            message_line_list:list = message.split("\n")
            
            for _message in message_line_list: 
                 cls._clogger("info", _message,
                        open_box_options,
                        log_type_options,
                        close_box_options,
                        message_options)
        
        else: cls._clogger("info", message,
                open_box_options,
                log_type_options,
                close_box_options,
                message_options)
    
    @classmethod
    def Warning(cls, message:str=None, 
                open_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                log_type_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                close_box_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None,
                message_options:t.Optional[t.Dict[str, t.Union[str, bool]]]=None
                ) -> None:
        """
        Log the warning message at terminal.

        :param message:
            the default message to be logged in the terminal.

        :param open_box_options:
            provide a dictionary to customize the look of open box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param log_type_options:
            provide a dictionary to customize the look of base type message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param close_box_options:
            provide a dictionary to customize the look of close box.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        :param message_options:
            provide a dictionary to customize the look of the message.
            This dictionary will be passed as kwargs on click.style()
            function for respective method.

        example::

            Console.log.Warning("Uploading image process is asking for S3 credentials.")
        """
        if "\n" in message:
            message_line_list:list = message.split("\n")
            
            for _message in message_line_list: 
                 cls._clogger("warning", _message,
                        open_box_options,
                        log_type_options,
                        close_box_options,
                        message_options)
        
        else: 
            cls._clogger("warning", message,
                open_box_options,
                log_type_options,
                close_box_options,
                message_options)

class input:

    _logger_class:t.Type["ilogger"] = ilogger

    @classmethod
    def _create_input_message(cls, message:str, type:t.Optional[str]=None):
        _logger = cls._logger_class(box_colour=_ip_box_colour, 
                            msg_colour=_ip_msg_colour, 
                            base_colour= _ip_base_colour,
                            type_colour=_ip_type_colour
                            )
        msg = _logger._open_box()+\
            _logger._create_input_type(type)+\
                _logger._close_box()+\
                    _logger._message(message)

        return msg

    @classmethod
    def String(cls, message:t.Optional[str]=None) -> str:
        """
        take the string type input from the terminal.

        :param message:
            the default message you want to log 
            while taking the string input from terminal.

        example::

            Console.input.String("Please enter your name: ")
        """

        while True:
            string = default_input(cls._create_input_message(message, "STRING"))
            try: 
                return str(string)
            
            except: 
                log.Error(f"String type data is required. got: {type(string).__name__}")
            
    @classmethod
    def Password(cls, message:t.Optional[str]=None) -> str:
        """
        take the password input from the terminal.

        :param message:
            the default message you want to log 
            while taking the password input from terminal.

        example::

            Console.input.Password("Please enter your password: ")
        """

        password = getpass(prompt=cls._create_input_message(message, "PASSWORD"))
        return password
                
    @classmethod
    def Integer(cls, message:t.Optional[str]=None) -> int:
        """
        take the integer input from the terminal.

        :param message:
            the default message you want to log 
            while taking the integer input from terminal.

        example::

            Console.input.Integer("Please enter your age: ")
        """

        
        while True:
            integer = default_input(cls._create_input_message(message, "INTEGER"))
            try: 
                return int(integer)
            except:
                log.Error(f"int type data required. got: {type(integer).__name__}")

    @classmethod
    def Float(cls, message:t.Optional[str]=None) -> float:
        """
        take the float input from the terminal.

        :param message:
            the default message you want to log 
            while taking the float input from terminal.

        example::

            Console.input.Float("Please enter any float value: ")
        """
        while True:
            _float = default_input(cls._create_input_message(message, "FLOAT"))
            try: 
                return float(_float)
            except:
                log.Error(f"float type data required. got: {type(_float).__name__}")

    @classmethod
    def Boolean(cls, message:t.Optional[str]=None) -> bool:
        """
        take the float input from the terminal.

        :param message:
            the default message you want to log 
            while taking the float input from terminal.
            It will add ? (Y/n): after the message automatically.

        example::

            Console.input.Boolean("Do you want to continue")
        """
        _extra_msg = c.style(" ? (Y/n): ", fg="red", bold=True)
        _message = cls._create_input_message(message, "BOOLEAN")+_extra_msg
        while True:
            boolean = default_input(_message)
            if not boolean: 
                continue

            if str(boolean).lower() == "y" or str(boolean).lower() == "yes": 
                return True

            if str(boolean).lower() == "n" or str(boolean).lower() == "no": 
                return False

            else: 
                log.Error("Invalid input type. Proper ans format is : y for yes and n for no") 
                continue