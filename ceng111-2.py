listq=range(32)
lista=range(32)
listq[0]="Pascaline and Leibnitz Wheel are ancient computers.(T/F) $False"
lista[0]="Pascaline and Leibnitz Wheel are mechanical calculators"
listq[1]="What was the first programmable device(Please write the full name)? $Jacquard's Loom"
listq[2]="(Difference Engine, Analytic Engine) Which one is a computing device(Please write the full name)? $Analytic Engine"
listq[3]="What was the first computer to use base-2 numeral system? $MARK I"
listq[4]="MARK I was the first fully electrical computer.(T/F) $False"
lista[4]="MARK I was electromechanical."
listq[5]="ENIAC was the first electromechanical computer.(T/F) $False"
lista[5]="ENIAC was fully electrical."
listq[6]="What is the machine that is used to crack the Enigma Code and by whom it is designed(Machine,Inventor)? $Colossus,Alan Turing"
listq[7]="What is the architecture based on stored program concept? $Von Neumann"
listq[8]="In Von Neumann Architecture, memory stores instruction as well as data.(T/F) $True"
listq[9]="In sign magnitude notation,there exists two zeros(+0 and -0).(T/F) $True"
listq[10]="Given 3 bits, two's complement notation of 4 and -4 are the same.(T/F) $True"
listq[11]="In fixed point notation, write the closest number in binary to 3.178 using 8 bits(Write using point(.)). $11.001011"
lista[11]="3 is 11, and 178 is 001011...(goes infinitely). Because we have 8 bits, we take 6 bits for mantissa."
listq[12]="In image processing, 7 bits are used to indicate RGB(Red-Green-Blue) levels seperately.(T/F) $False"
lista[12]="In image processing, 8 bits are used to indicate RGB(Red-Green-Blue) levels seperately."
listq[13]="Using sampling method, original sound can be reproduced 100% accurately.(T/F) $False"
lista[13]="Sound needs to be sampled infinitely many times in order to be reproduced %100 accurately."
listq[14]="UNICODE uses 16 bit representation today.(T/F) $True"
listq[15]="A gate is the smallest unit of a computer.(T/F) $False"
lista[15]="It is a transistor."
listq[16]="(a*b*c') + (a'*b*c') + (a'*b'*c') + (a*b'*c')=? Please reduce the left boolean system using the symbols defined in parantheses, also do not have any space between operands and operators(a'is not a, a*b is a and b, a+b is a or b). $c'"
lista[16]="Factor out the common b'*c' and b*c'. We will have a common (a+a') which is to be factored out again. [(a+a')*(b'c'+bc')] If you factor out c', this will evaluate to c'."
listq[17]="Control circuits carry out arithmetic operations.(T/F) $False"
lista[17]="Control circuits determine the order in which operations are carried out."
listq[18]="What is the circuit that signals the selected result on a single line given n selector lines and 2^n input lines? $Multiplexor"
listq[19]="What is the circuit that signals the selected result on one of the 2^n output lines given n input lines? $Decoder"
listq[20]="BIOS stands for Built-In Open System.(T/F) $False"
lista[20]="BIOS stands for Basic Input Output System."
listq[21]="[MBR,BIOS,Hardwarecheck,OS]Please put the elements in brackets in order using -> without space. $BIOS->Hardwarecheck->MBR->OS"
listq[22]="If a data is frequently accessed in a memory,where is it transferred? $Cache"
listq[23]="Every device has its own bus.(T/F) $False"
lista[23]="Bus is a single wire system connecting all devices."
listq[24]="If CPU is busy, DMA executes the operation.(T/F) $False"
lista[24]="If CPU is busy, there is no other device to handle its task."
listq[25]="ASCII in original, can contain Turkish characters.(T/F) $False"
lista[25]="ASCII in original, only contains English characters."
listq[26]="Registers handle execution in their addresses.(T/F) $False"
lista[26]="Registers don't have addresses."
listq[27]="General purpose registers are not memory mapped.(T/F) $True"
listq[28]="Main purpose of virtual memory is to extend the physical memory.(T/F) $True"
listq[29]="Ambigious instructions are disambiguated by decoder circuit.(T/F) $False"
lista[29]="There is no device for ambigious instructions."
listq[30]="Instructions or data has to be evenly spaced.(T/F) $False"
lista[30]="Instructions or data doesn't have to be equally spaced."
listq[31]="In linux, using find command , the user cannot find the searched file under current directory.(T/F) $False"
lista[31]="Find command is executed recursively."
p=0
n=len(listq)
for i in range(n):
        no=i+1
        print "Question "+str(no)+":"
        index=listq[i].find("$")
        q=str(raw_input(listq[i][:index:]))
        if q.lower()==listq[i][index+1::].lower():
                print "Correct answer"
                p=p+1
        else:
		print "Incorrect answer"
                print "The correct answer is:"+ listq[i][index+1::]
		if listq[i][index+1::]=="False":
			print "Because "+str(lista[i])

print "Test has been finished."+str(p)+" out of "+str(n)+" questions are correctly answered"
