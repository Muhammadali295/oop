class Education(Exception):
    pass
def years():
    years = int(input('enter years of education:'))
    try:
        if(years<=16):
            raise Education('Its not enough')
    except TypeError as obj:
        print('input correct type',obj)
    else:
        print('you are eligible')
years()
