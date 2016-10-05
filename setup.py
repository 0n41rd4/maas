# Copyright 2012-2016 Canonical Ltd.  This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

"""Setuptools installer for MAAS."""

from os.path import (
    dirname,
    join,
)

from setuptools import (
    find_packages,
    setup,
)

# The directory in which setup.py lives.
here = dirname(__file__)


def read(filename):
    """Return the whitespace-stripped content of `filename`."""
    path = join(here, filename)
    with open(path, "r") as fin:
        return fin.read().strip()


setup(
    name="maas",
    version="1.10a1",
    url="https://launchpad.net/maas",
    license="AGPLv3",
    description="Metal As A Service",
    long_description=read('README'),

    author="MAAS Developers",
    author_email="maas-devel@lists.launchpad.net",

    packages=find_packages(
        where='src',
        exclude=[
            "*.testing",
            "*.tests",
            "maastesting",
        ],
    ),
    package_dir={'': 'src'},
    include_package_data=True,

    data_files=[
        ('/etc/maas',
            ['etc/maas/drivers.yaml']),
        ('/usr/share/maas',
            ['contrib/maas-rsyslog.conf',
             'contrib/maas-http.conf']),
        ('/etc/maas/preseeds',
            ['contrib/preseeds_v2/commissioning',
             'contrib/preseeds_v2/enlist',
             'contrib/preseeds_v2/enlist_userdata',
             'contrib/preseeds_v2/curtin',
             'contrib/preseeds_v2/curtin_userdata',
             'contrib/preseeds_v2/curtin_userdata_centos',
             'contrib/preseeds_v2/curtin_userdata_custom',
             'contrib/preseeds_v2/curtin_userdata_suse',
             'contrib/preseeds_v2/curtin_userdata_windows']),
        ('/usr/bin',
            ['scripts/maas-generate-winrm-cert',
             'scripts/uec2roottar']),
        ('/usr/sbin',
            ['scripts/maas-dhcp-helper']),
        ('/usr/lib/maas',
            ['scripts/maas-dhcp-monitor',
             'scripts/maas-network-monitor']),
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration',
    ],
)
