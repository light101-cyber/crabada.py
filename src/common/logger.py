"""
Create a logger for app-related events (bugs, info, etc)

For more advanced uses, see https://realpython.com/python-logging/
"""

import logging
import logging.handlers
from typing import Any, Union
from web3 import Web3
from src.common.dotenv import getenv
from web3.types import TxReceipt
from web3.datastructures import AttributeDict
from pprint import pformat

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(getenv("DEBUG_LEVEL", "WARNING"))

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.handlers.TimedRotatingFileHandler(
    "storage/logs/app/app.log", "midnight"
)
c_handler.setLevel(getenv("DEBUG_LEVEL", "WARNING"))
f_handler.setLevel(getenv("DEBUG_LEVEL", "WARNING"))

# Create formatters and add it to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


def logTx(txReceipt: TxReceipt) -> None:
    """Given a tx receipt, print to screen the transaction details
    and its cost"""
    logger.debug(formatAttributeDict(txReceipt))
    ethSpent = Web3.fromWei(
        txReceipt["effectiveGasPrice"] * txReceipt["gasUsed"], "ether"
    )
    logger.debug("Spent " + str(ethSpent) + " ETH")


def formatAttributeDict(
    attributeDict: Union[TxReceipt, AttributeDict[str, Any]], indent: int = 4
) -> str:
    """
    Web3 often returns AttributeDict instead of simple Dictionaries;
    this function return a pretty string with the AttributeDict content
    """
    output = "{"
    for key, value in attributeDict.items():
        output += " " * indent + f"{key} -> {pformat(value, indent=indent)}"
    output += "}"

    return output
