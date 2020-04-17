import sys
import xml.etree.ElementTree as ET

from manifest import UsesPermission

namespaces = {'android': 'http://schemas.android.com/apk/res/android'}


def get_user_permission_list(root):
    permission_nodes = root.findall('uses-permission', namespaces)
    permissions = []
    for node in permission_nodes:
        up = UsesPermission()
        if node.get('{http://schemas.android.com/apk/res/android}name'):
            up.name = node.get('{http://schemas.android.com/apk/res/android}name')
        if node.get('{http://schemas.android.com/apk/res/android}maxSdkVersion'):
            up.maxSdkVersion = node.get('{http://schemas.android.com/apk/res/android}maxSdkVersion')
        permissions.append(up)
    return permissions


def parse_xml(path):
    xml_tree = ET.parse(path)
    root = xml_tree.getroot()
    permissions = get_user_permission_list(root)
    return permissions


def compare_permission_list(old_permissions, new_permissions):
    if set(old_permissions) != set(new_permissions):
        all_permissions = set(old_permissions) & set(new_permissions)

        for permission in old_permissions:
            if not permission in all_permissions:
                print("Deleted permission: ", permission.name)

        for permission in new_permissions:
            if not permission in all_permissions:
                print("New permission: ", permission.name)


if len(sys.argv) < 3:
    print("python old_xml_path.xml new_xml_path.xml")
    exit(-1)
else:
    old_xml = sys.argv[1]
    new_xml = sys.argv[2]

    old_permissions = parse_xml(old_xml)
    new_permissions = parse_xml(new_xml)

    compare_permission_list(old_permissions, new_permissions)
