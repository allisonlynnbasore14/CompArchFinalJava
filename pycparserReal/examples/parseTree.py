

import ASTnode
import plyj.model as m


def parseTreeStart(tree):

	VarValueList = []
	VarTypeList = []
	VarNameList = []

	for tD in tree.type_declarations: #for fD in tD.body:# this takes off the top level of java
		for methodDecl in [decl for decl in tD.body if type(decl) is m.MethodDeclaration]:
			if methodDecl.body is not None:
				for statement in methodDecl.body:
					VarTypeList.append(statement.type)
					if type(statement) is m.VariableDeclaration:
						for var_decl in statement.variable_declarators:
							#print(var_decl.initializer)
							VarValueList.append(var_decl.initializer.value)
							VarNameList.append(var_decl.variable.name)
							
							if type(statement.type) is str:
								type_name = statement.type
							else:
								type_name = statement.type.name.value


	compoundList = []

	for i in range(len(VarNameList)):

		ConstantComp = ASTnode.Constant(VarTypeList[i], VarValueList[i])
		IdentTypeComp = ASTnode.IdentifierType([VarTypeList[i]], None)
		TypeDeclComp = ASTnode.TypeDecl(VarNameList[i], [], IdentTypeComp)
		DeclComp = ASTnode.Decl(VarNameList[i], [], [], [], TypeDeclComp, ConstantComp, None )
		compoundList.append(DeclComp)

	ConstantRComp = ASTnode.Constant('int', 0)
	returnComp = ASTnode.Return(ConstantRComp, None)
	compoundList.append(returnComp)

	#Levels 1-8 Func are constant across all parsing

	#Level 8 Func
	newIdentType2 = ASTnode.IdentifierType(['void'], None)

	#Level 7 Func
	newTypeDecl2 = ASTnode.TypeDecl(None,[],newIdentType2)

	#Level 6 Func
	newTypename = ASTnode.Typename(None, [], newTypeDecl2,None)
	newIdentType1 = ASTnode.IdentifierType(['int'], None)

	#Level 5 Func
	newParamList = ASTnode.ParamList([newTypename])
	newTypeDecl1 = ASTnode.TypeDecl('main', [], newIdentType1)

	#Level 4 Func
	newFuncDecl = ASTnode.FuncDecl(newParamList, newTypeDecl1, None)

	#Level 3 Func
	newDecl = ASTnode.Decl('main', [], [], [], newFuncDecl, None, None )

	#Level 2 Func
	newCompound = ASTnode.Compound(compoundList, None)
	newFunc = ASTnode.FuncDef(newDecl, None, newCompound, None)

	#Level 1 Func
	newTree = ASTnode.FileAST([newFunc],None)

	newTree.show()
	print("--------------------------")

	return newTree

                        



# Going throuhgh and combininng all the stuff to be under the main function
# make new tree
# fill with variables and such 

#for variableDecl in [decl for decl in tD.body if type(decl) is m.MethodDeclaration]: