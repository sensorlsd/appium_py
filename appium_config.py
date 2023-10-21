
class AppiumConfig:

    desired_android_caps = dict(
        deviceName='Samsung A525',
        platformName='Android',
        appPackage='com.android',
        appActivity='.Settings'
    )

    desired_ios_caps = dict(
        deviceName='iPhone 8',
        platformName='IOS',
        appPackage='com.ios',
        appActivity='.Settings'
    )