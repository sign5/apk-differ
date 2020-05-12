import argparse
import sys

from androguard.core.bytecodes.apk import APK

from ManifestDiffer import ManifestDiffer
from ManifestParser import ManifestParser


def get_manifest_from_apk(apk_path):
    apk = APK(apk_path)
    xml = apk.get_android_manifest_axml().get_xml().decode('utf-8')
    manifest = ManifestParser.parse_string(xml)
    return manifest


def main(args):
    files = vars(args)['file']
    old_path, new_path = files
    old_manifest = get_manifest_from_apk(old_path) if old_path.endswith("apk") else ManifestParser.parse_xml(old_path)
    new_manifest = get_manifest_from_apk(new_path) if new_path.endswith("apk") else ManifestParser.parse_xml(new_path)
    manifest_differ = ManifestDiffer(old_manifest, new_manifest, args.verbose)
    manifest_differ.compare_manifests()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("python <path_to_old_apk_or_xml> <path_to_new_apk_or_xml>")
        exit(-1)

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='+', help='path to the file')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()
    main(args)
