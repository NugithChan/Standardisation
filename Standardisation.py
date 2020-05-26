print('''


<<<!Project Standardisation!>>>



READ THE INSTRUCTIONS BELOW CAREFULLY!
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
''')

startup=input('''
The list of examination marks to be standardised should be in a "txt" extension file.
NAME this file "stdthis.txt". Please leave no spaces in between.
All marks must be in a range of 0 to 100(inclusive).
After the following are checked and valid, press enter to continue:''')

print('''
Processing and analysing data. May take a couple of minutes. DON'T CLOSE EXE UNTIL PROCESS IS COMPLETE!




''')
f1=open('stdthis.txt','r')
count=0  #keeps count when reading file
total=0  #keeps track of the total of successful marks located
stotal=0 
end=0
errorc=0
line=''
while errorc==0:
    try:
        maxi=int(input('Enter maximum mark for paper:'))
        errorc=1
    except:
        print('Not valid data type!')
errorc=0                
while end==0:
    line=f1.readline()
    if line=='end':
        end=1
        print('End Of File Detected!')
        print('Running End File Results On Secondary File("standardisedresults.txt")')
    else:
        try:
            bb=((int(str(line)))/maxi)*100
            total=total+bb
            count=count+1
            stotal=stotal+(bb**2)
            print('Data '+str(count)+' Status: Completed! No error!')
        except:
            count=count+1
            errorc=errorc+1
            print('Data '+str(count)+' Status: Error detected! Either Space or String Value was entered.(This was omitted)')
f1.close()
count=count-errorc #Removes and omits error values
#Math stuff
mean=float(total/count)
var=float((stotal/count)-(mean**2))

sdev=var**(0.5)
f2=open('standardisedresults.txt','w')
f2.write('Grade  '+'New Standardised Mark'+'\n')
f2.write('-------   -----------------------------'+'\n')
astar=(1.03644*sdev)+mean #TOP 15.000% 
f2.write('A* ==  '+str(int(astar))+'\n')
justa=(0.6745*sdev)+mean  #TOP 25.000%
f2.write('A  ==  '+str(int(justa))+'\n')
justb=(0.12566*sdev)+mean #TOP 45.000%
f2.write('B  ==  '+str(int(justb))+'\n')
justc=(-0.38532*sdev)+mean#TOP 65.000%
f2.write('C  ==  '+str(int(justc))+'\n')
justd=(-1.03644*sdev)+mean#TOP 85.000%
f2.write('D  ==  '+str(int(justd))+'\n')
juste=(-1.64485*sdev)+mean#TOP 95.000%
f2.write('E  ==  '+str(int(juste))+'\n')
justf=0
f2.write('F  ==  '+str(int(justf))+'\n')
f2.close()
print('Thank you for you patience.')
print('Total error count: '+str(errorc))
print('''Program successful...

Closed all files!
''')
quiter=input('Press enter to exit the program!')
