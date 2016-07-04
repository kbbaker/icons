import os
import urllib

for i in [1,5,22,23,24,6,7,2,8,9,25,26,10,3,14,27]:

    type = i

    original = 'ty%s-si64.png'%type

    urllib.urlretrieve('http://theme.routeyou.com/rty/route/%s'%original,'temp/' + original)
    #create gray
    os.system('convert temp/%s -colorspace Gray -gamma 8 temp/gray.png'%original)

    for per in [10,20,30,40,50,60,70,80,90,100]:
        os.system('composite -compose copy_opacity %s.jpg temp/%s temp/ori_%s.png'%(per,original,per))
        os.system('composite -compose dst_over temp/gray.png temp/ori_%s.png output/ty%s_%s.png'%(per,type,per))
        