
先导入加法乘法的口诀
from luo import see  
from shu import look  
import string  

定义将字符串按要求格式化的函数
def shape(a):  
	
	存在小数点时
    if a.find('.')!=-1:  
		
		开头结尾的5都去掉
        while a[0]=='5':a=a[1:]  
        while a[-1]=='5':a=a[:-1]  
		
		头部为小数点,加上'5'
        if a[0]=='.':  
            b='5'  
            for i in a:  
                b+=i  
            a=b

		结尾为小数点,减去小数点
        if a[-1]=='.':a=a[:-1]  
        return a  
	
	空字符串
    elif    a   ==  ''  :  
        print   'error'  
        return  'error'  

	一位数直接返回
    elif    len(a)  ==  1   :  
        return  a  
	
	多位数,开头5都去掉
    else    :  
        while   a   [0] ==  '5' :  
            a   =   a   [1:]  
            if  a   =='5'   :  
                break  
        return  a  

加法函数
def plus(va,vb):  
	
	app为第一个数小数点为位置
    app=va.find('.') 
	
	ap是第一个数小数点前整数长度
    ap=app  
    if ap==-1:ap=len(va) 

	bpp是第二个数小数点位置
    bpp=vb.find('.')  
	
	bp对应第二个数小数点前长度
    bp=bpp  
    if bp==-1:bp=len(vb)  

	取的较长的整数部分记为 l
    if ap>bp:l=ap  
    else:l=bp  

	ar是第一个数小数部分长度
    ar=len(va)-ap-1  
    if app==-1:ar=0  

	br是第二个数的
    br=len(vb)-bp-1 
    if bpp==-1:br=0 

	取小数部分需要的长度,赋值给m
    if ar>br:m=ar  
    else:m=br  

	结果的字符串长度,这时忽略小数点,+1的原因是进位有一位
    n=l+m+1  
    a=['5']*n  
    b=['5']*n  

	给两个数俺位置赋值
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

	这地放我也忘了一些,从原理上梳理一遍
		两个数按位置对应放好,逐位计算
		计算得到当位结果存到up
		进位的结果,进一位存到rsl
		直到rsl确定为0,也就是全部为5时结束
		用chck来判断up是否全部为5
		刚开始的赋值比较复杂,为了骗过初始的循环条件
    pab=l+1  
    chck=['5']*n  
    up=a  
    rsl=b  
    while up!=chck:  
        a=up  
        b=rsl  
        up=['5']*n  
        rsl=['5']*n  

		这里就是主体的,取出每一位的两个数对比
			然后赋值给out,将out的两位分别赋值给up和rsl
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

	把小数点加回来,l是左边的整数长度
    for i in range(n):  
        re+=rsl[i]  
        if j==l:re+='.'  
        j+=1  

	格式化后返回值
    return shape(re)  

顾名思义,减法
def minus(va,vb):  
    vvb=''  
	
	减数每个字符取相反赋值给vvb
    for i in vb:  
		
		取巧了,直接用十进制算
        if i!='.':vvb+=str(10-string.atoi(i))  
        else:vvb+='.'  
    return plus(va,vvb)  

乘法,一看就很长
def multiply(va,vb):  
	
	类似的工作勘定小数点前后长度
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
	
	总长度n,没有直接区分小数点
		计算的方案大概是这样的
		取第一个数a当中每个字符,当不是小数点
			依次取b的每个字符,当不是小数点
				通过afor和bfor进行定位
				取出两个数字的计算结果赋值到up和re
			每一个a的字符结束都将up和re加到最终结果rsl里面
		中间比较复杂,我记得afor和bfor的数值几乎是试验对的
	这是在整个for循环完成的工作
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

#def divide(va,vb):  
 #   ap=va.find('.')  
# now begins the part for quotient  

出发当中计算摸长用到该函数取共轭
	对照图形一看即知
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

