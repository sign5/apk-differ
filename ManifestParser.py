import xml.etree.ElementTree as ET

from manifest import Action, Activity, ActivityAlias, Application, Category, CompatibleScreens, Data, \
    GrantUriPermission, Instrumentation, IntentFilter, Layout, Manifest, MetaData, PathPermission, Permission, \
    PermissionGroup, PermissionTree, Provider, Receiver, Screen, Service, SupportsGlTexture, SupportsScreens, Tags, \
    UsesConfiguration, UsesFeature, UsesLibrary, UsesPermission, UsesPermissionSdk23, UsesSdk


class ManifestParser:
    namespaces = {'android': 'http://schemas.android.com/apk/res/android'}

    @staticmethod
    def process_xml(root):
        manifest = Manifest()
        for key in manifest.__dict__.keys():
            if type(getattr(manifest, key)) is not list:
                setattr(manifest, key, root.get('{http://schemas.android.com/apk/res/android}%s' % key))
        manifest.application = ManifestParser.get_application(root)
        manifest.compatible_screens = ManifestParser.get_compatible_screens(root)
        manifest.instrumentation = ManifestParser.get_instrumentation(root)
        manifest.permissions = ManifestParser.get_permissions(root)
        manifest.permission_groups = ManifestParser.get_permission_groups(root)
        manifest.permission_trees = ManifestParser.get_permission_trees(root)
        manifest.supports_gl_textures = ManifestParser.get_supports_gl_textures(root)
        manifest.supports_screens = ManifestParser.get_supports_screens(root)
        manifest.uses_configuration = ManifestParser.get_uses_configuration(root)
        manifest.uses_features = ManifestParser.get_uses_features(root)
        manifest.uses_permissions = ManifestParser.get_uses_permission(root)
        manifest.uses_permissions_sdk_23 = ManifestParser.get_uses_permission_sdk_23(root)
        manifest.uses_sdk = ManifestParser.get_uses_sdk(root)
        return manifest

    @staticmethod
    def parse_xml(xml_path):
        xml_tree = ET.parse(xml_path)
        root = xml_tree.getroot()
        return ManifestParser.process_xml(root)

    @staticmethod
    def parse_string(xml_string):
        root = ET.fromstring(xml_string)
        return ManifestParser.process_xml(root)

    @staticmethod
    def get_application(root):
        nodes = root.findall(Tags.application, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            application = Application()
            for key in application.__dict__.keys():
                if type(getattr(application, key)) is not list:
                    setattr(application, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            application.activities = ManifestParser.get_activities(node)
            application.activity_aliases = ManifestParser.get_activity_aliases(node)
            application.meta_datas = ManifestParser.get_meta_datas(node)
            application.services = ManifestParser.get_services(node)
            application.receivers = ManifestParser.get_receivers(node)
            application.providers = ManifestParser.get_providers(node)
            application.uses_libraries = ManifestParser.get_uses_libraries(node)
            return application
        else:
            return None

    @staticmethod
    def get_activity_aliases(application):
        nodes = application.findall(Tags.activity_alias, ManifestParser.namespaces)
        activity_aliases = []
        for node in nodes:
            activity_alias = ActivityAlias()
            for key in activity_alias.__dict__.keys():
                if type(getattr(activity_alias, key)) is not list:
                    setattr(activity_alias, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            activity_alias.intent_filters = ManifestParser.get_intent_filters(node)
            activity_alias.meta_datas = ManifestParser.get_meta_datas(node)
            activity_aliases.append(activity_alias)
        return activity_aliases

    @staticmethod
    def get_receivers(application):
        nodes = application.findall(Tags.receiver, ManifestParser.namespaces)
        receivers = []
        for node in nodes:
            receiver = Receiver()
            for key in receiver.__dict__.keys():
                if type(getattr(receiver, key)) is not list:
                    setattr(receiver, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            receiver.intent_filters = ManifestParser.get_intent_filters(node)
            receiver.meta_datas = ManifestParser.get_meta_datas(node)
            receivers.append(receiver)
        return receivers

    @staticmethod
    def get_services(application):
        nodes = application.findall(Tags.service, ManifestParser.namespaces)
        services = []
        for node in nodes:
            service = Service()
            for key in service.__dict__.keys():
                if type(getattr(service, key)) is not list:
                    setattr(service, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            service.intent_filters = ManifestParser.get_intent_filters(node)
            service.meta_datas = ManifestParser.get_meta_datas(node)
            services.append(service)
        return services

    @staticmethod
    def get_activities(application):
        nodes = application.findall(Tags.activity, ManifestParser.namespaces)
        activities = []
        for node in nodes:
            activity = Activity()
            for key in activity.__dict__.keys():
                if type(getattr(activity, key)) is not list:
                    setattr(activity, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            activity.intent_filters = ManifestParser.get_intent_filters(node)
            activity.meta_datas = ManifestParser.get_meta_datas(node)
            activity.layout = ManifestParser.get_layout(node)
            activities.append(activity)
        return activities

    @staticmethod
    def get_intent_filters(root):
        nodes = root.findall(Tags.intent_filter, ManifestParser.namespaces)
        intent_filters = []
        if len(nodes) > 0:
            for node in nodes:
                intent_filter = IntentFilter()
                for key in intent_filter.__dict__.keys():
                    if type(getattr(intent_filter, key)) is not list:
                        setattr(intent_filter, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))

                intent_filter.actions = ManifestParser.get_actions(node)
                intent_filter.categories = ManifestParser.get_categories(node)
                intent_filter.datas = ManifestParser.get_datas(node)
                intent_filters.append(intent_filter)
        return intent_filters

    @staticmethod
    def get_actions(intent_filter):
        nodes = intent_filter.findall(Tags.action, ManifestParser.namespaces)
        actions = []
        for node in nodes:
            action = Action()
            for key in action.__dict__.keys():
                setattr(action, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            actions.append(action)
        return actions

    @staticmethod
    def get_categories(intent_filter):
        nodes = intent_filter.findall(Tags.category, ManifestParser.namespaces)
        categories = []
        for node in nodes:
            category = Category()
            for key in category.__dict__.keys():
                setattr(category, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            categories.append(category)
        return categories

    @staticmethod
    def get_datas(intent_filter):
        nodes = intent_filter.findall(Tags.data, ManifestParser.namespaces)
        datas = []
        if len(nodes) > 0:
            for node in nodes:
                data = Data()
                for key in data.__dict__.keys():
                    setattr(data, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                datas.append(data)
        return datas

    @staticmethod
    def get_providers(application):
        nodes = application.findall(Tags.provider, ManifestParser.namespaces)
        providers = []
        if len(nodes) > 0:
            for node in nodes:
                provider = Provider()
                for key in provider.__dict__.keys():
                    if type(getattr(provider, key)) is not list:
                        setattr(provider, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                provider.grant_uri_permissions = ManifestParser.get_grant_uri_permissions(node)
                provider.meta_datas = ManifestParser.get_meta_datas(node)
                provider.path_permissions = ManifestParser.get_path_permissions(node)
                providers.append(provider)
        return providers

    @staticmethod
    def get_grant_uri_permissions(provider):
        nodes = provider.findall(Tags.grant_uri_permission, ManifestParser.namespaces)
        grant_uri_permissions = []
        if len(nodes) > 0:
            for node in nodes:
                grant_uri_permission = GrantUriPermission()
                for key in grant_uri_permission.__dict__.keys():
                    setattr(grant_uri_permission, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                grant_uri_permissions.append(grant_uri_permission)
        return grant_uri_permissions

    @staticmethod
    def get_path_permissions(provider):
        nodes = provider.findall(Tags.path_permission, ManifestParser.namespaces)
        path_permissions = []
        if len(nodes) > 0:
            for node in nodes:
                path_permission = PathPermission()
                for key in path_permission.__dict__.keys():
                    setattr(path_permission, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                path_permissions.append(path_permission)
        return path_permissions

    @staticmethod
    def get_meta_datas(root):
        nodes = root.findall(Tags.meta_data, ManifestParser.namespaces)
        meta_datas = []
        if len(nodes) > 0:
            for node in nodes:
                meta_data = MetaData()
                for key in meta_data.__dict__.keys():
                    setattr(meta_data, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                meta_datas.append(meta_data)
        return meta_datas

    @staticmethod
    def get_layout(activity):
        nodes = activity.findall(Tags.layout, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            layout = Layout()
            for key in layout.__dict__.keys():
                setattr(layout, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            return layout
        else:
            return None

    @staticmethod
    def get_compatible_screens(manifest):
        nodes = manifest.findall(Tags.compatible_screens, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            compatible_screens = CompatibleScreens()
            compatible_screens.screens = ManifestParser.get_screens(node)
            return compatible_screens
        else:
            return None

    @staticmethod
    def get_screens(compatible_screen):
        nodes = compatible_screen.findall(Tags.screen, ManifestParser.namespaces)
        screens = []
        if len(nodes) > 0:
            for node in nodes:
                screen = Screen()
                for key in screen.__dict__.keys():
                    setattr(screen, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                screens.append(screen)
        return screens

    @staticmethod
    def get_uses_libraries(application):
        nodes = application.findall(Tags.uses_library, ManifestParser.namespaces)
        uses_libraries = []
        if len(nodes) > 0:
            for node in nodes:
                uses_library = UsesLibrary()
                for key in uses_library.__dict__.keys():
                    setattr(uses_library, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                uses_libraries.append(uses_library)
        return uses_libraries

    @staticmethod
    def get_instrumentation(manifest):
        nodes = manifest.findall(Tags.instrumentation, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            instrumentation = Instrumentation()
            for key in instrumentation.__dict__.keys():
                # if node.get('{http://schemas.android.com/apk/res/android}%s' % key):
                setattr(instrumentation, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            return instrumentation
        else:
            return None

    @staticmethod
    def get_permissions(manifest):
        nodes = manifest.findall(Tags.permission, ManifestParser.namespaces)
        permissions = []
        if len(nodes) > 0:
            for node in nodes:
                permission = Permission()
                for key in permission.__dict__.keys():
                    setattr(permission, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                permissions.append(permission)
        return permissions

    @staticmethod
    def get_permission_groups(manifest):
        nodes = manifest.findall(Tags.permission_group, ManifestParser.namespaces)
        permission_groups = []
        if len(nodes) > 0:
            for node in nodes:
                permission_group = PermissionGroup()
                for key in permission_group.__dict__.keys():
                    setattr(permission_group, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                permission_groups.append(permission_group)
        return permission_groups

    @staticmethod
    def get_permission_trees(manifest):
        nodes = manifest.findall(Tags.permission_tree, ManifestParser.namespaces)
        permission_trees = []
        if len(nodes) > 0:
            for node in nodes:
                permission_tree = PermissionTree()
                for key in permission_tree.__dict__.keys():
                    setattr(permission_tree, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                permission_trees.append(permission_tree)
        return permission_trees

    @staticmethod
    def get_supports_gl_textures(manifest):
        nodes = manifest.findall(Tags.supports_gl_texture, ManifestParser.namespaces)
        supports_gl_textures = []
        if len(nodes) > 0:
            for node in nodes:
                supports_gl_texture = SupportsGlTexture()
                for key in supports_gl_texture.__dict__.keys():
                    setattr(supports_gl_texture, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                supports_gl_textures.append(supports_gl_texture)
        return supports_gl_textures

    @staticmethod
    def get_supports_screens(manifest):
        nodes = manifest.findall(Tags.supports_screens, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            supports_screens = SupportsScreens()
            for key in supports_screens.__dict__.keys():
                setattr(supports_screens, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            return supports_screens
        else:
            return None

    @staticmethod
    def get_uses_configuration(manifest):
        nodes = manifest.findall(Tags.uses_configuration, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            uses_configuration = UsesConfiguration()
            for key in uses_configuration.__dict__.keys():
                setattr(uses_configuration, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            return uses_configuration
        else:
            return None

    @staticmethod
    def get_uses_features(manifest):
        nodes = manifest.findall(Tags.uses_feature, ManifestParser.namespaces)
        uses_features = []
        if len(nodes) > 0:
            for node in nodes:
                uses_feature = UsesFeature()
                for key in uses_feature.__dict__.keys():
                    setattr(uses_feature, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                uses_features.append(uses_feature)
        return uses_features

    @staticmethod
    def get_uses_permission(manifest):
        nodes = manifest.findall(Tags.uses_permission, ManifestParser.namespaces)
        uses_permissions = []
        if len(nodes) > 0:
            for node in nodes:
                uses_permission = UsesPermission()
                for key in uses_permission.__dict__.keys():
                    setattr(uses_permission, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                uses_permissions.append(uses_permission)
        return uses_permissions

    @staticmethod
    def get_uses_permission_sdk_23(manifest):
        nodes = manifest.findall(Tags.uses_permission_sdk_23, ManifestParser.namespaces)
        uses_permissions = []
        if len(nodes) > 0:
            for node in nodes:
                uses_permission = UsesPermissionSdk23()
                for key in uses_permission.__dict__.keys():
                    setattr(uses_permission, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
                uses_permissions.append(uses_permission)
        return uses_permissions

    @staticmethod
    def get_uses_sdk(manifest):
        nodes = manifest.findall(Tags.uses_sdk, ManifestParser.namespaces)
        if len(nodes) > 0:
            node = nodes[0]
            uses_sdk = UsesSdk()
            for key in uses_sdk.__dict__.keys():
                setattr(uses_sdk, key, node.get('{http://schemas.android.com/apk/res/android}%s' % key))
            return uses_sdk
        else:
            return None
