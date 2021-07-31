#!/usr/bin/env python
# coding: utf-8

# In[9]:


##############################################################################################################################
###         Hassan Shahzad
###         CS-D
###         Artificial Intelligence Lab (Lab # 9)
###         FAST-NUCES
###         chhxnshah@gmail.com
##############################################################################################################################


################################################## GLOBAL DECLARATIONS ####################################################

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

DOMAIN_VALUES = ["Monday", "Tuesday", "Wednesday"]

######################################### BACK TRACK FUNCTION IMPLEMENTATION ##############################################


def backtrack(assignment):

    if len(assignment) == len (VARIABLES):                # Check if assignment is complete
        return assignment
   
    temp_var = select_unassigned_variable(assignment)     # selecting a new un-assigned variable's index
    
    for value in DOMAIN_VALUES:                           # Checking the array containing days
        ass = assignment.copy()
        ass[temp_var] = value
        if consistent(ass):                               # Checking is assignment is consistent
            result = backtrack(ass)                       # Resursive function
            
            if result is not None:
                return result
    return None
    
  

############################################### Selects Unassigned Variable ###############################################

def select_unassigned_variable(assignment):
    for i in VARIABLES:
        if i not in assignment:                      # Checks and returns the variable not currently assigned
            return i                                 # Returns the index
    return None

################################################### Consistent Function ###################################################

def consistent(assignment):
    
    for (i,j) in CONSTRAINTS:                        
        
        if i not in assignment or j not in assignment:   # If the selected value hasn't been assigned yet
            continue
        
        if assignment[i] == assignment[j]:               # Both having same value (Constraint failed)
            return False
    return True

################################################# MAIN Implementation #####################################################
# The main entry point for this module
def main():
    
    solution = backtrack(dict())
    print(solution)
# Tell python to run main method
if __name__ == "__main__": main()


# In[ ]:




