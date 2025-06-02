# Install the paho-mqtt library using: pip install paho-mqtt

import paho.mqtt.client as mqtt

# MQTT Broker details
MQTT_BROKER = "localhost"  # Replace with your broker's IP address
MQTT_PORT = 1883
MQTT_TOPIC = "gripper/commands"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

# Function to publish a command to the MQTT topic
def send_command(command):
    client.publish(MQTT_TOPIC, command)
    print(f"Command sent: {command}")

# Function to display available commands
def show_commands():
    print("\nAvailable Commands:")
    print("  h  - Home the gripper")
    print("  xN - Move to position X=N (e.g., x1000)")
    print("  yN - Move to position Y=N (e.g., y2000)")
    print("  zN - Move to position Z=N (e.g., z100)")
    print("  i  - Move Z-axis in")
    print("  o  - Move Z-axis out")
    print("  gX,Y,Z,Speed - Move to X, Y, Z with Speed (e.g., g1000,3000,100,200)")
    print("  bX,Y,Angle - Bring object at X, Y with gripper angle (e.g., b1000,2000,40)")
    print("  exit - Exit the program")

# Initialize the MQTT client
client = mqtt.Client()
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the MQTT client loop in a separate thread
client.loop_start()

# Example commands to send
try:
    while True:
        show_commands()
        print("\nEnter a command to send to the gripper:")
        command = input("> ")
        if command.lower() == "exit":
            break
        send_command(command)
except KeyboardInterrupt:
    print("\nExiting...")

# Stop the MQTT client loop and disconnect
client.loop_stop()
client.disconnect()