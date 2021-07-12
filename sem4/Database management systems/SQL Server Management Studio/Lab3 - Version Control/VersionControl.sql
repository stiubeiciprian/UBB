CREATE OR ALTER PROCEDURE applyChanges @version INT
AS
	DECLARE @procedure VARCHAR(255)
	SET @procedure = (SELECT applyProcedure FROM DatabaseVersion WHERE versionId = @version);
	EXEC @procedure
GO

CREATE OR ALTER PROCEDURE revertChanges @version INT
AS
	DECLARE @procedure VARCHAR(255)
	SET @procedure = (SELECT revertProcedure FROM DatabaseVersion WHERE versionId = @version);
	EXEC @procedure
GO

CREATE OR ALTER PROCEDURE changeVersion @version INT
AS
	DECLARE @currentVersion INT
	SET @currentVersion = (SELECT currentVersion FROM CurrentVersion);

	IF @version > (SELECT COUNT(*) FROM DatabaseVersion) OR @version <= 0
	BEGIN
		PRINT 'The given version does not exist.';
		RETURN
	END

	IF @version = @currentVersion
	BEGIN
		PRINT 'The database version is already ' + CAST(@currentVersion AS VARCHAR(10)) + '.'
		RETURN
	END

	-- Check if upgrade is needed
	IF @version > @currentVersion
		BEGIN
			DECLARE @nextVersion INT
			SET @nextVersion = @currentVersion + 1

			WHILE @nextVersion <= @version
				BEGIN
					EXEC applyChanges @version = @nextVersion
					SET @nextVersion = @nextVersion + 1
				END
			
			UPDATE CurrentVersion
			SET currentVersion = @version
			PRINT 'The database version is ' + CAST(@version AS VARCHAR(10)) + '.'
		END

	-- Check if downgrade is needed
	IF @version < @currentVersion
		BEGIN
			DECLARE @previousVersion INT
			SET @previousVersion = @currentVersion

			WHILE @previousVersion > @version
				BEGIN
					EXEC revertChanges @version = @previousVersion
					SET @previousVersion = @previousVersion - 1
				END

	
			UPDATE CurrentVersion 
			SET currentVersion = @version 
			PRINT 'The database version is ' + CAST(@version AS VARCHAR(10)) + '.'
		END
GO

EXEC changeVersion @version = 1
GO

SELECT currentVersion 
FROM CurrentVersion