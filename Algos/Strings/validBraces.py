def validBraces(braces):
    """ Return True/False if braces are 'valid' """
    # [[({)}]]
    #   => [[({ "{"
    # [[{(whoa, thats, crazy)}]]
    # ][
    """
        Trick:  stack: maintain tally of encountered braces
                dictionary: holds a map of associated braces
    """
    opens = []
    closes = (')', '}', ']')
    brace_map = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    # CASE: first brace is close (FAIL)

    # loop braces, 
    for brace in braces:
        # check if is not a brace, continue
        # if brace not in closes or brace not in brace_map:
        #     continue
        
        # check if brace is open brace
        if brace in brace_map:
            # push open braces to opens
            opens.append(brace)

        # check to see if close
        elif brace in closes:
            # check if opens empty
            if len(opens) == 0:
                return False

            # if so check if close matches last open
            if brace_map[opens.pop()] != brace:
                return False
    
    # CASE: anything in opens after loop (FAIL)
    return len(opens) == 0
    
    

print(validBraces("(!{})[()]"))


    