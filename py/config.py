import logging
import os


class ServerConfig:
    _host = os.getenv("PYTHON_SERVER_HOST")
    _port = os.getenv("PYTHON_SERVER_PORT")
    if not _host:
        logging.info("PYTHON_SERVER_HOST not set, using default 127.0.0.1")
        _host = "127.0.0.1"
    if not _port:
        logging.info("PYTHON_SERVER_PORT not set, using default 60100")
        _port = "60100"