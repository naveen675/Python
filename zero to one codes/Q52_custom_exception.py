class custom_exception(Exception):

    def __init__(self,msg):
        self.msg = msg

    
    
#c = custom_exception("some thing went wrong")

if __name__ == '__main__':
    n = int(input())

    try:
        
        if n < 0:
            raise custom_exception('Some thing went Wrong')
    except custom_exception as e:

        print(e)

    
    