# ethereum-pi

Instructions to user:
1. Prepare Raspberry PI 4 with fresh Raspbian OS Legacy (Not tested on Bullseye, which you may need to run `sudo raspi-config` to enable legacy camera support)
2. Install Docker and docker-compose
3. Enable container's access to Pi Camera
    - One time setup `echo "SUBSYSTEM==\"vchiq\",MODE=\"0666\"" | sudo tee /etc/udev/rules.d/99-camera.rules`
    - Every reboot `xhost +local:`
4. Clone this repo
5. `cd ethereum-pi`

6. run 'docker-compose run backend'
7. It will pull the image and run.
8. Depends on where you issued the `docker-compose`, i.e. from SSH terminal, or a terminal in Desktop mode, a full graphical preivew or text preview may appear.
9. Aim the Pi Camera at a QR code, representing a valid Etherum (ERC20) address
10. Adjust the Camera and QR code, the QR code will be captured and decoded.
11. Follow the instruction on the screen to

