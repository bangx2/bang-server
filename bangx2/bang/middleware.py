#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bang.models import Bang

class BangMiddleware(object):
    
    def process_request(self, request):
        """
        从header重读出bang_id, 从而获取用户当前操作的bang，放入request中。
        """

        bang_id = request.META.get('HTTP_X_BANG_ID', None)
        if bang_id:
            try:
                bang = Bang.objects.get(bang_id=bang_id)
                request.current_bang = bang
            except Bang.DoesNotExist:
                request.current_bang = None
        else:
            request.current_bang = None

        return

