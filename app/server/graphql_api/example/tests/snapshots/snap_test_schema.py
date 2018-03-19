# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_query 1'] = {
    'data': {
        'address': {
            'latlng': '(32.2,12.0)'
        }
    }
}

snapshots['test_mutation 1'] = {
    'data': {
        'createAddress': {
            'latlng': '(32.2,12.0)'
        }
    }
}
