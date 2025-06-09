@echo off
setlocal

REM Get current date in YYYY-MM-DD format
for /f "tokens=2 delims==" %%G in ('wmic os get localdatetime /value') do set datetime=%%G
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set today=%year%-%month%-%day%

REM Get current branch name
for /f "tokens=*" %%a in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%a

REM Ask for branch name (default to current branch)
set /p branch_name="Branch to push to [%current_branch%]: "
if "%branch_name%"=="" set branch_name=%current_branch%

REM Ask for commit message
set /p message="What is this version about? "

REM Form full commit message with date
set full_message=%today% %message%

REM Stage all changes
git add .

REM Commit with the date-prefixed message
git commit -m "%full_message%"

REM Create a tag with the same message
git tag "%full_message%"

REM Push commits and tags
git push origin %branch_name%
git push origin --tags

echo Done! Committed to branch [%branch_name%] and tagged: "%full_message%"
pause
