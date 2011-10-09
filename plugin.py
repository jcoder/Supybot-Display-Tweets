###
# Copyright (c) 2011, jCoder
# All rights reserved.
#
# This software is provided as-is, without any warrenty,
# you can use it freely on your own risk.
###

import supybot.utils as utils
from supybot.commands import *
import supybot.ircmsgs as ircmsgs
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import urllib
import threading
import time
import re
import simplejson as json

class DisplayTweet(callbacks.Plugin):
    def __init__(self, irc):
        self.__parent = super(DisplayTweet, self)
        self.__parent.__init__(irc)

    def callCommand(self, method, irc, msg, *L, **kwargs):
        try:
            self.__parent.callCommand(method, irc, msg, *L, **kwargs)
        except utils.web.Error, e:
            irc.error(str(e))

    def _twitterFetchData(self, irc, msg, id):
        jsondata = None
        tweetText = None
        try:
            jsondata = utils.web.getUrl('http://api.twitter.com/1/statuses/show.json?id=%s&include_entities=true' % (id))
        except utils.web.Error, e:
            self.log.info('server returned the error: %s', utils.web.strError(e))
        if jsondata is not None:
            twitterResponse = json.loads(jsondata)
            tweetText = twitterResponse['text']
            tweetNick = twitterResponse['user']['screen_name']
            tweetTime = twitterResponse['created_at']
            return [tweetText, tweetNick, tweetTime]

    def doPrivmsg(self, irc, msg):
        txt = msg.args[1]
        twitterRegex = r'http[s]?://(?:www\.)?(?:twitter\.com)/(?P<nick>.*?)/status/(?P<id>\d+)'
        twitterMatch = re.match(twitterRegex, txt)
        if twitterMatch is not None:
            id = twitterMatch.groupdict()['id']
            tweetData = self._twitterFetchData(irc, msg, id)
            if tweetData is not None:
                (twText, twNick, twTime) = tweetData
                responseTxt = 'Tweet von "' + twNick + '": ' + twText + ' (' + twTime + ')'
                irc.reply(responseTxt, prefixNick=False)    

Class = DisplayTweet

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
