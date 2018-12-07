la 	$t0, array # address of array
addi 	$t1, $zero, 11 # 11 elements in array

#initialize variables
addi	$t2, $zero, 0		# i, the current array element being accessed
addi	$t3, $t0, 0		# address of array[i] (starts from base address for i=0)
addi	$t4, $zero, 3		# adder = 3

LOOPSTART:
beq 	$t2, $t1, LOOPEND	# if i == 16: GOTO DONE

lw	$t5, 0($t3)		# temp = my_array[i]		{LOAD FROM MEMORY}
addi	$t5, $t5, $t4		# Add 5 to element temp		{MODIFY IN REGISTER}
sw	$t5, 0($t3)		# my_array[i] = temp		{STORE TO MEMORY}

addi	$t2, $t2, 1		# increment i counter
addi	$t3, $t3, 4		# increment address by 1 word
j	LOOPSTART		# GOTO start of loop
LOOPEND:
j	LOOPEND			# Jump trap prevents falling off end of program

.data 
array:
0x00000000	# array[0]
0x00000001
0x00000002
0x00000003
0x00000004
0x00000005
0x00000006
0x00000007
0x00000008
0x00000009
0x0000000A
