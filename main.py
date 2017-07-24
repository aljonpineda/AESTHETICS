#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2
from maps import MapLocation

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/index.html')
        self.response.out.write(template.render())
    #def post(self):
        #get data out of json object

class PostHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        template = env.get_template('templates/map.html')
        page_id = int(self.request.get('page_id'))
        map_location = map_list[page_id]
        template_variables = {"title": map_location.title,
                              "info": map_location.info,
                              "content": map_location.content}
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/map', PostHandler)
], debug=True)
