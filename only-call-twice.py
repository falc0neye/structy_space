def set_call_times(num):
    
    call_count = 0
    
    def inner_func():
        if call_count > num:
            return 'Reached maximum call count'
        else:
            call_count += 1
            return f'Call count: {call_count}'
            
    return inner_func()
        
        
my_func = set_call_times(5)


print(my_func())

