import hashlib

from DictDiffer import DictDiffer


class Tags:
    action = "action"
    activity = "activity"
    activity_alias = "activity-alias"
    application = "application"
    category = "category"
    compatible_screens = "compatible-screens"
    data = "data"
    grant_uri_permission = "grant-uri-permission"
    instrumentation = "instrumentation"
    intent_filter = "intent-filter"
    layout = "layout"
    manifest = "manifest"
    meta_data = "meta-data"
    path_permission = "path-permission"
    permission = "permission"
    permission_group = "permission-group"
    permission_tree = "permission-tree"
    provider = "provider"
    receiver = "receiver"
    screen = "screen"
    service = "service"
    supports_gl_texture = "supports-gl-texture"
    supports_screens = "supports-screens"
    uses_configuration = "uses-configuration"
    uses_feature = "uses-feature"
    uses_library = "uses-library"
    uses_permission = "uses-permission"
    uses_permission_sdk_23 = "uses-permission-sdk-23"
    uses_sdk = "uses-sdk"


def object_list_hash(prev, next):
    return hash(prev) + hash(next)


class Action:
    def __init__(self):
        self.name = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Action) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Activity:
    def __init__(self):
        self.allowEmbedded = ""  # ["true" | "false"]
        self.allowTaskReparenting = ""  # ["true" | "false"]
        self.alwaysRetainTaskState = ""  # ["true" | "false"]
        self.autoRemoveFromRecents = ""  # ["true" | "false"]
        self.banner = ""  # "drawable resource"
        self.clearTaskOnLaunch = ""  # ["true" | "false"]
        self.colorMode = ""  # [ "hdr" | "wideColorGamut"]
        self.configChanges = ""  # ["mcc", "mnc", "locale", "touchscreen", "keyboard", "keyboardHidden", "navigation", "screenLayout", "fontScale", "uiMode", "orientation", "density", "screenSize", "smallestScreenSize"]
        self.directBootAware = ""  # ["true" | "false"]
        self.documentLaunchMode = ""  # ["intoExisting" | "always" | "none" | "never"]
        self.enabled = ""  # ["true" | "false"]
        self.excludeFromRecents = ""  # ["true" | "false"]
        self.exported = ""  # ["true" | "false"]
        self.finishOnTaskLaunch = ""  # ["true" | "false"]
        self.hardwareAccelerated = ""  # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        self.immersive = ""  # ["true" | "false"]
        # self.label = ""  # "string resource"
        self.launchMode = ""  # ["standard" | "singleTop" | "singleTask" | "singleInstance"]
        self.lockTaskMode = ""  # ["normal" | "never" | "if_whitelisted" | "always"]
        self.maxRecents = ""  # "integer"
        self.maxAspectRatio = ""  # "float"
        self.multiprocess = ""  # ["true" | "false"]
        self.name = ""  # "string"
        self.noHistory = ""  # ["true" | "false"]
        self.parentActivityName = ""  # "string"
        self.persistableMode = ""  # ["persistRootOnly" | "persistAcrossReboots" | "persistNever"]
        self.permission = ""  # "string"
        self.process = ""  # "string"
        self.relinquishTaskIdentity = ""  # ["true" | "false"]
        self.resizeableActivity = ""  # ["true" | "false"]
        self.screenOrientation = ""  # ["unspecified" | "behind" | "landscape" | "portrait" | "reverseLandscape" | "reversePortrait" | "sensorLandscape" | "sensorPortrait" | "userLandscape" | "userPortrait" | "sensor" | "fullSensor" | "nosensor" | "user" | "fullUser" | "locked"]
        self.showForAllUsers = ""  # ["true" | "false"]
        self.stateNotNeeded = ""  # ["true" | "false"]
        self.supportsPictureInPicture = ""  # ["true" | "false"]
        self.taskAffinity = ""  # "string"
        # self.theme = ""  # "resource or theme"
        self.uiOptions = ""  # ["none" | "splitActionBarWhenNarrow"]
        self.windowSoftInputMode = ""  # ["stateUnspecified", "stateUnchanged", "stateHidden", "stateAlwaysHidden", "stateVisible", "stateAlwaysVisible", "adjustUnspecified", "adjustResize", "adjustPan"]
        self.layout = None

        self.intent_filters = []
        self.meta_datas = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Activity) and (self.meta_datas == other.meta_datas) and \
               (self.intent_filters == other.intent_filters) and (self.layout == other.layout) and \
               DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, manifest_classes):
                    if isinstance(field_value, list):
                        for item in field_value:
                            h.update(str(hash(item)).encode('utf-8'))
                    else:
                        h.update(str(hash(field_value)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class ActivityAlias:
    def __init__(self):
        self.enabled = ""  # "" # ["true" | "false"]
        self.exported = ""  # "" # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        # self.label = ""  # "string resource"
        self.name = ""  # "string"
        self.permission = ""  # "string"
        self.targetActivity = ""  # "string"

        self.intent_filters = []
        self.meta_datas = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, ActivityAlias) and (self.meta_datas == other.meta_datas) and \
               (self.intent_filters == other.intent_filters) and DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Application:
    def __init__(self):
        self.allowTaskReparenting = ""  # ["true" | "false"]
        self.allowBackup = ""  # ["true" | "false"]
        self.allowClearUserData = ""  # ["true" | "false"]
        self.allowNativeHeapPointerTagging = ""  # ["true" | "false"]
        self.backupAgent = ""  # "string"
        self.backupInForeground = ""  # ["true" | "false"]
        self.banner = ""  # "drawable resource"
        self.debuggable = ""  # ["true" | "false"]
        self.description = ""  # "string resource"
        self.directBootAware = ""  # ["true" | "false"]
        self.enabled = ""  # ["true" | "false"]
        self.extractNativeLibs = ""  # ["true" | "false"]
        self.fullBackupContent = ""  # "string"
        self.fullBackupOnly = ""  # ["true" | "false"]
        self.hasCode = ""  # ["true" | "false"]
        self.hasFragileUserData = ""  # ["true" | "false"]
        self.hardwareAccelerated = ""  # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        self.isGame = ""  # ["true" | "false"]
        self.killAfterRestore = ""  # ["true" | "false"]
        self.largeHeap = ""  # ["true" | "false"]
        # self.label = ""  # "string resource"
        self.logo = ""  # "drawable resource"
        self.manageSpaceActivity = ""  # "string"
        self.name = ""  # "string"
        self.networkSecurityConfig = ""  # "xml resource"
        self.permission = ""  # "string"
        self.persistent = ""  # ["true" | "false"]
        self.process = ""  # "string"
        self.restoreAnyVersion = ""  # ["true" | "false"]
        self.requestLegacyExternalStorage = ""  # ["true" | "false"]
        self.requiredAccountType = ""  # "string"
        self.resizeableActivity = ""  # ["true" | "false"]
        self.restrictedAccountType = ""  # "string"
        self.supportsRtl = ""  # ["true" | "false"]
        self.taskAffinity = ""  # "string"
        self.testOnly = ""  # ["true" | "false"]
        # self.theme = ""  # "resource or theme"
        self.uiOptions = ""  # ["none" | "splitActionBarWhenNarrow"]
        self.usesCleartextTraffic = ""  # ["true" | "false"]
        self.vmSafeMode = ""  # ["true" | "false"]

        self.activities = []
        self.activity_aliases = []
        self.meta_datas = []
        self.providers = []
        self.receivers = []
        self.services = []
        self.uses_libraries = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Application) and (self.activities == other.activities) and \
               (self.activity_aliases == other.activity_aliases) and (self.meta_datas == other.meta_datas) and \
               (self.providers == other.providers) and (self.receivers == other.receivers) and \
               (self.services == other.services) and (self.uses_libraries == other.uses_libraries) and \
               DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Category:
    def __init__(self):
        self.name = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Category) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class CompatibleScreens:
    def __init__(self):
        self.screens = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, CompatibleScreens) and (self.screens == other.screens)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Data:
    def __init__(self):
        self.scheme = ""  # "string"
        self.host = ""  # "string"
        self.port = ""  # "string"
        self.path = ""  # "string"
        self.pathPattern = ""  # "string"
        self.pathPrefix = ""  # "string"
        self.mimeType = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Data) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class GrantUriPermission:
    def __init__(self):
        self.path = ""  # "string"
        self.pathPattern = ""  # "string"
        self.pathPrefix = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, GrantUriPermission) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Instrumentation:
    def __init__(self):
        self.functionalTest = ""  # ["true" | "false"]
        self.handleProfiling = ""  # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        # self.label = ""  # "string resource"
        self.name = ""  # "string"
        self.targetPackage = ""  # "string"
        self.targetProcesses = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Instrumentation) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class IntentFilter:
    def __init__(self):
        self.icon = ""  # "drawable resource"
        # self.label = ""  # "string resource"
        self.priority = ""  # "integer"

        self.actions = []
        self.categories = []
        self.datas = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, IntentFilter) and (self.actions == other.actions) and \
               (self.categories == other.categories) and (self.datas == other.datas) and \
               DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Layout:
    def __init__(self):
        self.defaultHeight = ""  # "500dp"
        self.defaultWidth = ""  # "600dp"
        self.gravity = ""  # "top|end"
        self.minimalSize = ""  # "450dp"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Layout) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Manifest:
    def __init__(self):
        self.application = None
        self.compatible_screens = None
        self.instrumentation = None
        self.supports_screens = None
        self.uses_configuration = None
        self.uses_sdk = None
        self.permissions = []
        self.permission_groups = []
        self.permission_trees = []
        self.supports_gl_textures = []
        self.uses_features = []
        self.uses_permissions = []
        self.uses_permissions_sdk_23 = []

        self.compileSdkVersion = ""  # "integer"
        self.compileSdkVersionCodename = ""  # "string"
        self.sharedUserId = ""  # "string"
        self.sharedUserLabel = ""  # "string resource"
        self.versionCode = ""  # "integer"
        self.versionName = ""  # "string"
        self.installLocation = ""  # ["auto" | "internalOnly" | "preferExternal"]

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Manifest) and (self.permissions == other.permissions) and \
               (self.permission_groups == other.permission_groups) and \
               (self.permission_trees == other.permission_trees) and \
               (self.supports_gl_textures == other.supports_gl_textures) and \
               (self.uses_features == other.uses_features) and \
               (self.uses_permissions == other.uses_permissions) and \
               (self.uses_permissions_sdk_23 == other.uses_permissions_sdk_23) and \
               DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class MetaData:
    def __init__(self):
        self.name = ""  # "string"
        self.resource = ""  # "resource specification"
        self.value = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, MetaData) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class PathPermission:
    def __init__(self):
        self.path = ""  # "string"
        self.pathPrefix = ""  # "string"
        self.pathPattern = ""  # "string"
        self.permission = ""  # "string"
        self.readPermission = ""  # "string"
        self.writePermission = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, PathPermission) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Permission:
    def __init__(self):
        # self.description = ""  # "string resource"
        self.icon = ""  # "drawable resource"
        # self.label = ""  # "string resource"
        self.name = ""  # "string"
        self.permissionGroup = ""  # "string"
        self.protectionLevel = ""  # ["normal" | "dangerous" | "signature" | ...]

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Permission) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class PermissionGroup:
    def __init__(self):
        self.name = ""  # "string"
        # self.label = ""  # "string resource"
        self.description = ""  # "string resource"
        self.icon = ""  # "drawable resource"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, PermissionGroup) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class PermissionTree:
    def __init__(self):
        self.name = ""  # "string"
        # self.label = ""  # "string resource"
        self.icon = ""  # "drawable resource"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, PermissionTree) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Provider:
    def __init__(self):
        self.authorities = ""  # "list"
        self.directBootAware = ""  # "" # ["true" | "false"]
        self.enabled = ""  # "" # ["true" | "false"]
        self.exported = ""  # "" # ["true" | "false"]
        self.grantUriPermissions = ""  # "" # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        self.initOrder = ""  # "integer"
        # self.label = ""  # "string resource"
        self.multiprocess = ""  # "" # ["true" | "false"]
        self.name = ""  # "string"
        self.permission = ""  # "string"
        self.process = ""  # "string"
        self.readPermission = ""  # "string"
        self.syncable = ""  # "" # ["true" | "false"]
        self.writePermission = ""  # "string"

        self.meta_datas = []
        self.grant_uri_permissions = []
        self.path_permissions = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Provider) and (self.meta_datas == other.meta_datas) and \
               (self.grant_uri_permissions == other.grant_uri_permissions) and \
               (self.path_permissions == other.path_permissions) and DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Receiver:
    def __init__(self):
        self.directBootAware = ""  # ["true" | "false"]
        self.enabled = ""  # ["true" | "false"]
        self.exported = ""  # ["true" | "false"]
        self.icon = ""  # "drawable resource"
        # self.label = ""  # "string resource"
        self.name = ""  # "string"
        self.permission = ""  # "string"
        self.process = ""  # "string"

        self.intent_filters = []
        self.meta_datas = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Receiver) and (self.meta_datas == other.meta_datas) and \
               (self.intent_filters == other.intent_filters) and DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Screen:
    def __init__(self):
        self.screenSize = ""  # ["small" | "normal" | "large" | "xlarge"]
        self.screenDensity = ""  # ["ldpi" | "mdpi" | "hdpi" | "xhdpi" | "280" | "360" | "420" | "480" | "560"]

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Screen) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class Service:
    def __init__(self):
        self.description = ""  # "string resource"
        self.directBootAware = ""  # ["true" | "false"]
        self.enabled = ""  # ["true" | "false"]
        self.exported = ""  # ["true" | "false"]
        self.foregroundServiceType = ""  # ["connectedDevice" | "dataSync" | "location" | "mediaPlayback" | "mediaProjection" | "phoneCall"]
        self.icon = ""  # "drawable resource"
        self.isolatedProcess = ""  # ["true" | "false"]
        # self.label = ""  # "string resource"
        self.name = ""  # "string"
        self.permission = ""  # "string"
        self.process = ""  # "string"

        self.intent_filters = []
        self.meta_datas = []

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, Service) and (self.meta_datas == other.meta_datas) and \
               (self.intent_filters == other.intent_filters) and DictDiffer(self, other).equal_excl_lists()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class SupportsGlTexture:
    def __init__(self):
        self.name = ""  # "string"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, SupportsGlTexture) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class SupportsScreens:
    def __init__(self):
        self.resizeable = ""  # ["true"| "false"]
        self.smallScreens = ""  # ["true" | "false"]
        self.normalScreens = ""  # ["true" | "false"]
        self.largeScreens = ""  # ["true" | "false"]
        self.xlargeScreens = ""  # ["true" | "false"]
        self.anyDensity = ""  # ["true" | "false"]
        self.requiresSmallestWidthDp = ""  # "integer"
        self.compatibleWidthLimitDp = ""  # "integer"
        self.largestWidthLimitDp = ""  # "integer"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, SupportsScreens) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesConfiguration:
    def __init__(self):
        self.reqFiveWayNav = ""  # ["true" | "false"]
        self.reqHardKeyboard = ""  # ["true" | "false"]
        self.reqKeyboardType = ""  # ["undefined" | "nokeys" | "qwerty" | "twelvekey"]
        self.reqNavigation = ""  # ["undefined" | "nonav" | "dpad" | "trackball" | "wheel"]
        self.reqTouchScreen = ""  # ["undefined" | "notouch" | "stylus" | "finger"]

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesConfiguration) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesFeature:
    def __init__(self):
        self.name = ""  # "string"
        self.required = ""  # ["true" | "false"]
        self.glEsVersion = ""  # "integer"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesFeature) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesLibrary:
    def __init__(self):
        self.name = ""  # "string"
        self.required = ""  # ["true" | "false"]

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesLibrary) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesPermission:
    def __init__(self):
        self.name = ""  # "string"
        self.maxSdkVersion = ""  # "integer"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesPermission) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesPermissionSdk23:
    def __init__(self):
        self.name = ""  # "string"
        self.maxSdkVersion = ""  # "integer"

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesPermissionSdk23) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


