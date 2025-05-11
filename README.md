# Smart Home Simulator

A Streamlit-based web application that simulates a smart home environment with voice command controls.

## Features

- Interactive 2D house layout with rooms and devices
- Voice command simulation through JSON input
- Real-time device state tracking
- Multiple language support
- Visual feedback for device states
- Item delivery simulation

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. The application displays a simple house layout with different rooms
2. Use the JSON input field to simulate voice commands
3. Example commands are provided in the right panel
4. Device states and brought items are displayed in real-time
5. The current system language is shown and can be changed

## Command Schema

Commands should follow this JSON format:

```json
{
  "action": "activate" | "deactivate" | "increase" | "decrease" | "change language" | "bring",
  "object": "music" | "lights" | "volume" | "heat" | "lamp" | "newspaper" | "juice" | "socks" | "shoes" | "Chinese" | "Korean" | "English" | "German" | "none"
}
```

## Example Commands

- Activate a device: `{"action": "activate", "object": "lamp"}`
- Change language: `{"action": "change language", "object": "Korean"}`
- Adjust volume: `{"action": "increase", "object": "volume"}`
- Request an item: `{"action": "bring", "object": "newspaper"}`
