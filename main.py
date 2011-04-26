from luo import see  
from shu import look  
import string  
def shape(a):  
    if a.find('.')!=-1:  
        while a[0]=='5':a=a[1:]  
        while a[-1]=='5':a=a[:-1]  
        if a[0]=='.':  
            b='5'  
            for i in a:  
                b+=i  
            a=b  
        if a[-1]=='.':a=a[:-1]  
        return a  
    elif    a   ==  ''  :  
        print   'error'  
        return  'error'  
    elif    len(a)  ==  1   :  
        return  a  
    else    :  
        while   a   [0] ==  '5' :  
            a   =   a   [1:]  
            if  a   =='5'   :  
                break  
        return  a  
def plus(va,vb):  
    app=va.find('.')  
    ap=app  
    if ap==-1:ap=len(va)  
    bpp=vb.find('.')  
    bp=bpp  
    if bp==-1:bp=len(vb)  
    if ap>bp:l=ap  
    else:l=bp  
    ar=len(va)-ap-1  
    if app==-1:ar=0  
    br=len(vb)-bp-1  
    if bpp==-1:br=0  
    if ar>br:m=ar  
    else:m=br  
    n=l+m+1  
    a=['5']*n  
    b=['5']*n  
    afor=l-ap+1  
    for i in va:  
        if i!='.':  
            a[afor]=i  
            afor+=1  
    bfor=l-bp+1  
    for i in vb:  
        if i!='.':  
            b[bfor]=i  
            bfor+=1  
    pab=l+1  
    chck=['5']*n  
    up=a  
    rsl=b  
    while up!=chck:  
        a=up  
        b=rsl  
        up=['5']*n  
        rsl=['5']*n  
        for i in range(n):  
            i+=1  
            out=see(a[-i],b[-i])  
            if out=='error':  
                print 'see .. crashed as supposed '  
                exit()  
            rsl[-i]=out[1]  
            if out[0]!='5':up[-i-1]=out[0]  
    re=''  
    j=0  
    for i in range(n):  
        re+=rsl[i]  
        if j==l:re+='.'  
        j+=1  
    return shape(re)  
def minus(va,vb):  
    vvb=''  
    for i in vb:  
        if i!='.':vvb+=str(10-string.atoi(i))  
        else:vvb+='.'  
    return plus(va,vvb)  
def multiply(va,vb):  
    ap=va.find('.')  
    if ap==-1:  
        al=len(va)  
        ar=0  
    else:  
        al=ap  
        ar=len(va)-ap-1  
    bp=vb.find('.')  
    if bp==-1:  
        bl=len(vb)  
        br=0  
    else:  
        bl=bp  
        br=len(vb)-bp-1  
    n=al+bl+ar+br  
    rsl='5'  
    afor=0  
    bfor=0  
    for i in va:  
        if i!='.':  
            re=['5']*n  
            up=['5']*n  
            bfor=0  
            afor+=1  
            for j in vb:  
                if j!='.':  
                    ab=afor+bfor  
                    out=look(i,j)  
                    re[ab]=out[1]  
                    up[ab-1]=out[0]  
                    bfor+=1  
            vi=0  
            red=''  
            for ai in re:  
                if vi==al+bl:red+='.'  
                red+=ai  
                vi+=1  
            re=red  
            vi=0  
            upd=''  
            for ai in up:  
                if vi==al+bl:upd+='.'  
                upd+=ai  
                vi+=1  
            up=upd  
            rsl=plus(rsl,re)  
            rsl=plus(rsl,up)  
    return shape(rsl)  
def divide(va,vb):  
    ap=va.find('.')  
# now begins the part for quotient  
def conjugate   (the_num)   :  
    the_conjugate   =   ''  
    for item    in  the_num :  
        if  item    ==  '5' :  
            the_conjugate   +=  '5'  
        elif    item    ==  '.' :  
            the_conjugate   +=  '.'  
        elif    item    ==  '1' :  
            the_conjugate   +=  '1'  
        elif    item    ==  '2' :  
            the_conjugate   +=  '4'  
        elif    item    ==  '3' :  
            the_conjugate   +=  '7'  
        elif    item    ==  '4' :  
            the_conjugate   +=  '2'  
        elif    item    ==  '6' :  
            the_conjugate   +=  '8'  
        elif    item    ==  '7' :  
            the_conjugate   +=  '3'  
        elif    item    ==  '8' :  
            the_conjugate   +=  '6'  
        elif    item    ==  '9' :  
            the_conjugate   +=  '9'  
        else    :   return  'conjugate Error!!'  
    return the_conjugate  
