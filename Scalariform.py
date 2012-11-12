#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin

class ScalariformCommand(sublime_plugin.TextCommand):
  SETTINGS = sublime.load_settings("Scalariform.sublime-settings")
  FORMATTING = SETTINGS.get("formatting")
  CMD = "java -jar " + sublime.packages_path().replace(" ", "\\ ") + \
        "/Scalariform/" + "scalariform.jar "

  def run(self, edit):
    self._setup_cmd()
    import os, subprocess, sys
    try:
      print "Executing command is : " + self.CMD + self.view.file_name()
      retcode = subprocess.call(self.CMD+self.view.file_name(), shell=True)
      if retcode < 0:
        print >>sys.stderr, "Aborted : ", -retcode
      else:
        print >>sys.stderr, "Return code : ", retcode
    except OSError, e:
      print >>sys.stderr, "OSError cptured : ", e

    self._force_refresh()

  def _force_refresh(self):
    (self_group, self_view_idx) = sublime.active_window().get_view_index(self.view)
 
    self_g_views = sublime.active_window().views_in_group(self_group)

    if(len(self_g_views)<=1):
      view_idx = 0
      i=0
      for v in sublime.active_window().views():
        if(v.id()==self.view.id()):
          view_idx = i
          break          
        i=i+1

      (other_group, other_view_idx) = sublime.active_window().get_view_index(sublime.active_window().views()[view_idx-1])
      active_view_other_group = sublime.active_window().active_view_in_group(other_group)
      sublime.active_window().focus_view(active_view_other_group)
    else:
      sublime.active_window().focus_view(sublime.active_window().views()[self_view_idx-1])
    
    sublime.active_window().focus_view(self.view)

  def _setup_cmd(self):
    for k, v in self.FORMATTING.items():
      if not k in ["encoding", "alignSingleLineCaseStatements.maxArrowIndent", "indentSpaces"]:
        self.CMD += ("+" if v else "-") + k + " "
      elif k == "encoding":
        self.CMD += "--" + k + "=" + v + " "
      else:
        self.CMD += "-" + k + "=" + str(v) + " "
