import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/app.log",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
