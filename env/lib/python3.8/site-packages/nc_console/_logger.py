import click as c
import typing as t

class logger:

    def __init__(self,
                box_colour:str = "white",
                msg_colour:str = "bright_yellow",
                type_info_colour:str = "bright_blue",
                type_success_colour:str = "bright_green",
                type_error_colour:str = "bright_red",
                type_warning_colour:str = "bright_magenta",
                ) -> None:

        self.box_colour:str = box_colour
        self.msg_colour:str = msg_colour
        self.type_info_colour:str = type_info_colour
        self.type_success_colour:str = type_success_colour
        self.type_error_colour:str = type_error_colour
        self.type_warning_colour:str = type_warning_colour

    def _open_box(self, **options:t.Any) ->str:
        options.setdefault("fg", self.box_colour)
        options.setdefault("bold", True)

        return c.style("[ ", **options)

    def _close_box(self, **options:t.Any) -> str:
        options.setdefault("fg", self.box_colour)
        options.setdefault("bold", True)

        return c.style(" ] ", **options)


    def _create_log_type_msg(self, type:str, **options:t.Any):

        colour:str = self.type_info_colour

        if options.get("colour", None) is None:
            
            if type.lower() == "warning":
                colour = self.type_warning_colour
            
            elif type.lower() == "success":
                colour = self.type_success_colour
            elif type.lower() == "error":
                colour = self.type_error_colour

        else:
            colour = options.get("colour")

        options.setdefault("fg", colour)
        options.setdefault("bold", True)
        return c.style(type.upper(), **options)


    def _message(self, msg:str, **options:t.Any):
        options.setdefault("fg", self.msg_colour)
        return c.style(msg, **options)

class ilogger(logger):
    def __init__(self, box_colour:str="bright_white", 
            msg_colour:str="bright_yellow",
            base_colour:str = "bright_blue",
            type_colour:str = "bright_blue"
            ) -> None:
        super(ilogger, self).__init__(box_colour=box_colour, 
                    msg_colour=msg_colour)

        self.base_colour = base_colour
        self.type_colour = type_colour
    
    def _create_input_type(self, type:t.Optional[str]=None, **options):
        options.setdefault("fg", self.base_colour)
        options.setdefault("bold", True)

        if type is not None:
            fst= c.style("INPUT-", **options)
            options.pop("fg")
            res = fst+c.style(type.upper(), fg=self.type_colour, **options)
            return res
        else:
            return c.style(f"INPUT", **options)