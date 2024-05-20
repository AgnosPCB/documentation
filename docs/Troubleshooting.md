# **Troubleshooting**


??? info "I am getting “time-out” errors when inspecting my circuits. How do I solve it?"

    The Agnospcb inspection software needs a fast and reliable internet connection, as some areas of the photos taken will be sent to our neural network server. That means that, an internet wired connection or Fiber internet service (100-1000Mbps) is mandatory. Otherwise, the software will take over 10 seconds to process one inspection and the “time-out” error message will appear. If you need an “off-line” solution, contact us.

??? info "The camera does not respond"

    Check if the battery dummy is connected to the correct USB power supply, capable of delivering 3A. Check if the USB cable is properly connected and fully inserted. Does the R a S keys of the keyboard trigger the camera?

??? info "Alignment problems"

    Alignment problems may arise due to background patterns that can confuse the alignment process, causing it to fail. It is recommended to use a clean, solid background to allow the software to align images accurately and detect errors properly.

    To ensure successful alignment:
    
    - Use a consistent size/resolution ratio between the REFERENCE and UUI images. This requires the camera to be placed at the same height when capturing photos of the REFERENCE and UUI. Inconsistent ratios will affect alignment accuracy.
    
    - Position the camera as low as possible while ensuring the entire PCB area is captured.
    
    - Utilize the same model for both REFERENCE and UUI images. If any modifications are made to the PCBA production, a new REFERENCE image must be loaded.
    
    - Ensure the UUI has the same layout as the REFERENCE image. Any discrepancies, such as missing boards on the panel, can affect the alignment process.
    
    - Use the "UUI to REF" function to designate a current UUI as a new REFERENCE if it meets alignment requirements, allowing inspections to continue seamlessly.
    
    - Additionally, you can crop the inspection area by right-clicking on the REFERENCE image and dragging the boundaries for improved accuracy.
    
??? info "Camera Does Not Shoot and "Camera Module RESTARTED" Error"

    If you encounter a situation where the camera fails to shoot and displays an error message "Camera Module RESTARTED," please follow these troubleshooting steps:
    
    1. Check Camera Power: Ensure the camera is powered and turned ON.
    
    2. Reinstall Battery Dummy: Reinstall the battery dummy inside the camera. Sometimes it may not be properly set, causing the camera to reboot.
    
    3. USB Cable Connection: Verify that the USB cable connected from the camera to the CPU unit is the straight cable supplied (not the angled one). Ensure it is connected to a USB 3.0 port of the NUC (identified by blue USB connectors).
    
    4. Camera Configuration: Confirm that the camera is configured correctly. For detailed instructions on camera setup, including "[How to connect the camera](Connect-the-camera.md "How to connect the camera")", refer to the user manual for a better and further explanation.
    
    5. Try Alternate USB Cable and Port: If possible, try using another USB cable and a different USB port on the CPU unit.
    
    6. Reboot CPU Unit: Reboot the CPU unit to refresh its settings.
    
    Following these steps should help resolve the issue.

??? info "How to make a report of undetected errors?"

    You can report an undetected fault by moving the cursor to the fault´s area and pressing DOWN arrow key. The images are reported to our server and we use them to train the Neural Network to detect these errors. It will be included in the next Neural Network update.

??? info "Remember sensibility between inspections."

    Regarding the sensibility, there is a parameter in the setup.json file called "remember_sensibility". Modify the file and set this value to 1 to hold the sensibility between inspections.