import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

class DecimalToAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
	        selected_dec = self.view.substr(selection)
	        selected_dec = selected_dec.split(" ")
	        decimal_list = list(selected_dec)

	        result = ""
	        for decimal in decimal_list:
	        	datas = int(decimal)
	        	if not result == "":
	        		result += " "
	        	result += chr(datas)

        self.view.replace(edit, selection, result)