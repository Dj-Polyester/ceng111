print "Please read before starting. Addition to previous prescriptions (in ceng111.py and ceng111-2.py), if there is ... in a question, you are assigned to replace this part with an answer.Also, do not use space unless you are permitted to write full name and use abbreviations for registers and units of the CPU"
lista=range(26)
listq=range(26)
listq[0]="... handles the fetch-decode-execute cycle.(Please write the full name) $CU"
listq[1]="The fact that the access time is the same for all addresses in a memory is called ... access $Random"
listq[2]="If the last address of a memory is x,and the memory width is y,find the size of the memory(use parantheses.Start with x. / * - + are operators). $(x+1)*y"
listq[3]="Reading the content from an address is called destructive fetch.(T/F) $False"
lista[3]="Fetching is an undestructive operation, which means after a value is fetched from the memory, it remains intact,the same."
listq[4]="Storing value necessitates the conservation of the data in the specified address.(T/F) $False"
lista[4]="Storing is a destructive operation, which means after another value is stored, the value is overwritten onto the previous one.The previous one is deleted."
listq[5]="... holds the address of a cell as ... holds the value of the data in the cell to be manipulated(Please seperate with a comma). $MAR,MDR"
listq[6]="In fetch operation, the address needs to be loaded into registers as well as the value.(T/F) $False"
lista[6]="In fetch operation, only the address is loaded into the MAR. Then, the value in the specified address is loaded into MDR. In store operation, the address and the value are loaded into MAR and MDR respectively.Then, the value is loaded into the specified address."
listq[7]="As computers became better, the difference between speed rates of CPU and RAM was hugely expanded. Because of that, ... was designed as it made accessing frequently fetched data faster. $Cache"
listq[8]="Cache memory is cheaper,faster and smaller in capacity compared to RAM.(T/F) $True"
listq[9]="For ... access devices, the time needed to access the information depends on the address's physical location and the current state of the device. Hard disks,floppy disks,CDs and DVDs are such devices. $Direct"
listq[10]="For a hard drive which has 1001 tracks,157 sectors in a track, 0.0093 msec arm movement time and 4.71 rev/msec rotation speed; find the worst case for access time(Please have a space between the value and the unit). $14.04 msec"
listq[11]="To compensate the huge difference between CPU and the input/output devices,I/O controller is designed.(T/F) $True"
listq[12]="I/O buffer runs the arithmetic operations in I/O controller.(T/F) $False"
lista[12]="I/O buffer is the memory of I/O controller. I/O controller also has its own Control/Logic unit corresponding to CU and ALU in CPU."
listq[13]="... selects the address of the data to be manipulated. $Decoder"
listq[14]="... selects the matching result from multiple results obtained by various operations in ALU. $Multiplexor"
listq[15]="PC holds the next instruction to be executed.(T/F) $False"
lista[15]="PC holds the address of the next instruction to be executed. The (next)instruction is then,copied to IR."
listq[16]="... creates a friendlier environment to make the computer and its hardware resources more accessible to the user(Please write the full name. All words start with uppercase letters). $System Software"
listq[17]="... allocate memory space for programs and data and retrieve this memory space when it is no longer needed(Please write the full name). $Memory Managers"
listq[18]="Information managers handle the organization, storage and retrieval of information on memory.(T/F) $False"
lista[18]="Information managers handle the organization, storage and retrieval of information on mass storage devices, not memory. Information managers allow user to organize information using directories,folders and files."
listq[19]="Assemblers,compilers and interpreters are language translators.(T/F) $True"
listq[20]="... allow user to easily and efficiently use the many different types of input and output devices that exist on amodern computer system(Please use abbreviation and a space.Also do not forget to start in Uppercase letter for all words). $I/O Systems"
listq[21]="...keeps a list of programs ready to run on the processor, and it selects the one that will execute next. $Scheduler"
listq[22]="...provide useful services either to a user or to other system routines. Text editors,drawing program and control panels are such programs. $Utilities"
listq[23]="Linker is a type of language service, because it works along with a compiler.(T/F) $False"
lista[23]="Linker is a type of memory manager,not a language service."
listq[24]="Non-volatile memory is typically used as secondary memory.(T/F) $True"
listq[25]="Magnetic Tape is an example for sequential memory.(T/F) $True"
p=0
n=len(listq)
for i in range(n):
        no=i+1
        print "Question "+str(no)+":"
        index=listq[i].find("$")
        q=str(raw_input(listq[i][:index:]))
        if q==listq[i][index+1::]:
                print "Correct answer"
                p=p+1
        elif q!=listq[i][index+1::]:
                print "Incorrect answer"
                print "The correct answer is:"+ listq[i][index+1::]
                if listq[i][index+1::]=="False":
                        print "Because "+str(lista[i])

print "Test has been finished."+str(p)+" out of "+str(n)+" questions are correctly answered"
