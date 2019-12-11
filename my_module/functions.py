import random

def end(msg_in):
    """Function to end this chatbot
    
    Parameters
    ----------
    msg_in: string
        Message as input
    
    Returns
    -------
    output: boolean
        Result of whether message is an end message"""
    
    if 'Quit' in msg_in:
        output = True
        
    else:
        output = False
        
    return output



def selector(input_list, check_list, return_list):
    """Function to check if the input is in a list waiting to be checked, and if so return something from a list
    
    Parameters
    ----------
    input_list: list of string
        A list of words as input
    
    check_list: list of string
        A list of words waiting to be checked with
        
    return_list: list of string
        A list of words that possibly be returned if input_list is in check_list
        
    Returns
    -------
    output: string
        Result of the words returned"""
    
    output = None
    
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            
    return output



def buy_cd(msg_in):
    """Function to check if message mentions CD
    
    Parameters
    ----------
    msg_in: string
        Message as input
    
    Returns
    -------
    output: boolean
        Result of whether message mentions CD"""
    
    if 'CD' in msg_in:
        output = True
        
    else:
        output = False
        
    return output



def fan_meeting(msg_in):
    """Function to check if message mentions fan meeting
    
    Parameters
    ----------
    msg_in: string
        Message as input
    
    Returns
    -------
    output: boolean
        Result of whether message mentions fan meeting"""
    
    if 'fan meeting' in msg_in:
        output = True
        
    else:
        output = False
        
    return output



def other_artist(msg_in):
    """Function to check if message mentions other artist
    
    Parameters
    ----------
    msg_in: string
        Message as input
    
    Returns
    -------
    output: boolean
        Result of whether message mentions other artist"""
    
    if 'other' in msg_in:
        output = True
        
    else:
        output = False
        
    return output