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
            if selected_dec:
                selected_dec = selected_dec.split(" ")
                decimal_list = list(selected_dec)

                result = ""
                for decimal in decimal_list:
                    if decimal.isdigit() and 0 <= int(decimal) <= 127:
                        datas = int(decimal)
                        result += chr(datas)

                if result:
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

class HexaDecimalToAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            selected_hex = self.view.substr(selection)
            if selected_hex:
                selected_hex = selected_hex.split(" ")
                hex_list = list(selected_hex)

                result = ""
                for hexa in hex_list:
                    if hexa[0] == '0' and hexa[1] == 'x' and str(eval(hexa)).isdigit() and 0 <= eval(hexa) <= 127:
                        string_decimal = eval(hexa)
                        decimal = int(string_decimal)
                        result += chr(decimal)

                if result:
                    self.view.replace(edit, selection, result)

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

class BinaryToAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            selected_bin = self.view.substr(selection)
            if selected_bin:
                selected_bin = selected_bin.split(" ")
                bin_list = list(selected_bin)

                result = ""
                for binary in bin_list:
                    if binary[0] == '0' and binary[1] == 'b' and str(eval(binary)).isdigit() and 0 <= eval(binary) <= 127:
                        string_decimal = eval(binary)
                        decimal = int(string_decimal)
                        result += chr(decimal)

                if result:
                    self.view.replace(edit, selection, result)