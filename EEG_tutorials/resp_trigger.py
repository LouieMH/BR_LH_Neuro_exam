import numpy as np

# select only correct-response trials 

def convert_triggers(events, return_event_ids=False):
    """Function to convert triggers to failed and successful inhibition.

    Parameters
    ----------
    events : numpy array
        The original events
    return_event_id: bool
        If true return event_id that matches the new triggers.

    Returns
    -------
    converted_events
        The converted events.
    """
    events_tmp = events.copy()
    for idx, line in enumerate(events_tmp):
        if any(line[2] == [101,102,111,112]): 
            events_tmp[idx-1][2] = events_tmp[idx-1][2]+5
            events_tmp[idx-2][2] = events_tmp[idx-2][2]+5
            events_tmp[idx-3][2] = events_tmp[idx-3][2]+5

    event_id = {'Word/wPos': 16,
              'Wait/wPos': 36,
              'Image/wPos': 26,
              'Word/wNeg': 17,
              'Wait/wNeg': 37,
              'Image/wNeg': 27,
            'Word/wNeu': 18,
            'Wait/wNeu/iPos': 56, # positive image
            'Image/wNeu/iPos': 46, # positive image
            'Wait/wNeu/iNeg': 57, # negative image
            'Image/wNeu/iNeg': 47, # negative image
            'Correct/wPos': 101, # correct response ('b') to positive word + image
            'Correct/wNeg': 102, # correct response ('y') to negative word + image
            #'Correct/wNeu/iPos': 111, # correct response ('b') to neutral word + positive image
            'Correct/wNeu/iNeg': 112, # correct response ('y') to neutral word + negative image
            #'Incorrect/wPos': 202, # incorrect response ('y') to positive word + image
            #'Incorrect/wNeg': 201, # incorrect response ('b') to negative word + image
            #'Incorrect/wNeu/iPos': 212 # incorrect response ('y') to neutral word + positive image
            #'Incorrect/Neu/iNeg': 211, # incorrect response ('b') to neutral word + negative image
    }

    if return_event_ids:
        return (
            events_tmp,
            event_id,
        )
    else:
        return events_tmp
