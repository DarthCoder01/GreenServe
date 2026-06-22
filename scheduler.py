from config import *

def scheduler_decision(carbon):

    if carbon >= DIRTY_THRESHOLD:

        return {
            "status": "DIRTY",
            "action": "DEFER_BRONZE"
        }

    elif carbon <= GREEN_THRESHOLD:

        return {
            "status": "GREEN",
            "action": "RUN_ALL"
        }

    else:

        return {
            "status": "NORMAL",
            "action": "RUN_GOLD_SILVER"
        }