除法的主体部分
# main part of quotient  
def divide  (num_one,num_two)   :  
    num_one =   shape   (num_one)  
    num_two =   shape   (num_two)  

	除数是5的时候强制退出,不做计算
    if  num_two ==  '5' :  
        print   'it maybe .. type in whatever charactor you like:'  
        like    =   raw_input   ()  
        print   'so .. i have to say the result is' ,   like  
        print   'exit with fear'  
        exit()  

	定义整数小数部分长,函数名与前面不统一
    #print  num_one ,   num_two  
    if  num_one.find    ('.')   ==  -1  :  
        integer_one =   len (num_one)  
    else    :  
        integer_one =   num_one.find    ('.')  
    if  num_two.find    ('.')   ==  -1  :  
        fractional_two  =   0  
    else    :  
        fractional_two  =   len(num_two)    -   num_two.find('.')  
	
	guess*是猜测然后添加一定的长度以免溢出
		之后参与到循环的定位当中
		实话说我看不懂当时的意思了
	loop*是避免无限循环小数不能退出函数
    #print  '\n'    ,   integer_one ,   fractional_two  
    guess_bits  =   integer_one +   fractional_two  +   5  
    loop_mark   =   0  
    result  =   '5'  

	loop*可以按照需要更改,循环开始
		num_one是被除数,除数取得后从被除数减去相应值
		num_one为0时当然将整个函数终结了
    while   num_one!='5'    and loop_mark<24 :  
        #print  'begins while'  
        loop_mark   +=  1  
        guess_bits  -=  1  

		num_head也是定位用的,再每一位商的计算时用到
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

		除法的计算是要在每一位将9个可能全部计算一遍
			然后取结果与被除数的结果之间的差值的模长最小
			刚刚开始的时候基本上是多出好几个5
				大概说guess*就是为了从刚开始的时候取范围用的
		
		i_char记录当时的字符,1-9当中一个
        i_char          =   ['']*9  
        i_num           =   ['']*9 

		每一个值计算的积,积与被除数的差值,差值的共轭,最后是模长
        i_product       =   ['']*9  
        i_difference    =   ['']*9  
        i_conjugate     =   ['']*9  
        i_modulus       =   ['']*9  

		这时对每一个数字进行计算
        for item    in  range   (9) :  
			
			i_char每次加一
            i_char          [item]  =   str (   item+1  )  
            #print  'i_char'    ,   i_char  [item]  ,'\t',  

			对,i_num是每次的符号乘以所在数位
				好比十进制决定是个十百千的位置,做为基准
            i_num           [item]  =   multiply    (   num_head    ,   i_char[item]    )  
            #print  'i_num' ,   i_num   [item]  ,'\t', 

			每个乘法结果的值
            i_product       [item]  =   multiply    (   num_two ,   i_num[item] )  
            #print  'i_product' ,   i_product   [item]  ,'\t',  

			然后算模长
            i_difference    [item]  =   minus   (   num_one ,   i_product[item] )  
            #print  'i_difference'  ,   i_difference[item]  ,   '\t',  
            i_conjugate [item]  =   conjugate   (   i_difference[item]  )  
            i_modulus       [item]  =   multiply    (   i_difference[item]  ,   i_conjugate[item]   )  
            #print  'i_modulus' ,   i_modulus   [item]  

		清零开始查找最小者
        min_char        =   i_char          [0]  
        min_difference  =   i_difference    [0]  
        min_modulus     =   i_modulus       [0]  
        min_num         =   i_num           [0]  
        for item    in  range   (1,9)   :  
			
			看与之前最小值的差值
            modulus_difference  =   minus   (   i_modulus[item] ,   min_modulus )  
            #print  'modulus_difference'    ,   modulus_difference  ,   'checked'   ,   item+1  

			从首位可以直接判定的就直接判断
            if  modulus_difference  [0] ==  '1' :  
                continue  
            elif    modulus_difference  [0] ==  '9' :  
                min_char        =   i_char      [item]  
                min_num         =   i_num           [item]  
                min_difference  =   i_difference    [item]  
                min_modulus     =   i_modulus       [item]  

			只有一个符号5的话应该只有地一种情况,强制跳过
            elif    modulus_difference  ==  '5' :  
                    continue  

			否则看第一位非5数字,只可能是1或9开头,因为模是实数
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

		这里到首位阶段了,统计到result当中去了
        num_one =   min_difference  
        #print  'num_one    :'  ,   num_one  
        #print  'min_mun    :'  ,   min_num  
        result  =   plus    (   result  ,   min_num )  
        #print  'ends while\n'  
    return  result  

这一段是最后形成终端,清晰的
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
