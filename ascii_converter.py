import sublime, sublime_plugin

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
        
class AsciiToHexaDecimalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selected_word in self.view.sel():
            if not selected_word.empty():
                target_string = self.view.substr(selected_word)
                char_list = list(target_string)

                result_string = ""
                for char in char_list:
                    if not result_string == "":
                        result_string += " "
                    result_string += str(hex(ord(char)))

                self.view.replace(edit, selected_word, result_string)

class AsciiToBinaryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selected_word in self.view.sel():
            if not selected_word.empty():
                target_string = self.view.substr(selected_word)
                char_list = list(target_string)

                result_string = ""
                for char in char_list:
                    if not result_string == "":
                        result_string += " "
                    result_string += "0b" + format(ord(char),'b')

                self.view.replace(edit, selected_word, result_string)

class HexaDecimalToAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            selected_hex = self.view.substr(selection)
            selected_hex = selected_hex.split(" ")
            hex_list = list(selected_hex)

            result = ""
            for hexa in hex_list:
                datas = eval(hexa)
                ss = int(datas)
                result += chr(ss)

        self.view.replace(edit, selection, result)