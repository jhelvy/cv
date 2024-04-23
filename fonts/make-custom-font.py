from fontTools.ttLib import TTFont
import os

def merge_fonts(base_font_path, numeral_font_path, output_font_path):
    base_font = TTFont(base_font_path)
    numeral_font = TTFont(numeral_font_path)

    # Unicode points for 0-9
    numerals_unicode = [str(i) for i in range(48, 58)]

    # Finding and replacing numerals
    for uni in numerals_unicode:
        numeral_char = chr(int(uni))
        base_glyph_name = base_font['cmap'].tables[0].cmap[int(uni)]
        numeral_glyph_name = numeral_font['cmap'].tables[0].cmap[int(uni)]

        if base_glyph_name and numeral_glyph_name:
            # Replace glyph in base font
            base_font['glyf'][base_glyph_name] = numeral_font['glyf'][numeral_glyph_name]
            print(f"Replaced Raleway's {numeral_char} glyph '{base_glyph_name}' with Roboto's '{numeral_glyph_name}'")

    # Save the modified font
    base_font.save(output_font_path)
    print(f"Modified font saved as {output_font_path}")

def process_font_styles(styles, fonts_dir):
    for style in styles:
        base_font_path = os.path.join(fonts_dir, f'Raleway-{style}.ttf')
        numeral_font_path = os.path.join(fonts_dir, f'Roboto-{style}.ttf')
        output_font_path = os.path.join(fonts_dir, f'Raleway-Mod-{style}.ttf')

        if os.path.exists(base_font_path) and os.path.exists(numeral_font_path):
            print(f"Processing {style} style...")
            merge_fonts(base_font_path, numeral_font_path, output_font_path)
        else:
            print(f"Font files not found for style {style}. Expected at {base_font_path} and {numeral_font_path}")

styles = ['Regular', 'Italic', 'BoldItalic', 'Bold']
fonts_dir = '/Users/jhelvy/gh/career/cv/fonts'
process_font_styles(styles, fonts_dir)







