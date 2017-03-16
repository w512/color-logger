#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import logging.handlers

from termcolor import cprint



class ColorLogger(object):
    """
    Write log messages to file and
    console (with any colors and backgrounds)
    """

    def __init__(self, logger_name, log_file_name):
        super(SmartLogger, self).__init__()

        self.logger_name = logger_name
        self.log_file_name = log_file_name

        self.logging_formatter = logging.Formatter(
            '[%(asctime)s][%(levelname)s] %(message)s',
            '%Y.%m.%d %H:%M:%S',
        )

        handler = get_rotation_handler(log_file_name)
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        self.logger.addHandler(handler)
        # self.logger_udp.addHandler(console_handler)

    def get_rotation_handler(log_file_name):
        rotating_handler = logging.handlers.RotatingFileHandler(
            log_file_name,
            maxBytes=3145728,   # 3Mb
            backupCount=5
        )
        rotating_handler.setFormatter(self.logging_formatter)

        return rotating_handler

    def write(self, message, color=None, background=None, attrs=[]):
        self.logger.debug(message)                         # write to file
        cprint(message, color, background, attrs=attrs)    # write to console

