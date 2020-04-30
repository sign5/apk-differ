import argparse
import os
import sys
import tempfile
from os import system

from ManifestDiffer import ManifestDiffer
from ManifestParser import ManifestParser


def get_manifest_from_apk(apk_path):
    apk_tmpdir = tempfile.TemporaryDirectory()
    system("apktool d %s -f -o %s" % (apk_path, apk_tmpdir.name))
    manifest_path = os.path.join(apk_tmpdir.name, 'AndroidManifest.xml')
    manifest = ManifestParser.parse_xml(manifest_path)
    return manifest


def main(files):
    old_apk_path, new_apk_path = files
    old_manifest = get_manifest_from_apk(old_apk_path)
    new_manifest = get_manifest_from_apk(new_apk_path)
    manifest_differ = ManifestDiffer(old_manifest, new_manifest)
    manifest_differ.compare_manifests()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("python <path_to_old_apk> <path_to_new_apk>")
        exit(-1)

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='+', help='path to the file')
    args_namespace = parser.parse_args()
    args = vars(args_namespace)['file']
    main(args)
