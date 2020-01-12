# AppiumIOS
Example of Appium for ios app.

Instructions:
1. Open the Xcode project, build to get .app package.
2. Open 'Tests/testLogin.py' and update the .app package location as well as the device information.
3. Install Appium on your Mac.   i.e. npm install -g appium
4. Open Terminal, run: appium     (This starts the Appium Rest listener)
5. Finally, on terminal, navgiate to Tests folder and run:  pytest testLogin.py

Reference:
https://www.appcoda.com/automated-ui-testing-appium/
