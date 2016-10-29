# -*- coding: utf-8 -*-

"""
Ci Addons command line tool
"""

import argparse
import ci_addons
import os


def main():
    """The main entry point to ``ci_addons``.

    This is installed as the script entry point.
    """

    version_str = ("This is scikit-ci-addons version %s, imported from %s\n" %
                   (ci_addons.__version__, os.path.abspath(ci_addons.__file__)))

    parser = argparse.ArgumentParser(description=ci_addons.__doc__)
    parser.add_argument(
        'addon', metavar='ADDON', type=str, nargs='?',
        help='name of addon to execute'
    )
    parser.add_argument(
        'arguments', metavar='ARG', type=str, nargs='*',
        help='addon arguments'
    )
    parser.add_argument(
        "--home", action="store_true",
        help="display directory where all addons can be found"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="list all available addons"
    )
    parser.add_argument(
        "--path", type=str,
        help="display addon path"
    )
    parser.add_argument(
        "--install", type=str,
        help="install addons in the selected directory"
    )
    parser.add_argument(
        "--version", action="version",
        version=version_str,
        help="display scikit-ci-addons version and import information"
    )
    args = parser.parse_args()

    if args.home:  # pragma: no cover
        print(ci_addons.home())
        exit()

    if args.list:
        previous_collection = ""
        for addon in ci_addons.addons():
            current_collection = addon.split(os.path.sep)[0]
            if previous_collection != current_collection:
                print("")
            print(addon)
            previous_collection = current_collection
        exit()

    if args.path is not None:  # pragma: no cover
        print(ci_addons.path(args.path))
        exit()

    if args.install is not None:  # pragma: no cover
        ci_addons.install(args.install)
        exit()

    if all([not getattr(args, arg)
            for arg in ['addon', 'home', 'install', 'list', 'path']]):
        parser.print_usage()
        exit()

    ci_addons.execute(args.addon, args.arguments)


if __name__ == '__main__':
    main()
