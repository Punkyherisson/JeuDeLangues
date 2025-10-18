#!/bin/bash

# Set display
export DISPLAY=:1

# Kill any existing VNC and X servers
pkill -9 Xvnc 2>/dev/null || true

# Set VNC password
mkdir -p ~/.vnc
echo "replit" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

echo "Starting VNC server on display :1..."

# Start Xvnc server directly in background
Xvnc :1 -geometry 1280x720 -depth 24 -rfbport 5901 -SecurityTypes None -ac &
XVNC_PID=$!

# Wait for X server to start
sleep 2

# Check if Xvnc started successfully
if ! kill -0 $XVNC_PID 2>/dev/null; then
    echo "ERROR: Failed to start Xvnc server"
    exit 1
fi

echo "VNC server started successfully (PID: $XVNC_PID)"

# Start window manager
DISPLAY=:1 fluxbox &
sleep 1

# Start the Python quiz application
echo "Starting Quiz application..."
cd /home/runner/workspace
DISPLAY=:1 python3 main.py &
APP_PID=$!

echo "Quiz application started (PID: $APP_PID)"
echo "VNC server is accessible. Use VNC viewer to interact with the application."

# Monitor both processes
while kill -0 $XVNC_PID 2>/dev/null && kill -0 $APP_PID 2>/dev/null; do
    sleep 5
done

echo "Application or VNC server stopped"
