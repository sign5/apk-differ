class ManifestDiffer:
    def __init__(self, old_manifest, new_manifest):
        self.old_manifest, self.new_manifest = old_manifest, new_manifest

    def compare_manifests(self):
        print("Is manifest equal:\t\t\t\t", self.old_manifest == self.new_manifest)
        print("Is application equal:\t\t\t", self.old_manifest.application == self.new_manifest.application)
        print("Is compatible_screens equal:\t", self.old_manifest.compatible_screens == self.new_manifest.compatible_screens)
        print("Is instrumentation equal:\t\t", self.old_manifest.instrumentation == self.new_manifest.instrumentation)
        print("Is permission_groups equal:\t\t", self.old_manifest.permission_groups == self.new_manifest.permission_groups)
        print("Is permission_trees equal:\t\t", self.old_manifest.permission_trees == self.new_manifest.permission_trees)
        print("Is permissions equal:\t\t\t", self.old_manifest.permissions == self.new_manifest.permissions)
        print("Is supports_gl_textures equal:\t", self.old_manifest.supports_gl_textures == self.new_manifest.supports_gl_textures)
        print("Is supports_screens equal:\t\t", self.old_manifest.supports_screens == self.new_manifest.supports_screens)
        print("Is uses_configuration equal:\t", self.old_manifest.uses_configuration == self.new_manifest.uses_configuration)
        print("Is uses_features equal:\t\t\t", self.old_manifest.uses_features == self.new_manifest.uses_features)
        print("Is uses_permissions equal:\t\t", self.old_manifest.uses_permissions == self.new_manifest.uses_permissions)
        print("Is uses_permissions_sdk23 equal:", self.old_manifest.uses_permissions_sdk_23 == self.new_manifest.uses_permissions_sdk_23)
        print("Is uses_sdk equal:\t\t\t\t", self.old_manifest.uses_sdk == self.new_manifest.uses_sdk)
