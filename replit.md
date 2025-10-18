# JeuDeLangues - Multilingual Quiz App

## Overview
A Python-based multilingual vocabulary quiz application built with Tkinter GUI. The app helps users learn vocabulary across French, German, and Spanish through interactive quizzes with different themes (Colors, Animals, Food).

## Project Structure
- `main.py` - Main Tkinter application with quiz logic
- `quiz_data.json` - Quiz data organized by themes with translations
- `colors.json` - Additional color vocabulary data
- `Vocab.json` - Legacy vocabulary data
- `start_vnc.sh` - VNC server startup script for running GUI in Replit

## Technology Stack
- **Language**: Python 3.11
- **GUI Framework**: Tkinter (standard library)
- **Display**: VNC (TigerVNC) for remote desktop access
- **Window Manager**: Fluxbox

## Running in Replit
This is a desktop GUI application running through VNC (Virtual Network Computing). The workflow "Quiz App" starts the VNC server and launches the application automatically. Users can interact with the GUI through the VNC viewer in the Replit interface.

### Setup Details
- VNC Server: TigerVNC running on display :1 (port 5901)
- Window Manager: Fluxbox (lightweight X11 window manager)
- The application launches automatically when the workflow starts
- No password required for VNC connection (SecurityTypes set to None for ease of use)

## Features
- Choose source and target languages (French, English, German, Spanish)
- Select quiz themes (Colors, Animals, Food)
- Interactive quiz with score tracking
- Immediate feedback on answers
- Random question ordering to avoid repetition

## Data Format
Quiz data is stored in JSON format with the following structure:
```json
{
  "themes": {
    "ThemeName": {
      "english_word": {
        "fr": "french_translation",
        "de": "german_translation",
        "es": "spanish_translation"
      }
    }
  }
}
```

## Recent Changes
- 2025-10-18: Initial setup in Replit environment
  - Installed Python 3.11
  - Configured VNC for Tkinter GUI display
  - Fixed filename case sensitivity issue (Quiz_Data.json → quiz_data.json)
  - Set up workflow for automatic VNC startup

## Architecture Notes
- This is a desktop application, not a web app
- Uses VNC to provide remote GUI access in cloud environment
- No external Python dependencies required (uses standard library only)
