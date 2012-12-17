import commands, subprocess, os.path
import sublime, sublime_plugin

class Recessify(sublime_plugin.TextCommand):
  def run(self, edit):
    self.save()
    self.recessify(edit)

  def save(self):
    self.view.run_command("save")

  def recessify(self, edit):
    cmd = ["recess", self.view.file_name(), "--compile"]
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    result = p.communicate()[0]

    if len(result) > 0:
      self.view.replace(edit, sublime.Region(0, self.view.size()), result.decode('utf-8'))
      sublime.set_timeout(self.save, 100)
