
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AS ASSIGN BLOCK_COMMENT BOOL BREAK CASE CLASS COLON COMMA COMPOSED_ASSIGN CONST CONTINUE DECREMENT DEFAULT DIVIDE DO DOC_COMMENT DOT DOUBLE DYNAMIC ELSE EQUALS EXTENDS FALSE FINAL FLOAT FOR GRAPH GREATER_EQ GREATER_THAN HASH IF IMPLEMENTS INCREMENT INTEGER INTEGER_DIVIDE INTERFACE IS IS_NOT LBRACE LESS_EQ LESS_THAN LINE_COMMENT LIST LPAREN LSQUARE MAP MINUS MODULE NEGATION NOT_EQUALS NULL NULL_ASSIGN NUMBER OBJECT OR PLUS PRINT PRIVATE PROTECTED PUBLIC QUEUE RBRACE RPAREN RSQUARE SEMICOLON SET STACK STRING STRING_LITERAL SWITCH TIMES TREE TRUE VARIABLE VOID WHILEprogram : statementsstatements : statements statement\n                  | statementstatement : var_declaration\n                 | data_structure\n                 | control_structurevar_declaration : VARIABLE ASSIGN ASSIGN expression SEMICOLON\n                       | VARIABLE NULL_ASSIGN expression SEMICOLONvar_declaration : type VARIABLE ASSIGN expression SEMICOLONvar_declaration : bool_type VARIABLE ASSIGN bool_expression SEMICOLONvar_declaration : num_type VARIABLE ASSIGN num_expression SEMICOLONtype : VOID\n            | STRING\n            | LIST\n            | SET\n            | MAP\n            | STACK\n            | QUEUE\n            | TREE\n            | GRAPHbool_type : BOOLnum_type : FLOAT\n                | INTEGER\n                | DOUBLEexpression : bool_expressionexpression : num_expressionexpression : VARIABLEbool_expression : TRUE\n                        | FALSEnum_expression : NUMBER\n                    | INTEGER\n                    | FLOATbool_expression : NEGATION bool_expression\n                      | bool_expression AND bool_expression\n                      | bool_expression OR bool_expressionnum_expression : num_expression PLUS num_expression\n                      | num_expression MINUS num_expression\n                      | num_expression TIMES num_expression\n                      | num_expression DIVIDE num_expression\n                      | num_expression INTEGER_DIVIDE num_expression\n                      | num_expression MODULE num_expressionbool_expression : LPAREN bool_expression RPARENnum_expression : LPAREN num_expression RPARENdata_structure : list_structure\n                      | map_structure\n                      | set_structurelist_structure : LSQUARE elements RSQUAREmap_structure : LBRACE key_value_pairs RBRACEset_structure : LBRACE elements RBRACEelements : elements COMMA expression\n                | expressionkey_value_pairs : key_value_pairs COMMA key_value\n                       | key_valuekey_value : expression COLON expressioncontrol_structure : if_structure\n                        | switch_structurewhile_structure : WHILE LPAREN condition RPAREN LBRACE statement RBRACEif_structure : IF LPAREN condition RPAREN LBRACE statement RBRACEswitch_structure : SWITCH LPAREN expression RPAREN LBRACE cases default RBRACEcondition : expression GREATER_THAN expression\n                 | expression LESS_THAN expression\n                 | expression GREATER_EQ expression\n                 | expression LESS_EQ expression\n                 | expression EQUALS expression\n                 | expression NOT_EQUALS expressioncases : cases case\n             | casecase : CASE NUMBER COLON statement BREAK SEMICOLONdefault : DEFAULT COLON statement\n               | emptyempty :statement : PRINT LPAREN expression RPAREN SEMICOLON'
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[7,7,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,7,-58,-59,7,7,]),'VARIABLE':([0,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,37,57,58,60,62,65,66,79,80,81,82,88,108,109,110,111,112,113,115,116,117,118,119,120,132,138,139,140,],[8,8,-3,-4,-5,-6,38,39,40,-44,-45,-46,-55,-56,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,45,45,-2,45,45,45,45,45,45,-47,45,-48,45,-49,45,-8,45,45,45,45,45,45,-72,-7,-9,-10,-11,8,-58,-59,8,8,]),'VOID':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[17,17,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,17,-58,-59,17,17,]),'STRING':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[18,18,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,18,-58,-59,18,18,]),'LIST':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[19,19,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,19,-58,-59,19,19,]),'SET':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[20,20,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,20,-58,-59,20,20,]),'MAP':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[21,21,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,21,-58,-59,21,21,]),'STACK':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[22,22,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,22,-58,-59,22,22,]),'QUEUE':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[23,23,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,23,-58,-59,23,23,]),'TREE':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[24,24,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,24,-58,-59,24,24,]),'GRAPH':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[25,25,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,25,-58,-59,25,25,]),'BOOL':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[26,26,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,26,-58,-59,26,26,]),'FLOAT':([0,2,3,4,5,6,12,13,14,15,16,30,31,34,35,37,49,57,58,60,62,64,65,66,69,70,71,72,73,74,79,80,81,82,88,92,108,109,110,111,112,113,115,116,117,118,119,120,132,138,139,140,],[27,27,-3,-4,-5,-6,-44,-45,-46,-55,-56,52,52,-2,52,52,52,52,52,52,52,52,-47,52,52,52,52,52,52,52,-48,52,-49,52,-8,52,52,52,52,52,52,52,-72,-7,-9,-10,-11,27,-58,-59,27,27,]),'INTEGER':([0,2,3,4,5,6,12,13,14,15,16,30,31,34,35,37,49,57,58,60,62,64,65,66,69,70,71,72,73,74,79,80,81,82,88,92,108,109,110,111,112,113,115,116,117,118,119,120,132,138,139,140,],[28,28,-3,-4,-5,-6,-44,-45,-46,-55,-56,51,51,-2,51,51,51,51,51,51,51,51,-47,51,51,51,51,51,51,51,-48,51,-49,51,-8,51,51,51,51,51,51,51,-72,-7,-9,-10,-11,28,-58,-59,28,28,]),'DOUBLE':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[29,29,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,29,-58,-59,29,29,]),'LSQUARE':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[30,30,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,30,-58,-59,30,30,]),'LBRACE':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,107,114,115,116,117,118,119,120,132,138,139,140,],[31,31,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,120,127,-72,-7,-9,-10,-11,31,-58,-59,31,31,]),'IF':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[32,32,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,32,-58,-59,32,32,]),'SWITCH':([0,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,120,132,138,139,140,],[33,33,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,33,-58,-59,33,33,]),'$end':([1,2,3,4,5,6,12,13,14,15,16,34,65,79,81,88,115,116,117,118,119,132,138,],[0,-1,-3,-4,-5,-6,-44,-45,-46,-55,-56,-2,-47,-48,-49,-8,-72,-7,-9,-10,-11,-58,-59,]),'RBRACE':([4,5,6,12,13,14,15,16,43,44,45,46,47,50,51,52,53,54,55,56,65,75,79,81,88,93,94,95,96,97,98,99,100,101,102,103,104,106,115,116,117,118,119,128,129,130,132,133,134,136,138,141,144,],[-4,-5,-6,-44,-45,-46,-55,-56,-25,-26,-27,-28,-29,-30,-31,-32,79,81,-53,-51,-47,-33,-48,-49,-8,-50,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-52,-54,-72,-7,-9,-10,-11,132,-71,-67,-58,138,-66,-70,-59,-69,-68,]),'BREAK':([4,5,6,12,13,14,15,16,65,79,81,88,115,116,117,118,119,132,138,142,],[-4,-5,-6,-44,-45,-46,-55,-56,-47,-48,-49,-8,-72,-7,-9,-10,-11,-58,-59,143,]),'LPAREN':([7,30,31,32,33,35,37,48,49,57,58,60,62,63,64,66,67,68,69,70,71,72,73,74,76,80,82,92,108,109,110,111,112,113,],[35,49,49,57,58,49,49,76,49,49,49,49,49,76,92,49,76,76,92,92,92,92,92,92,76,49,49,92,49,49,49,49,49,49,]),'ASSIGN':([8,36,38,39,40,],[36,60,62,63,64,]),'NULL_ASSIGN':([8,],[37,]),'TRUE':([30,31,35,37,48,49,57,58,60,62,63,66,67,68,76,80,82,108,109,110,111,112,113,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FALSE':([30,31,35,37,48,49,57,58,60,62,63,66,67,68,76,80,82,108,109,110,111,112,113,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'NEGATION':([30,31,35,37,48,49,57,58,60,62,63,66,67,68,76,80,82,108,109,110,111,112,113,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'NUMBER':([30,31,35,37,49,57,58,60,62,64,66,69,70,71,72,73,74,80,82,92,108,109,110,111,112,113,131,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,137,]),'RSQUARE':([41,42,43,44,45,46,47,50,51,52,75,93,94,95,96,97,98,99,100,101,102,103,],[65,-51,-25,-26,-27,-28,-29,-30,-31,-32,-33,-50,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'COMMA':([41,42,43,44,45,46,47,50,51,52,53,54,55,56,75,93,94,95,96,97,98,99,100,101,102,103,104,106,],[66,-51,-25,-26,-27,-28,-29,-30,-31,-32,80,66,-53,-51,-33,-50,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-52,-54,]),'COLON':([43,44,45,46,47,50,51,52,56,75,94,95,96,97,98,99,100,101,102,103,105,135,137,],[-25,-26,-27,-28,-29,-30,-31,-32,82,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,82,139,140,]),'RPAREN':([43,44,45,46,47,50,51,52,59,75,77,78,83,85,94,95,96,97,98,99,100,101,102,103,121,122,123,124,125,126,],[-25,-26,-27,-28,-29,-30,-31,-32,86,-33,102,103,107,114,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-60,-61,-62,-63,-64,-65,]),'SEMICOLON':([43,44,45,46,47,50,51,52,61,75,86,87,89,90,91,94,95,96,97,98,99,100,101,102,103,143,],[-25,-26,-27,-28,-29,-30,-31,-32,88,-33,115,116,117,118,119,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,144,]),'GREATER_THAN':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,108,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'LESS_THAN':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,109,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'GREATER_EQ':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,110,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'LESS_EQ':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,111,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'EQUALS':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,112,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'NOT_EQUALS':([43,44,45,46,47,50,51,52,75,84,94,95,96,97,98,99,100,101,102,103,],[-25,-26,-27,-28,-29,-30,-31,-32,-33,113,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,]),'AND':([43,46,47,75,77,90,94,95,102,],[67,-28,-29,67,67,67,67,67,-42,]),'OR':([43,46,47,75,77,90,94,95,102,],[68,-28,-29,68,68,68,68,68,-42,]),'PLUS':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[69,-30,-31,-32,69,69,69,69,69,69,69,69,-43,]),'MINUS':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[70,-30,-31,-32,70,70,70,70,70,70,70,70,-43,]),'TIMES':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[71,-30,-31,-32,71,71,71,71,71,71,71,71,-43,]),'DIVIDE':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[72,-30,-31,-32,72,72,72,72,72,72,72,72,-43,]),'INTEGER_DIVIDE':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[73,-30,-31,-32,73,73,73,73,73,73,73,73,-43,]),'MODULE':([44,50,51,52,78,91,96,97,98,99,100,101,103,],[74,-30,-31,-32,74,74,74,74,74,74,74,74,-43,]),'CASE':([127,129,130,134,144,],[131,131,-67,-66,-68,]),'DEFAULT':([129,130,134,144,],[135,-67,-66,-68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,120,139,140,],[3,34,128,141,142,]),'var_declaration':([0,2,120,139,140,],[4,4,4,4,4,]),'data_structure':([0,2,120,139,140,],[5,5,5,5,5,]),'control_structure':([0,2,120,139,140,],[6,6,6,6,6,]),'type':([0,2,120,139,140,],[9,9,9,9,9,]),'bool_type':([0,2,120,139,140,],[10,10,10,10,10,]),'num_type':([0,2,120,139,140,],[11,11,11,11,11,]),'list_structure':([0,2,120,139,140,],[12,12,12,12,12,]),'map_structure':([0,2,120,139,140,],[13,13,13,13,13,]),'set_structure':([0,2,120,139,140,],[14,14,14,14,14,]),'if_structure':([0,2,120,139,140,],[15,15,15,15,15,]),'switch_structure':([0,2,120,139,140,],[16,16,16,16,16,]),'elements':([30,31,],[41,54,]),'expression':([30,31,35,37,57,58,60,62,66,80,82,108,109,110,111,112,113,],[42,56,59,61,84,85,87,89,93,105,106,121,122,123,124,125,126,]),'bool_expression':([30,31,35,37,48,49,57,58,60,62,63,66,67,68,76,80,82,108,109,110,111,112,113,],[43,43,43,43,75,77,43,43,43,43,90,43,94,95,77,43,43,43,43,43,43,43,43,]),'num_expression':([30,31,35,37,49,57,58,60,62,64,66,69,70,71,72,73,74,80,82,92,108,109,110,111,112,113,],[44,44,44,44,78,44,44,44,44,91,44,96,97,98,99,100,101,44,44,78,44,44,44,44,44,44,]),'key_value_pairs':([31,],[53,]),'key_value':([31,80,],[55,104,]),'condition':([57,],[83,]),'cases':([127,],[129,]),'case':([127,129,],[130,134,]),'default':([129,],[133,]),'empty':([129,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','AnalizadorSintactico.py',8),
  ('statements -> statements statement','statements',2,'p_statements','AnalizadorSintactico.py',13),
  ('statements -> statement','statements',1,'p_statements','AnalizadorSintactico.py',14),
  ('statement -> var_declaration','statement',1,'p_statement','AnalizadorSintactico.py',23),
  ('statement -> data_structure','statement',1,'p_statement','AnalizadorSintactico.py',24),
  ('statement -> control_structure','statement',1,'p_statement','AnalizadorSintactico.py',25),
  ('var_declaration -> VARIABLE ASSIGN ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration','AnalizadorSintactico.py',31),
  ('var_declaration -> VARIABLE NULL_ASSIGN expression SEMICOLON','var_declaration',4,'p_var_declaration','AnalizadorSintactico.py',32),
  ('var_declaration -> type VARIABLE ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration_with_type','AnalizadorSintactico.py',37),
  ('var_declaration -> bool_type VARIABLE ASSIGN bool_expression SEMICOLON','var_declaration',5,'p_var_declaration_with_bool_type','AnalizadorSintactico.py',42),
  ('var_declaration -> num_type VARIABLE ASSIGN num_expression SEMICOLON','var_declaration',5,'p_var_declaration_with_num_type','AnalizadorSintactico.py',47),
  ('type -> VOID','type',1,'p_type','AnalizadorSintactico.py',52),
  ('type -> STRING','type',1,'p_type','AnalizadorSintactico.py',53),
  ('type -> LIST','type',1,'p_type','AnalizadorSintactico.py',54),
  ('type -> SET','type',1,'p_type','AnalizadorSintactico.py',55),
  ('type -> MAP','type',1,'p_type','AnalizadorSintactico.py',56),
  ('type -> STACK','type',1,'p_type','AnalizadorSintactico.py',57),
  ('type -> QUEUE','type',1,'p_type','AnalizadorSintactico.py',58),
  ('type -> TREE','type',1,'p_type','AnalizadorSintactico.py',59),
  ('type -> GRAPH','type',1,'p_type','AnalizadorSintactico.py',60),
  ('bool_type -> BOOL','bool_type',1,'p_bool_type','AnalizadorSintactico.py',65),
  ('num_type -> FLOAT','num_type',1,'p_num_type','AnalizadorSintactico.py',70),
  ('num_type -> INTEGER','num_type',1,'p_num_type','AnalizadorSintactico.py',71),
  ('num_type -> DOUBLE','num_type',1,'p_num_type','AnalizadorSintactico.py',72),
  ('expression -> bool_expression','expression',1,'p_b_expression','AnalizadorSintactico.py',78),
  ('expression -> num_expression','expression',1,'p_n_expression','AnalizadorSintactico.py',84),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','AnalizadorSintactico.py',89),
  ('bool_expression -> TRUE','bool_expression',1,'p_expression_boolean','AnalizadorSintactico.py',94),
  ('bool_expression -> FALSE','bool_expression',1,'p_expression_boolean','AnalizadorSintactico.py',95),
  ('num_expression -> NUMBER','num_expression',1,'p_expression_numeric','AnalizadorSintactico.py',100),
  ('num_expression -> INTEGER','num_expression',1,'p_expression_numeric','AnalizadorSintactico.py',101),
  ('num_expression -> FLOAT','num_expression',1,'p_expression_numeric','AnalizadorSintactico.py',102),
  ('bool_expression -> NEGATION bool_expression','bool_expression',2,'p_bool_expression','AnalizadorSintactico.py',107),
  ('bool_expression -> bool_expression AND bool_expression','bool_expression',3,'p_bool_expression','AnalizadorSintactico.py',108),
  ('bool_expression -> bool_expression OR bool_expression','bool_expression',3,'p_bool_expression','AnalizadorSintactico.py',109),
  ('num_expression -> num_expression PLUS num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',114),
  ('num_expression -> num_expression MINUS num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',115),
  ('num_expression -> num_expression TIMES num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',116),
  ('num_expression -> num_expression DIVIDE num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',117),
  ('num_expression -> num_expression INTEGER_DIVIDE num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',118),
  ('num_expression -> num_expression MODULE num_expression','num_expression',3,'p_num_expression','AnalizadorSintactico.py',119),
  ('bool_expression -> LPAREN bool_expression RPAREN','bool_expression',3,'p_bool_expression_group','AnalizadorSintactico.py',124),
  ('num_expression -> LPAREN num_expression RPAREN','num_expression',3,'p_num_expression_group','AnalizadorSintactico.py',129),
  ('data_structure -> list_structure','data_structure',1,'p_data_structure','AnalizadorSintactico.py',135),
  ('data_structure -> map_structure','data_structure',1,'p_data_structure','AnalizadorSintactico.py',136),
  ('data_structure -> set_structure','data_structure',1,'p_data_structure','AnalizadorSintactico.py',137),
  ('list_structure -> LSQUARE elements RSQUARE','list_structure',3,'p_list_structure','AnalizadorSintactico.py',142),
  ('map_structure -> LBRACE key_value_pairs RBRACE','map_structure',3,'p_map_structure','AnalizadorSintactico.py',147),
  ('set_structure -> LBRACE elements RBRACE','set_structure',3,'p_set_structure','AnalizadorSintactico.py',151),
  ('elements -> elements COMMA expression','elements',3,'p_elements','AnalizadorSintactico.py',155),
  ('elements -> expression','elements',1,'p_elements','AnalizadorSintactico.py',156),
  ('key_value_pairs -> key_value_pairs COMMA key_value','key_value_pairs',3,'p_key_value_pairs','AnalizadorSintactico.py',164),
  ('key_value_pairs -> key_value','key_value_pairs',1,'p_key_value_pairs','AnalizadorSintactico.py',165),
  ('key_value -> expression COLON expression','key_value',3,'p_key_value','AnalizadorSintactico.py',173),
  ('control_structure -> if_structure','control_structure',1,'p_control_structure','AnalizadorSintactico.py',179),
  ('control_structure -> switch_structure','control_structure',1,'p_control_structure','AnalizadorSintactico.py',180),
  ('while_structure -> WHILE LPAREN condition RPAREN LBRACE statement RBRACE','while_structure',7,'p_while','AnalizadorSintactico.py',185),
  ('if_structure -> IF LPAREN condition RPAREN LBRACE statement RBRACE','if_structure',7,'p_if','AnalizadorSintactico.py',190),
  ('switch_structure -> SWITCH LPAREN expression RPAREN LBRACE cases default RBRACE','switch_structure',8,'p_switch','AnalizadorSintactico.py',195),
  ('condition -> expression GREATER_THAN expression','condition',3,'p_condition','AnalizadorSintactico.py',200),
  ('condition -> expression LESS_THAN expression','condition',3,'p_condition','AnalizadorSintactico.py',201),
  ('condition -> expression GREATER_EQ expression','condition',3,'p_condition','AnalizadorSintactico.py',202),
  ('condition -> expression LESS_EQ expression','condition',3,'p_condition','AnalizadorSintactico.py',203),
  ('condition -> expression EQUALS expression','condition',3,'p_condition','AnalizadorSintactico.py',204),
  ('condition -> expression NOT_EQUALS expression','condition',3,'p_condition','AnalizadorSintactico.py',205),
  ('cases -> cases case','cases',2,'p_cases','AnalizadorSintactico.py',210),
  ('cases -> case','cases',1,'p_cases','AnalizadorSintactico.py',211),
  ('case -> CASE NUMBER COLON statement BREAK SEMICOLON','case',6,'p_case','AnalizadorSintactico.py',218),
  ('default -> DEFAULT COLON statement','default',3,'p_default','AnalizadorSintactico.py',222),
  ('default -> empty','default',1,'p_default','AnalizadorSintactico.py',223),
  ('empty -> <empty>','empty',0,'p_empty','AnalizadorSintactico.py',230),
  ('statement -> PRINT LPAREN expression RPAREN SEMICOLON','statement',5,'p_print','AnalizadorSintactico.py',235),
]