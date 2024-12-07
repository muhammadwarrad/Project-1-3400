
# config.py

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "root": {
            "level": "DEBUG",  # Log level for the root logger
            "handlers": ["logp", "loge", 'console'],  # Handlers to be used by the root logger
        },
        "matplotlib": {
            "level": "WARNING",  # Set matplotlib's log level to WARNING
            "handlers": [],  # No handlers for matplotlib logger
        },
    },
    "handlers": {
        "logp": {
            "class": "logging.FileHandler",
            "filename": "logp.log",
            "level": "DEBUG",  # Log all processes, from DEBUG level upwards
            "formatter": "default",  # Correctly referencing the 'default' formatter
            "mode": "w",  # Overwrite the log file each time
        },
        "loge": {
            "class": "logging.FileHandler",
            "filename": "loge.log",
            "level": "WARNING",  # Log only warnings and errors
            "formatter": "default",  # Correctly referencing the 'default' formatter
            "mode": "w",  # Overwrite the log file each time
        },
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",  # Log all processes, from DEBUG level upwards
            "formatter": "default",  # Correctly referencing the 'default' formatter
        },
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",  # Formatter format
        },
    },
}

CSV_CONFIG = {
    'filepath_or_buffer': 'Data.csv',
    'sep': ',',  # Delimiter, default is a comma
    'header': 0,  # Row number to use as column names
    'encoding': 'utf-8',  # File encoding
    'index_col': False,  # Do not set any column as the index
    'skiprows': 0,  # Skip rows before reading
}


API_CONFIG = {
    "params":{
    "latitude":None,
    "logitude":None,
    "current_weather": "true",
    "precipitation": "true",
    "rain": "true",
    "temperature_unit": "fahrenheit",
    "timezone": "America/Chicago"
    },
    "url": "https://api.open-meteo.com/v1/forecast",
}