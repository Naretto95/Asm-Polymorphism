# CONSULTER LE README.txt

from termcolor import colored
import shutil
import random
import subprocess
import string
import sys
import struct
import uuid
import os

def copyFile(x, y):
	shutil.copyfile(x, y)
	
def shellCode(allLines, allReg, tmpFileName):
	print("\nTransfert des opcodes dans payload.txt")
	payload = open("payload.txt", "a")
	cmd = "objdump -d tmp_gen.bin | grep -Po '\s\K[a-f0-9]{2}(?=\s)'"
	result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	opcode = result.stdout.decode("utf-8").replace("\n", " ")
	if (opcode!="objdump: 'tmp_gen.bin': No such file "):
		while (verifyOpcode(opcode)):
			payload.close()
			regen(allLines, allReg, tmpFileName)
			return
		payload.write(opcode + "\n")
		print(colored("\t\tTerminé", "blue"))
	else:
		print(colored("\t\tImpossible de récupérer les opcodes.", "red"))
	payload.close()
	
def verifyOpcode(opcode):
	print("\nVérification de l'existence de l'opcode.")
	tmpFile = open("payload.txt", "r")
	line = tmpFile.readline()
	while line:
		line = tmpFile.readline()
		if (line.replace(" ", "").replace("\n", "")==opcode.replace(" ", "").replace("\n", "")):
			print(colored("\t\tRecherche d'une autre signature...\n", "green"))
			return True
	tmpFile.close()
	print(colored("\t\tSignature de fichier inexistante trouvée.", "blue"))
	return False
	
def fileToArray():
	print("\nTransformation du fichier ASM en Array")
	allLines = []
	tmpFile = open("tmp_gen.asm", "r")
	line = tmpFile.readline()
	while line:
		line = tmpFile.readline()
		allLines.append(line)
	tmpFile.close()
	print(colored("\t\tTerminé", "blue"))
	return allLines

def unusedReg(allLines):
	print("\nRécupération de registres non utilisés")
	allReg = []
	for i in [12,13,14,15]:
		allReg.append("r" + str(i))
	for a in allLines:
		for b in allReg:
			if a.count(b):
				allReg.remove(b)
				print(colored("\t" + b + " non modifiable", "red"))
	print(colored("\t\tTerminé", "blue"))
	return allReg
	
def recomposeASM(allLines):
	print("\nReconstruction du code ASM")
	tmpFinGen = open("tmp_gen.asm", "w")
	for line in allLines:
		tmpFinGen.write(str(line))
	tmpFinGen.close()
	print(colored("\t\tTerminé", "blue"))
	
def trier(liste,registre):
	print("\nModification des instructions")
	watchout=["xor","mov"]
	bit8=["al","ah","bl","bh","cl","ch","dl","dh","bpl","sil","dil","spl","r8b","r9b","r10b","r11b","r12b","r13b","r14b","r15b"]
	bit16=["ax","bx","cx","dx","bp","si","di","sp","ip","r8w","r9w","r10w","r11w","r12w","r13w","r14w","r15w"]
	bit32=["eax","ebx","ecx","edx","ebp","esi","edi","esp","eip","r8d","r9d","r10d","r11d","r12d","r13d","r14d","r15d"]
	bit64=["rax","rbx","rcx","rdx","rbp","rsi","r8","r9","r10","r11","r12","r13","r14","r15","rdi","rsp","rip"]
	i=0
	taille=True
	while taille:
		phrase = liste[i]
		for watch in watchout:
			if watch in phrase and random.randint(1,2)==1:
				nbt = phrase.count("\t")
				phrase = phrase.replace(" ","")
				phrase = phrase.replace("\t","")
				phrase = phrase.replace("\n","")
				phrase = phrase.replace(watch,"")
				phrase = phrase.split(",")
				if phrase[0] in bit8:
					registreuse=registre[0]+"b"
				elif phrase[0] in bit16:
					registreuse=registre[0]+"w"
				elif phrase[0] in bit32:
					registreuse=registre[0]+"d"
				elif phrase[0] in bit64:
					registreuse=registre[0]
				if watch=="xor":
					xor=nbt*"\t"+"xor "+registreuse+", "+registreuse+"\n"
					mov=nbt*"\t"+"mov "+ phrase[0] + ", "+registreuse+"\n"
					liste[i:i+1] = xor, mov
					i+=1
				elif watch=="mov":
					mov1=nbt*"\t"+"mov "+registreuse+", "+phrase[1]+"\n"
					mov2=nbt*"\t"+"mov "+phrase[0]+", "+registreuse+"\n"
					liste[i:i+1] = mov1, mov2
					i+=1
		i+=1
		if i == len(liste)-1 or i == len(liste):
			taille=False
	print(colored("\t\tTerminé", "blue"))
	
def regen(allLines, allReg, tmpFileName):
	print(colored("\t\tGénération d'une nouvelle signature...\n", "green"))
	trier(allLines, allReg)
	recomposeASM(allLines)
	os.system('nasm -f elf64 -o ' + tmpFileName + '.o ' + tmpFileName + '.asm')
	os.system('ld -o ' + tmpFileName + '.bin ' + tmpFileName + '.o')
	shellCode(allLines, allReg, tmpFileName)
	print(colored("\t\t...\n\n", "green"))
	
def generate(source, destination):
	tmpFileName = destination[:-4]
	if os.path.exists(destination):
		os.remove(destination)
	copyFile(source, destination)
	allLines = fileToArray()
	allReg = unusedReg(allLines)
	trier(allLines, allReg)
	recomposeASM(allLines)
	os.system('nasm -f elf64 -o ' + tmpFileName + '.o ' + tmpFileName + '.asm')
	os.system('ld -o ' + tmpFileName + '.bin ' + tmpFileName + '.o')
	shellCode(allLines, allReg, tmpFileName)
	
def start():
	system = struct.calcsize("P") * 8
	if system==64:
		print(colored("\nVous utilisez un système 64bits, ce code peut être exécuté.\n", "green"))
		print("Entrez le chemin (relatif ou absolu) de votre fichier .asm :")
		source=	input()
		generate(source, 'tmp_gen.asm')
	else:
		print(colored("\nVous utilisez un système 32bits, ce code ne peut pas être exécuté.\n", "red"))

start()
	