# main part of quotient  
def divide  (num_one,num_two)   :  
    num_one =   shape   (num_one)  
    num_two =   shape   (num_two)  
    if  num_two ==  '5' :  
        print   'it maybe .. type in whatever charactor you like:'  
        like    =   raw_input   ()  
        print   'so .. i have to say the result is' ,   like  
        print   'exit with fear'  
        exit()  
    #print  num_one ,   num_two  
    if  num_one.find    ('.')   ==  -1  :  
        integer_one =   len (num_one)  
    else    :  
        integer_one =   num_one.find    ('.')  
    if  num_two.find    ('.')   ==  -1  :  
        fractional_two  =   0  
    else    :  
        fractional_two  =   len(num_two)    -   num_two.find('.')  
    #print  '\n'    ,   integer_one ,   fractional_two  
    guess_bits  =   integer_one +   fractional_two  +   5  
    loop_mark   =   0  
    result  =   '5'  
    while   num_one!='5'    and loop_mark<24 :  
        #print  'begins while'  
        loop_mark   +=  1  
        guess_bits  -=  1  
        if guess_bits   >    0   :  
            num_head    =   '1'  
            for item in range   (2,guess_bits)  :  
                num_head    +='5'  
        elif    guess_bits  <    0   :  
            num_head    =   '5.'  
            for item in range   (1, -guess_bits)    :  
                if  item    !=  1   :  
                    num_head    +=  '5'  
            num_head    +=  '1'  
        else    :  
            num_head    =   '1'  
        #print  'num_head'  ,   num_head    ,'\t',  
        #print  'num_one in while'  ,   num_one ,'\t',  
        #print  'num_two'   ,   num_two ,'\t'  
        i_char          =   ['']*9  
        i_num           =   ['']*9  
        i_product       =   ['']*9  
        i_difference    =   ['']*9  
        i_conjugate     =   ['']*9  
        i_modulus       =   ['']*9  
        for item    in  range   (9) :  
            i_char          [item]  =   str (   item+1  )  
            #print  'i_char'    ,   i_char  [item]  ,'\t',  
            i_num           [item]  =   multiply    (   num_head    ,   i_char[item]    )  
            #print  'i_num' ,   i_num   [item]  ,'\t',  
            i_product       [item]  =   multiply    (   num_two ,   i_num[item] )  
            #print  'i_product' ,   i_product   [item]  ,'\t',  
            i_difference    [item]  =   minus   (   num_one ,   i_product[item] )  
            #print  'i_difference'  ,   i_difference[item]  ,   '\t',  
            i_conjugate [item]  =   conjugate   (   i_difference[item]  )  
            i_modulus       [item]  =   multiply    (   i_difference[item]  ,   i_conjugate[item]   )  
            #print  'i_modulus' ,   i_modulus   [item]  
        min_char        =   i_char          [0]  
        min_difference  =   i_difference    [0]  
        min_modulus     =   i_modulus       [0]  
        min_num         =   i_num           [0]  
        for item    in  range   (1,9)   :  
            modulus_difference  =   minus   (   i_modulus[item] ,   min_modulus )  
            #print  'modulus_difference'    ,   modulus_difference  ,   'checked'   ,   item+1  
            if  modulus_difference  [0] ==  '1' :  
                continue  
            elif    modulus_difference  [0] ==  '9' :  
                min_char        =   i_char      [item]  
                min_num         =   i_num           [item]  
                min_difference  =   i_difference    [item]  
                min_modulus     =   i_modulus       [item]  
            elif    modulus_difference  ==  '5' :  
                    continue  
            else    :  
                #print  modulus_difference  ,'\t',  
                modulus_difference  =   modulus_difference  [2:]  
                #print  modulus_difference  
                while   modulus_difference  [0] ==  '5' :  
                    modulus_difference  =   modulus_difference  [1:]  
                if  modulus_difference  [0] ==  '1' :  
                    continue  
                elif    modulus_difference  [0] ==  '9' :  
                    min_char        =   i_char          [item]  
                    min_num         =   i_num           [item]  
                    min_difference  =   i_difference    [item]  
                    min_modulus     =   i_modulus       [item]  
                else    :  
                    print   'another can\'t believe!!'  
        #print  min_char  
        #print  min_difference  
        num_one =   min_difference  
        #print  'num_one    :'  ,   num_one  
        #print  'min_mun    :'  ,   min_num  
        result  =   plus    (   result  ,   min_num )  
        #print  'ends while\n'  
    return  result  
while   True    :  
    print   '\n>>>',  
    command =   raw_input   ()  
    seek_plus       =   command.find    ('+')  
    seek_minus      =   command.find    ('-')  
    seek_multiply   =   command.find    ('*')  
    seek_divide     =   command.find    ('/')  
    if  command ==  'q' :  
        print   '\t\t\tbye ~'  
        exit()  
    elif    command ==  'help'  :  
        print   "\t\t'q'\tto quit"  
        print   "\t\tonly   '+' '-' '*' '/' '.' and number 1~9 in the right range will be responsed successfully"  
        print   "\t\tfor more details please visit jiyinyiyong.blog.163.com"  
        print   "\t\tanyway , i'm not able to make it right in every aspect , still some hidden problems uncoverd .."  
        print   "\t\tchecked in Python 2.7.1+\tand\tGCC 4.5.2 linux2"  
    elif    seek_plus   !=  -1  :  
        number_a    =   command [   :seek_plus  ]  
        number_b    =   command [   seek_plus+1 :   ]  
        response    =   plus    (   number_a    ,   number_b    )  
        print   'sum:\t'    ,   response  
    elif    seek_minus  !=  -1  :  
        number_a    =   command [   :seek_minus ]  
        number_b    =   command [   seek_minus+1    :   ]  
        response    =   minus   (   number_a    ,   number_b    )  
        print   'difference:\t' ,   response      
    elif    seek_multiply   !=  -1  :  
        number_a    =   command [   :seek_multiply  ]  
        number_b    =   command [   seek_multiply+1 :]  
        response    =   multiply    (   number_a    ,   number_b    )  
        print   'product:\t'    ,   response  
    elif    seek_divide !=  -1  :  
        number_a    =   command [   :seek_divide    ]  
        number_b    =   command [   seek_divide+1   :   ]  
        response    =   divide  (   number_a    ,   number_b    )  
        print   'quotient:\t'   ,   response  
    else    :  
        print   'pardon ?'  
