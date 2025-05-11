import streamlit as st
import json
from PIL import Image, ImageDraw
import io
import base64

# Initialize session state for persistent variables
if 'current_language' not in st.session_state:
    st.session_state.current_language = "English"
if 'device_states' not in st.session_state:
    st.session_state.device_states = {
        'lamp': False,
        'lights': False,
        'music': False,
        'heat': 20,  # Temperature in Celsius
        'volume': 50,  # Volume percentage
    }
if 'brought_items' not in st.session_state:
    st.session_state.brought_items = []
if 'last_command' not in st.session_state:
    st.session_state.last_command = ""
if 'last_result' not in st.session_state:
    st.session_state.last_result = ""

def create_house_layout():
    # Create a blank image for the house layout
    img = Image.new('RGB', (1600, 1200), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw rooms
    # Living Room
    draw.rectangle([100, 100, 700, 600], outline='black', width=4)
    draw.text((300, 40), "Living Room", fill='black', font=None, font_size=36)
    # TV
    draw.rectangle([200, 200, 400, 300], outline='black', fill='gray', width=3)
    draw.text((270, 240), "TV", fill='white', font=None, font_size=30)
    # Sofa
    draw.rectangle([500, 400, 650, 550], outline='black', fill='brown', width=3)
    draw.text((550, 460), "Sofa", fill='white', font=None, font_size=30)
    # Lamp
    draw.ellipse([550, 250, 600, 300], outline='black', fill='yellow' if st.session_state.device_states['lamp'] else 'gray', width=3)
    draw.text((565, 265), "💡", fill='black', font=None, font_size=30)
    # Living Room Lights
    draw.ellipse([350, 150, 450, 250], outline='black', fill='yellow' if st.session_state.device_states['lights'] else 'gray', width=3)
    draw.text((375, 175), "💡", fill='black', font=None, font_size=30)
    
    # Kitchen
    draw.rectangle([800, 100, 1400, 600], outline='black', width=4)
    draw.text((1050, 40), "Kitchen", fill='black', font=None, font_size=36)
    # Stove
    draw.rectangle([900, 200, 1100, 300], outline='black', fill='gray', width=3)
    draw.text((970, 240), "Stove", fill='white', font=None, font_size=30)
    # Fridge
    draw.rectangle([1200, 200, 1350, 400], outline='black', fill='white', width=3)
    draw.text((1250, 280), "Fridge", fill='black', font=None, font_size=30)
    # Sink
    draw.rectangle([900, 400, 1100, 500], outline='black', fill='lightblue', width=3)
    draw.text((970, 440), "Sink", fill='black', font=None, font_size=30)
    # Kitchen Lights
    draw.ellipse([1150, 150, 1250, 250], outline='black', fill='yellow' if st.session_state.device_states['lights'] else 'gray', width=3)
    draw.text((1175, 175), "💡", fill='black', font=None, font_size=30)
    
    # Bedroom
    draw.rectangle([100, 700, 700, 1100], outline='black', width=4)
    draw.text((300, 640), "Bedroom", fill='black', font=None, font_size=36)
    # Bed
    draw.rectangle([200, 800, 400, 1000], outline='black', fill='lightblue', width=3)
    draw.text((280, 880), "Bed", fill='black', font=None, font_size=30)
    # Wardrobe
    draw.rectangle([500, 800, 600, 1000], outline='black', fill='brown', width=3)
    draw.text((520, 880), "Wardrobe", fill='white', font=None, font_size=30)
    # Music System
    draw.rectangle([200, 600, 300, 700], outline='black', fill='gray', width=3)
    draw.text((230, 640), "Music", fill='white', font=None, font_size=30)
    # Bedroom Lights
    draw.ellipse([350, 750, 450, 850], outline='black', fill='yellow' if st.session_state.device_states['lights'] else 'gray', width=3)
    draw.text((375, 775), "💡", fill='black', font=None, font_size=30)
    
    # Bathroom
    draw.rectangle([800, 700, 1400, 1100], outline='black', width=4)
    draw.text((1050, 640), "Bathroom", fill='black', font=None, font_size=36)
    # Shower
    draw.rectangle([900, 800, 1100, 1000], outline='black', fill='lightblue', width=3)
    draw.text((970, 880), "Shower", fill='black', font=None, font_size=30)
    # Toilet
    draw.rectangle([1200, 800, 1350, 1000], outline='black', fill='white', width=3)
    draw.text((1250, 880), "Toilet", fill='black', font=None, font_size=30)
    # Bathroom Lights
    draw.ellipse([1150, 750, 1250, 850], outline='black', fill='yellow' if st.session_state.device_states['lights'] else 'gray', width=3)
    draw.text((1175, 775), "💡", fill='black', font=None, font_size=30)
    
    # Convert image to base64 for display
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def process_command(command):
    try:
        data = json.loads(command)
        action = data.get('action')
        obj = data.get('object')
        
        if action == 'activate':
            if obj == 'lamp':
                st.session_state.device_states['lamp'] = True
                return "Lamp activated"
            elif obj == 'lights':
                st.session_state.device_states['lights'] = True
                return "Lights activated"
            elif obj == 'music':
                st.session_state.device_states['music'] = True
                return "Music System activated"
                
        elif action == 'deactivate':
            if obj == 'lamp':
                st.session_state.device_states['lamp'] = False
                return "Lamp deactivated"
            elif obj == 'lights':
                st.session_state.device_states['lights'] = False
                return "Lights deactivated"
            elif obj == 'music':
                st.session_state.device_states['music'] = False
                return "Music System deactivated"
                
        elif action == 'increase':
            if obj in ['volume', 'heat']:
                st.session_state.device_states[obj] = min(100, st.session_state.device_states[obj] + 10)
                return f"{obj.capitalize()} increased to {st.session_state.device_states[obj]}"
                
        elif action == 'decrease':
            if obj in ['volume', 'heat']:
                st.session_state.device_states[obj] = max(0, st.session_state.device_states[obj] - 10)
                return f"{obj.capitalize()} decreased to {st.session_state.device_states[obj]}"
                
        elif action == 'change language':
            if obj in ['English', 'Korean', 'Chinese', 'German']:
                st.session_state.current_language = obj
                return f"Language changed to {obj}"
                
        elif action == 'bring':
            if obj in ['newspaper', 'juice', 'socks', 'shoes']:
                st.session_state.brought_items.append(obj)
                return f"Bringing {obj}"
                
        return "Invalid command"
    except json.JSONDecodeError:
        return "Invalid JSON format"

def main():
    st.title("Smart Home Simulator")
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Display house layout
        st.subheader("House Layout")
        house_layout = create_house_layout()
        st.image(f"data:image/png;base64,{house_layout}")
        
        # Display device states
        st.subheader("Device States")
        for device, state in st.session_state.device_states.items():
            if isinstance(state, bool):
                status = "🟢 On" if state else "🔴 Off"
            else:
                status = f"📊 {state}"
            st.write(f"{device.replace('_', ' ').title()}: {status}")
        
        # Display current language
        st.subheader("Current Language")
        st.write(f"🌐 {st.session_state.current_language}")
        
        # Display brought items
        if st.session_state.brought_items:
            st.subheader("Brought Items")
            for item in st.session_state.brought_items:
                st.write(f"📦 {item}")
    
    with col2:
        # Command input
        st.subheader("Voice Command Input")
        command_input = st.text_area("Enter JSON command:", 
                                   value='{"action": "activate", "object": "lights"}',
                                   height=100,
                                   key="command_input")
        
        # Process command automatically when it changes
        if command_input != st.session_state.last_command:
            st.session_state.last_command = command_input
            st.session_state.last_result = process_command(command_input)
        
        # Display last result
        if st.session_state.last_result:
            st.write("Result:", st.session_state.last_result)
        
        # Command examples
        st.subheader("Example Commands")
        examples = [
            '{"action": "activate", "object": "lights"}',
            '{"action": "activate", "object": "lamp"}',
            '{"action": "change language", "object": "Korean"}',
            '{"action": "increase", "object": "volume"}',
            '{"action": "bring", "object": "newspaper"}'
        ]
        for example in examples:
            st.code(example)

if __name__ == "__main__":
    main() 