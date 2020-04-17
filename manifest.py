from functools import reduce


class UsesPermission:
    name = "string"  # Name of permission
    maxSdkVersion = ''  # At some API level permission may be requires is no longer needed beginning at a certain API level.

    def __str__(self):
        return "%s [%s]" % (self.name, self.maxSdkVersion)

    def __eq__(self, other):
        return (self.name == other.name) and (self.maxSdkVersion == other.maxSdkVersion)

    def __hash__(self):
        return reduce(lambda x, y: 37 * x + hash(y), [self.name, self.maxSdkVersion], 0)


class Permission:
    name = "string"
    label = "string resource"
    description = "string resource"
    icon = "drawable resource"
    permissionGroup = "string"
    protectionLevel = "[\"normal\" | \"dangerous\" | \"signature\" | \"signatureOrSystem\"]"


class PermissionTree:
    name = "string"
    label = "string resource"
    icon = "drawable resource"


class PermissionGroup:
    name = "string"
    label = "string resource"
    description = "string resource"
    icon = "drawable resource"


class Instrumentation:
    functionalTest = "[\"true\" | \"false\"]"
    handleProfiling = "[\"true\" | \"false\"]"
    icon = "drawable resource"
    label = "string resource"
    name = "string"
    targetPackage = "string"
    targetProcesses = "string"


class UsesSdk:
    minSdkVersion = "integer"
    targetSdkVersion = "integer"
    maxSdkVersion = "integer"


class UsesConfiguration:
    reqFiveWayNav = "[\"true\" | \"false\"]"
    reqHardKeyboard = "[\"true\" | \"false\"]"
    reqKeyboardType = "[\"undefined\" | \"nokeys\" | \"qwerty\" | \"twelvekey\"]"
    reqNavigation = "[\"undefined\" | \"nonav\" | \"dpad\" | \"trackball\" | \"wheel\"]"
    reqTouchScreen = "[\"undefined\" | \"notouch\" | \"stylus\" | \"finger\"]"


class UsesFeature:
    name = "string"
    required = "[\"true\" | \"false\"]"
    glEsVersion = "integer"


class SupportsScreens:
    resizeable = "[\"true\"| \"false\"]"
    smallScreens = "[\"true\" | \"false\"]"
    normalScreens = "[\"true\" | \"false\"]"
    largeScreens = "[\"true\" | \"false\"]"
    xlargeScreens = "[\"true\" | \"false\"]"
    anyDensity = "[\"true\" | \"false\"]"
    requiresSmallestWidthDp = "integer"
    compatibleWidthLimitDp = "integer"
    largestWidthLimitDp = "integer"


class CompatibleScreens:
    pass


class SupportsGlTexture:
    name = "string"


class Application:
    activity_list = []
    activity_alias_list = []
    service_list = []
    receiver_list = []
    provider_list = []

    pass
