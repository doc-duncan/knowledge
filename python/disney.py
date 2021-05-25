# Everything is overly commented to hopefully give you a gimpse into my thoughts

def compute_execution_times(call_history: list) -> dict:
    """
    Computes the execution time of each function ID in the given call history and returns the corresponding results as follows:

    {function_id: execution_time, ...}
    """
    
    # to hold our results
    exec_time = {}
    # the stack can be viewed as a stack of the latest running functions with
    # the current executing function at the top. Since the top function is what
    # is currently running, its corresponding "execution time" is what will
    # need to be updated when a new call is read 
    stack = []
    # decided to store stack length so the full length calculation could be avoided for each iteration in hopes to be more efficient
    stack_length = 0
    # this is a helper variable that marks if the last call read was of type "end"
    last_end = False 

    for call in call_history:
        # cleaned this up a bit from before to capture in one line
        func_id, call_type, time = call.split(":")
        time = int(time)

        if call_type == "start":
            # this one-liner was nicer for me than checking if "func_id" was in "exec_time" for each update
            exec_time[func_id] = 0 if func_id not in exec_time else exec_time[func_id]
            # we only want to update an execution time if there is actually something "running"
            if stack_length > 0:
                stack_top = stack[stack_length - 1]
                stack_top_func_id = stack_top["func_id"]
                stack_top_time = stack_top["time"]
                # if the last call read was NOT of type "end" then everything between the start time for the function
                # at the top of the stack (current running funtion) and the current time can be attributed to the
                # current running function
                if not last_end:
                    exec_time[stack_top_func_id] += (time - stack_top_time)
                # if the last call read was of type "end" then we only want to attribute the gap between the current time
                # and the last time of type "end" to the current running function (subtracting 1 because it is truly only the gap between - exclusive)
                else:
                    exec_time[stack_top_func_id] += (time - last_end_time - 1)
            # add the new current running function to stack
            stack.append({"func_id": func_id, "time": time})
            stack_length += 1
            # last call was of type "start"
            last_end = False
        
        if call_type == "end":
            stack_top = stack[stack_length - 1]
            stack_top_func_id = stack_top["func_id"]
            stack_top_time = stack_top["time"]
            # if the last call read was NOT of type "end" then everything between the start time for the function
            # at the top of the stack (current running function) and the current time can be attributed to the
            # current running function (+1 because end is inclusive)
            if not last_end:
                exec_time[stack_top_func_id] += (time - stack_top_time + 1)
            # if the last call read was of type "end" then we only want to attribute the gap between the current time and
            # the last time of type "end" to the current running function (no "-1" here because end is inclusive)
            else:
                exec_time[stack_top_func_id] += (time - last_end_time) 
            # last call was of type "end"
            last_end = True
            # update last_end_time to be used in calculations when last call was of type "end"
            last_end_time = time
            # current function is done running so remove
            stack.pop()
            stack_length -= 1

    return exec_time