class UsesSdk:
    def __init__(self):
        self.minSdkVersion = ""
        self.targetSdkVersion = ""
        self.maxSdkVersion = ""

    def __str__(self):
        dict_wo_nones = dict(sorted(filter(lambda x: (x[1] is not None) and (x[1] != []), self.__dict__.items())))
        return dict_wo_nones.__str__()

    def __eq__(self, other):
        return (other is not None) and isinstance(other, UsesSdk) and DictDiffer(self, other).equal()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        h = hashlib.sha256()
        data = dict(sorted(self.__dict__.items()))
        for key in data:
            field_value = data[key]
            if field_value is not None:
                if isinstance(field_value, list):
                    for item in field_value:
                        h.update(str(hash(item)).encode('utf-8'))
                else:
                    h.update(field_value.encode('utf-8'))
        return int(h.hexdigest(), 16)


manifest_classes = (
    Action, Activity, ActivityAlias, Application, Category, CompatibleScreens, Data, GrantUriPermission,
    Instrumentation, IntentFilter, Layout, Manifest, MetaData, PathPermission, Permission, PermissionGroup,
    PermissionTree, Provider, Receiver, Screen, Service, SupportsGlTexture, SupportsScreens, Tags, UsesConfiguration,
    UsesFeature, UsesLibrary, UsesPermission, UsesPermissionSdk23, UsesSdk, list)
