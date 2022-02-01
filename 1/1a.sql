SELECT StudentID, Name FROM name_table 
	WHERE StudentID IN (
    	SELECT StudentID FROM mark_table 
        	WHERE Total_marks > (
            	SELECT Total_marks FROM mark_table 
                	WHERE StudentID = 'V002'
            )
    );