

addi   $v1, $zero, $zero	#variable sum

# Initialize variables
addi	$t2, $zero, $zero	# i, the current array element being accessed
addi	$t1, $zero, 10		# when i == 10

LOOPSTART:
	beq 	$t2, $t1, LOOPPREEND	# if i == 10: GOTO DONE

	add	$v1, $v1, $t2		# Add 5 to element temp		{MODIFY IN REGISTER}

	addi	$t2, $t2, 1		# increment i counter

	
	j	LOOPSTART		# GOTO start of loop
	
	LOOPPREEND:
	ret	$zero
	j	LOOPEND	
	
	
	LOOPEND:
	j	LOOPEND			# Jump trap prevents falling off end of program


