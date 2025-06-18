
/*==================== delete command====================
  we already seen drop vs truncate
  DROP table ======= > complete table will be deleted
  Truncate table ===== > all the data will be deleted but 
  table will be reamain

  what If I want to delete a specific rows or all the rows DELETE 

  Syntax:
  
  DELETE from <table_name> where <condition>  */

  use nareshit_eve_march
  select * from student_details

  -- Case-1)
  -- Delete the row where id =2

  Delete from student_details where student_id=2

  select * from student_details

  -- Case-2) Delete the row having Null value
  select * from student_details where city is NULL
  Delete from student_details where city is NULL

  select * from student_details

  -- you can use IN / NOT IN /Between

  -- Case3) delete all the rows

  delete from student_details

  select * from student_details


  /*qn) 
     difference between truncate and delete
    ans:
     - truncate will delete all the rows 
	 - but delete can delete a specifc rows aswellas all the rows
	 - but in both cases table remain same

	 qn) drop vs truncate
	 qn) drop vs delete
	 qn) truncate vs delete


	only replace   select *  with delete