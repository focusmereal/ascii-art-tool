import os
import sys
import time
import argparse
import re
import json
import random
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'
    END = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

class ASCIIArtTool:
    def __init__(self):
        self.font_names = ['standard', 'slant', 'bubble', 'block', '3d', 'small', 'big', 'doom', 'graffiti', 'mini', 'star', 'fire', 'matrix', 'ghost', 'neon']
        self.colors = {
            'black': Colors.BG_BLACK + Colors.WHITE,
            'red': Colors.RED,
            'green': Colors.GREEN,
            'yellow': Colors.YELLOW,
            'blue': Colors.BLUE,
            'purple': Colors.PURPLE,
            'cyan': Colors.CYAN,
            'white': Colors.WHITE,
            'bold': Colors.BOLD,
            'rainbow': 'rainbow',
            'random': 'random',
            'fire': 'fire',
            'ice': 'ice',
            'matrix': 'matrix',
            'neon': 'neon',
            'pastel': 'pastel'
        }
        self._init_letters()
        self._init_fonts()
        self.history = []
        self.load_history()
        
    def _init_letters(self):
        self.letters = {
            'A': ['  ██  ', ' ████  ', '██  ██ ', '██████ ', '██  ██'],
            'B': ['█████ ', '██  ██', '█████ ', '██  ██', '█████ '],
            'C': [' ████ ', '██  ██', '██    ', '██  ██', ' ████ '],
            'D': ['████  ', '██  ██', '██  ██', '██  ██', '████  '],
            'E': ['██████', '██    ', '████  ', '██    ', '██████'],
            'F': ['██████', '██    ', '████  ', '██    ', '██    '],
            'G': [' ████ ', '██    ', '██ ███', '██  ██', ' ████ '],
            'H': ['██  ██', '██  ██', '██████', '██  ██', '██  ██'],
            'I': ['██████', '  ██  ', '  ██  ', '  ██  ', '██████'],
            'J': ['██████', '  ██  ', '  ██  ', '██  ██', ' ████ '],
            'K': ['██  ██', '██ ██ ', '████  ', '██ ██ ', '██  ██'],
            'L': ['██    ', '██    ', '██    ', '██    ', '██████'],
            'M': ['██  ██', '██████', '██  ██', '██  ██', '██  ██'],
            'N': ['██  ██', '███ ██', '██ ███', '██  ██', '██  ██'],
            'O': [' ████ ', '██  ██', '██  ██', '██  ██', ' ████ '],
            'P': ['█████ ', '██  ██', '█████ ', '██    ', '██    '],
            'Q': [' ████ ', '██  ██', '██  ██', '██ ██ ', ' ████ '],
            'R': ['█████ ', '██  ██', '█████ ', '██ ██ ', '██  ██'],
            'S': [' ████ ', '██    ', ' ████ ', '    ██', '████  '],
            'T': ['██████', '  ██  ', '  ██  ', '  ██  ', '  ██  '],
            'U': ['██  ██', '██  ██', '██  ██', '██  ██', ' ████ '],
            'V': ['██  ██', '██  ██', '██  ██', ' ████ ', '  ██  '],
            'W': ['██  ██', '██  ██', '██  ██', '██████', '██  ██'],
            'X': ['██  ██', ' ████ ', '  ██  ', ' ████ ', '██  ██'],
            'Y': ['██  ██', ' ████ ', '  ██  ', '  ██  ', '  ██  '],
            'Z': ['██████', '   ██ ', '  ██  ', ' ██   ', '██████'],
            '0': [' ████ ', '██  ██', '██  ██', '██  ██', ' ████ '],
            '1': ['  ██  ', ' ███  ', '  ██  ', '  ██  ', '██████'],
            '2': ['█████ ', '    ██', ' ████ ', '██    ', '██████'],
            '3': ['████  ', '    ██', ' ███  ', '    ██', '████  '],
            '4': ['██  ██', '██  ██', '██████', '    ██', '    ██'],
            '5': ['██████', '██    ', '█████ ', '    ██', '████  '],
            '6': [' ████ ', '██    ', '█████ ', '██  ██', ' ████ '],
            '7': ['██████', '    ██', '   ██ ', '  ██  ', ' ██   '],
            '8': [' ████ ', '██  ██', ' ████ ', '██  ██', ' ████ '],
            '9': [' ████ ', '██  ██', ' ████ ', '    ██', ' ████ '],
            '+': ['      ', '  ██  ', '██████', '  ██  ', '      '],
            '-': ['      ', '      ', '██████', '      ', '      '],
            '=': ['      ', '██████', '      ', '██████', '      '],
            '*': ['      ', '██  ██', ' ████ ', '██  ██', '      '],
            '/': ['     █', '    █ ', '   █  ', '  █   ', ' █    '],
            '\\': ['█     ', ' █    ', '  █   ', '   █  ', '    █ '],
            '|': [' ██  ', ' ██  ', ' ██  ', ' ██  ', ' ██  '],
            '_': ['      ', '      ', '      ', '      ', '██████'],
            '.': ['      ', '      ', '      ', '      ', ' ████ '],
            ',': ['      ', '      ', '      ', ' ████ ', ' ██   '],
            '!': [' ████ ', ' ████ ', ' ████ ', '      ', ' ████ '],
            '?': [' ████ ', '    ██', '  ██  ', '      ', '  ██  '],
            '@': [' ████ ', '██  ██', '██ ██ ', '██    ', ' ████ '],
            '#': ['██  ██', '██████', '██  ██', '██████', '██  ██'],
            '$': [' ████ ', '██ ██ ', ' ████ ', '██ ██ ', ' ████ '],
            '%': ['██  ██', '   ██ ', '  ██  ', ' ██   ', '██  ██'],
            '&': [' ████ ', '██ ██ ', ' ████ ', '██ ██ ', ' ████ '],
            '(': ['  ██  ', ' ██   ', ' ██   ', ' ██   ', '  ██  '],
            ')': ['  ██  ', '   ██ ', '   ██ ', '   ██ ', '  ██  '],
            '[': ['████  ', '██    ', '██    ', '██    ', '████  '],
            ']': ['  ████', '    ██', '    ██', '    ██', '  ████'],
            '{': ['  ███ ', ' ██   ', ' ███  ', ' ██   ', '  ███ '],
            '}': [' ███  ', '   ██ ', '  ███ ', '   ██ ', ' ███  '],
            ' ': ['     ', '     ', '     ', '     ', '     '],
        }
    
    def _init_fonts(self):
        self.fonts = {}
        for font_name in self.font_names:
            self.fonts[font_name] = self._apply_font_style(self.letters, font_name)
    
    def _apply_font_style(self, letters, style):
        styled = {}
        for char, lines in letters.items():
            if style == 'small':
                styled[char] = [line[1:-1] if len(line) > 2 else line for line in lines]
                styled[char] = [line.replace('█', '▄') for line in styled[char]]
            elif style == 'big':
                styled[char] = [line.replace(' ', '  ').replace('█', '██') for line in lines]
            elif style == 'bubble':
                if char != ' ':
                    styled[char] = [f"○{line.replace('█', '●')}○" for line in lines]
                else:
                    styled[char] = ['     ' for _ in lines]
            elif style == 'block':
                styled[char] = [line.replace('█', '▓') for line in lines]
            elif style == '3d':
                styled[char] = [line.replace('█', '▣') for line in lines]
            elif style == 'doom':
                styled[char] = [line.replace('█', '▓') for line in lines]
                styled[char] = [line.replace(' ', '░') for line in styled[char]]
            elif style == 'graffiti':
                if char != ' ':
                    styled[char] = [line.replace('█', '▓') for line in lines]
                    styled[char] = [f"█{line}█" for line in styled[char]]
                else:
                    styled[char] = ['     ' for _ in lines]
            elif style == 'mini':
                styled[char] = [line[1:-1] if len(line) > 2 else line for line in lines]
                styled[char] = [line.replace(' ', '').replace('█', '▄') if line.strip() else '  ' for line in styled[char]]
            elif style == 'star':
                styled[char] = [line.replace('█', '✦') for line in lines]
                styled[char] = [line.replace(' ', '·') for line in styled[char]]
            elif style == 'fire':
                styled[char] = [line.replace('█', '▓') for line in lines]
                styled[char] = [line.replace(' ', '░') for line in styled[char]]
            elif style == 'matrix':
                styled[char] = [line.replace('█', '█') for line in lines]
                styled[char] = [line.replace(' ', ' ').replace('█', '█') for line in styled[char]]
            elif style == 'ghost':
                if char != ' ':
                    styled[char] = [f"👻{line.replace('█', '░')}👻" for line in lines]
                else:
                    styled[char] = ['     ' for _ in lines]
            elif style == 'neon':
                styled[char] = [line.replace('█', '▒') for line in lines]
            else:
                styled[char] = lines[:]
        return styled

    def _get_color_palette(self, color_type):
        palettes = {
            'rainbow': [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE],
            'fire': [Colors.RED, Colors.YELLOW, Colors.RED, Colors.YELLOW, Colors.RED],
            'ice': [Colors.CYAN, Colors.BLUE, Colors.WHITE, Colors.CYAN, Colors.BLUE],
            'matrix': [Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN, Colors.GREEN],
            'neon': [Colors.PURPLE, Colors.CYAN, Colors.PURPLE, Colors.CYAN, Colors.PURPLE],
            'pastel': ['\033[38;2;255;182;193m', '\033[38;2;221;160;221m', '\033[38;2;173;216;230m', '\033[38;2;144;238;144m', '\033[38;2;255;218;185m']
        }
        return palettes.get(color_type, [Colors.WHITE])

    def generate_art(self, text, font='standard', color='white', bg_color=None, output_file=None, animate=False, save_history=True):
        font_data = self.fonts.get(font, self.fonts['standard'])
        
        lines = ['' for _ in range(5)]
        for char in text.upper():
            if char in font_data:
                for i, line in enumerate(font_data[char]):
                    lines[i] += line + ' '
            else:
                for i in range(len(lines)):
                    lines[i] += '     '
        
        art = '\n'.join(lines)
        
        if color == 'rainbow' or color == 'fire' or color == 'ice' or color == 'matrix' or color == 'neon' or color == 'pastel':
            palette = self._get_color_palette(color)
            lines = art.split('\n')
            colored_lines = []
            char_count = 0
            for line in lines:
                colored_line = ''
                for ch in line:
                    if ch != ' ':
                        color_idx = char_count % len(palette)
                        colored_line += f"{palette[color_idx]}{ch}{Colors.END}"
                        char_count += 1
                    else:
                        colored_line += ' '
                colored_lines.append(colored_line)
            art = '\n'.join(colored_lines)
        elif color == 'random':
            colors_list = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan']
            rand_color = random.choice(colors_list)
            color_code = self.colors.get(rand_color, Colors.WHITE)
            if bg_color:
                bg_code = self.colors.get(bg_color, '')
                art = f"{bg_code}{color_code}{art}{Colors.END}"
            else:
                art = f"{color_code}{art}{Colors.END}"
        else:
            color_code = self.colors.get(color, Colors.WHITE)
            bg_code = self.colors.get(bg_color, '') if bg_color else ''
            if bg_code:
                art = f"{bg_code}{color_code}{art}{Colors.END}"
            else:
                art = f"{color_code}{art}{Colors.END}"
        
        if animate:
            self._animate_art(art)
        
        if output_file:
            self.save_to_file(art, output_file, text, font, color, bg_color)
        
        if save_history:
            self.save_history(text, font, color, bg_color)
        
        return art
    
    def _animate_art(self, art):
        lines = art.split('\n')
        for i in range(len(lines)):
            os.system('cls' if os.name == 'nt' else 'clear')
            for j in range(i + 1):
                print(lines[j])
            time.sleep(0.05)
        time.sleep(0.5)
    
    def save_to_file(self, art, filename, text, font, color, bg_color):
        clean_art = re.sub(r'\x1b\[[0-9;]*m', '', art)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("ASCII ART TOOL - by MeFocus\n")
            f.write("="*60 + "\n")
            f.write(f"Text: {text}\n")
            f.write(f"Font: {font}\n")
            f.write(f"Color: {color}\n")
            f.write(f"Background: {bg_color or 'None'}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            f.write(clean_art)
            f.write("\n\n" + "="*60 + "\n")
            f.write("Generated by ASCII Art Tool - MeFocus\n")
            f.write("="*60 + "\n")
    
    def save_history(self, text, font, color, bg_color):
        entry = {
            'text': text,
            'font': font,
            'color': color,
            'bg_color': bg_color,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.history.append(entry)
        if len(self.history) > 100:
            self.history = self.history[-100:]
        try:
            with open('ascii_history.json', 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except:
            pass
    
    def load_history(self):
        try:
            with open('ascii_history.json', 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        except:
            self.history = []
    
    def show_history(self):
        if not self.history:
            print(f"{Colors.YELLOW}No history found.{Colors.END}")
            return
        print(f"{Colors.CYAN}{'─'*80}{Colors.END}")
        for i, entry in enumerate(self.history[-20:], 1):
            print(f"{Colors.GREEN}{i:2}. {Colors.WHITE}{entry['text']}{Colors.DIM} - {entry['font']} - {entry['color']} - {entry['date']}{Colors.END}")
        print(f"{Colors.CYAN}{'─'*80}{Colors.END}")
    
    def random_art(self, text=None):
        if not text:
            words = ['ART', 'CODE', 'HACK', 'CYBER', 'ASCII', 'ME', 'FOCUS', 'STAR', 'DREAM', 'LIFE', 'LOVE', 'HOPE', 'PEACE', 'KING', 'QUEEN']
            text = random.choice(words)
        font = random.choice(self.font_names)
        color = random.choice(list(self.colors.keys()))
        return self.generate_art(text, font, color)
    
    def print_banner(self):
        banner = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════╗
{Colors.PURPLE}║                                                                          ║
{Colors.CYAN}║   █████╗ ███████╗ ██████╗██╗██╗  ██╗                                     ║
{Colors.CYAN}║  ██╔══██╗██╔════╝██╔════╝██║██║  ██║                                     ║
{Colors.CYAN}║  ███████║███████╗██║     ██║███████║                                     ║
{Colors.CYAN}║  ██╔══██║╚════██║██║     ██║██╔══██║                                     ║
{Colors.CYAN}║  ██║  ██║███████║╚██████╗██║██║  ██║                                     ║
{Colors.CYAN}║  ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝  ╚═╝                                     ║
{Colors.PURPLE}║                                                                          ║
{Colors.YELLOW}║  ███████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗██████╗              ║
{Colors.YELLOW}║  ██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗             ║
{Colors.YELLOW}║  ███████╗   ██║   ██║   ██║██║   ██║██║     █████╗  ██████╔╝             ║
{Colors.YELLOW}║  ╚════██║   ██║   ██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗             ║
{Colors.YELLOW}║  ███████║   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║             ║
{Colors.YELLOW}║  ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝             ║
{Colors.PURPLE}║                                                                          ║
{Colors.GREEN}║           🦅  {Colors.BOLD}ASCII ART TOOL v4.0  {Colors.END}{Colors.GREEN}by {Colors.CYAN}{Colors.BOLD}MeFocus{Colors.END}{Colors.GREEN}                         ║
{Colors.PURPLE}║                                                                          ║
{Colors.PURPLE}╚══════════════════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(banner)
        print(f"{Colors.DIM}{'─'*80}{Colors.END}")
        print(f"{Colors.CYAN}💻 ASCII Art Generator - Convert text to ASCII art{Colors.END}")
        print(f"{Colors.DIM}{'─'*80}{Colors.END}\n")
    
    def show_fonts(self):
        print(f"{Colors.YELLOW}📚 Available Fonts:{Colors.END}")
        for i, font in enumerate(self.font_names, 1):
            sample = self.generate_art(font[:3], font, 'white')
            print(f"  {Colors.CYAN}{i:2}. {Colors.WHITE}{font:<10}{Colors.END}{Colors.DIM} - {font}{Colors.END}")
        print()
    
    def show_colors(self):
        print(f"{Colors.YELLOW}🎨 Available Colors:{Colors.END}")
        for i, color in enumerate(self.colors.keys(), 1):
            if color == 'rainbow':
                display = f"{Colors.RED}R{Colors.YELLOW}A{Colors.GREEN}I{Colors.BLUE}N{Colors.PURPLE}B{Colors.CYAN}O{Colors.WHITE}W"
            elif color == 'fire':
                display = f"{Colors.RED}🔥{Colors.YELLOW}F{Colors.RED}I{Colors.YELLOW}R{Colors.RED}E{Colors.END}"
            elif color == 'ice':
                display = f"{Colors.CYAN}❄️{Colors.BLUE}I{Colors.CYAN}C{Colors.BLUE}E{Colors.END}"
            elif color == 'matrix':
                display = f"{Colors.GREEN}💻{Colors.GREEN}M{Colors.GREEN}A{Colors.GREEN}T{Colors.GREEN}R{Colors.GREEN}I{Colors.GREEN}X{Colors.END}"
            elif color == 'neon':
                display = f"{Colors.PURPLE}💡{Colors.PURPLE}N{Colors.CYAN}E{Colors.PURPLE}O{Colors.CYAN}N{Colors.END}"
            elif color == 'pastel':
                display = f"\033[38;2;255;182;193m🌸{Colors.END}\033[38;2;221;160;221mP{Colors.END}\033[38;2;173;216;230mA{Colors.END}\033[38;2;144;238;144mS{Colors.END}\033[38;2;255;218;185mT{Colors.END}\033[38;2;221;160;221mE{Colors.END}\033[38;2;255;182;193mL{Colors.END}"
            else:
                display = f"{self.colors.get(color, Colors.WHITE)}{color}{Colors.END}"
            print(f"  {Colors.CYAN}{i:2}. {display}{Colors.END}")
        print()
    
    def interactive_mode(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        
        while True:
            print(f"{Colors.CYAN}📝 Enter your text (or 'exit', 'random', 'history'):{Colors.END}")
            text = input(f"{Colors.YELLOW}➜ {Colors.END}").strip()
            
            if text.lower() == 'exit':
                break
            if text.lower() == 'random':
                self.random_art()
                continue
            if text.lower() == 'history':
                self.show_history()
                continue
            if not text:
                text = "AAT"
            
            print()
            self.show_fonts()
            print(f"{Colors.CYAN}🔤 Choose font (default: standard):{Colors.END}")
            font_choice = input(f"{Colors.YELLOW}➜ {Colors.END}").strip().lower()
            if font_choice in self.font_names:
                font = font_choice
            elif font_choice.isdigit() and 1 <= int(font_choice) <= len(self.font_names):
                font = self.font_names[int(font_choice) - 1]
            else:
                font = 'standard'
            
            print()
            self.show_colors()
            print(f"{Colors.CYAN}🎨 Choose color (default: white):{Colors.END}")
            color_choice = input(f"{Colors.YELLOW}➜ {Colors.END}").strip().lower()
            if color_choice in self.colors:
                color = color_choice
            elif color_choice.isdigit() and 1 <= int(color_choice) <= len(self.colors):
                color = list(self.colors.keys())[int(color_choice) - 1]
            else:
                color = 'white'
            
            print()
            print(f"{Colors.CYAN}🎨 Choose background color (optional, press Enter for none):{Colors.END}")
            print(f"{Colors.DIM}   Available: black, red, green, yellow, blue, purple, cyan, white{Colors.END}")
            bg_choice = input(f"{Colors.YELLOW}➜ {Colors.END}").strip().lower()
            bg_color = bg_choice if bg_choice in self.colors else None
            
            print()
            print(f"{Colors.CYAN}💾 Save to file? (y/n, default: n):{Colors.END}")
            save_choice = input(f"{Colors.YELLOW}➜ {Colors.END}").strip().lower()
            
            print()
            print(f"{Colors.CYAN}🎬 Animate? (y/n, default: n):{Colors.END}")
            animate_choice = input(f"{Colors.YELLOW}➜ {Colors.END}").strip().lower()
            
            print()
            print(f"{Colors.GREEN}🎨 Generating ASCII Art...{Colors.END}")
            time.sleep(0.3)
            
            output_file = None
            if save_choice in ['y', 'yes']:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_file = f"ascii_art_{timestamp}.txt"
            
            art = self.generate_art(text, font, color, bg_color, output_file, animate_choice in ['y', 'yes'])
            
            print("\n" + "="*80)
            print(f"{Colors.GREEN}✨ ASCII Art Generated!{Colors.END}")
            print("="*80 + "\n")
            print(art)
            print("\n" + "="*80)
            
            if output_file:
                print(f"{Colors.GREEN}✅ Saved to: {output_file}{Colors.END}")
            
            print(f"{Colors.DIM}{'─'*80}{Colors.END}")
            print(f"{Colors.PURPLE}🦅 ASCII Art Tool by MeFocus{Colors.END}\n")
    
    def command_line_mode(self):
        parser = argparse.ArgumentParser(
            description='ASCII Art Tool - Convert text to beautiful ASCII art',
            epilog='Example: python ascii_art.py -t "Hello" -f slant -c cyan -o output.txt'
        )
        
        parser.add_argument('-t', '--text', type=str, help='Text to convert to ASCII art')
        parser.add_argument('-f', '--font', type=str, choices=self.font_names, default='standard', help='Font style')
        parser.add_argument('-c', '--color', type=str, choices=list(self.colors.keys()), default='white', help='Color of the art')
        parser.add_argument('-b', '--bg', type=str, choices=['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white', None], default=None, help='Background color')
        parser.add_argument('-o', '--output', type=str, help='Output file name')
        parser.add_argument('-a', '--animate', action='store_true', help='Animate the art')
        parser.add_argument('-r', '--random', action='store_true', help='Generate random ASCII art')
        parser.add_argument('--list-fonts', action='store_true', help='List all available fonts')
        parser.add_argument('--list-colors', action='store_true', help='List all available colors')
        parser.add_argument('--history', action='store_true', help='Show history')
        
        args = parser.parse_args()
        
        if args.list_fonts:
            self.print_banner()
            self.show_fonts()
            return
        
        if args.list_colors:
            self.print_banner()
            self.show_colors()
            return
        
        if args.history:
            self.print_banner()
            self.show_history()
            return
        
        if args.random:
            self.print_banner()
            art = self.random_art()
            print("\n" + "="*80)
            print(f"{Colors.GREEN}✨ Random ASCII Art Generated!{Colors.END}")
            print("="*80 + "\n")
            print(art)
            print("\n" + "="*80)
            print(f"{Colors.PURPLE}🦅 ASCII Art Tool by MeFocus{Colors.END}")
            return
        
        if not args.text:
            args.text = "AAT"
        
        art = self.generate_art(args.text, args.font, args.color, args.bg, args.output, args.animate)
        
        print("\n" + "="*80)
        print(f"{Colors.GREEN}✨ ASCII Art Generated!{Colors.END}")
        print("="*80 + "\n")
        print(art)
        print("\n" + "="*80)
        
        if args.output:
            print(f"{Colors.GREEN}✅ Saved to: {args.output}{Colors.END}")
        
        print(f"{Colors.PURPLE}🦅 ASCII Art Tool by MeFocus{Colors.END}")

def main():
    tool = ASCIIArtTool()
    
    if len(sys.argv) > 1:
        tool.command_line_mode()
    else:
        tool.interactive_mode()

if __name__ == "__main__":
    main()