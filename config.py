###
# Copyright (c) 2011, jCoder
# All rights reserved.
#
# This software is provided as-is, without any warrenty,
# you can use it freely on your own risk.
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('DisplayTweet', True)

DisplayTweet = conf.registerPlugin('DisplayTweet')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
