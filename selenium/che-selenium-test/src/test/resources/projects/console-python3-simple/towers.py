#
# Copyright (c) 2012-2018 Red Hat, Inc.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which is available at http://www.eclipse.org/legal/epl-2.0.html
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#   Red Hat, Inc. - initial API and implementation
#


def towers(i, start, finish, middle):
    if i > 0:
        towers(i-1, start, middle, finish)
        print('move disk from ', start, ' to ', finish)
        towers  ( i-1, middle, finish, start   )

towers  ( 5, 'X', 'Z', 'Y'      )