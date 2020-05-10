from DictDiffer import DictDiffer

from manifest import manifest_classes


class ManifestDiffer:
    def __init__(self, old_manifest, new_manifest, verbose=False):
        self.old_manifest, self.new_manifest, self.verbose = old_manifest, new_manifest, verbose

    def compare_manifests(self):
        self.compare_manifest_fields()
        self.compare_instrumentation()
        self.compare_supports_screens()
        self.compare_uses_configuration()
        self.compare_uses_sdk()
        self.compare_compatible_screens()
        self.compare_permissions()
        self.compare_permission_groups()
        self.compare_permission_trees()
        self.compare_supports_gl_textures()
        self.compare_uses_features()
        self.compare_uses_permissions()
        self.compare_uses_permissions_sdk_23()
        self.compare_application_fields()
        self.compare_uses_libraries()
        self.compare_activity_lists()
        self.compare_activity_aliases_lists()
        self.compare_services()
        self.compare_receivers()
        self.compare_providers()

    def compare_manifest_fields(self):
        # Comparison 1
        if not DictDiffer(self.old_manifest, self.new_manifest).equal_excl_lists():
            print('[Manifest fields have changed]')
            for key in self.new_manifest.__dict__.keys():
                old_value = getattr(self.old_manifest, key)
                new_value = getattr(self.new_manifest, key)
                if old_value != new_value and not isinstance(new_value, manifest_classes) and not isinstance(old_value, manifest_classes):
                    if not (old_value.startswith("@")) and not (new_value.startswith("@")):
                        print('  %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            print('[Manifest fields equal]')

    def compare_instrumentation(self):
        old_instrumentation, new_instrumentation = self.old_manifest.instrumentation, self.new_manifest.instrumentation
        # Comparison 2
        if old_instrumentation != new_instrumentation:
            if old_instrumentation is None:
                print('  [New instrumentation] %s' % new_instrumentation)
            if new_instrumentation is None:
                print('  [Deleted instrumentation]  %s' % old_instrumentation)

            if old_instrumentation is not None and new_instrumentation is not None:
                print('  [Modified instrumentation]')
                for key in new_instrumentation.__dict__.keys():
                    old_value = getattr(old_instrumentation, key)
                    new_value = getattr(new_instrumentation, key)
                    if old_value != new_value:
                        print('    %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            if self.verbose:
                if old_instrumentation is not None:
                    print('  [Instrumentation equal]')
                else:
                    print('  [Instrumentation is absent]')

    def compare_supports_screens(self):
        old_supports_screens, new_supports_screens = self.old_manifest.supports_screens, self.new_manifest.supports_screens
        # Comparison 2
        if old_supports_screens != new_supports_screens:
            if old_supports_screens is None:
                print('  [New supports screens] %s' % new_supports_screens)
            if new_supports_screens is None:
                print('  [Deleted supports screens]  %s' % old_supports_screens)

            if old_supports_screens is not None and new_supports_screens is not None:
                print('  [Modified supports screens]')
                for key in new_supports_screens.__dict__.keys():
                    old_value = getattr(old_supports_screens, key)
                    new_value = getattr(new_supports_screens, key)
                    if old_value != new_value:
                        print('    %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            if self.verbose:
                if old_supports_screens is not None:
                    print('  [Supports screens equal]')
                else:
                    print('  [Supports screens is absent]')

    def compare_uses_configuration(self):
        old_uses_configuration, new_uses_configuration = self.old_manifest.uses_configuration, self.new_manifest.uses_configuration
        # Comparison 2
        if old_uses_configuration != new_uses_configuration:
            if old_uses_configuration is None:
                print('  [New uses configuration] %s' % new_uses_configuration)
            if new_uses_configuration is None:
                print('  [Deleted uses configuration]  %s' % old_uses_configuration)

            if old_uses_configuration is not None and new_uses_configuration is not None:
                print('  [Modified uses configuration]')
                for key in new_uses_configuration.__dict__.keys():
                    old_value = getattr(old_uses_configuration, key)
                    new_value = getattr(new_uses_configuration, key)
                    if old_value != new_value:
                        print('    %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            if self.verbose:
                if old_uses_configuration is not None:
                    print('  [Uses configuration equal]')
                else:
                    print('  [Uses configuration is absent]')

    def compare_uses_sdk(self):
        old_uses_sdk, new_uses_sdk = self.old_manifest.uses_sdk, self.new_manifest.uses_sdk
        # Comparison 2
        if old_uses_sdk != new_uses_sdk:
            if old_uses_sdk is None:
                print('  [New uses sdk] %s' % new_uses_sdk)
            if new_uses_sdk is None:
                print('  [Deleted uses sdk]  %s' % old_uses_sdk)

            if old_uses_sdk is not None and new_uses_sdk is not None:
                print('  [Modified uses sdk]')
                for key in new_uses_sdk.__dict__.keys():
                    old_value = getattr(old_uses_sdk, key)
                    new_value = getattr(new_uses_sdk, key)
                    if old_value != new_value:
                        print('    %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            if self.verbose:
                if old_uses_sdk is not None:
                    print('  [Uses-sdk equal]')
                else:
                    print('  [Uses-sdk is absent]')

    def compare_compatible_screens(self):
        old_compatible_screens, new_compatible_screens = self.old_manifest.compatible_screens, self.new_manifest.compatible_screens
        # Comparison 3
        if old_compatible_screens != new_compatible_screens:
            if old_compatible_screens is None:
                print('  [New compatible screens]\n\t%s' % new_compatible_screens)
            elif new_compatible_screens is None:
                print('  [Deleted compatible screens]  %s' % old_compatible_screens)
            else:
                print('  [Modified compatible screens]')
                old_screens = set(old_compatible_screens.screens)
                new_screens = set(new_compatible_screens.screens)
                all_screens = old_screens | new_screens
                # Comparison 3.1
                for screen in all_screens:
                    if screen in old_screens and screen not in new_screens:
                        print('    [Deleted screen]\t%s' % screen)
                    if screen in new_screens and screen not in old_screens:
                        print('    [New screen]\t%s' % screen)
        else:
            if self.verbose:
                if new_compatible_screens is not None:
                    print('  [Compatible screens equal]')
                else:
                    print('  [Compatible screens is absent]')

    def compare_permissions(self):
        old_permissions, new_permissions = self.old_manifest.permissions, self.new_manifest.permissions
        # Comparison 4
        if old_permissions != new_permissions:
            old_permissions = set(old_permissions)
            new_permissions = set(new_permissions)
            all_permissions = old_permissions | new_permissions

            print('  [List of "permission" has changed]')
            for permission in all_permissions:
                if permission in old_permissions and permission not in new_permissions:
                    print('    [Deleted permission] %s' % permission)
                if permission in new_permissions and permission not in old_permissions:
                    print('    [New permission] %s' % permission)
        else:
            if self.verbose:
                if new_permissions:
                    print('  [Lists of permissions are equal]')
                else:
                    print('  [No permissions]')

    def compare_permission_groups(self):
        old_permission_groups, new_permission_groups = self.old_manifest.permission_groups, self.new_manifest.permission_groups
        # Comparison 4
        if old_permission_groups != new_permission_groups:
            old_permission_groups = set(old_permission_groups)
            new_permission_groups = set(new_permission_groups)
            all_permission_groups = old_permission_groups | new_permission_groups

            print('  [List of "permission-group" has changed]')
            for permission_group in all_permission_groups:
                if permission_group in old_permission_groups and permission_group not in new_permission_groups:
                    print('    [Deleted permission_group] %s' % permission_group)
                if permission_group in new_permission_groups and permission_group not in old_permission_groups:
                    print('    [New permission_group] %s' % permission_group)
        else:
            if self.verbose:
                if new_permission_groups:
                    print('  [Lists of permission-groups are equal]')
                else:
                    print('  [No permission-groups]')

    def compare_permission_trees(self):
        old_permission_trees, new_permission_trees = self.old_manifest.permission_trees, self.new_manifest.permission_trees
        # Comparison 4
        if old_permission_trees != new_permission_trees:
            old_permission_trees = set(old_permission_trees)
            new_permission_trees = set(new_permission_trees)
            all_permission_trees = old_permission_trees | new_permission_trees

            print('  [List of "permission-tree" has changed]')
            for permission_tree in all_permission_trees:
                if permission_tree in old_permission_trees and permission_tree not in new_permission_trees:
                    print('    [Deleted permission-tree] %s' % permission_tree)
                if permission_tree in new_permission_trees and permission_tree not in old_permission_trees:
                    print('    [New permission-tree] %s' % permission_tree)
        else:
            if self.verbose:
                if new_permission_trees:
                    print('  [Lists of permission-trees are equal]')
                else:
                    print('  [No permission-trees]')

    def compare_supports_gl_textures(self):
        old_supports_gl_textures, new_supports_gl_textures = self.old_manifest.supports_gl_textures, self.new_manifest.supports_gl_textures
        # Comparison 4
        if old_supports_gl_textures != new_supports_gl_textures:
            old_supports_gl_textures = set(old_supports_gl_textures)
            new_supports_gl_textures = set(new_supports_gl_textures)
            all_supports_gl_textures = old_supports_gl_textures | new_supports_gl_textures

            print('  [List of "supports-gl-texture" has changed]')
            for supports_gl_textures in all_supports_gl_textures:
                if supports_gl_textures in old_supports_gl_textures and supports_gl_textures not in new_supports_gl_textures:
                    print('    [Deleted supports-gl-textures] %s' % supports_gl_textures)
                if supports_gl_textures in new_supports_gl_textures and supports_gl_textures not in old_supports_gl_textures:
                    print('    [New supports-gl-textures] %s' % supports_gl_textures)
        else:
            if self.verbose:
                if new_supports_gl_textures:
                    print('  [Lists of supports-gl-textures are equal]')
                else:
                    print('  [No supports-gl-textures]')

    def compare_uses_features(self):
        old_uses_features, new_uses_features = self.old_manifest.uses_features, self.new_manifest.uses_features
        # Comparison 4
        if old_uses_features != new_uses_features:
            old_uses_features = set(old_uses_features)
            new_uses_features = set(new_uses_features)
            all_uses_features = old_uses_features | new_uses_features

            print('  [List of "uses-feature" has changed]')
            for uses_feature in all_uses_features:
                if uses_feature in old_uses_features and uses_feature not in new_uses_features:
                    print('    [Deleted uses-features] %s' % uses_feature)
                if uses_feature in new_uses_features and uses_feature not in old_uses_features:
                    print('    [New uses-features] %s' % uses_feature)
        else:
            if self.verbose:
                if new_uses_features:
                    print('  [Lists of uses-features are equal]')
                else:
                    print('  [No uses-features]')


    def compare_uses_permissions(self):
        old_uses_permissions, new_uses_permissions = self.old_manifest.uses_permissions, self.new_manifest.uses_permissions
        # Comparison 4
        if old_uses_permissions != new_uses_permissions:
            old_uses_permissions = set(old_uses_permissions)
            new_uses_permissions = set(new_uses_permissions)
            all_uses_permissions = old_uses_permissions | new_uses_permissions

            print('  [List of "uses-permission" has changed]')
            for uses_permission in all_uses_permissions:
                if uses_permission in old_uses_permissions and uses_permission not in new_uses_permissions:
                    print('    [Deleted uses-permission] %s' % uses_permission)
                if uses_permission in new_uses_permissions and uses_permission not in old_uses_permissions:
                    print('    [New uses-permission] %s' % uses_permission)
        else:
            if self.verbose:
                if new_uses_permissions:
                    print('  [Lists of uses-permissions are equal]')
                else:
                    print('  [No uses-permissions]')

    def compare_uses_permissions_sdk_23(self):
        old_uses_permissions, new_uses_permissions = self.old_manifest.uses_permissions_sdk_23, self.new_manifest.uses_permissions_sdk_23
        # Comparison 4
        if old_uses_permissions != new_uses_permissions:
            old_uses_permissions = set(old_uses_permissions)
            new_uses_permissions = set(new_uses_permissions)
            all_uses_permissions = old_uses_permissions | new_uses_permissions

            print('  [List of "uses-permission-sdk-23" has changed]')
            for uses_permission in all_uses_permissions:
                if uses_permission in old_uses_permissions and uses_permission not in new_uses_permissions:
                    print('    [Deleted uses-permission-sdk-23] %s' % uses_permission)
                if uses_permission in new_uses_permissions and uses_permission not in old_uses_permissions:
                    print('    [New uses-permission-sdk-23] %s' % uses_permission)
        else:
            if self.verbose:
                if new_uses_permissions:
                    print('  [Lists of uses-permission-sdk-23 are equal]')
                else:
                    print('  [No uses-permissions-sdk-23]')

    def compare_application_fields(self):
        # Comparison 5
        old_application = self.old_manifest.application
        new_application = self.new_manifest.application
        if not DictDiffer(old_application, new_application).equal_excl_lists():
            print('  [Application fields have changed]')
            for key in old_application.__dict__.keys():
                old_value = getattr(old_application, key)
                new_value = getattr(new_application, key)
                if old_value != new_value and not isinstance(new_value, manifest_classes) and not isinstance(old_value, manifest_classes):
                    if old_value is None:
                        old_value = ''
                    if new_value is None:
                        old_value = ''
                    if not (old_value.startswith("@")) and not (new_value.startswith("@")):
                        print('    %s:\t(%s) -> (%s)' % (key, old_value, new_value))
        else:
            print('  [Application fields are equal]')

    def compare_uses_libraries(self):
        old_uses_libraries, new_uses_libraries = self.old_manifest.application.uses_libraries, self.new_manifest.application.uses_libraries
        # Comparison 5.1
        if old_uses_libraries != new_uses_libraries:
            old_uses_libraries = set(old_uses_libraries)
            new_uses_libraries = set(new_uses_libraries)
            all_uses_libraries = old_uses_libraries | new_uses_libraries

            print('    [List of "uses-library" has changed]')
            for uses_library in all_uses_libraries:
                if uses_library in old_uses_libraries and uses_library not in new_uses_libraries:
                    print('      [Deleted uses-library] %s' % uses_library)
                if uses_library in new_uses_libraries and uses_library not in old_uses_libraries:
                    print('      [New uses-library] %s' % uses_library)
        else:
            if self.verbose:
                if new_uses_libraries:
                    print('    [Lists of uses-library are equal]')
                else:
                    print('    [No uses-library]')

    def compare_activity_lists(self):
        old_activities, new_activities = self.old_manifest.application.activities, self.new_manifest.application.activities
        # Comparison 5.2
        if old_activities != new_activities:
            old_activities = set(old_activities)
            new_activities = set(new_activities)
            all_activities = old_activities | new_activities
            deleted_activities = all_activities - new_activities
            added_activities = all_activities - old_activities

            print('    [List of activities has changed]')
            for activity in deleted_activities:
                activity_name = activity.name
                activities_with_same_name = list(filter(lambda x: x.name == activity_name, added_activities))
                if len(activities_with_same_name) > 0:
                    activity_with_same_name = activities_with_same_name[0]
                    self.compare_two_activities(activity, activity_with_same_name)
                    added_activities.remove(activity_with_same_name)
                else:
                    print('      [DELETED] %s' % activity)

            for activity in added_activities:
                activity_name = activity.name
                activities_with_same_name = list(filter(lambda x: x.name == activity_name, deleted_activities))
                if len(activities_with_same_name) > 0:
                    self.compare_two_activities(activity, activities_with_same_name[0])
                else:
                    print('      [NEW] %s' % activity)
        else:
            if self.verbose:
                if new_activities is not None:
                    print('    [Lists of activities are equal]')
                else:
                    print('    [No activities]')

    def compare_two_activities(self, old_activity, new_activity):
        # Comparison 5.2.1
        if old_activity.name == new_activity.name:
            print('      [Activity "%s" fields CHANGED]' % new_activity.name)
            not_list_keys = sorted(filter(lambda x: not isinstance(x, manifest_classes), new_activity.__dict__.keys()))
            for key in not_list_keys:
                old_value = getattr(old_activity, key)
                new_value = getattr(new_activity, key)
                if not isinstance(new_value, list):
                    if old_value != new_value:
                        print('        %s:\t(%s) -> (%s)' % (key, old_value, new_value))
            self.compare_intent_filter_lists(old_activity, new_activity)
            self.compare_meta_data_lists(old_activity, new_activity)
        else:
            raise Exception('Activities with different names are compared')

    def compare_intent_filter_lists(self, old_activity, new_activity):
        # Comparison 5.2.1.1
        old_intent_filters = set(old_activity.intent_filters)
        new_intent_filters = set(new_activity.intent_filters)
        all_intent_filters = old_intent_filters | new_intent_filters
        deleted_intent_filters = all_intent_filters - new_intent_filters
        added_intent_filters = all_intent_filters - old_intent_filters

        if old_intent_filters != new_intent_filters:
            print('        [Lists of intent-filters of "%s" activity has changed]' % old_activity.name)
            for intent_filter in deleted_intent_filters:
                print('          [DELETED] %s' % intent_filter)

            for intent_filter in added_intent_filters:
                print('          [ADDED] %s' % intent_filter)
        else:
            if self.verbose:
                if new_intent_filters != []:
                    print('    [Lists of intent-filters of "%s" activity are equal]')
                else:
                    print('    [No intent-filters]')

    def compare_meta_data_lists(self, old_activity, new_activity):
        # Comparison 5.2.1.2
        old_meta_datas = set(old_activity.meta_datas)
        new_meta_datas = set(new_activity.meta_datas)
        all_meta_datas = old_meta_datas | new_meta_datas
        deleted_meta_datas = all_meta_datas - new_meta_datas
        added_meta_datas = all_meta_datas - old_meta_datas

        if old_meta_datas != new_meta_datas:
            print('        [Lists of meta-datas of "%s" activity has changed]' % old_activity.name)
            for intent_filter in deleted_meta_datas:
                print('          [DELETED] %s' % intent_filter)

            for intent_filter in added_meta_datas:
                print('          [ADDED] %s' % intent_filter)
        else:
            if self.verbose:
                if new_meta_datas != []:
                    print('    [Lists of meta-datas of "%s" activity are equal]')
                else:
                    print('    [No meta-datas]')

    def compare_activity_aliases_lists(self):
        # Comparison 5.3
        old_activity_aliases, new_activity_aliases = self.old_manifest.application.activity_aliases, self.new_manifest.application.activity_aliases
        if old_activity_aliases != new_activity_aliases:
            old_activity_aliases = set(old_activity_aliases)
            new_activity_aliases = set(new_activity_aliases)
            all_activity_aliases = old_activity_aliases | new_activity_aliases
            deleted_activity_aliases = all_activity_aliases - new_activity_aliases
            added_activity_aliases = all_activity_aliases - old_activity_aliases

            print('    [List of activity-aliases has changed]')
            for activity in deleted_activity_aliases:
                activity_name = activity.name
                activity_aliases_with_same_name = list(filter(lambda x: x.name == activity_name, added_activity_aliases))
                if len(activity_aliases_with_same_name) > 0:
                    activity_with_same_name = activity_aliases_with_same_name[0]
                    self.compare_two_activity_aliases(activity, activity_with_same_name)
                    added_activity_aliases.remove(activity_with_same_name)
                else:
                    print('      [DELETED] %s' % activity)

            for activity in added_activity_aliases:
                activity_name = activity.name
                activity_aliases_with_same_name = list(filter(lambda x: x.name == activity_name, deleted_activity_aliases))
                if len(activity_aliases_with_same_name) > 0:
                    self.compare_two_activity_aliases(activity, activity_aliases_with_same_name[0])
                else:
                    print('      [NEW] %s' % activity)
        else:
            if self.verbose:
                if new_activity_aliases is not None:
                    print('    [Lists of activity_aliases are equal]')
                else:
                    print('    [No activity_aliases]')

    def compare_two_activity_aliases(self, old_activity_alias, new_activity_alias):
        # Comparison 5.3.1
        if old_activity_alias.name == new_activity_alias.name:
            print('      [Activity-alias "%s" fields CHANGED]' % new_activity_alias.name)
            not_list_keys = sorted(filter(lambda x: not isinstance(x, manifest_classes), new_activity_alias.__dict__.keys()))
            for key in not_list_keys:
                old_value = getattr(old_activity_alias, key)
                new_value = getattr(new_activity_alias, key)
                if not isinstance(new_value, list):
                    if old_value != new_value:
                        print('        %s:\t(%s) -> (%s)' % (key, old_value, new_value))
            self.compare_intent_filter_lists(old_activity_alias, new_activity_alias)
            self.compare_meta_data_lists(old_activity_alias, new_activity_alias)
        else:
            raise Exception('Activity-aliases with different names are compared')

    def compare_services(self):
        # Comparison 5.4
        old_services, new_services = self.old_manifest.application.services, self.new_manifest.application.services
        if old_services != new_services:
            old_services = set(old_services)
            new_services = set(new_services)
            all_services = old_services | new_services
            deleted_services = all_services - new_services
            added_services = all_services - old_services

            print('    [List of services has changed]')
            for activity in deleted_services:
                activity_name = activity.name
                services_with_same_name = list(filter(lambda x: x.name == activity_name, added_services))
                if len(services_with_same_name) > 0:
                    activity_with_same_name = services_with_same_name[0]
                    self.compare_two_services(activity, activity_with_same_name)
                    added_services.remove(activity_with_same_name)
                else:
                    print('      [DELETED] %s' % activity)

            for activity in added_services:
                activity_name = activity.name
                services_with_same_name = list(filter(lambda x: x.name == activity_name, deleted_services))
                if len(services_with_same_name) > 0:
                    self.compare_two_services(activity, services_with_same_name[0])
                else:
                    print('      [NEW] %s' % activity)
        else:
            if self.verbose:
                if new_services is not None:
                    print('    [Lists of services are equal]')
                else:
                    print('    [No services]')

    def compare_two_services(self, old_service, new_service):
        # Comparison 5.4.1
        if old_service.name == new_service.name:
            print('      [Service "%s" fields CHANGED]' % new_service.name)
            not_list_keys = sorted(filter(lambda x: not isinstance(x, manifest_classes), new_service.__dict__.keys()))
            for key in not_list_keys:
                old_value = getattr(old_service, key)
                new_value = getattr(new_service, key)
                if not isinstance(new_value, list):
                    if old_value != new_value:
                        print('        %s:\t(%s) -> (%s)' % (key, old_value, new_value))
            self.compare_intent_filter_lists(old_service, new_service)
            self.compare_meta_data_lists(old_service, new_service)
        else:
            raise Exception('Services with different names are compared')

    def compare_receivers(self):
        # Comparison 5.5
        old_receivers, new_receivers = self.old_manifest.application.receivers, self.new_manifest.application.receivers
        if old_receivers != new_receivers:
            old_receivers = set(old_receivers)
            new_receivers = set(new_receivers)
            all_receivers = old_receivers | new_receivers
            deleted_receivers = all_receivers - new_receivers
            added_receivers = all_receivers - old_receivers

            print('    [List of receivers has changed]')
            for activity in deleted_receivers:
                activity_name = activity.name
                receivers_with_same_name = list(filter(lambda x: x.name == activity_name, added_receivers))
                if len(receivers_with_same_name) > 0:
                    activity_with_same_name = receivers_with_same_name[0]
                    self.compare_two_receivers(activity, activity_with_same_name)
                    added_receivers.remove(activity_with_same_name)
                else:
                    print('      [DELETED] %s' % activity)

            for activity in added_receivers:
                activity_name = activity.name
                receivers_with_same_name = list(filter(lambda x: x.name == activity_name, deleted_receivers))
                if len(receivers_with_same_name) > 0:
                    self.compare_two_receivers(activity, receivers_with_same_name[0])
                else:
                    print('      [NEW] %s' % activity)
        else:
            if self.verbose:
                if new_receivers is not None:
                    print('    [Lists of receivers are equal]')
                else:
                    print('    [No receivers]')

    def compare_two_receivers(self, old_receiver, new_receiver):
        # Comparison 5.5.1
        if old_receiver.name == new_receiver.name:
            print('      [Receiver "%s" fields CHANGED]' % new_receiver.name)
            not_list_keys = sorted(filter(lambda x: not isinstance(x, manifest_classes), new_receiver.__dict__.keys()))
            for key in not_list_keys:
                old_value = getattr(old_receiver, key)
                new_value = getattr(new_receiver, key)
                if not isinstance(new_value, list):
                    if old_value != new_value:
                        print('        %s:\t(%s) -> (%s)' % (key, old_value, new_value))
            self.compare_intent_filter_lists(old_receiver, new_receiver)
            self.compare_meta_data_lists(old_receiver, new_receiver)
        else:
            raise Exception('Receivers with different names are compared')

    def compare_providers(self):
        # Comparison 5.6
        old_providers, new_providers = self.old_manifest.application.providers, self.new_manifest.application.providers
        if old_providers != new_providers:
            old_providers = set(old_providers)
            new_providers = set(new_providers)
            all_providers = old_providers | new_providers
            deleted_providers = all_providers - new_providers
            added_providers = all_providers - old_providers

            print('    [List of providers has changed]')
            for provider in deleted_providers:
                provider_name = provider.name
                providers_with_same_name = list(filter(lambda x: x.name == provider_name, added_providers))
                if len(providers_with_same_name) > 0:
                    activity_with_same_name = providers_with_same_name[0]
                    self.compare_two_providers(provider, activity_with_same_name)
                    added_providers.remove(activity_with_same_name)
                else:
                    print('      [DELETED] %s' % provider)

            for provider in added_providers:
                provider_name = provider.name
                providers_with_same_name = list(filter(lambda x: x.name == provider_name, deleted_providers))
                if len(providers_with_same_name) > 0:
                    self.compare_two_providers(provider, providers_with_same_name[0])
                else:
                    print('      [NEW] %s' % provider)
        else:
            if self.verbose:
                if new_providers is not None:
                    print('    [Lists of providers are equal]')
                else:
                    print('    [No providers]')

    def compare_two_providers(self, old_provider, new_provider):
        # Comparison 5.6.1
        if old_provider.name == new_provider.name:
            print('      [Provider "%s" fields CHANGED]' % new_provider.name)
            not_list_keys = sorted(filter(lambda x: not isinstance(x, manifest_classes), new_provider.__dict__.keys()))
            for key in not_list_keys:
                old_value = getattr(old_provider, key)
                new_value = getattr(new_provider, key)
                if not isinstance(new_value, list):
                    if old_value != new_value:
                        print('        %s:\t(%s) -> (%s)' % (key, old_value, new_value))
            self.compare_grant_uri_permissions(old_provider, new_provider)
            self.compare_meta_data_lists(old_provider, new_provider)
            self.compare_path_permissions(old_provider, new_provider)
        else:
            raise Exception('Providers with different names are compared')

    def compare_grant_uri_permissions(self, old_provider, new_provider):
        # Comparison 5.6.1.1
        old_grant_uri_permissions = set(old_provider.grant_uri_permissions)
        new_grant_uri_permissions = set(new_provider.grant_uri_permissions)
        all_grant_uri_permissions = old_grant_uri_permissions | new_grant_uri_permissions
        deleted_grant_uri_permissions = all_grant_uri_permissions - new_grant_uri_permissions
        added_grant_uri_permissions = all_grant_uri_permissions - old_grant_uri_permissions

        if old_grant_uri_permissions != new_grant_uri_permissions:
            print('        [Lists of grant-uri-permissions of "%s" provider has changed]' % old_provider.name)
            for intent_filter in deleted_grant_uri_permissions:
                print('          [DELETED] %s' % intent_filter)

            for intent_filter in added_grant_uri_permissions:
                print('          [ADDED] %s' % intent_filter)
        else:
            if self.verbose:
                if new_grant_uri_permissions != []:
                    print('    [Lists of grant-uri-permissions of "%s" activity are equal]')
                else:
                    print('    [No grant-uri-permissions]')

    def compare_path_permissions(self, old_provider, new_provider):
        # Comparison 5.6.1.3
        old_path_permissions = set(old_provider.path_permissions)
        new_path_permissions = set(new_provider.path_permissions)
        all_path_permissions = old_path_permissions | new_path_permissions
        deleted_path_permissions = all_path_permissions - new_path_permissions
        added_path_permissions = all_path_permissions - old_path_permissions

        if old_path_permissions != new_path_permissions:
            print('        [Lists of path-permissions of "%s" provider has changed]' % old_provider.name)
            for intent_filter in deleted_path_permissions:
                print('          [DELETED] %s' % intent_filter)

            for intent_filter in added_path_permissions:
                print('          [ADDED] %s' % intent_filter)
        else:
            if self.verbose:
                if new_path_permissions != []:
                    print('    [Lists of path-permissions of "%s" activity are equal]')
                else:
                    print('    [No path-permissions]')
