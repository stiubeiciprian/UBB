
-- Dirty read: occurs when one transaction reads data that is being modified by another transaction which has not been commited yet. 

-- T1
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
	UPDATE Movies
	SET title = 'Super Secret Title'
	WHERE movieId = 2
	WAITFOR DELAY '00:00:10'
ROLLBACK TRAN


--T2
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRAN
	SELECT * FROM Movies WHERE movieId = 2
COMMIT TRAN
 
 /*
  
  T1 is set to isolation level read committed (default)
  T2 is set to isolation level read uncommitted (so it doesnt acquire S locks when reading data)

  T1 updates movie with id 2 (acquiring an X lock) then waits for 10 seconds
  Meanwhile T2 begins and because it doesnt need to acquire any locks it reads the updated title and finishes ( dirty data )
  T1 is rolled back after it finished waiting for the delay

  the solution is to set T2 to isolation level read committed so that it needs to acquire an S lock before reading,
  causing it to wait for the X lock of T1 to be released
  --SET TRANSACTION ISOLATION LEVEL READ COMMITTED

 */






















