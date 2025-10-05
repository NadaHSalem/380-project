#!/usr/bin/env python3
"""
Simple servo test to debug communication
"""

import serial
import time
import json

def test_servo_connection():
    """Test servo connection and communication"""
    print("=== SERVO COMMUNICATION TEST ===")
    
    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    servo_port = config['servo']['port']
    neutral_angle = config['servo']['neutral_angle']
    
    print(f"Testing servo on port: {servo_port}")
    print(f"Neutral angle: {neutral_angle}")
    
    try:
        # Connect to servo
        print("\n1. Connecting to servo...")
        servo = serial.Serial(servo_port, 9600)
        time.sleep(2)
        print("✓ Connected to servo")
        
        # Clear any existing data
        servo.flushInput()
        
        # Test communication
        print("\n2. Testing communication...")
        
        # Send neutral position
        servo.write(bytes([neutral_angle]))
        print(f"✓ Sent neutral angle: {neutral_angle}")
        time.sleep(1)
        
        # Test different angles
        test_angles = [20, 30, 40, 25, 35]
        for angle in test_angles:
            print(f"Sending angle: {angle}°")
            servo.write(bytes([angle]))
            time.sleep(2)  # Wait to see movement
        
        # Return to neutral
        print("Returning to neutral position...")
        servo.write(bytes([neutral_angle]))
        time.sleep(1)
        
        servo.close()
        print("✓ Servo test completed")
        
    except Exception as e:
        print(f"✗ Servo test failed: {e}")
        print("\nTroubleshooting:")
        print("1. Check if Arduino is connected to the correct port")
        print("2. Verify servo_controller.ino is uploaded to Arduino")
        print("3. Check if another program is using the serial port")
        print("4. Try disconnecting and reconnecting the Arduino")

if __name__ == "__main__":
    test_servo_connection()
