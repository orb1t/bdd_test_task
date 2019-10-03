
# install dependencies :
pip install -r requirements.txt

# update 'deviceName' and webdriver.Remote address/port according to test target device/emulator setup in :
./features/util/Driver.py

# start Appium

# run tests :
behave ./features
