import numpy as np

__all__ = ["mm2in", "AxPaperHW", "BxPaperHW", "figure_size"]

def mm2in(x):
    ''' Changes mm unit to inch.
    '''
    return x / 25.4

def AxPaperHW(x, rounding=True):
    ''' Returns height and width of Ax size in mm unit.
    For example, for A4 size, set ``x=4``.
    '''
    if (not isinstance(x, int)) or (x < 0):
        raise ValueError("x must be 0 or a positive integer!")
    
    power_i = 1/4 - (x)/2
    
    height = 1000 * 2**power_i # in mm
    width = height / 2**0.5   # in mm
    
    if rounding:
        height = round(height)
        width = round(width)
    
    return height, width

def BxPaperHW(x, rounding=True):
    ''' Returns height and width of Bx size in mm unit.
    For example, for B5 size, set ``x=5``.
    '''
    height, width = AxPaperHW(x, rounding=False)
    height *= 2**(1/4)
    width *= 2**(1/4)
    
    if rounding:
        height = round(height)
        width = round(width)
        
    return height, width 

def figure_size(paper_type='A', paper_size=4):
    if paper_type.upper() == 'A':
        figsize = mm2in(np.array(AxPaperHW(int(paper_size))))[::-1]
    elif paper_type.upper() == 'B':
        figsize = mm2in(np.array(BxPaperHW(int(paper_size))))[::-1]
    else:
        raise ValueError("Paper type not understood.")

    return figsize