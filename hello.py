from coldtype import *

@animation(bg=1)
def scratch(f:Frame):
    return (StSt("ABC", Font.MuSan(), 100, wdth=f.e("eeio"))
        .align(f.a.r))
