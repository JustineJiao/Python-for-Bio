#This is a homework from Jiao Yushun. Date:2019-11-24

prostr='MNAPERQPQPDGGDAPGHEPGGSPQDELDFSILFDYEYLNPNEEEPNAHKVASPPSGPAYPDDVLDYGLKPYSPLASLSGEPPGRFGEPDRVGPQKFLSAAKPAGASGLSPRIEITPSHELIQAVGPLRMRDAGLLVEQPPLAGVAASPRFTLPVPGFEGYREPLCLSPASSGSSASFISDTFSPYTSPCVSPNNGGPDDLCPQFQNIPAHYSPRTSPIMSPRTSLAEDSCLGRHSPVPRPASRSSSPGAKRRHSCAEALVALPPGASPQRSRSPSPQPSSHVAPQDHGSPAGYPPVAGSAVIMDALNSLATDSPCGIPPKMWKTSP'
aa_name=[]  #The list that store animo acid name
for i in prostr:
    if i not in aa_name:
        aa_name.append(i) #store animo acid name in list

total_num=len(prostr)  
aa_dic={} #The dict that store animo acid (name, number) pairs
aa_dic_frq={}  #The dict for animo acid (name, frequency) pairs
aa_dic_stdfrq1={}
aa_dic_stdfrq2={}

for i in aa_name: #for each animo acid name
    aa_num = 0
    for j in prostr:  #for each character in prostr
        if j==i:  
            aa_num+=1   # count each animo acid in aa_name
    aa_dic[i] = aa_num #add animo acid (name,number) pairs to aa_dic
    aa_dic_frq[i]=aa_num/total_num  #add animo acid (name,frequency) pairs to aa_dic
    aa_dic_stdfrq1[i]='%.4f' %(aa_num/total_num) #标准化输出4位小数
    aa_dic_stdfrq2[i]='%.2f%%' %(aa_num/total_num*100) #标准化输出带2位小数的百分数,两个%%表示对%进行转义

#output the result to a file
import os
isExists=os.path.exists('F:/test') #判断路径是否存在
if not isExists:
    mkdirs('F:/test')    #creat test folder
pro_file_name='F:/test/frq.txt'
ofl=open(pro_file_name, 'wt') #open file in writing and text model
aastr='\t'.join(aa_name)+'\n' #the first line is animo acid name

for d in aa_name:
     aastr+=str(aa_dic[d])+'\t'   #the second line is animo acid number
aastr+='\n'  #to the next line
for d in aa_name:
     aastr+=str(aa_dic_frq[d])+'\t'   #the third line is animo acid frequency
aastr+='\n'  #to the next line
for d in aa_name:
     aastr+=str(aa_dic_stdfrq1[d])+'\t'
aastr+='\n'  #to the next line
for d in aa_name:
     aastr+=str(aa_dic_stdfrq2[d])+'\t'
     
ofl.write(aastr)
ofl.close()

print('done! You can check your file in F:/test/frq.txt')



    

        
