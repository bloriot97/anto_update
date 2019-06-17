# tslib environment variables

cat <<EOF | sudo tee /etc/profile.d/tslib.sh
export TSLIB_TSDEVICE=/dev/input/touchscreen
export TSLIB_FBDEVICE=/dev/fb1
EOF

cat <<EOF | sudo tee /etc/sudoers.d/tslib
Defaults env_keep += "TSLIB_TSDEVICE TSLIB_FBDEVICE"
EOF

sudo chmod 0440 /etc/sudoers.d/tslib


# SDL environment variables

cat <<EOF | sudo tee /etc/profile.d/sdl.sh
export SDL_VIDEODRIVER=fbcon
export SDL_FBDEV=/dev/fb1
if [[ -e /dev/input/touchscreen ]]; then
	export SDL_MOUSEDRV=TSLIB
	export SDL_MOUSEDEV=/dev/input/touchscreen
fi
EOF

cat <<EOF | sudo tee /etc/sudoers.d/sdl
Defaults env_keep += "SDL_VIDEODRIVER SDL_FBDEV SDL_MOUSEDRV SDL_MOUSEDEV"
EOF

sudo chmod 0440 /etc/sudoers.d/tslib
