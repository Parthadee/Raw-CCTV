@echo off
setlocal

echo =====================================
echo Store Intelligence Pipeline Started
echo =====================================

set VIDEO_DIR=C:\Users\Partha\Desktop\store-intelligence\CCTV Footage
set OUTPUT_DIR=C:\Users\Partha\Desktop\store-intelligence\output
set EVENT_FILE=%OUTPUT_DIR%\events.jsonl

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

if exist "%EVENT_FILE%" del "%EVENT_FILE%"

echo [1/3] Processing CCTV clips...

for %%f in ("%VIDEO_DIR%\*.mp4") do (
    echo Processing: %%f

    python "%~dp0detect.py" --video "%%f" --output "%EVENT_FILE%"
)

echo [2/3] Events generated successfully

echo Event file:
echo %EVENT_FILE%

echo [3/3] Sending events to API...

python "%~dp0replay_events.py" --file "%EVENT_FILE%" --api http://localhost:8000/events/ingest

echo =====================================
echo Pipeline Completed Successfully
echo =====================================

pause