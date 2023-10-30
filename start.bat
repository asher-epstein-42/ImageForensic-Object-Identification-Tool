@echo off

rem Install Ultralytics silently
pip show ultralytics > nul 2>&1 || (
    echo Installing Ultralytics...
    pip install ultralytics > nul
    if errorlevel 1 (
        echo Error installing Ultralytics. Exiting.
        exit /b 1
    )
)

rem Install OpenCV silently
pip show opencv-python > nul 2>&1 || (
    echo Installing OpenCV...
    pip install opencv-python > nul
    if errorlevel 1 (
        echo Error installing OpenCV. Exiting.
        exit /b 1
    )
)

rem Run main.py
echo Running main.py...
python main.py

rem Pause to keep the console window open (optional)
pause
