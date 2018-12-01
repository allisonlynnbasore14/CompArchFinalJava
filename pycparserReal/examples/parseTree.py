

from pycparser import c_ast
import plyj.model as m


def parseTreeStart(tree):

	VarValueList = []
	VarTypeList = []
	VarNameList = []

	if tree is not None:

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

		ConstantComp = c_ast.Constant(VarTypeList[i], VarValueList[i])
		IdentTypeComp = c_ast.IdentifierType([VarTypeList[i]])
		TypeDeclComp = c_ast.TypeDecl(VarNameList[i], [], IdentTypeComp)
		DeclComp = c_ast.Decl(VarNameList[i], [], [], [], TypeDeclComp, ConstantComp, None )
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

	newTree.show(attrnames=True, nodenames=True, showcoord=True)
	print("--------------------------")

	return newTree





# Going throuhgh and combininng all the stuff to be under the main function
# make new tree
# fill with variables and such

#for variableDecl in [decl for decl in tD.body if type(decl) is m.MethodDeclaration]:
