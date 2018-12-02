

from pycparser import c_ast
import plyj.model as m


def parseTreeStart(tree):

	#List of tuples with each element has a value, a type, a name, a structType (literal, addivitive, etc.), opperation type, lhs, and rhs
	VariableList = []

	if tree is not None:

		for tD in tree.type_declarations: #for fD in tD.body:# this takes off the top level of java
			for methodDecl in [decl for decl in tD.body if type(decl) is m.MethodDeclaration]:
				if methodDecl.body is not None:
					for statement in methodDecl.body:
						#VarTypeList.append(statement.type)
						nodeType = statement.type
						if type(statement) is m.VariableDeclaration:
							for var_decl in statement.variable_declarators:
								#If not an opperation
								if type(var_decl.initializer) is m.Literal:
									VariableList.append((var_decl.initializer.value, nodeType, var_decl.variable.name, type(var_decl.initializer), None, None, None )) #The last three are None because there is no operation information to pass on 
								#If an operation
								else:
									opp = var_decl.initializer.operator
									lhs = var_decl.initializer.lhs
									rhs = var_decl.initializer.rhs
									VariableList.append((None, nodeType, var_decl.variable.name, type(var_decl.initializer), opp, lhs.value, rhs.value ))


	compoundList = []

	for i in range(len(VariableList)):

		tupleTarget = VariableList[i]
		value = tupleTarget[0]
		typeT = tupleTarget[1]
		name = tupleTarget[2]
		strType = tupleTarget[3]
		opType = tupleTarget[4]
		lhs = tupleTarget[5]
		rhs = tupleTarget[6]

		ConstantComp = c_ast.Constant([typeT], value)

		IdentTypeComp = c_ast.IdentifierType([typeT])
		TypeDeclComp = c_ast.TypeDecl(name, [], IdentTypeComp)
		if opType is not None:
			ID1 = c_ast.ID(lhs, None)
			ID2 = c_ast.ID(rhs, None)
			BinaryOp = c_ast.BinaryOp(opType, ID1, ID2, None)
			DeclComp = c_ast.Decl(name, [], [], [], TypeDeclComp, BinaryOp, None )
		else:
			DeclComp = c_ast.Decl(name, [], [], [], TypeDeclComp, ConstantComp, None )

		compoundList.append(DeclComp)

	ConstantRComp = c_ast.Constant('int', 0)
	returnComp = c_ast.Return(ConstantRComp, None)
	compoundList.append(returnComp)

	# create an id type for main
	id_obj = c_ast.ID('main')

	#Levels 1-8 Func are constant across all parsing

	#Level 8 Func
	newIdentType2 = c_ast.IdentifierType(['void'])

	#Level 7 Func
	newTypeDecl2 = c_ast.TypeDecl(None,[],newIdentType2)

	#Level 6 Func
	newTypename = c_ast.Typename(None, [], newTypeDecl2,None)
	newIdentType1 = c_ast.IdentifierType(['int'])

	#Level 5 Func
	newParamList = c_ast.ParamList([newTypename])
	newTypeDecl1 = c_ast.TypeDecl(id_obj.name, [], newIdentType1)

	#Level 4 Func
	newFuncDecl = c_ast.FuncDecl(newParamList, newTypeDecl1, None)

	#Level 3 Func
	newDecl = c_ast.Decl(id_obj.name, [], [], [], newFuncDecl, None, None )

	#Level 2 Func
	newCompound = c_ast.Compound(compoundList, None)
	newFunc = c_ast.FuncDef(newDecl, None, newCompound, None)

	#Level 1 Func
	newTree = c_ast.FileAST([newFunc],None)


	print("--------------------------")

	return newTree





# Going throuhgh and combininng all the stuff to be under the main function
# make new tree
# fill with variables and such

#for variableDecl in [decl for decl in tD.body if type(decl) is m.MethodDeclaration]:
