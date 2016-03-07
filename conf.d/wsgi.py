#!/usr/bin/env python

import subprocess
from os import getenv
from os.path import join


def application(env, start_response):
    msg = b"<p>Python say hello'</p>"

    memcached_dir = getenv('OPENSHIFT_MEMCACHED_DIR', None)

    if memcached_dir:
        path_to_common = join(memcached_dir, 'bin/_common')
        memcached_stats = subprocess.Popen(
            [
                'bash', '-c',
                '. {}; memcached_ping'.format(path_to_common)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        msg += b"<p>memcached say hello</p><pre>"
        msg += memcached_stats.stdout.read().strip()


    start_response('200 OK', [('Content-Type','text/html')])
    return [msg]
