import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

class AsciiToDecimalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for selected_word in self.view.sel():
			if not selected_word.empty():
				target_string = self.view.substr(selected_word)
				char_list = list(target_string)
				
				result_string = ""
				for char in char_list:
					if not result_string == "":
						result_string += " "
					result_string += str(ord(char))

				self.view.replace(edit, selected_word, result_string)